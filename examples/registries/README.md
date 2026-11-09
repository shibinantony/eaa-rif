# Sample governance registries

These synthetic, vendor-neutral records demonstrate one coherent Architecture-to-Evidence thread. They contain no client data and confer no real authorization.

- `system-registry.json` defines the governed configuration and accountable owners.
- `risk-registry.json` contains scenario-based risks and explicitly labels NIST alignments as derived mappings.
- `requirement-registry.json` states the governance outcomes used by the sample gate.
- `control-contract.json` is validated by `schemas/control-contract.schema.json`.
- `policy-registry.json` links the control to the illustrative OPA implementation.
- `enforcement-point-registry.json` identifies where a deny decision is made authoritative.
- `evidence-record.json` is validated by `schemas/evidence-record.schema.json`.
- `assurance-thread.json` links the objective, principle, decision, risks, requirements, control, policy, enforcement, evidence, and authorization.

Run `python tools/validate_traceability.py --root .` from the repository root to validate structure, cross-references, graph integrity, configuration binding, and decision chronology.

## Canonical machine fields

- `source_label` is one of `SOURCE_FRAMEWORK`, `DERIVED_MAPPING`, or `ORIGINAL_IP`. No `ip_label` alias is used.
- `impact_tier` is the consequence-severity input: `low`, `moderate`, `high`, or `critical`.
- `risk_tier` is the resulting governance classification after impact, exposure, uncertainty, controls, context, and agent authority are considered.
- `agent_authority` is the canonical A0–A5 machine field. “Autonomy” is display language only and does not create a second classification field.
