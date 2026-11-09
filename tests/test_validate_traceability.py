from __future__ import annotations

import copy
import unittest
from pathlib import Path

from tools.validate_traceability import (
    CANONICAL_SOURCE_LABELS,
    REGISTRY_SPECS,
    load_json,
    validate_assurance_graph,
    validate_instance,
    validate_machine_labels,
    validate_repository,
)


ROOT = Path(__file__).resolve().parents[1]


def load_registries() -> dict[str, dict[str, dict]]:
    result: dict[str, dict[str, dict]] = {}
    for name, spec in REGISTRY_SPECS.items():
        document = load_json(ROOT / spec["path"])
        result[name] = {record[spec["id_field"]]: record for record in document["records"]}
    return result


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_examples_are_coherent(self) -> None:
        report = validate_repository(ROOT)
        self.assertEqual([], report.errors, "\n".join(report.errors))
        self.assertEqual(3, report.counts["schemas"])
        self.assertGreaterEqual(report.counts["assurance_nodes"], 10)

    def test_schema_validation_rejects_missing_required_field(self) -> None:
        schema = load_json(ROOT / "schemas/control-contract.schema.json")
        instance = load_json(ROOT / "examples/registries/control-contract.json")
        del instance["control_id"]
        errors = validate_instance(instance, schema)
        self.assertTrue(any("missing required property 'control_id'" in error for error in errors))

    def test_schema_validation_rejects_unexpected_field(self) -> None:
        schema = load_json(ROOT / "schemas/evidence-record.schema.json")
        instance = load_json(ROOT / "examples/registries/evidence-record.json")
        instance["uncontrolled_claim"] = True
        errors = validate_instance(instance, schema)
        self.assertTrue(any("unexpected property 'uncontrolled_claim'" in error for error in errors))

    def test_source_label_vocabulary_is_canonical_across_schemas(self) -> None:
        for schema_name in (
            "control-contract.schema.json",
            "evidence-record.schema.json",
            "assurance-thread.schema.json",
        ):
            schema = load_json(ROOT / "schemas" / schema_name)
            self.assertEqual(
                CANONICAL_SOURCE_LABELS,
                set(schema["properties"]["source_label"]["enum"]),
            )

    def test_legacy_ip_label_is_rejected(self) -> None:
        errors = validate_machine_labels(
            {"source_label": "ORIGINAL_IP", "ip_label": "ORIGINAL_IP"}
        )
        self.assertTrue(any("legacy ip_label is prohibited" in error for error in errors))

    def test_control_taxonomy_requires_impact_and_accepts_a5_authority(self) -> None:
        schema = load_json(ROOT / "schemas/control-contract.schema.json")
        instance = load_json(ROOT / "examples/registries/control-contract.json")
        instance["agent_authority"] = "A5"
        self.assertEqual([], validate_instance(instance, schema))
        del instance["impact_tier"]
        errors = validate_instance(instance, schema)
        self.assertTrue(any("missing required property 'impact_tier'" in error for error in errors))

    def test_invalid_source_label_is_rejected(self) -> None:
        errors = validate_machine_labels({"source_label": "OFFICIAL_MAPPING"})
        self.assertTrue(any("is not a canonical value" in error for error in errors))

    def test_graph_validation_rejects_dangling_edge(self) -> None:
        thread = load_json(ROOT / "examples/registries/assurance-thread.json")
        evidence = load_json(ROOT / "examples/registries/evidence-record.json")
        thread["edges"][0]["to"] = "MISSING-NODE-001"
        errors = validate_assurance_graph(thread, evidence, load_registries())
        self.assertTrue(any("unresolved target node MISSING-NODE-001" in error for error in errors))

    def test_graph_validation_rejects_configuration_mismatch(self) -> None:
        thread = load_json(ROOT / "examples/registries/assurance-thread.json")
        evidence = load_json(ROOT / "examples/registries/evidence-record.json")
        thread["authorization"]["configuration_digest"] = "sha256:" + "2" * 64
        errors = validate_assurance_graph(thread, evidence, load_registries())
        self.assertIn("authorization configuration digest does not match thread system", errors)

    def test_graph_validation_rejects_duplicate_node(self) -> None:
        thread = load_json(ROOT / "examples/registries/assurance-thread.json")
        evidence = load_json(ROOT / "examples/registries/evidence-record.json")
        thread["nodes"].append(copy.deepcopy(thread["nodes"][0]))
        errors = validate_assurance_graph(thread, evidence, load_registries())
        self.assertTrue(any("duplicate node OBJ-CUSTOMER-SERVICE-001" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
