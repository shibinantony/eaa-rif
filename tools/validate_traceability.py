#!/usr/bin/env python3
"""Validate EAA-RIF executable examples with only the Python standard library.

The validator intentionally implements the small JSON Schema subset used by
this repository and adds semantic checks that JSON Schema cannot express:
registry cross-references, assurance-graph integrity, configuration binding,
authorization chronology, and an objective-to-decision trace path.

It validates structure and traceability, not legal compliance, control
effectiveness, or the adequacy of a residual-risk decision.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


SCHEMA_FILES = {
    "control": Path("schemas/control-contract.schema.json"),
    "evidence": Path("schemas/evidence-record.schema.json"),
    "thread": Path("schemas/assurance-thread.schema.json"),
}

INSTANCE_FILES = {
    "control": Path("examples/registries/control-contract.json"),
    "evidence": Path("examples/registries/evidence-record.json"),
    "thread": Path("examples/registries/assurance-thread.json"),
}

REGISTRY_SPECS = {
    "systems": {
        "path": Path("examples/registries/system-registry.json"),
        "id_field": "system_id",
        "id_pattern": r"^SYS-[A-Z0-9_-]+$",
        "required": {
            "system_id",
            "name",
            "business_owner",
            "product_owner",
            "impact_tier",
            "risk_tier",
            "agent_authority",
            "lifecycle_state",
            "configuration_digest",
        },
    },
    "risks": {
        "path": Path("examples/registries/risk-registry.json"),
        "id_field": "risk_id",
        "id_pattern": r"^RISK-[A-Z0-9_-]+$",
        "required": {
            "risk_id",
            "title",
            "scenario",
            "owner",
            "inherent_rating",
            "target_residual_rating",
            "status",
        },
    },
    "requirements": {
        "path": Path("examples/registries/requirement-registry.json"),
        "id_field": "requirement_id",
        "id_pattern": r"^REQ-[A-Z0-9_-]+$",
        "required": {
            "requirement_id",
            "statement",
            "owner",
            "priority",
            "verification",
        },
    },
    "policies": {
        "path": Path("examples/registries/policy-registry.json"),
        "id_field": "policy_id",
        "id_pattern": r"^POL-[A-Z0-9_-]+$",
        "required": {
            "policy_id",
            "title",
            "description",
            "control_ids",
            "enforcement_point_ids",
            "implementation",
            "version",
            "status",
        },
    },
    "enforcement_points": {
        "path": Path("examples/registries/enforcement-point-registry.json"),
        "id_field": "enforcement_point_id",
        "id_pattern": r"^EP-[A-Z0-9_-]+$",
        "required": {
            "enforcement_point_id",
            "title",
            "type",
            "owner",
            "failure_behavior",
            "description",
        },
    },
}

REQUIRED_EXECUTABLE_FILES = (
    Path("examples/policy-as-code/opa/agent_deployment_gate.rego"),
    Path("examples/policy-as-code/opa/agent_deployment_gate_test.rego"),
    Path("examples/policy-as-code/opa/input-allow.json"),
    Path("examples/policy-as-code/opa/input-deny.json"),
    Path("examples/policy-as-code/azure-policy/require-private-ai-service.json"),
    Path("examples/policy-as-code/terraform/versions.tf"),
    Path("examples/policy-as-code/terraform/variables.tf"),
    Path("examples/policy-as-code/terraform/main.tf"),
    Path("examples/policy-as-code/terraform/allow.tfvars.json"),
    Path("examples/policy-as-code/terraform/deny.tfvars.json"),
)

SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema",
    "$id",
    "title",
    "description",
    "type",
    "additionalProperties",
    "required",
    "properties",
    "items",
    "minItems",
    "maxItems",
    "uniqueItems",
    "minLength",
    "maxLength",
    "pattern",
    "enum",
    "const",
    "format",
    "minProperties",
    "maxProperties",
    "default",
}

CANONICAL_SOURCE_LABELS = {"SOURCE_FRAMEWORK", "DERIVED_MAPPING", "ORIGINAL_IP"}
IMPACT_TIERS = {"low", "moderate", "high", "critical"}
RISK_TIERS = {"low", "moderate", "high", "critical"}
AGENT_AUTHORITIES = {"A0", "A1", "A2", "A3", "A4", "A5", "not_applicable"}

NODE_PREFIXES = {
    "business_objective": "OBJ-",
    "architecture_principle": "PRINCIPLE-",
    "architecture_decision": "ADR-",
    "risk": "RISK-",
    "requirement": "REQ-",
    "control": "CTRL-",
    "policy": "POL-",
    "enforcement_point": "EP-",
    "evidence": "EVID-",
    "exception": "EXC-",
    "gate_decision": "GATE-",
    "actor": "ACTOR-",
}

MANDATORY_NODE_TYPES = {
    "business_objective",
    "architecture_principle",
    "architecture_decision",
    "risk",
    "requirement",
    "control",
    "policy",
    "enforcement_point",
    "evidence",
    "gate_decision",
}


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def add(self, message: str) -> None:
        self.errors.append(message)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _is_json_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _format_is_valid(value: str, format_name: str) -> bool:
    try:
        if format_name == "date":
            date.fromisoformat(value)
            return "T" not in value
        if format_name == "date-time":
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return "T" in value and parsed.tzinfo is not None
        if format_name == "uri":
            parsed = urlparse(value)
            return bool(parsed.scheme and (parsed.netloc or parsed.scheme == "urn"))
    except ValueError:
        return False
    return True


def validate_instance(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate an instance against the repository's supported schema subset."""

    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type and not _is_json_type(instance, expected_type):
        return [f"{path}: expected {expected_type}, got {type(instance).__name__}"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']!r}")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: string is longer than maxLength")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            errors.append(f"{path}: value does not match {schema['pattern']!r}")
        if "format" in schema and not _format_is_valid(instance, schema["format"]):
            errors.append(f"{path}: invalid {schema['format']} value")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: array has more than maxItems")
        if schema.get("uniqueItems"):
            canonical = [json.dumps(item, sort_keys=True, separators=(",", ":")) for item in instance]
            if len(canonical) != len(set(canonical)):
                errors.append(f"{path}: array items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                errors.extend(validate_instance(item, item_schema, f"{path}[{index}]"))

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")

        for key, child_schema in properties.items():
            if key in instance:
                errors.extend(validate_instance(instance[key], child_schema, f"{path}.{key}"))

        if len(instance) < schema.get("minProperties", 0):
            errors.append(f"{path}: object has fewer than minProperties")
        if "maxProperties" in schema and len(instance) > schema["maxProperties"]:
            errors.append(f"{path}: object has more than maxProperties")

    return errors


def validate_schema_document(schema: Any, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return [f"{label}: schema root must be an object"]
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append(f"{label}: schema must declare JSON Schema draft 2020-12")
    if not schema.get("$id"):
        errors.append(f"{label}: schema is missing $id")

    def walk(node: Any, node_path: str) -> None:
        if not isinstance(node, dict):
            return
        unknown = set(node) - SUPPORTED_SCHEMA_KEYWORDS
        if unknown:
            errors.append(f"{label}:{node_path}: unsupported schema keywords {sorted(unknown)}")
        if "required" in node and not isinstance(node["required"], list):
            errors.append(f"{label}:{node_path}: required must be an array")
        if "properties" in node:
            if not isinstance(node["properties"], dict):
                errors.append(f"{label}:{node_path}: properties must be an object")
            else:
                for name, child in node["properties"].items():
                    walk(child, f"{node_path}.properties.{name}")
        if isinstance(node.get("items"), dict):
            walk(node["items"], f"{node_path}.items")
        if isinstance(node.get("additionalProperties"), dict):
            walk(node["additionalProperties"], f"{node_path}.additionalProperties")

    walk(schema, "$")
    return errors


def validate_machine_labels(value: Any, path: str = "$") -> list[str]:
    """Reject legacy provenance keys and non-canonical source-label values."""

    errors: list[str] = []
    if isinstance(value, dict):
        if "ip_label" in value:
            errors.append(f"{path}: legacy ip_label is prohibited; use source_label")
        source_label = value.get("source_label")
        if isinstance(source_label, str) and source_label not in CANONICAL_SOURCE_LABELS:
            errors.append(
                f"{path}.source_label: {source_label!r} is not a canonical value"
            )
        for key, child in value.items():
            errors.extend(validate_machine_labels(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(validate_machine_labels(child, f"{path}[{index}]"))
    return errors


def _load_registry(root: Path, name: str, report: ValidationReport) -> dict[str, dict[str, Any]]:
    spec = REGISTRY_SPECS[name]
    path = root / spec["path"]
    if not path.is_file():
        report.add(f"{spec['path']}: required registry is missing")
        return {}
    try:
        document = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        report.add(f"{spec['path']}: cannot load JSON: {exc}")
        return {}

    if document.get("registry_type") != name:
        report.add(f"{spec['path']}: registry_type must be {name!r}")
    if document.get("source_label") not in CANONICAL_SOURCE_LABELS:
        report.add(
            f"{spec['path']}: source_label must be one of {sorted(CANONICAL_SOURCE_LABELS)}"
        )
    records = document.get("records")
    if not isinstance(records, list) or not records:
        report.add(f"{spec['path']}: records must be a non-empty array")
        return {}

    by_id: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records):
        location = f"{spec['path']}:records[{index}]"
        if not isinstance(record, dict):
            report.add(f"{location}: record must be an object")
            continue
        missing = spec["required"] - set(record)
        if missing:
            report.add(f"{location}: missing fields {sorted(missing)}")
        record_id = record.get(spec["id_field"])
        if not isinstance(record_id, str) or re.fullmatch(spec["id_pattern"], record_id) is None:
            report.add(f"{location}: invalid {spec['id_field']}")
            continue
        if record_id in by_id:
            report.add(f"{location}: duplicate identifier {record_id}")
        if name == "systems":
            if record.get("impact_tier") not in IMPACT_TIERS:
                report.add(f"{location}: invalid impact_tier")
            if record.get("risk_tier") not in RISK_TIERS:
                report.add(f"{location}: invalid risk_tier")
            if record.get("agent_authority") not in AGENT_AUTHORITIES:
                report.add(f"{location}: invalid agent_authority")
        by_id[record_id] = record
    return by_id


def _check_references(
    root: Path,
    control: dict[str, Any],
    evidence: dict[str, Any],
    thread: dict[str, Any],
    registries: dict[str, dict[str, dict[str, Any]]],
) -> list[str]:
    errors: list[str] = []

    reference_sets = (
        ("control.risk_ids", control.get("risk_ids", []), registries["risks"]),
        (
            "control.source_requirement_ids",
            control.get("source_requirement_ids", []),
            registries["requirements"],
        ),
        ("control.system_scope", control.get("system_scope", []), registries["systems"]),
        ("control.policy_ids", control.get("policy_ids", []), registries["policies"]),
        (
            "control.enforcement_point_ids",
            control.get("enforcement_point_ids", []),
            registries["enforcement_points"],
        ),
    )
    for label, references, target in reference_sets:
        for identifier in references:
            if identifier not in target:
                errors.append(f"{label}: unresolved identifier {identifier}")

    control_ids = {control.get("control_id")}
    for policy_id, policy in registries["policies"].items():
        for identifier in policy.get("control_ids", []):
            if identifier not in control_ids:
                errors.append(f"policy {policy_id}: unresolved control {identifier}")
        for identifier in policy.get("enforcement_point_ids", []):
            if identifier not in registries["enforcement_points"]:
                errors.append(f"policy {policy_id}: unresolved enforcement point {identifier}")
        implementation = policy.get("implementation")
        if isinstance(implementation, str) and not (root / implementation).is_file():
            errors.append(f"policy {policy_id}: implementation does not exist: {implementation}")

    if evidence.get("control_id") != control.get("control_id"):
        errors.append("evidence.control_id does not resolve to the sample control")
    if evidence.get("system_id") not in registries["systems"]:
        errors.append(f"evidence.system_id is unresolved: {evidence.get('system_id')}")
    if evidence.get("policy_id") not in registries["policies"]:
        errors.append(f"evidence.policy_id is unresolved: {evidence.get('policy_id')}")
    if evidence.get("enforcement_point_id") not in registries["enforcement_points"]:
        errors.append(
            f"evidence.enforcement_point_id is unresolved: {evidence.get('enforcement_point_id')}"
        )

    system = registries["systems"].get(evidence.get("system_id"), {})
    if evidence.get("configuration_digest") != system.get("configuration_digest"):
        errors.append("evidence configuration digest does not match the system registry")
    if thread.get("system", {}).get("system_id") != evidence.get("system_id"):
        errors.append("assurance-thread system does not match evidence system")
    if thread.get("system", {}).get("configuration_digest") != evidence.get("configuration_digest"):
        errors.append("assurance-thread configuration digest does not match evidence")
    for field_name in ("impact_tier", "risk_tier", "agent_authority"):
        if control.get(field_name) != system.get(field_name):
            errors.append(f"control {field_name} does not match the system registry")
        if thread.get("system", {}).get(field_name) != system.get(field_name):
            errors.append(f"assurance-thread {field_name} does not match the system registry")
    if control.get("evidence_contract", {}).get("record_schema"):
        schema_path = root / control["evidence_contract"]["record_schema"]
        if not schema_path.is_file():
            errors.append(f"control evidence schema does not exist: {schema_path}")

    return errors


def _parse_datetime(value: str, label: str, errors: list[str]) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timezone is required")
        return parsed
    except (AttributeError, ValueError) as exc:
        errors.append(f"{label}: invalid date-time: {exc}")
        return None


def _has_path(adjacency: dict[str, set[str]], starts: Iterable[str], targets: set[str]) -> bool:
    queue = deque(starts)
    seen = set(starts)
    while queue:
        current = queue.popleft()
        if current in targets:
            return True
        for neighbor in adjacency.get(current, set()):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False


def validate_assurance_graph(
    thread: dict[str, Any],
    evidence: dict[str, Any],
    registries: dict[str, dict[str, dict[str, Any]]],
) -> list[str]:
    errors: list[str] = []
    nodes = thread.get("nodes", [])
    edges = thread.get("edges", [])

    node_by_id: dict[str, dict[str, Any]] = {}
    for index, node in enumerate(nodes):
        node_id = node.get("id")
        if node_id in node_by_id:
            errors.append(f"thread.nodes[{index}]: duplicate node {node_id}")
        else:
            node_by_id[node_id] = node
        expected_prefix = NODE_PREFIXES.get(node.get("type"))
        if expected_prefix and isinstance(node_id, str) and not node_id.startswith(expected_prefix):
            errors.append(
                f"thread.nodes[{index}]: {node_id} does not use prefix {expected_prefix} for {node.get('type')}"
            )

    present_types = {node.get("type") for node in nodes}
    missing_types = MANDATORY_NODE_TYPES - present_types
    if missing_types:
        errors.append(f"assurance thread lacks mandatory node types: {sorted(missing_types)}")

    adjacency: dict[str, set[str]] = {}
    degree = {node_id: 0 for node_id in node_by_id}
    seen_edges: set[tuple[str, str, str]] = set()
    for index, edge in enumerate(edges):
        source = edge.get("from")
        target = edge.get("to")
        relationship = edge.get("relationship")
        edge_key = (source, relationship, target)
        if edge_key in seen_edges:
            errors.append(f"thread.edges[{index}]: duplicate edge {edge_key}")
        seen_edges.add(edge_key)
        if source not in node_by_id:
            errors.append(f"thread.edges[{index}]: unresolved source node {source}")
        if target not in node_by_id:
            errors.append(f"thread.edges[{index}]: unresolved target node {target}")
        if source in node_by_id and target in node_by_id:
            adjacency.setdefault(source, set()).add(target)
            degree[source] += 1
            degree[target] += 1

    for node_id, node_degree in degree.items():
        if node_degree == 0:
            errors.append(f"assurance thread contains orphan node {node_id}")

    objective_ids = {
        node["id"] for node in nodes if node.get("type") == "business_objective"
    }
    gate_ids = {node["id"] for node in nodes if node.get("type") == "gate_decision"}
    if objective_ids and gate_ids and not _has_path(adjacency, objective_ids, gate_ids):
        errors.append("assurance thread has no directed path from a business objective to a gate decision")

    expected_registry_nodes = (
        set(registries["risks"])
        | set(registries["requirements"])
        | set(registries["policies"])
        | set(registries["enforcement_points"])
        | {evidence.get("control_id"), evidence.get("evidence_id")}
    )
    for identifier in expected_registry_nodes:
        if identifier and identifier not in node_by_id:
            errors.append(f"assurance thread does not contain referenced node {identifier}")

    authorization = thread.get("authorization", {})
    gate_id = authorization.get("gate_decision_id")
    if gate_id not in node_by_id or node_by_id.get(gate_id, {}).get("type") != "gate_decision":
        errors.append("authorization.gate_decision_id does not resolve to a gate_decision node")
    if authorization.get("configuration_digest") != thread.get("system", {}).get("configuration_digest"):
        errors.append("authorization configuration digest does not match thread system")
    if evidence.get("evidence_id") not in authorization.get("evidence_ids", []):
        errors.append("authorization does not cite the sample evidence record")

    collected = _parse_datetime(evidence.get("collected_at", ""), "evidence.collected_at", errors)
    evidence_expiry = _parse_datetime(
        evidence.get("validity", {}).get("expires_at", ""),
        "evidence.validity.expires_at",
        errors,
    )
    decided = _parse_datetime(authorization.get("decided_at", ""), "authorization.decided_at", errors)
    authorization_expiry = _parse_datetime(
        authorization.get("expires_at", ""), "authorization.expires_at", errors
    )
    residual_decided = _parse_datetime(
        authorization.get("residual_risk", {}).get("decided_at", ""),
        "authorization.residual_risk.decided_at",
        errors,
    )
    if collected and decided and collected > decided:
        errors.append("evidence was collected after the authorization decision")
    if evidence_expiry and decided and evidence_expiry <= decided:
        errors.append("evidence was expired when the authorization decision was made")
    if decided and authorization_expiry and authorization_expiry <= decided:
        errors.append("authorization expiry must be after the decision")
    if residual_decided and decided and residual_decided > decided:
        errors.append("residual risk was accepted after the authorization decision")

    return errors


def _validate_policy_inputs(root: Path) -> list[str]:
    errors: list[str] = []
    base = Path("examples/policy-as-code/opa")
    allow_path = root / base / "input-allow.json"
    deny_path = root / base / "input-deny.json"
    try:
        allow_input = load_json(allow_path)
        deny_input = load_json(deny_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"OPA input fixture: cannot load JSON: {exc}"]

    required_top = {"system", "release", "now"}
    required_release = {
        "target_environment",
        "configuration_digest",
        "approved_configuration_digest",
        "allowed_agent_authority",
        "required_control_ids",
        "satisfied_control_ids",
        "control_states",
        "evidence",
        "approval",
        "exceptions",
    }
    required_system = {
        "system_id",
        "impact_tier",
        "risk_tier",
        "agent_authority",
        "lifecycle_state",
        "configuration_digest",
    }
    for label, document in (("allow", allow_input), ("deny", deny_input)):
        missing_top = required_top - set(document)
        if missing_top:
            errors.append(f"OPA {label} input: missing top-level fields {sorted(missing_top)}")
            continue
        missing_system = required_system - set(document["system"])
        if missing_system:
            errors.append(f"OPA {label} input: missing system fields {sorted(missing_system)}")
        missing_release = required_release - set(document["release"])
        if missing_release:
            errors.append(f"OPA {label} input: missing release fields {sorted(missing_release)}")
        for field_name, allowed in (
            ("impact_tier", IMPACT_TIERS),
            ("risk_tier", RISK_TIERS),
            ("agent_authority", AGENT_AUTHORITIES),
        ):
            if document["system"].get(field_name) not in allowed:
                errors.append(f"OPA {label} input: invalid system.{field_name}")

    if allow_input.get("system", {}).get("configuration_digest") != allow_input.get("release", {}).get(
        "configuration_digest"
    ):
        errors.append("OPA allow input must use a configuration-matched release")
    if deny_input.get("system", {}).get("configuration_digest") == deny_input.get("release", {}).get(
        "configuration_digest"
    ):
        errors.append("OPA deny input must exercise a configuration mismatch")
    if all(state == "pass" for state in deny_input.get("release", {}).get("control_states", {}).values()):
        errors.append("OPA deny input must exercise a failed control state")
    return errors


def validate_repository(root: Path) -> ValidationReport:
    root = root.resolve()
    report = ValidationReport()

    for relative in REQUIRED_EXECUTABLE_FILES:
        if not (root / relative).is_file():
            report.add(f"{relative}: required executable example is missing")

    for path in sorted((root / "schemas").glob("*.json")) + sorted(
        (root / "examples").rglob("*.json")
    ):
        try:
            document = load_json(path)
            report.errors.extend(
                f"{path.relative_to(root)}: {error}"
                for error in validate_machine_labels(document)
            )
        except (OSError, json.JSONDecodeError) as exc:
            report.add(f"{path.relative_to(root)}: invalid JSON: {exc}")

    schemas: dict[str, dict[str, Any]] = {}
    instances: dict[str, dict[str, Any]] = {}
    schema_ids: set[str] = set()
    for name, relative in SCHEMA_FILES.items():
        path = root / relative
        try:
            schema = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            report.add(f"{relative}: cannot load schema: {exc}")
            continue
        schemas[name] = schema
        report.errors.extend(validate_schema_document(schema, str(relative)))
        schema_id = schema.get("$id")
        if schema_id in schema_ids:
            report.add(f"{relative}: duplicate schema $id {schema_id}")
        schema_ids.add(schema_id)

    for name, relative in INSTANCE_FILES.items():
        path = root / relative
        try:
            instance = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            report.add(f"{relative}: cannot load instance: {exc}")
            continue
        instances[name] = instance
        if name in schemas:
            errors = validate_instance(instance, schemas[name])
            report.errors.extend(f"{relative}: {error}" for error in errors)

    registries: dict[str, dict[str, dict[str, Any]]] = {}
    for name in REGISTRY_SPECS:
        registries[name] = _load_registry(root, name, report)

    if {"control", "evidence", "thread"} <= instances.keys() and len(registries) == len(
        REGISTRY_SPECS
    ):
        report.errors.extend(
            _check_references(
                root,
                instances["control"],
                instances["evidence"],
                instances["thread"],
                registries,
            )
        )
        report.errors.extend(
            validate_assurance_graph(instances["thread"], instances["evidence"], registries)
        )

    report.errors.extend(_validate_policy_inputs(root))
    report.counts = {
        "schemas": len(schemas),
        "schema_bound_instances": len(instances),
        "registry_records": sum(len(records) for records in registries.values()),
        "assurance_nodes": len(instances.get("thread", {}).get("nodes", [])),
        "assurance_edges": len(instances.get("thread", {}).get("edges", [])),
    }
    return report


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=_default_root(),
        help="Repository root; defaults to the parent of tools/.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit a machine-readable result.",
    )
    args = parser.parse_args(argv)

    report = validate_repository(args.root)
    if args.json:
        print(
            json.dumps(
                {"ok": report.ok, "counts": report.counts, "errors": report.errors},
                indent=2,
                sort_keys=True,
            )
        )
    elif report.ok:
        summary = ", ".join(f"{key}={value}" for key, value in report.counts.items())
        print(f"EAA-RIF traceability validation passed ({summary}).")
    else:
        print(f"EAA-RIF traceability validation failed with {len(report.errors)} error(s):")
        for error in report.errors:
            print(f"- {error}")

    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
