# AI Architecture Review

## 1. Artifact envelope

| Field | Value |
|---|---|
| Review ID / System ID |  |
| Title / Version / Environment |  |
| Product owner / Business owner |  |
| Lead enterprise, solution, AI, data, and security architects |  |
| Impact tier / Risk tier / Agent authority |  |
| Review gate / Review date / Next review |  |
| Classification |  |

## 2. Business intent

- Business outcome and measures:
- Intended users and affected parties:
- Intended, foreseeable, misuse, and prohibited uses:
- Non-AI or simpler alternatives considered:
- Why the proposed AI approach is justified:
- Accountable business risk owner:

## 3. Scope and boundaries

- System boundary and external dependencies:
- Lifecycle state and deployment geography:
- Human roles and decision points:
- Material assumptions and constraints:
- Out-of-scope functions:

Attach or link the context, trust-boundary, data-flow, and sequence diagrams.

## 4. Architecture views

### Business

- Capabilities, processes, value streams, roles, customer/employee journeys:
- Operating-model and service impacts:
- Human fallback, recourse, and accessibility:

### Data

- Sources, owners, classifications, provenance, lineage, quality, permitted purpose:
- Training, evaluation, RAG, prompt, memory, embedding, cache, trace, and output data:
- Residency, retention, deletion, rights, and secondary-use controls:
- Authorization before retrieval and data minimization:

### Application

- Models, prompts, RAG, agents, orchestrators, tools, APIs, policy points, human approvals:
- Interfaces, schemas, state, memory, error handling, and dependency contracts:
- Separation between reasoning, authorization, and execution:

### Technology

- Hosting, networks, identity, secrets, encryption, key management, isolation, egress:
- Registries, CI/CD, signing, SBOM/AIBOM, configuration/version control:
- Capacity, availability, performance, resilience, recovery, rollback, decommissioning:

## 5. Agent and authority model

- `agent_authority` classification and rationale:
- Allowed/prohibited tools and actions:
- Subject chain and delegation rules:
- Time, cost, step, recursion, transaction, and amount budgets:
- Reversibility, idempotency, compensation, and kill switch:

## 6. Principles, standards, and decisions

| Principle/standard | Conform / exception / not applicable | Evidence or ADR | Owner |
|---|---|---|---|
|  |  |  |  |

## 7. Risk, control, and assurance hooks

| Risk ID | Architecture decision | Required control | Enforcement point | Evidence hook |
|---|---|---|---|---|
|  |  |  |  |  |

## 8. Operations and change

- SLOs, KRIs, thresholds, dashboards, and on-call ownership:
- Safe-degradation modes and failure matrix:
- Incident/complaint/appeal handling:
- Material-change triggers and re-entry gates:
- Provider exit, portability, and retirement plan:

## 9. Findings and decision

| Finding | Severity | Owner | Due date | Gate impact |
|---|---|---|---|---|
|  |  |  |  |  |

Decision: `approved | approved_with_conditions | restricted_pilot | return_for_change | rejected`

Conditions, scope, configuration digest, expiry, and linked exception IDs:

Signatures: Enterprise Architecture decision owner; consulted domain architects; product owner acknowledgement.
