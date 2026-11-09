# Critical analysis and anti-theatre safeguards

EAA-RIF is deliberately challengeable. The framework can fail even when every template is complete.

## Structural limitations

### TOGAF may be too architecture-centric

Architecture methods are strong at structure, dependencies, target state, and change governance. They do not by themselves prove how a statistical or generative system behaves in deployment. Teams can produce elegant target views while missing representativeness, emergent behavior, human factors, or rare harmful outcomes.

**Safeguard:** architecture gates must identify required independent TEVV and runtime evidence. Architecture conformance never substitutes for AI assurance.

### NIST AI RMF is intentionally non-prescriptive

**SOURCE FRAMEWORK:** NIST supplies outcomes and a flexible risk vocabulary rather than mandatory controls, metrics, thresholds, or a project method; see the [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [Playbook](https://airc.nist.gov/airmf-resources/playbook/). Two organizations can both claim alignment while applying very different rigor.

**Safeguard:** EAA-RIF defines explicit control contracts, evidence quality, decision rights, and versioned profiles while retaining the label **DERIVED MAPPING**.

### Implementation can become complex

Stable identifiers, policy services, evaluation suites, evidence integrity, cross-system telemetry, and multiple authorities require investment. A premature enterprise-scale platform can cost more than it solves.

**Safeguard:** start with one end-to-end assurance thread; automate only repeated decisions and evidence with clear value.

### Ownership conflicts are inevitable

Enterprise Architecture, AI Governance, CISO, Privacy, Compliance, MRM, Data Governance, Platform, and business teams may each believe they approve “the system.” This creates duplicated review, unclear vetoes, and risk orphaning.

**Safeguard:** define the decision object and one accountable owner. Architecture fitness, domain conformance, assurance conclusion, production authorization, and residual-risk acceptance are separate records.

### Governance can drive shadow AI

If all systems face the same heavyweight process, teams avoid registration or use unapproved tools.

**Safeguard:** use impact and authority tiers, standard patterns, delegated automated gates, review service levels, and an easy registration path. Consequential deviations receive deeper review.

## Automation limitations

### Policy-as-Code covers only codifiable decisions

Structured rules can enforce identity, classification, scope, limits, versions, and approvals. They cannot decide whether a purpose is legitimate, a fairness trade-off is acceptable, an explanation is meaningful, or residual harm is justified.

**Safeguard:** mark controls as deterministic, probabilistic, manual, or hybrid. Define the human decision and evidence surrounding automated outputs.

### Probabilistic evaluation can create false confidence

Evaluation data may be unrepresentative. Rare failures may be missed. LLM-as-judge methods can share biases and failure modes with the system under test. Aggregate scores can hide severe subgroup or tail risk.

**Safeguard:** combine deterministic invariants, statistical evaluation, adversarial testing, human research, independent challenge, production outcomes, and uncertainty/coverage disclosure.

### Guardrails are neither perfect nor authoritative

Content and injection controls can be bypassed, conflict, increase latency, and degrade under distribution shift. A guardrail may also be unavailable while the model remains reachable.

**Safeguard:** keep authority and transaction limits outside the model; test guardrail failure; define fail-safe modes; minimize blast radius.

### Monitoring creates its own privacy and security risk

Prompts, retrieved content, tool arguments, and outputs may contain personal data, secrets, intellectual property, or regulated records.

**Safeguard:** collect structured metadata and hashes by default; capture content only for an approved purpose; redact, encrypt, restrict, retain minimally, and disclose limitations.

### Provider opacity limits assurance

Organizations may lack visibility into model training data, architecture, safety controls, changes, incidents, and internal evaluations.

**Safeguard:** state assurance limitations; require contractual evidence/change notice; use provider-independent system controls; pin versions where possible; maintain fallback and exit plans.

## Human limitations

### Oversight can become rubber-stamping

Reviewers may lack time, authority, competence, context, or a credible alternative. High model confidence and repetitive approvals encourage automation bias.

**Safeguard:** test human oversight with seeded errors and time pressure; measure detection, rejection, escalation, and latency; display evidence and uncertainty; preserve authority to stop; staff the role.

### Residual-risk acceptance can become ritual

A named executive may sign a record without understanding exposure, uncertainty, or control weakness.

**Safeguard:** present cause-event-impact scenarios, control evidence quality, credible loss/harm range, unresolved uncertainty, conditions, and triggers. Escalate beyond delegated authority.

### Fairness and affected-party impact require contextual judgment

No single metric captures fairness. Quantitative parity can conflict with validity, privacy, accessibility, legal duties, and differentiated needs.

**Safeguard:** combine relevant metrics with qualitative impact analysis, affected-party input, recourse, and documented trade-offs. Do not claim universal fairness.

## Agentic and multi-agent limitations

- Long-horizon behavior creates failure combinations that test sets may not cover.
- Tool results, peers, memory, and environment become additional untrusted instruction channels.
- Delegation obscures identity, causality, separation of duties, and responsibility.
- Irreversible external actions cannot always be rolled back.
- Emergent coordination can exceed the intent of any individual agent design.
- Resource loops can cause financial, operational, or denial-of-service harm.

**Safeguards:** use hard authority ceilings, per-action authorization, subject chains, typed tools, step/time/cost/transaction budgets, limited recursion, isolation, simulation, canary/shadow operation, idempotency, compensating actions, and rapid suspension. A5 delegated autonomy should be exceptional and frequently reauthorized.

## Governance-theatre failure modes

| Theatre signal | Why it fails | Required challenge |
|---|---|---|
| Every mapping cell is marked “direct” | Similar vocabulary replaces analysis | Maintain weak/no-mapping cases and rationale |
| A framework alignment badge is treated as compliance | Voluntary frameworks do not establish legal compliance | Map actual obligations and obtain legal/compliance judgment |
| A green dashboard has no scope or evidence provenance | Presence of data is mistaken for effectiveness | Show version, coverage, freshness, uncertainty, and control failure behavior |
| More controls always means lower risk | Controls can conflict, fail, or create new harms | Test the control objective and side effects |
| Architecture review approves model risk | Wrong authority and method | Require independent model/system validation |
| A human approval step is assumed meaningful | The human may lack information or power | Test oversight performance and workflow conditions |
| Red teaming is a one-time launch event | Threats, models, prompts, and tools change | Maintain regression scenarios and runtime triggers |
| Prompt logs are called an audit trail | Logs may omit identity, policy decision, tool result, and business outcome | Use the structured Evidence Spine |
| An expired exception remains operational | Temporary risk silently becomes permanent | Enforce expiry and deny/restrict automatically |
| Artifact count is a maturity measure | Documentation can coexist with control failure | Measure operating effectiveness and outcomes |

## Anti-theatre operating rules

1. Scale review and evidence to `impact_tier`, `risk_tier`, and `agent_authority`.
2. Maintain a “no meaningful mapping” register and publish disputed mappings.
3. Use one evidence packet across boards; each body records only its decision.
4. Treat every control as a falsifiable hypothesis with explicit failure behavior.
5. Separate control operation, independent validation, and audit.
6. Combine deterministic, statistical, adversarial, human, and production evidence.
7. Rate evidence quality across provenance, integrity, freshness, coverage, representativeness, independence, and interpretability.
8. Test rollback, kill switch, safe mode, and human escalation rather than only documenting them.
9. Track near misses, complaints, overrides, and false denials alongside technical metrics.
10. Audit incentives and business pressure around gates and exceptions.
11. Time-bound assurance and reauthorize on material change.
12. Keep hard authorization and transaction boundaries outside the model.

## Known non-goals

EAA-RIF does not:

- certify conformity to TOGAF, NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, or regulation;
- prescribe universal risk thresholds or fairness metrics;
- replace enterprise risk management, cybersecurity, privacy, legal, MRM, safety, quality, or audit methods;
- guarantee that automated controls prevent all AI harm;
- require every source framework or tool for every system; or
- establish ownership of third-party intellectual property.
