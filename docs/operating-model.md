# Enterprise operating model and decision rights

> **PROPOSED MODEL — ORIGINAL IP:** EAA-RIF uses linked governance forums with explicit decision objects. No board becomes a universal sign-off body.

## Three lines of accountability

> **SOURCE / INDUSTRY PRACTICE:** This structure is adapted from [The IIA Three Lines Model](https://www.theiia.org/globalassets/site/resources/statements-of-position/tlm_assurance_advice_support_effective_gov_en.pdf). **ORIGINAL IP:** EAA-RIF's allocation of AI roles, decision objects, assurance evidence, and agentic-AI responsibilities.

- **First line:** Business owner, AI product owner, architects, engineering, platform, MLOps/LLMOps, and operations own outcomes, risks, implementation, and control operation.
- **Second line:** AI Governance, CISO risk functions, Privacy, Legal/Compliance, Data Governance, and Model Risk set policy, challenge, validate, and oversee.
- **Third line:** Internal Audit independently assesses whether governance and controls are designed and operating effectively.

The model separates four decisions:

1. **Architecture approval** — Is the target architecture coherent and conformant?
2. **Domain control approval** — Does the proposed control design satisfy the security, privacy, data, legal, model-risk, or operational requirement?
3. **Independent assurance conclusion** — Does current evidence support the stated claim for this version and context?
4. **Residual-risk acceptance** — Does the accountable business risk owner accept the remaining exposure within delegated authority?

## Role charters

| Role | Designs or contributes | Owns | Approves or challenges | Monitors/evidence |
|---|---|---|---|---|
| **Enterprise Architecture Board (EAB)** | Enterprise principles, target states, reference architectures, standards | Architecture governance process and architecture exceptions | Approves architecture direction and conformance; challenges duplication, debt, interoperability, resilience | Architecture repository, exceptions, conformance, material architecture drift |
| **AI Governance Board (AIGB)** | AI policy, impact tiers, risk tiers, minimum assurance, agent-authority ceilings, gate criteria | AI governance process and cross-domain risk escalation | Approves tiering and gate integrity; coordinates domain dispositions; does not absorb business risk | Inventory coverage, gate quality, exceptions, incidents, portfolio risk |
| **AI Center of Excellence (CoE)** | Patterns, reusable controls, evaluation assets, education | Advisory assets and platform adoption | Recommends; should not approve its own platform or own business risk | Pattern reuse, support issues, evaluation asset quality |
| **CISO / Cybersecurity** | Threat model, security requirements, AI identity, containment, incident design | Security policy and cyber risk controls | Approves security control design; independently challenges attack resistance | Security telemetry, red-team results, supply-chain posture, cyber incidents |
| **Privacy** | Minimization, purpose, notices/consent, retention, privacy-by-design | Privacy policy and assessment process | Determines privacy requirements and disposition | Data-use conformance, privacy incidents, rights/complaints, retention/deletion evidence |
| **Legal / Compliance** | Applicable obligations, disclosures, contracts, records, regulatory engagement | Legal interpretation and compliance policy | Advises/approves within mandated authority; does not certify technical effectiveness | Regulatory change, contractual duties, disclosure and recordkeeping evidence |
| **Business Owner / Risk Owner** | Outcome, process, affected-party and customer-harm criteria | Business outcome and residual business risk | Sponsors use; accepts residual risk within authority; escalates material exposure | Benefits, losses, complaints, customer outcomes, operating risk |
| **AI Product Owner** | Product requirements, risk treatment backlog, operating model | End-to-end system lifecycle and evidence completeness | Prepares release and risk decisions; cannot self-validate | Service KPIs, risk/control status, releases, incidents, remediation |
| **Model Risk Management (MRM)** | Validation plan, model/system challenge, limitations and monitoring expectations | Independent model-risk methodology where applicable | Independently validates or challenges; does not operate the model control | Validation findings, limitations, performance/drift, remediation |
| **Data Governance / Data Owner** | Data products, provenance, quality, access, retention, purpose | Data-use approval and data risk | Approves source admission and permitted use | Lineage, quality, access, retention, RAG corpus state |
| **Platform Engineering** | Shared identity, policy, evaluation, observability, evidence, deployment capabilities | Platform control operation and reliability | Implements approved patterns; approves platform changes within delegation | Platform health, policy distribution, evidence pipeline, shared-control failures |
| **MLOps / LLMOps** | Model/prompt/configuration lifecycle, release, rollback, monitoring | Configuration and release operation | Executes authorized release; cannot expand approved scope | Version, drift, evaluation regression, deployment evidence, rollback |
| **Engineering / Control Operators** | Application and control implementation | Code quality and assigned control operation | Supply evidence; do not approve their own independent assurance | Tests, logs, defects, control events, remediation |
| **SOC / SRE / Operations** | Detection, response, recovery, safe degradation | Service operation and incident execution | May suspend, contain, roll back, or fail safe under runbook | Alerts, traces, incidents, control health, recovery evidence |
| **Internal Audit** | Independent audit plan and sampling | Third-line assessment | Issues audit conclusions; does not operate or approve first-line controls | Audit findings and remediation closure |

## Decision-right matrix

| Decision | Designs/recommends | Mandatory review or concurrence | Final decision right |
|---|---|---|---|
| Intended use and business scope | Business owner, product owner, business architect | Legal/Compliance, Privacy, MRM where applicable | Accountable business executive |
| Impact tier, risk tier, and agent-authority ceiling | Product owner, AI architect, AI Governance | CISO, Privacy, MRM, operations risk | AIGB within enterprise policy; material exception escalates |
| Target architecture and exception | Enterprise, solution, AI, data, security architects | AIGB, CISO, Privacy, Data, Platform | EAB |
| Data-source admission to RAG | Data owner and product team | Data Governance, Privacy, Security | Data owner under approved data policy |
| Model, tool, and provider selection | AI architecture and engineering | Procurement, CISO, Privacy, MRM, third-party risk | Designated service/technology owner within architecture approval |
| Domain control design | Relevant control owner with architect/engineering | Product owner, operators, independent risk specialist | Relevant policy/control owner |
| Independent validation | MRM or independent assurance | Engineering and business provide evidence but do not approve their work | Independent validation authority |
| Production authorization | Product owner prepares release record | Required architecture, security, privacy, compliance, MRM, data dispositions | Delegated release authority |
| Residual-risk acceptance | Product owner prepares decision | AIGB and affected control owners challenge/escalate | Named business risk owner; material risk escalates to enterprise/board authority |
| Emergency suspension | SOC, operations, incident commander | No prior approval required | Any named emergency authority under runbook |
| Re-enable after incident | Product and engineering | CISO, MRM, affected control owners | Named reauthorization authority |
| Material model/prompt/RAG/tool change | Engineering proposes | Same independent functions as baseline release | Release authority after required gates; no developer self-approval |

## RACI-style assignment

RACI is shown as **A** (accountable), **R** (responsible), **C** (consulted), and **I** (informed). One activity may have several responsible roles, but only one accountable role in a specific enterprise implementation.

| Activity | A | R | C | I |
|---|---|---|---|---|
| Sponsor outcome and funding | Business Owner | AI Product Owner | EA, AIGB, Finance | Domain owners |
| Register and impact-tier use case | AIGB | Product Owner | AI Architect, CISO, Privacy, MRM, Data Governance | Business Owner, EAB |
| Lead target-architecture design and exercise design authority | Lead Enterprise/AI Architect | Solution/Data/Application/Security Architects | Product Owner, EAB, CoE, CISO, Privacy, MRM, Platform | AIGB |
| Execute product delivery against the approved architecture | AI Product Owner | Engineering, Platform, MLOps/LLMOps | Lead Enterprise/AI Architect, CISO, Privacy, Data, MRM | EAB, AIGB |
| Approve architecture conformance | EAB | Enterprise Architect | CISO, AIGB, Platform, Data | Business/Product Owner |
| Perform AI and agent risk assessment | Business Risk Owner | Product Owner and domain risk specialists | CISO, Privacy, Legal, MRM, Data, affected stakeholders | EAB |
| Approve data use | Data Owner | Data Steward and Engineering | Privacy, Security, Legal | Product Owner |
| Define domain control | Relevant Control Owner | Architect and Control Engineer | Product, risk specialists, operators | Business Owner |
| Implement controls | Product Owner | Engineering, Platform, MLOps/LLMOps | Architect, CISO, Data, CoE | AIGB |
| Independently validate model/system | Independent Validation/MRM Lead | Validation Team | Domain experts, CISO, Privacy | Product and Business Owner |
| Administer pre-production gate | AIGB | Gate Coordinator | EAB, CISO, Privacy, Legal, MRM, Data | Business Owner |
| Accept residual risk | Business Owner or delegated executive risk authority | Product Owner prepares record | AIGB and affected control owners | EAB, Internal Audit |
| Authorize production release | Delegated Release Authority | Product Owner and MLOps | Required gate signatories | Business Owner |
| Monitor and operate | Service/Product Owner | MLOps, SRE, SOC | Control owners, MRM, Data | AIGB |
| Respond to AI/service incident | Service Owner | SRE, MLOps, Engineering, SOC | CISO, Legal, Privacy, Business, AIGB | Executives/regulators as applicable |
| Command cyber incident | CISO or designated incident commander | SOC and incident-response team | Service Owner, Legal, Privacy, Business | AIGB and executives as applicable |
| Supply control evidence | Control Owner | Control Operator | Assurance/Validation | Internal Audit |
| Independently audit | Internal Audit Leader | Audit Team | All evidence owners | Audit/Risk Committee |
| Authorize bounded policy deviation | Policy Owner | Product Owner prepares exception record | Business Risk Owner and relevant second-line functions | EAB, AIGB, Internal Audit |
| Accept incremental exception risk | Business Risk Owner | Product Owner prepares risk record | Policy Owner and relevant second-line functions | EAB, AIGB, Internal Audit |

## Dual-key exceptions

An exception requires two different authorities:

- the **policy owner** authorizes the bounded deviation from policy; and
- the **business risk owner** accepts the incremental residual risk.

The exception also requires scope, compensating controls, evidence, limits, expiry, remediation, monitoring, and immediate revocation triggers. Neither authority can silently grant the other's decision.

## Escalation rules

- Material business, customer, prudential, safety, or regulatory exposure exceeds local acceptance authority and moves to the enterprise risk body.
- A mandatory legal, security, privacy, or model-risk prohibition cannot be accepted away by a product owner.
- A control failure affecting a high-consequence action triggers safe degradation or suspension before committee review.
- Repeated exceptions against the same control trigger architecture and policy redesign rather than indefinite renewal.
- A decision without an owner, scope, version, evidence snapshot, and expiry is not a valid gate decision.
