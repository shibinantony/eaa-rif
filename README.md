# EAA-RIF

## Enterprise AI Architecture & Risk Integration Framework

EAA-RIF is a vendor-neutral, architecture-led operating model for connecting enterprise architecture decisions, AI risks, enforceable controls, runtime evidence, and continuous governance.

It is designed for traditional machine learning, generative AI, retrieval-augmented generation, AI agents, and multi-agent systems. The framework uses TOGAF and the NIST AI Risk Management Framework as independent source frameworks, then adds an original **Architecture-to-Evidence (A2E)** integration model. It does not claim an official crosswalk, endorsement, or one-to-one equivalence.

> **Framework status:** Version 0.1.0, research baseline 9 November 2026. NIST states that AI RMF 1.0 is being revised. EAA-RIF therefore version-pins its NIST baseline to NIST AI 100-1 and records source versions explicitly.

## The architectural question

> How can an enterprise connect architecture decisions, AI risks, enforceable controls, runtime evidence, and continuous governance into one traceable operating model?

EAA-RIF answers with four linked mechanisms:

1. **Seven operating layers** from business strategy through runtime evidence.
2. **Seven lifecycle gates** with separate architecture, control, assurance, and residual-risk decisions.
3. **An Architecture-to-Evidence graph** linking objectives, decisions, risks, controls, policies, enforcement points, evidence, and residual-risk acceptance.
4. **Control contracts** that translate human requirements into deploy-time gates and runtime guardrails without pretending that every governance judgment can be automated.

## Start here

- [Whitepaper](docs/whitepaper.md)
- [TOGAF and NIST AI RMF relationship matrix](docs/mapping/togaf-nist-ai-rmf.md)
- [EAA-RIF core model](docs/core-model.md)
- [Enterprise operating model](docs/operating-model.md)
- [Agentic banking case study](docs/case-studies/agentic-banking.md)
- [Governance-as-Code](docs/governance-as-code.md)
- [Control traceability](docs/control-traceability.md)
- [Reference architecture](docs/reference-architecture.md)
- [Visual models](docs/visual-models.md)
- [Maturity model](docs/maturity-model.md)
- [Implementation roadmap](docs/implementation-roadmap.md)
- [Source and IP boundary](docs/ip-provenance.md)
- [Authoritative references](docs/references.md)

## Reusable assets

The repository contains:

- twelve project-ready governance and assurance [templates](templates/README.md);
- machine-readable [control-contract and evidence schemas](schemas/);
- tested [OPA/Rego deployment-gate examples](examples/policy-as-code/opa/);
- an illustrative [Azure Policy definition](examples/policy-as-code/azure-policy/);
- a Terraform precondition example and a CI governance gate;
- sample AI risk, control, system, policy, and evidence records;
- a dependency-free traceability validator for local and CI use; and
- eight Mermaid architecture diagrams.

## Correct use of the framework

EAA-RIF is an integration method, not a compliance certificate. It helps teams build a defensible evidence chain, but legal compliance, model validation, security authorization, privacy assessment, and business risk acceptance remain accountable human decisions.

The repository deliberately keeps these decisions separate:

- the Enterprise Architecture Board approves architecture direction and exceptions;
- domain control owners approve control design;
- independent assurance functions judge evidence sufficiency;
- the accountable business owner accepts residual business risk; and
- operations can suspend the service when runtime thresholds are breached.

## Source labels

Every major assertion uses one of three labels:

- **SOURCE FRAMEWORK** — a fact about TOGAF, NIST, ISO, MITRE, or another cited source.
- **DERIVED MAPPING** — EAA-RIF's interpretation of relationships between source frameworks.
- **ORIGINAL IP** — an EAA-RIF model, schema, gate, artifact, or operating convention.

## Licensing and trademarks

- Original documentation is licensed under [CC BY 4.0](LICENSE-DOCS.md).
- Original code and machine-readable examples are licensed under [Apache License 2.0](LICENSE-CODE).
- Third-party standards, trademarks, and source material remain the property of their owners. See [NOTICE.md](NOTICE.md).

Commercial use involving TOGAF materials may require review of The Open Group licensing terms. This repository contains original summaries and analysis and intentionally does not reproduce protected TOGAF figures, tables, or substantial text.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Proposed mappings must identify their source versions, preserve the three labels above, and state whether the change affects architecture approval, control approval, assurance, or residual-risk acceptance.
