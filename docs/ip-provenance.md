# Source, mapping, and original-IP boundary

## Required labels

### SOURCE FRAMEWORK

Existing third-party concepts, facts, standards, frameworks, tools, or practices. Cite the authoritative source and version. Do not claim ownership.

### DERIVED MAPPING

An EAA-RIF interpretation that relates source concepts, activities, artifacts, roles, or outcomes. State clearly that the mapping is not official.

### ORIGINAL IP

An EAA-RIF name, integrated method, schema, decision model, trace rule, control pattern, gate logic, example, or implementation asset created for this framework. The underlying generic ideas may still be industry knowledge.

## Register

### SOURCE FRAMEWORK

Do not claim as original:

- TOGAF, the ADM, architecture domains, principles, requirements management, architecture repository, architecture governance, implementation governance, or change concepts;
- NIST AI RMF functions, categories, subcategories, trustworthiness characteristics, profiles, Playbook suggestions, and AI actor/lifecycle concepts;
- NIST CSF 2.0 functions, profiles, tiers, or outcomes;
- NIST adversarial-machine-learning taxonomy and terminology;
- ISO/IEC 42001 AI management-system requirements or ISO/IEC 23894 risk-management guidance;
- MITRE ATLAS tactics, techniques, mitigations, matrices, and case studies;
- RACI, three-lines models, policy-as-code, CI/CD, zero trust, model/system cards, risk/control registers, maturity levels, and standard control types; or
- third-party products, languages, and tool capabilities.

### DERIVED MAPPING

Always label these as non-official interpretation:

- any TOGAF activity or artifact relationship to GOVERN, MAP, MEASURE, or MANAGE;
- relationships between architecture gates and NIST AI RMF outcomes;
- mappings from NIST outcomes to enterprise roles, artifacts, controls, or technologies;
- mappings from ISO, NIST CSF, MITRE ATLAS, law, or regulation into the EAA-RIF control graph; and
- project-specific control selections, metrics, thresholds, and residual-risk decisions.

Recommended disclaimer:

> This mapping is an EAA-RIF architecture interpretation. It is not an official crosswalk or endorsement published by NIST or The Open Group.

### ORIGINAL IP

The following integrated specifications are candidate reusable EAA-RIF IP:

- the seven-layer EAA-RIF integration model and layer contracts;
- the Architecture-to-Evidence assurance-thread method;
- the versioned assurance graph, object model, relationship types, and completeness rules;
- the seven governance and assurance gates with material-change re-entry logic;
- separation of architecture approval, domain control approval, independent assurance, release authorization, and residual-risk acceptance;
- dual classification of system impact and agent authority;
- the control-contract and evidence-record schemas;
- the Evidence Spine, evidence-quality dimensions, and control-health states;
- the Governance-as-Code chain integrating policy, tests, telemetry, evidence, exceptions, and reauthorization;
- the Agentic Action Envelope, Deterministic Action Boundary, Trust-Graded Context Envelope, Safe-Degradation Contract, and Delegation Ceiling;
- the exact-plan approval and single-use action-capability pattern;
- the template field structures, worked traceability chains, and reference implementations;
- measurable maturity claim rules and phased adoption method; and
- the mapping matrix's original selection method, classification rationale, and presentation—not the source-framework concepts or relationships themselves—and the case-study synthesis.

The defensible IP lies in the names, precise schemas, relationship rules, decision logic, integrated method, curated examples, and versioned implementation assets—not ownership of the generic idea of governance, traceability, or controls.

## Artifact metadata

Every governed artifact should include:

```yaml
artifact_id: unique-stable-id
title: human-readable-name
source_label: SOURCE_FRAMEWORK | DERIVED_MAPPING | ORIGINAL_IP
eaa_rif_version: 0.1.0
artifact_version: 1.0.0
owner: accountable-maintainer
status: draft | approved | superseded | retired
source_frameworks:
  - name: NIST AI RMF
    version: "1.0 / NIST AI 100-1"
    url: https://doi.org/10.6028/NIST.AI.100-1
derivation_note: concise explanation of adaptation or original contribution
license: CC-BY-4.0 | Apache-2.0 | third-party
reviewed_on: 2026-11-09
next_review: organization-defined
```

`source_label` is the canonical machine field. Its closed vocabulary is `SOURCE_FRAMEWORK`, `DERIVED_MAPPING`, or `ORIGINAL_IP`; implementations must not introduce `ip_label` as an alias.

## Publication safeguards

- Use original diagrams and language.
- Do not include copied TOGAF figures, tables, templates, or substantial wording.
- Do not reproduce ISO/IEC clauses beyond permitted citation or short description.
- Keep framework trademarks and ownership notices.
- Preserve source URLs, versions, and access/review dates.
- Separate neutral public IP from corporate, client, or confidential branding and data.
- Review The Open Group licensing terms before commercial client use involving TOGAF material.
- Perform a trademark and legal review before registering or commercializing the EAA-RIF name.

## Versioning policy

EAA-RIF follows semantic versioning for its own schemas and methods:

- **MAJOR:** incompatible graph, gate, schema, or decision-right change;
- **MINOR:** backward-compatible capability, mapping, template, or control addition; and
- **PATCH:** clarification, citation refresh, typo, or compatible example repair.

Mappings also record their source version. A source-framework update does not silently replace the prior mapping; it creates a new reviewed mapping version and an impact assessment.
