# EAA-RIF core model

## Framework identity

**EAA-RIF** means **Enterprise AI Architecture & Risk Integration Framework**. Its operational method is **Architecture-to-Evidence (A2E)**.

> **PROPOSED MODEL — ORIGINAL IP:** EAA-RIF connects business intent, architecture decisions, AI risks, control requirements, executable policies, runtime events, evidence, and residual-risk decisions through a versioned traceability graph.

EAA-RIF is an integration overlay. It does not merge TOGAF and NIST AI RMF, replace either framework, or claim an official crosswalk.

## Design principles

1. **Complement, do not collapse.** Architecture, AI risk, security, privacy, model validation, compliance, and business accountability keep distinct purposes.
2. **Context precedes scoring.** Intended purpose, affected parties, data, environment, and authority define the risk before a rating can be meaningful.
3. **Every decision has one accountable owner.** A committee can advise or govern a process, but accountability remains named.
4. **Architecture approval does not accept business risk.** Architects approve target-state fitness and conformance.
5. **Controls execute at the closest authoritative point.** Authentication belongs to identity services; transaction authorization belongs to the transaction service; content evaluation belongs at model/application boundaries.
6. **Hard authority remains deterministic.** Identity, permissions, monetary limits, transaction rules, and safety stops do not depend on an LLM's self-assessment.
7. **Evidence is part of control design.** Each control defines what proof it emits, when, with what provenance, and how failure appears.
8. **Assurance is scoped, versioned, and time-bound.** Approval attaches to a configuration and deployment context, not a product name.
9. **Agent authority increases assurance depth.** A higher `agent_authority` requires stronger containment, observability, testing, and reauthorization.
10. **Runtime evidence can reopen upstream decisions.** Drift, incidents, complaints, provider change, and control degradation may trigger redesign.
11. **No owner means no valid acceptance; no evidence means no assurance claim.**
12. **Exceptions expire.** An exception is a bounded risk decision with compensating controls, monitoring, and a revocation trigger.

## Seven coupled operating layers

