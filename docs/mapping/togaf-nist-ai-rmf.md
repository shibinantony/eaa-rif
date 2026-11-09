# TOGAF and NIST AI RMF relationship

> **DERIVED MAPPING:** This document is an EAA-RIF architecture interpretation. It is not an official crosswalk, profile, or endorsement published by NIST or The Open Group.

## Mapping method

EAA-RIF first treats the frameworks independently, then tests whether two activities share an operational outcome. Similar words are not enough. Every proposed relationship receives one of four strengths:

| Strength | Test |
|---|---|
| **DIRECT** | The activities pursue substantially aligned operational outcomes and can share a gate or linked artifact with little translation. Direct still does not mean official equivalence. |
| **COMPLEMENTARY** | The outcomes are different, but one materially informs, constrains, or consumes the other. |
| **WEAK** | The relationship is conditional, indirect, or useful only in some implementations. |
| **NO MEANINGFUL MAPPING** | No defensible operational relationship exists at this level. Keep the activities separate. |

The unit of comparison is an activity and its decision outcome, not a diagram position. NIST states that GOVERN is cross-cutting and that the four AI RMF functions may be applied iteratively rather than as a mandatory sequence. EAA-RIF therefore does not turn GOVERN, MAP, MEASURE, and MANAGE into four TOGAF phases.

## Independent centers of gravity

### TOGAF

> **FACT — SOURCE FRAMEWORK:** The TOGAF Standard provides an enterprise architecture method, vocabulary, content concepts, architecture capability, and governance guidance. Its public descriptions cover Architecture Vision; Business, Information Systems, and Technology Architectures; Opportunities and Solutions; Migration Planning; Implementation Governance; Architecture Change Management; and continuous requirements work.

TOGAF's center of gravity is enterprise change: understanding business intent, describing baseline and target architectures, choosing building blocks and transition states, sequencing change, governing implementation, and sustaining the architecture.

### NIST AI RMF

> **FACT — SOURCE FRAMEWORK:** NIST AI RMF 1.0 is a voluntary, rights-preserving, non-sector-specific, and use-case-agnostic resource for managing AI risk. Its Core is organized around GOVERN, MAP, MEASURE, and MANAGE. It addresses risks to individuals, groups, organizations, society, and the environment and describes characteristics of trustworthy AI.

NIST AI RMF's center of gravity is contextual AI risk: establishing governance, understanding the intended and actual context, measuring risk and trustworthiness, prioritizing treatment, documenting residual risk, and adapting as the system and context change.

## Rigorous comparison

| Dimension | TOGAF — SOURCE FRAMEWORK | NIST AI RMF — SOURCE FRAMEWORK | EAA-RIF interpretation — DERIVED MAPPING |
|---|---|---|---|
| Purpose | Develop, govern, and evolve enterprise architecture | Manage AI risk and promote trustworthy AI | TOGAF asks what enterprise change and target architecture are needed. AI RMF asks what AI risk exists, how it is evidenced, and what response is justified. |
| Scope | Enterprise strategy and Business, Data, Application, and Technology architecture, plus implementation and change | AI systems, lifecycle actors, benefits, harms, use context, and trustworthiness | AI risk crosses architecture domains; it is not an extra architecture domain. |
| Primary stakeholders | Sponsors, enterprise and domain architects, transformation, portfolio, delivery, and architecture governance | Designers, developers, deployers, operators, acquirers, evaluators, risk functions, users, and affected communities | Link decision forums while keeping accountable roles distinct. |
| Lifecycle | Iterative ADM from capability and vision through domain architecture, migration, implementation, and change | GOVERN/MAP/MEASURE/MANAGE used iteratively throughout AI lifecycles | Do not draw the four functions as four sequential ADM stages. |
| Governance model | Architecture capability, principles, content, repository, conformance, implementation, and change | Risk culture, policies, accountability, risk tolerance, inventory, stakeholder engagement, and third-party risk | Governance overlaps, but the decision objects differ. |
| Architecture emphasis | Strong focus on baseline/target states, dependencies, building blocks, and roadmaps | No prescribed target-architecture method | TOGAF supplies the structural design canvas. |
| Risk emphasis | Risk and security can be integrated, but TOGAF is not an AI-risk taxonomy or TEVV method | AI risk, impact, trustworthiness, measurement, treatment, and residual risk are central | AI RMF supplies risk outcomes and assurance expectations. |
| Artifacts | Architecture views, descriptions, requirements, decisions, roadmaps, migration and governance records | Outcomes encourage inventories, risk/impact records, metrics, tests, monitoring, response, and documentation without mandating a template set | Connect artifacts with stable identifiers rather than merging every repository. |
| Decision mechanisms | Scope, target-state selection, roadmap priority, architecture approval, conformance, exceptions, and change | Risk tolerance, treatment priority, go/no-go, residual-risk, monitoring, response, and deactivation | Joint gates should record separate architecture-fitness and risk-acceptability decisions. |
| Technical controls | Does not prescribe AI control technologies | Also outcome-oriented and non-prescriptive | EAA-RIF adds a control-engineering translation layer. |
| Assurance | Architecture conformance and implementation oversight | TEVV, independent assessment where appropriate, measurement, and documented results | Architecture review is not model or system validation. |
| Continuous monitoring | Requirements and architecture change management sustain the target state | Ongoing measurement, emergent-risk tracking, incident response, and improvement | Runtime evidence can trigger both risk treatment and architecture change. |
| Compliance relevance | Useful structure and evidence, not AI compliance by itself | Voluntary and useful for obligations, but not legal compliance by itself | Map applicable law and policy separately. Framework alignment is not a legal conclusion. |

