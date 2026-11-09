# Practical templates

These **ORIGINAL IP** templates are starting points. Tailor fields, risk scales, approval authorities, retention, and legal requirements to the enterprise and jurisdiction.

| Template | Primary decision supported |
|---|---|
| [AI Architecture Review](ai-architecture-review.md) | Is the target design fit, coherent, conformant, operable, and governable? |
| [AI Risk Assessment](ai-risk-assessment.md) | What risk exists in context and what treatment is required? |
| [Architecture Decision Record](architecture-decision-record.md) | Why was a material architecture choice made and what does it change? |
| [AI Risk Register](ai-risk-register.md) | What material risks, owners, treatments, thresholds, and decisions remain open? |
| [AI Control Register](ai-control-register.md) | Which controls treat which risks, where do they operate, and what evidence exists? |
| [Agent Risk Assessment](agent-risk-assessment.md) | What authority, tools, data, delegation, and failure modes does an agent have? |
| [AI Governance Gate](ai-governance-gate.md) | Can the system/configuration proceed, under what conditions, and until when? |
| [AI System Card](ai-system-card.md) | What is the system, what can it do, what are its limits, and what is its current authorization? |
| [AI Assurance Report](ai-assurance-report.md) | What evidence supports which assurance conclusion for which scope and period? |
| [Policy-as-Code Specification](policy-as-code-specification.md) | How does a human requirement become an executable, testable decision? |
| [Control Evidence Record](control-evidence-record.md) | What evidence was produced, for which control/version, with what integrity and result? |
| [Exception / Risk-Acceptance Record](exception-risk-acceptance.md) | Who accepts which deviation and residual risk, with what bounds and expiry? |

## Common envelope

The individual template files contain artifact-specific body sections and intentionally do not repeat this envelope. Every project artifact must prepend this envelope, or implement the same fields in its governing system of record, before the template body is completed.

The common envelope is:

```yaml
artifact_id: TYPE-0001
system_id: SYS-0001
title: descriptive title
version: 1.0.0
status: draft | in_review | approved | superseded | retired
owner: accountable role or named owner
approver: decision authority
impact_tier: low | moderate | high | critical
risk_tier: low | moderate | high | critical
agent_authority: A0 | A1 | A2 | A3 | A4 | A5 | not_applicable
environment: sandbox | development | test | staging | production
effective_date: YYYY-MM-DD
review_date: YYYY-MM-DD
classification: public | internal | confidential | restricted
source_label: SOURCE_FRAMEWORK | DERIVED_MAPPING | ORIGINAL_IP
source_links: []
related_object_ids: []
change_history: []
```

`impact_tier` records the consequence-severity input. `risk_tier` is the resulting governance classification after context, exposure, uncertainty, controls, and `agent_authority` are considered. `agent_authority` is the only canonical machine field for the A0–A5 scale; “autonomy” may appear in display labels but must not be stored as a separate level.

Use stable identifiers rather than filenames or free-text names for cross-artifact references.
