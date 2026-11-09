# EAA-RIF maturity model

> **PROPOSED MODEL — ORIGINAL IP:** The model measures operating capability and evidence, not document count. An enterprise cannot claim a level when a critical dimension materially lags.

## Levels

| Level | Name | Enterprise condition |
|---|---|---|
| **1** | Ad Hoc | Outcomes depend on individual effort; inventory, ownership, controls, and evidence are incomplete. |
| **2** | Documented | Policies, templates, inventory, and repeatable reviews exist, but execution and evidence remain largely manual. |
| **3** | Governed | Impact-based decision rights, gates, independent challenge, control ownership, and standard patterns operate consistently. |
| **4** | Automated | Eligible controls, tests, evidence, exceptions, and deployment/runtime decisions are versioned and automated with human oversight. |
| **5** | Continuous / Adaptive | Runtime outcomes, threat and regulatory change, and control effectiveness continuously inform governed reassessment and improvement. |

## Dimension matrix

Percentages are proposed starting thresholds. Calibrate them to scope, materiality, and measurement quality.

| Dimension | 1 — Ad Hoc | 2 — Documented | 3 — Governed | 4 — Automated | 5 — Continuous / Adaptive |
|---|---|---|---|---|---|
| Architecture | Project diagrams; portfolio dependencies unknown | Standard review template; at least 80% of known material AI systems documented | Approved reference patterns; all high-impact systems reviewed; architecture exceptions governed | Machine-readable architecture metadata, configuration binding, and drift checks | Portfolio graph supports rapid impact analysis and evidence-driven target-state change |
| Risk governance | Inconsistent assessment and unclear owners | AI inventory, owners, and manual risk assessments | Tiering, gates, delegated authority, independent challenge, residual-risk decisions | Workflow triggers reassessment, escalation, conditions, and exception expiry | Runtime outcomes continuously inform risk decisions; humans retain acceptance authority |
| AI security | Generic application security only | AI threat checklist and periodic tests | AI threat modeling, supply-chain review, red-team program, agent identity and action boundaries | Continuous attack regression, signed policies/artifacts, runtime containment | Threat intelligence updates scenarios and controls through governed rapid change |
| Control automation | Mostly manual controls and screenshots | Reusable scripts for selected systems | Enterprise control library with owners, contracts, tests, evidence definitions | At least 80% of eligible controls automatically enforced or evidenced | Control effectiveness and failure correlations drive governed adaptation |
| Policy-as-Code | Policy exists only in prose | Selected infrastructure rules are versioned | Policies link to requirements, risks, controls, owners, inputs, tests, and enforcement | Deployment/runtime enforcement uses signed bundles, decision logs, and controlled overrides | Portable policy composition, impact analysis, simulation, and continuously tested change |
| Monitoring | Infrastructure availability only | Model performance/drift monitoring for priority systems | Risk-based quality, safety, security, fairness, human and outcome thresholds | Unified model/RAG/agent/tool/policy traces with automated alerts and safe action | Cross-portfolio leading indicators, causal investigation, and tested automated containment |
| Evidence | Email, screenshots, manual packs | Central repository with owners and retention | Evidence links to controls, versions, risks, gates, and limitations | At least 90% of eligible evidence collected with provenance/integrity and freshness rules | Continuous evidence graph supports audit sampling and trigger-based reauthorization |
| Agentic AI assurance | No distinct agent control | Tool access manually constrained | `agent_authority` classification, tool registry, limits, human checkpoints, kill switch | Per-action policy, subject-chain traces, simulation, delegation ceiling, continuous regression | Multi-agent behavior continuously evaluated within hard authority and resource ceilings |

## Claim rules

An enterprise-level maturity claim should require:

- at least 80% of in-scope systems meeting the claimed level;
- 100% of the highest-impact systems meeting at least the level below it;
- no critical dimension more than one level behind the claim;
- current evidence of operating effectiveness, not policy or tooling alone; and
- a disclosed scope, assessment date, assessor, method, exceptions, and confidence level.

Maturity may differ by business unit, system type, geography, and environment. Report the distribution rather than one unqualified enterprise number.

## Measurable indicators

### Architecture

- Percentage of material AI systems with current business/data/application/technology views.
- Percentage of production configurations bound to an approved architecture decision and digest.
- Median time to identify systems affected by a provider, model, tool, data, or policy change.
- Architecture exceptions by age, recurrence, owner, and risk.

### Risk governance

- Percentage of systems with named business, product, control, and residual-risk owners.
- Percentage of high-impact systems with current context, impact, agent, and threat assessments.
- Gate decision lead time by impact and change class.
- Percentage of conditions and exceptions expired without disposition.

### AI security

- Adversarial scenarios covered by system and lifecycle stage.
- Unauthorized-action and protected-data invariants exercised per release.
- Mean time to detect, contain, and recover from an AI/control incident.
- Percentage of external models/tools/data with current provenance and supplier evidence.

### Control automation

- Percentage of eligible controls with executable policy or automated evidence.
- Policy unit-test, negative-test, and outage-test coverage.
- False-allow, false-deny, bypass, and control-unavailable rates.
- Controls with unknown or stale operating-effectiveness evidence.

### Monitoring and evidence

- Percentage of consequential actions traceable from intent through outcome.
- Evidence freshness, coverage, representativeness, integrity, and independence by critical control.
- Time from material change to evidence invalidation and reassessment.
- Incidents attributable to missing, failed, bypassed, or misdesigned controls.

### Agentic assurance

- Percentage of agents with explicit `agent_authority`, Action Envelope, tool registry, and safe-degradation contract.
- Percentage of state-changing calls with subject chain, exact plan, policy decision, and authoritative result.
- Delegation and recursion ceiling violations.
- Kill-switch, rollback, idempotency, compensation, and human-oversight test success.

## Anti-gaming rules

Do not use these as primary maturity measures:

- number of policies, templates, committees, meetings, controls, or dashboards;
- raw count of policy denials without context;
- evaluation volume without scenario coverage and data quality;
- percentage “compliant” without evidence freshness, scope, and exception state; or
- tooling deployment without proof that authoritative decisions use it.

The maturity question is whether the enterprise makes better, faster, more defensible decisions and reduces or contains harm—not whether it produces more governance artifacts.