## Direct answers

### What TOGAF solves that NIST AI RMF does not

- Strategy-to-capability and business-to-technology alignment.
- Coherent baseline and target architectures across Business, Data, Application, and Technology.
- Portfolio dependencies, transition architectures, roadmaps, and migration sequencing.
- Enterprise reuse and rationalization of platforms, applications, data, and services.
- Architecture governance, implementation conformance, repository structure, and change control.

### What NIST AI RMF solves that TOGAF does not

- AI-specific trustworthiness and harm framing.
- Contextual risk to people, organizations, society, and the environment.
- AI testing, evaluation, verification, and validation for validity, safety, security, privacy, fairness, explainability, and human-AI interaction.
- Risk tolerance, treatment, residual-risk documentation, and emergent-risk monitoring.
- AI supply-chain and third-party model/data risk.
- GenAI-specific risk treatment through NIST AI 600-1.

### Where they overlap

They overlap in governance, accountability, stakeholder engagement, requirements, documentation, monitoring, change, and risk-informed decisions. The overlap is functional, not proof of formal equivalence.

### Where they should remain separate

- Architecture approval and residual-risk acceptance.
- Architecture conformance and independent model/system assurance.
- Enterprise Architecture Board accountability and business risk ownership.
- Architecture repository and detailed risk, test, telemetry, incident, and assurance stores. Link them; do not collapse them.
- AI-risk outcomes and detailed cybersecurity threats and controls from NIST CSF or MITRE ATLAS.
- Human legal, privacy, fairness, purpose, and acceptable-harm judgments and automated policy gates.

## ADM activity × NIST AI RMF function matrix

Every cell below is a **DERIVED MAPPING**.