**SOURCE FRAMEWORK:** NIST describes GOVERN as cross-cutting and the Core functions as iterative rather than a mandatory sequence; see the [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [Playbook](https://airc.nist.gov/airmf-resources/playbook/). The EAA-RIF layers describe accountability and information flow, not a waterfall. MAP, MEASURE, and MANAGE may recur wherever context or evidence changes.

| Layer | Responsibility | Primary inputs | Primary outputs | Accountable owner | Decision rights | Core artifacts |
|---|---|---|---|---|---|---|
| **1. Business Strategy & Risk Appetite** | Define outcome, permissible and prohibited use, affected parties, impact tolerance, agent-authority ceiling, geography, and accountable executive. Ask whether AI is appropriate. | Strategy, customer commitments, laws, regulation, ethical commitments, process context | Use-case charter, success/harm criteria, impact tier, agent-authority ceiling, risk appetite, named risk owner | Business executive | Sponsor, narrow, defer, choose non-AI, or stop; accept business residual risk within authority | Objective record, stakeholder/harm map, alternatives assessment, prohibited-use statement |
| **2. Enterprise Architecture & Portfolio Governance** | Place the use case within capabilities, processes, information, applications, technology, sourcing, roadmaps, and dependencies. | Layer 1, baseline/target architecture, standards, platform catalog, portfolio constraints | Target architecture, option decision, standards disposition, transition roadmap, architecture exceptions | Chief/enterprise architect and EAB | Approve architecture direction and conformance; does not accept domain or business risk | Domain views, ADRs, dependency map, standards assessment, roadmap |
| **3. AI System Architecture & Engineering** | Define system boundary and decompose models, data, prompts, RAG, memory, agents, tools, identities, APIs, humans, and suppliers. | Approved intent, impact tier, data products, platform capabilities, standards | Implementable design, authority envelope, interfaces, trust boundaries, assurance hooks | Lead enterprise/AI architect (design); AI product owner (delivery) | Architect exercises design authority; product owner executes delivery within the approved design; material deviation escalates | Context/decomposition, lineage, threat boundaries, tool matrix, human oversight, AI BOM, SLOs |
| **4. AI Risk & Governance** | Identify risk scenarios and evaluate security, privacy, fairness, safety, robustness, transparency, legal, model, supplier, and human-factor risk. | Layers 1–3, threat intelligence, obligations, incidents, affected-party input | Risk baseline, governance requirements, control objectives, assurance criteria, treatment, residual-risk thresholds | Business risk owner plus domain policy owners | Domain owners judge conformance; business owner accepts residual risk; high impact escalates | Risk/impact/agent assessments, risk and control registers, threat model, assurance plan |
| **5. Control Engineering & Delivery Assurance** | Convert control objectives into versioned control contracts, policies, tests, evaluations, infrastructure controls, guardrails, and procedures. | Approved control objectives, evidence criteria, design, thresholds | Implemented controls, policy bundles, evaluation results, attestations, findings | Product owner and relevant control owner | Control owner approves design; engineering implements; validators challenge; release authority gates | Control contracts, policy code/tests, eval suites, red-team report, build provenance, runbooks |
| **6. Runtime Assurance & Operations** | Enforce identity, authorization, access, tool permissions, transaction limits, approvals, guardrails, thresholds, rollback, and incident response. | Approved policies, limits, authority envelope, monitoring and response rules | Decisions, alerts, interventions, traces, control-health signals, incidents | Service owner | Operators may contain, suspend, roll back, or fail safe; they cannot expand appetite or authority | Decision logs, traces, dashboards, incidents, kill-switch tests, control-health reports |
| **7. Evidence & Continuous Governance** | Preserve evidence integrity, assess operating effectiveness, update residual risk, expire exceptions, reauthorize, restrict, redesign, or retire. | Gate evidence, runtime outcomes, incidents, complaints, provider/regulatory/threat change | Assurance conclusions, corrective actions, updated risk, reauthorization or retirement | AI Governance and enterprise risk, with independent assurance | Governance reauthorizes or restricts; Internal Audit independently assesses the system of governance | Evidence graph, assurance report, exception aging, periodic decision, audit pack, change backlog |

Rows that name more than one authority summarize several linked decision objects. In an implementation, each architecture decision, control disposition, assurance conclusion, release authorization, and residual-risk decision has exactly one accountable owner.

## The A2E assurance thread

The reusable unit of governance is an **assurance thread**:

`BusinessObjective → ArchitecturePrinciple → ArchitectureDecision → Risk → Requirement → Control → Policy/Test → EnforcementPoint → Evidence → ResidualRisk → GateDecision`

### Core objects

| Object | Minimum attributes |
|---|---|
| System | `system_id`, owner, purpose, `impact_tier`, `risk_tier`, `agent_authority`, lifecycle state, approved version/context |
| BusinessObjective | desired outcome, success measure, affected parties, accountable executive |
| ArchitectureDecision | context, options, rationale, consequences, assumptions, reversibility, linked risks |
| Risk | cause-event-impact scenario, affected parties/assets, inherent/residual rating, uncertainty, owner, trigger |
| Requirement | source, normative statement, scope, testability, owner, effective date |
| Control | objective, owner, operator, lifecycle point, mode, dependencies, failure behavior |
| Policy | trusted input schema, decision logic, outputs/reason codes, version, signer, deployment location |
| EnforcementPoint | component that can actually allow, deny, transform, limit, suspend, or escalate |
| Evidence | producer, source, time, scope, result, raw pointer, hash, classification, retention, reviewer |
| Exception | deviation, scope, policy owner, risk owner, compensating control, expiry, revocation trigger |
| GateDecision | decision, authority, system/configuration scope, conditions, evidence snapshot, expiry |
| Actor | named person or accountable role, authority, delegation, separation-of-duty constraints |

### Completeness rules

- Every production AI system has an accountable business owner, product owner, `impact_tier`, `risk_tier`, `agent_authority`, and current authorization.
- Every material architecture decision links to affected objectives, risks, and controls.
- Every material risk has an owner, treatment, residual status, and reassessment trigger.
- Every required control has an owner, implementation, test, evidence contract, and failure behavior.
- Every policy decision traces backward to a control and forward to an evidence record.
- Every exception identifies scope, policy owner, risk owner, compensating controls, expiry, and revocation trigger.
- Every approval binds to a system version, configuration digest, environment, intended use, and validity period.

The model is logically a graph even when implemented with relational tables and stable IDs. A folder of documents is not a traceability model until relationships and completeness are machine-checkable.

## Seven governance and assurance gates

A gate is a recorded decision. It does not require a meeting when evidence and delegated authority are clear.

| Gate | Decision | Minimum evidence | Primary decision right |
|---|---|---|---|
| **G0 Registration & Triage** | Register, sandbox, enhance review, prohibit, or return | Purpose, owners, AI type, affected parties, data class, providers, `agent_authority`, preliminary impact | AI Governance triage authority |
| **G1 Architecture Intent** | Approve direction, require alternative, or reject | Non-AI alternative, boundary, target views, sourcing, data flows, trust boundaries, standards, roadmap | Enterprise Architecture Board |
| **G2 Risk & Control Design** | Approve control design baseline, constrain, or return | Risk/impact/agent assessments, threat model, privacy/data review, control contracts, evaluation and evidence plans | AI Governance gate with explicit domain-owner dispositions |
| **G3 Pre-production Assurance** | Evidence sufficient, conditional pilot, remediate, or reject | Implemented tests, evaluations, red-team findings, provenance, supplier evidence, operational readiness, rollback/kill-switch exercise | Independent validators and control owners provide conclusions; gate authority decides readiness |
| **G4 Production Authorization** | Authorize, time-bound authorize, restrict, or reject | Named risk owner, residual-risk decision, approved configuration, monitoring, incident ownership, support, expiry, release attestation | Delegated release authority and business risk owner within their separate authorities |
| **G5 Continuous Release & Runtime Conformance** | Allow standard change, block, roll back, or send to earlier gate | Trace completeness, policy/eval regression, signed artifacts, approved dependencies, fresh evidence, current exceptions, drift status | Automated gate for pre-authorized low-risk change; material change escalates |
| **G6A Architecture/Change Reauthorization or Retirement Disposition** | Continue, restrict, rework, suspend, or retire the approved configuration or use | Runtime outcomes, incidents, complaints, drift, material change, required architecture/domain dispositions, provider/obligation changes, exception state | Named reauthorization authority |
| **G6B Residual-Risk Acceptance** | Accept, conditionally accept, escalate, or reject the residual risk for the proposed disposition | Current residual-risk statement, control/evidence limitations, conditions, acceptance authority, and expiry | Business risk owner within delegated authority |

G6 produces two separately accountable records: the named reauthorization authority owns the lifecycle disposition after required architecture and domain reviews; the business risk owner separately owns residual-risk acceptance. Neither decision substitutes for the other, and reauthorization cannot proceed when required residual risk is not accepted within authority.

“Approved with conditions” always identifies conditions, owner, monitoring, and expiry. It cannot become a permanent status.

## Three-axis classification: impact, risk, and authority

These fields are related but not interchangeable:

| Machine field | Meaning | Assignment use |
|---|---|---|
| `impact_tier` | Consequence-severity input: the plausible magnitude of harm if the use case fails, is misused, or produces an adverse outcome. | Established during context and impact analysis before the governance classification is finalized. |
| `risk_tier` | Resulting governance classification after `impact_tier`, likelihood/exposure, uncertainty, context, control dependence, and `agent_authority` are considered. | Drives gate depth, approval authority, assurance independence, monitoring, and reauthorization cadence. |
| `agent_authority` | Maximum approved action authority on the A0–A5 scale. | Constrains tool access, delegation, human approval, deterministic authorization, and runtime containment. |

A read-only agent handling highly sensitive data can have `agent_authority: A1`, `impact_tier: high`, and `risk_tier: high`. “Autonomy” is descriptive display language only; it is not a separate machine field. Named labels such as “A5 Delegated Autonomy” map to `agent_authority: A5`.

| Authority | Capability | Required boundary |
|---|---|---|
| **A0 Generate/Observe** | No tool or state-changing access | Output-only; content controls and disclosure |
| **A1 Read** | Approved read-only retrieval or APIs | Subject/purpose authorization and data minimization |
| **A2 Recommend** | Prepares an action; human independently executes | Clear evidence, uncertainty, alternatives, and accountability |
| **A3 Propose** | Creates a binding request; human approves exact action | Exact-plan hash, fresh approval, backend reauthorization |
| **A4 Bounded Execute** | Executes pre-authorized, reversible actions within deterministic limits | Per-action policy, scoped identity, limits, idempotency, containment |
| **A5 Delegated Autonomy** | Dynamically chooses/delegates consequential actions or coordinates agents | Exceptional approval, constrained delegation, causal traces, simulation, budgets, isolation, frequent reauthorization |

## Agentic control patterns

> **PROPOSED MODEL — ORIGINAL IP**

- **Agentic Action Envelope:** explicit bounds on purpose, data, tools, steps, time, cost, monetary exposure, reversibility, and approval.
- **Deterministic Action Boundary:** the model proposes; authoritative policy and transaction services authorize and execute.
- **Trust-Graded Context Envelope:** system policy, verified user facts, governed enterprise content, and untrusted content retain distinct trust labels.
- **Evidence Spine:** correlates intent, identity, context, model/version, retrieved sources, plan, policy decision, approval, tool/API result, and outcome.
- **Safe-Degradation Contract:** predefines abstain, escalate, read-only, manual fallback, suspend, compensate, and roll back.
- **Delegation Ceiling:** a sub-agent cannot inherit or amplify authority beyond the originating subject and approved purpose.

## Control-health states

| State | Meaning | Default governance response |
|---|---|---|
| **Designed** | Objective and contract approved; implementation incomplete | No production reliance |
| **Implemented** | Enforcement exists; evidence incomplete or not independently tested | Pre-production only |
| **Effective** | Current evidence supports design and operating effectiveness for stated scope | Eligible for authorization |
| **Degraded** | Partial failure, stale evidence, drift, or threshold warning | Constrain, increase review, or time-bound exception |
| **Failed** | Control did not achieve the objective or cannot prove operation | Block, fail safe, contain, or suspend |
| **Superseded** | Replaced by a new version | Prevent new reliance; preserve historical evidence |
| **Retired** | No longer active | Confirm removal, data disposition, and dependency closure |

## Evidence quality model

Evidence should be assessed across independent dimensions rather than collapsed into one reassuring score:

- **Provenance:** who or what produced it, from which system and version.
- **Integrity:** hashes, signatures, immutability, and access controls.
- **Freshness:** whether it reflects the current configuration and context.
- **Coverage:** which control population, scenarios, users, and environments it represents.
- **Representativeness:** whether test data and conditions reflect intended and misuse contexts.
- **Independence:** whether the assessor or evidence producer is sufficiently independent for the claim.
- **Interpretability:** whether a decision maker can understand scope, result, limitations, and uncertainty.

Evidence presence is not evidence quality. A dashboard can be complete and still provide false assurance.

## Architectural answer

An enterprise connects architecture decisions, AI risks, controls, runtime evidence, and continuous governance by maintaining one versioned assurance thread for every material AI system. Architecture establishes context and constraints. Risk governance defines scenarios and treatment. Control engineering converts treatment into enforceable contracts. Authoritative systems enforce deterministic limits. Evaluations and telemetry measure behavior. Evidence records control performance. Accountable humans use that evidence to authorize, restrict, redesign, or retire the system.
