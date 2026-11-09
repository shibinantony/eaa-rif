# Control traceability

## Traceability model

> **PROPOSED MODEL — ORIGINAL IP:** EAA-RIF uses a versioned assurance thread rather than a control spreadsheet with free-text references.

```text
Business Objective
→ Architecture Principle
→ Architecture Decision
→ AI Risk Scenario
→ NIST AI RMF Outcome
→ Governance Requirement
→ Control Objective
→ Technical Policy or Test
→ Enforcement Point
→ Evidence
→ Residual-Risk Decision
→ Change Trigger
```

Each arrow must have a typed relationship such as `motivates`, `constrains`, `creates_risk`, `treats`, `implements`, `enforces`, `produces_evidence`, `supports_decision`, or `triggers_reassessment`.

## Worked examples

Every NIST AI RMF alignment below is an **INTERPRETATION — DERIVED MAPPING**: an EAA-RIF interpretation, not an official NIST mapping or profile.

### TR-01 — bounded transaction execution

| Trace object | Worked value |
|---|---|
| Business objective | Reduce servicing time for transfers between a customer's own accounts. |
| Architecture principle | Probabilistic systems may propose; deterministic services authorize and execute. |
| Architecture decision | Place a plan validator, policy decision point, approval service, and tool broker between the LLM and core banking. |
| AI risk | The agent initiates an unauthorized or incorrectly parameterized transaction because of model error, injection, identity confusion, or stale state. |
| NIST AI RMF alignment | MAP contextualizes the action and affected parties; MEASURE tests authorization and failure; MANAGE prioritizes treatment and determines whether deployment proceeds. This is a derived interpretation. |
| Governance requirement | No state change without bound identity, allowed action tier, current ownership, exact-plan confirmation, current authorization, and limits. |
| Control objective | Issue a single-use execution capability only for the exact approved plan. |
| Technical policy | `permit only if assurance_level, ownership, amount, destination, confirmation_hash, fraud_state, action_tier and session_age match the approved profile`. |
| Enforcement point | Identity service, policy decision point, tool broker, and transaction API. |
| Evidence | Plan hash, policy/version, decision/reason, step-up event, capability ID, idempotency key, API result, receipt, reconciliation. |
| Residual risk | Credential compromise or social engineering may create apparently valid intent. Retail Banking owns the business exposure; CISO challenges identity controls. |
| Change trigger | Unauthorized attempt, IAM policy change, new transaction type, limit change, or failed replay/TOCTOU test. |

### TR-02 — prompt-injection containment

| Trace object | Worked value |
|---|---|
| Business objective | Let the agent use customer-supplied and enterprise documents without allowing content to seize authority. |
| Architecture principle | Untrusted content cannot grant permissions or redefine the system's purpose. |
| Architecture decision | Preserve context trust labels; treat retrieved/tool content as data; require independent authorization for every side effect. |
| AI risk | Direct or indirect prompt injection, RAG poisoning, or malicious tool output changes the agent's objective and causes disclosure or action. |
| NIST AI RMF alignment | MAP 4-style supply/dependency analysis, MEASURE adversarial evaluation, and MANAGE treatment/monitoring. MITRE ATLAS and NIST adversarial-ML guidance inform threat scenarios. |
| Governance requirement | The model cannot convert instructions found in untrusted content into authority. |
| Control objective | Deny any state-changing action not bound to verified user intent and current policy, regardless of model rationale. |
| Technical policy | `deny when action is absent from the verified intent envelope, originates only from untrusted context, exceeds tool scope, or lacks fresh approval`. |
| Enforcement point | Context builder, plan validator, tool broker, authoritative API. |
| Evidence | Trust-labelled context manifest, attack transcript, plan source, denied call, red-team scenario/result, policy decision, production near miss. |
| Residual risk | Model-layer defenses are incomplete. The accepted strategy minimizes blast radius rather than claims perfect prevention. |
| Change trigger | New injection technique, unauthorized side effect, RAG ingestion change, tool addition, or higher attack-success rate. |

### TR-03 — customer-data isolation