| TOGAF activity | GOVERN | MAP | MEASURE | MANAGE |
|---|---|---|---|---|
| Preliminary: capability, tailoring, principles | **DIRECT** — establishes governance capability, roles, and principles | **COMPLEMENTARY** — supplies enterprise scope and taxonomy | **NO MEANINGFUL MAPPING** — no system-level AI evaluation | **WEAK** — enables resources but does not treat a system risk |
| Phase A: Architecture Vision | **COMPLEMENTARY** — sponsorship, stakeholders, approval, principles | **DIRECT** — purpose, context, affected parties, constraints, initial decision | **COMPLEMENTARY** — success and harm criteria seed assurance | **COMPLEMENTARY** — initial constraints shape response options |
| Phase B: Business Architecture | **COMPLEMENTARY** — operating model, accountability, policy context | **DIRECT** — processes, actors, benefits, harms, and oversight context | **COMPLEMENTARY** — business outcome and harm indicators | **COMPLEMENTARY** — process controls, intervention, and non-AI alternatives |
| Phase C1: Data Architecture | **COMPLEMENTARY** — ownership, policy, and supplier accountability | **DIRECT** — sources, provenance, subjects, permitted use, dependencies | **COMPLEMENTARY** — defines data-quality, representativeness, privacy, bias, and drift requirements and evidence hooks; it does not itself perform AI TEVV | **COMPLEMENTARY** — access, lineage, retention, and remediation controls |
| Phase C2: Application Architecture | **COMPLEMENTARY** — application ownership and standards | **DIRECT** — boundary, model/RAG/agent components, interfaces, users | **COMPLEMENTARY** — places evaluation points for models, retrieval, orchestration, tools, and output; independent assurance performs the evaluation | **COMPLEMENTARY** — tool mediation, approval, authorization, and containment |
| Phase D: Technology Architecture | **COMPLEMENTARY** — platform standards, ownership, supply-chain governance | **COMPLEMENTARY** — deployment context, infrastructure, third parties | **COMPLEMENTARY** — telemetry, resilience, security, and testability | **COMPLEMENTARY** — IAM, isolation, guardrails, fail-safe, and recovery mechanisms |
| Phase E: Opportunities & Solutions | **COMPLEMENTARY** — governance constrains solution choice | **WEAK** — context should already exist, though options may add risk | **COMPLEMENTARY** — evidence compares options and controls | **DIRECT** — selects treatment work packages, including non-AI alternatives |
| Phase F: Migration Planning | **COMPLEMENTARY** — funding, authority, and risk appetite | **WEAK** — migration can alter context but does not primarily map risk | **COMPLEMENTARY** — risk and assurance evidence inform priority | **DIRECT** — sequences and resources treatments and exposes residual risk |
| Phase G: Implementation Governance | **DIRECT** — oversight, accountability, conformance, exceptions | **COMPLEMENTARY** — implementation changes may require remapping | **COMPLEMENTARY** — consumes TEVV and control evidence; it is not TEVV itself | **DIRECT** — enforces treatments, gates, conditions, and escalation |
| Phase H: Architecture Change Management | **DIRECT** — continuing accountability and change policy | **COMPLEMENTARY** — use/context changes trigger renewed mapping | **COMPLEMENTARY** — monitoring evidence triggers change but remains assurance work | **DIRECT** — improve, restrict, respond, disengage, or retire |
| Continuous Requirements Management | **COMPLEMENTARY** — policies and responsibilities become requirements | **COMPLEMENTARY** — mapped risks become requirements | **COMPLEMENTARY** — metrics and thresholds become acceptance criteria | **COMPLEMENTARY** — treatments and residual-risk conditions remain traceable |
| Architecture Repository/content management | **COMPLEMENTARY** — supports governed architecture inventory and ownership while AI governance remains a distinct outcome | **COMPLEMENTARY** — links context and impact artifacts | **COMPLEMENTARY** — references evidence without duplicating all raw data | **COMPLEMENTARY** — links treatments, exceptions, decisions, and residual risk |

## Examples where no mapping should be forced

| Activity | Tempting but invalid claim | Correct treatment |
|---|---|---|
| Enterprise application-portfolio rationalization | “MAP covers application rationalization” | Portfolio rationalization is an architecture concern. AI-risk findings may inform it, but AI RMF does not supply the method. |
| Fairness evaluation | “Phase C or G performs fairness testing” | Architecture identifies components and gates. Independent AI assurance performs and challenges fairness evaluation. |
| Cloud landing-zone selection | “MANAGE selects the cloud” | Architecture selects a platform. MANAGE informs treatments and residual-risk decisions. |
| Legal basis or regulatory interpretation | “TOGAF approval establishes legality” | Legal and compliance functions make the applicable-obligation judgment. Architecture records resulting constraints. |
| Model validity | “Architecture conformance proves model validity” | Conformance checks implementation against architecture; model/system validation requires separate methods and evidence. |

## Integration conclusion

> **PROPOSED MODEL — ORIGINAL IP:** TOGAF is the enterprise change and architecture spine. NIST AI RMF is a cross-cutting AI-risk loop. EAA-RIF integrates them through stable identifiers, decision gates, control contracts, and runtime evidence rather than a forced phase-to-function crosswalk.

The operative chain is:

`business objective → architecture decision → AI risk → assurance criterion → control requirement → enforcement point → evidence → residual-risk decision → architecture/risk change trigger`

See [Authoritative references](../references.md) for source versions and URLs.
