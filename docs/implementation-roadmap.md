# Implementation roadmap

> **PROPOSED MODEL — ORIGINAL IP:** The roadmap builds one complete assurance thread first, then scales shared controls. It avoids launching a large governance program before proving the operating loop.

## Phase 0 — mobilize and baseline, weeks 0–6

### Actions

- Name the executive sponsor, EAA-RIF owner, and accountable domain authorities.
- Define scope, `impact_tier`, `risk_tier`, `agent_authority`, principles, and decision rights.
- Inventory material AI systems, models, RAG sources, agents, tools, providers, and current governance.
- Baseline maturity and identify one consequential but bounded pilot.
- Establish source-version, IP-label, licensing, and evidence-handling conventions.

### Exit criteria

- accountable owners and decision authorities;
- approved pilot and business objective;
- initial inventory with impact/authority classification;
- minimum governance and exception model; and
- confirmed authoritative source baseline.

## Phase 1 — minimum viable EAA-RIF, weeks 6–12

### Actions

- Implement stable identifiers and the A2E trace schema.
- Publish the twelve project templates and G0–G4 gate criteria.
- Define the first control contracts, evidence records, and completeness rules.
- Apply the lifecycle to the pilot from context through residual-risk decision.
- Measure missing links, duplicate reviews, decision lead time, and evidence effort.

### Exit criteria

- one end-to-end assurance thread with real evidence;
- architecture, domain-control, assurance, and residual-risk decisions recorded separately;
- at least five material risks linked to enforceable controls and evidence; and
- a retrospective with process and schema changes.

## Phase 2 — engineer reusable controls, months 3–6

### Actions

- Build reference architectures and a versioned control library.
- Establish policy source control, review, unit testing, signing, distribution, rollback, and exceptions.
- Add CI/CD schema, trace, policy, evaluation, dependency, and signature gates.
- Build representative evaluation data, red-team scenarios, and release attestations.
- Instrument model, retrieval, agent, tool, policy, and outcome traces.
- Create the evidence store and control-health state machine.

### Exit criteria

- repeatable deployment gate and runtime evidence for at least two AI patterns;
- tested policy and safe-degradation behavior;
- current evidence for critical controls; and
- control reuse and false-decision measures.

## Phase 3 — scale as an enterprise service, months 6–12

### Actions

- Offer shared identity, policy, evaluation, guardrail, telemetry, and evidence services.
- Establish model, prompt, data, RAG, tool, agent, provider, and policy catalogs.
- Introduce a self-service standard path for low-impact patterns and enhanced review for consequential systems.
- Train architects, product/risk owners, engineers, validators, operators, and auditors by role.
- Extend to bounded-action and multi-agent patterns with delegation and resource ceilings.
- Integrate portfolio, service, incident, privacy, data, security, and model-risk workflows through identifiers and events.

### Exit criteria

- most new material AI systems use shared patterns and trace schema;
- high-impact systems pass the full gate and evidence model;
- low-risk standard changes move quickly through delegated automation; and
- duplicated reviews and unowned findings trend down.

## Phase 4 — continuous assurance, months 12–18

### Actions

- Automate eligible evidence collection, freshness, exception expiry, drift, and material-change triggers.
- Analyze control effectiveness, correlated failure, near misses, complaints, and overrides.
- Add periodic reauthorization and portfolio risk reporting.
- Add regulatory/standard mappings as separate views over the core control graph.
- Test rapid restriction, provider exit, rollback, kill switch, evidence continuity, and manual fallback.
- Commission an independent assessment of EAA-RIF itself.

### Exit criteria

- current control evidence and authorization state available without a manual audit-pack exercise;
- material change reliably invokes reassessment;
- critical failures cause tested safe action; and
- governance measures include outcome and control effectiveness, not only artifact completion.

## First 90-day pilot plan

| Week | Outcome | Deliverables |
|---|---|---|
| 1–2 | Sponsorship and scope | Charter, decision rights, pilot, source/version register |
| 3–4 | Context and architecture | Objective, alternatives, domain views, ADRs, impact and authority tier |
| 5–6 | Risk and controls | Risk/agent assessments, threat model, control contracts, evidence plan |
| 7–9 | Implementation and tests | Policy examples, CI gate, evaluation/red-team set, telemetry, runbooks |
| 10–11 | Assurance and decision | Independent findings, control evidence, system card, residual-risk record |
| 12–13 | Restricted pilot and learning | Staged release, outcome/incident review, framework backlog, scale decision |

## Outcome measures

- AI systems with named business, product, risk, and control owners.
- Architecture decisions linked to risks and controls.
- High-risk controls with current, representative evidence.
- Runtime decisions traceable to approved policy and configuration versions.
- Exceptions by age, scope, recurrence, and overdue remediation.
- Mean time to detect and contain a failed control.
- Time from material change to evidence invalidation and reassessment.
- False-allow and false-deny rates for automated controls.
- Evaluation coverage across intended, foreseeable, misuse, and prohibited scenarios.
- Production incidents attributable to missing, failed, bypassed, or misdesigned controls.
- Control and architecture-pattern reuse.
- Decision lead time by impact tier and change class.
- Production releases missing a complete assurance thread.

## Adoption risks and mitigations

| Adoption risk | Safeguard |
|---|---|
| Too many gates drive shadow AI | Tiered evidence, delegated authority, reusable standard patterns, clear service levels |
| Boards duplicate questions | One evidence packet; each board records only its own decision |
| Tooling precedes operating model | Prove a manual A2E thread before automating it |
| “Green” evidence hides poor quality | Score provenance, freshness, coverage, representativeness, independence, and limitations separately |
| Business ownership remains vague | No production authorization without a named residual-risk owner |
| Exceptions become permanent | Dual-key approval, monitoring, hard expiry, revocation, recurrence analysis |
| Platform team self-approves | Independent control owners and validators; separation of duties |
| Agent authority grows silently | Separate `agent_authority` classification, configuration binding, material-change trigger, per-action policy |

## Version maintenance

At least quarterly, and after any material source change:

1. review NIST AI RMF status, Playbook, profiles, NIST security guidance, MITRE ATLAS, and relevant ISO metadata;
2. record version/date and affected EAA-RIF mappings;
3. update mappings as a new version rather than silently overwriting historical decisions;
4. identify which system approvals, controls, tests, or evidence become stale; and
5. issue a migration note with required enterprise actions.