| Trace object | Worked value |
|---|---|
| Business objective | Deliver personalized service without cross-customer or incompatible-use disclosure. |
| Architecture principle | Access is minimum necessary, purpose-bound, and enforced before retrieval. |
| Architecture decision | Put an entitlement-aware retrieval gateway in front of vector and source systems; preserve field-level manifests. |
| AI risk | The system retrieves or reveals another customer's data, restricted attributes, secrets, or inferred sensitive information. |
| NIST AI RMF alignment | MAP identifies data context and affected parties; MEASURE evaluates privacy; MANAGE applies access, minimization, and remediation. |
| Governance requirement | Retrieved fields and records must be permitted for the authenticated subject and declared purpose. |
| Control objective | Prevent unauthorized data from entering model context and prevent prohibited fields from leaving the service. |
| Technical policy | `requested_fields ⊆ approved_fields[purpose]` and `resource.customer_id == subject.customer_id`; output DLP acts as defense in depth. |
| Enforcement point | Retrieval gateway, system of record, output gateway. |
| Evidence | Authorization decision, retrieved-field manifest, source/version, redacted response, seeded-secret result, DLP event, access review. |
| Residual risk | Identity compromise and inference remain possible. Privacy owns purpose/minimization policy; business owns service risk. |
| Change trigger | New data source/field/purpose, cross-border deployment, retention change, privacy incident, or deletion failure. |

### TR-04 — grounded recommendation

| Trace object | Worked value |
|---|---|
| Business objective | Provide accurate, current policy and transaction guidance. |
| Architecture principle | Authoritative evidence has priority over model fluency. |
| Architecture decision | Retrieve versioned sources, use structured account facts, verify citations, and abstain when evidence is inadequate. |
| AI risk | Confabulation or stale policy produces a plausible but false action-bearing claim. |
| NIST AI RMF alignment | MAP documents source/use context; MEASURE assesses validity, explanation, and limitations; MANAGE restricts or disengages on poor outcomes. |
| Governance requirement | Every action-bearing claim has current authoritative support or the system abstains/escalates. |
| Control objective | Block unsupported recommendations and actions. |
| Technical policy/test | `recommend only if claim-source mapping validates, policy version is current, structured facts reconcile, and confidence rules pass`; gold-set and adversarial grounding tests. |
| Enforcement point | Grounding verifier, response gate, action validator. |
| Evidence | Claim/source map, source digest/version/effective date, verifier result, evaluation score and limitations, abstention/escalation log. |
| Residual risk | Authoritative sources may be ambiguous or wrong; domain expert and customer recourse remain necessary. |
| Change trigger | Policy publication, source conflict, elevated complaints/corrections, or grounding regression. |

### TR-05 — agent identity and delegation

| Trace object | Worked value |
|---|---|
| Business objective | Allow safe automation on behalf of an authenticated customer. |
| Architecture principle | Every human, workload, agent, delegation, purpose, and action is explicit. |
| Architecture decision | Use identity token exchange with a subject chain, audience, purpose, resource, action, limits, and expiry. |
| AI risk | Confused deputy, stale authority, privilege escalation, peer-agent impersonation, or replay. |
| NIST AI RMF alignment | GOVERN clarifies accountability; MAP identifies dependency and authority; MEASURE tests security/resilience; MANAGE treats and monitors. |
| Governance requirement | Each tool/API call binds the originating principal, delegated agent, purpose, resource, operation, and expiry. |
| Control objective | A sub-agent cannot exercise or delegate more authority than the originating approved envelope. |
| Technical policy | `token.subject_chain`, audience, purpose, action, resource, delegation depth, amount, and expiry must match the invocation. |
| Enforcement point | IAM token exchange, policy point, API gateway, tool and target API. |
| Evidence | Token/capability ID, subject chain, decision, privilege revocation/replay test, delegated action trace. |
| Residual risk | Identity-provider or device compromise remains. CISO owns identity controls; business owns service exposure. |
| Change trigger | New agent/tool, delegation-depth change, IAM provider change, identity incident, or privilege test failure. |

### TR-06 — fair and contestable service

| Trace object | Worked value |
|---|---|
| Business objective | Provide consistent, accessible service and meaningful recourse. |
| Architecture principle | Affected people can understand, challenge, and obtain an appropriate alternative. |
| Architecture decision | Preserve a human channel; measure subgroup service outcomes; prohibit autonomous high-impact eligibility decisions. |
| AI risk | Differential error, escalation, abandonment, accessibility, or outcome creates harmful bias or automation bias. |
| NIST AI RMF alignment | MAP identifies affected communities and impacts; MEASURE evaluates fairness and human-AI interaction; MANAGE responds and communicates. |
| Governance requirement | Representative quantitative and qualitative evidence supports release; contested decisions have a timely path. |
| Control objective | Detect and prevent unexplained harmful disparity and preserve recourse. |
| Technical policy/test | CI gate requires approved segment measures and impact review; high-impact adverse outcome requires human decision and appeal record. |
| Enforcement point | Evaluation gate, case-management workflow, channel router. |
| Evidence | Subgroup results, coverage/uncertainty, accessibility research, reviewer sign-off, appeal and final outcome. |
| Residual risk | Fairness definitions and trade-offs remain contextual. Business, Compliance, and MRM share challenge roles; business owns outcome. |
| Change trigger | New population/geography, disparity threshold, complaints, access failure, or use-case change. |

### TR-07 — supply-chain integrity

| Trace object | Worked value |
|---|---|
| Business objective | Use external models and components without untracked integrity or change risk. |
| Architecture principle | Production components are approved, attributable, versioned, reproducible, and replaceable. |
| Architecture decision | Use approved registries, signatures, BOMs, version pinning, provider contracts, sandboxing, and fallback. |
| AI risk | Malicious artifact, vulnerable dependency, silent provider change, poisoned data, tool supply-chain attack, or concentration failure. |
| NIST AI RMF alignment | GOVERN addresses third parties; MAP captures dependencies; MEASURE tests provenance and behavior; MANAGE monitors and treats supplier risk. |
| Governance requirement | Every component has approved provenance, integrity, current evaluation, and change/incident obligations. |
| Control objective | Reject an unapproved, unsigned, stale, or materially changed artifact. |
| Technical policy | `deploy only if digest is approved, signature verifies, BOM exists, provider is current, and required evaluation/evidence is fresh`. |
| Enforcement point | Artifact registry, CI gate, deployment admission controller, model gateway. |
| Evidence | Signatures, digest, BOM, supplier record, evaluation ID, contract/change notice, admission decision, fallback exercise. |
| Residual risk | Supplier opacity and concentration remain. Service owner and third-party risk owner maintain treatment. |
| Change trigger | New digest/provider, advisory, contract change, silent behavior change, signature failure, or fallback failure. |

### TR-08 — drift and material change

| Trace object | Worked value |
|---|---|
| Business objective | Preserve authorized performance and behavior after release. |
| Architecture principle | Approval attaches to configuration and context, not a product label. |
| Architecture decision | Create an approved configuration digest across model, prompt, RAG, policy, tools, and infrastructure; use shadow/canary and rollback. |
| AI risk | Model, prompt, retrieval, provider, tool, population, or context drift invalidates earlier evidence. |
| NIST AI RMF alignment | GOVERN establishes monitoring; MAP repeats when context changes; MEASURE detects drift; MANAGE restricts, improves, or deactivates. |
| Governance requirement | An unapproved material digest cannot enter production; context changes trigger scoped reassessment. |
| Control objective | Prevent silent change and re-evaluate material change. |
| Technical policy | `production_config_hash == approved_config_hash`; material-change classifier selects required gates and regression suite. |
| Enforcement point | CI/CD controller, model gateway, configuration service. |
| Evidence | Manifest, digest/signature, change classification, regression, canary comparison, decision, rollback record. |
| Residual risk | Gradual contextual drift may evade thresholds. Product owner operates monitoring; MRM challenges evidence. |
| Change trigger | Any material component, purpose, data, user, geography, `agent_authority`, provider, incident, or obligation change. |

### TR-09 — meaningful human oversight

| Trace object | Worked value |
|---|---|
| Business objective | Preserve accountable judgment for high-consequence actions. |
| Architecture principle | Human control must be informed, timely, empowered, and specific to the exact action. |
| Architecture decision | Approval UI shows evidence, uncertainty, alternatives, and exact parameters; reviewer may reject, modify, or stop. |
| AI risk | Reviewer rubber-stamps, lacks authority/time, receives misleading confidence, or is unavailable. |
| NIST AI RMF alignment | GOVERN assigns roles; MAP defines human-AI configuration; MEASURE tests oversight; MANAGE sustains intervention and recourse. |
| Governance requirement | High-impact action requires an authorized reviewer and fresh approval bound to the plan hash. |
| Control objective | Prevent stale, generic, or uninformed approval from authorizing action. |
| Technical policy | `high_impact implies reviewer_role in approved_roles and approval.plan_hash == action.plan_hash and approval.age <= limit`. |
| Enforcement point | Approval service, tool broker, authoritative API. |
| Evidence | Reviewer identity/role, information displayed, plan hash, decision time, override/rejection, sampled outcome, competence record. |
| Residual risk | Automation bias and workload pressure remain. Operations executive owns staffing and competence; business owns the outcome. |
| Change trigger | Oversight test failure, latency/backlog, low override despite seeded errors, role change, incident, or UI change. |

## Completeness and evidence checks

The repository validator checks structure and references, not substantive adequacy. Human reviewers still ask:

- Does the risk scenario describe cause, event, and impact rather than a label?
- Does the control actually treat the scenario at an authoritative enforcement point?
- Can the evidence show design and operating effectiveness for the current version and context?
- Are test conditions representative, adversarial, and independent enough for the claim?
- Is residual risk clearly owned, bounded, and within delegated authority?
- What evidence or change would invalidate the decision?
