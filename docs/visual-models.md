# Visual models

The diagram compositions and layouts are **PROPOSED MODEL — ORIGINAL IP**. TOGAF/ADM and NIST AI RMF names, domains, functions, and lifecycle concepts are **SOURCE FRAMEWORK**. Relationships between them are **DERIVED MAPPING** and are not official crosswalks. The diagrams use original layouts and do not reproduce proprietary TOGAF figures.

## 1. TOGAF versus NIST AI RMF

**Purpose:** Distinguish the two frameworks' centers of gravity while showing a legitimate shared decision surface.

**Components:** TOGAF enterprise-architecture lane; proposed shared decision surface; NIST AI RMF lane.

**Relationships:** Architecture decisions and change governance connect to principles, gates, and evidence; AI-risk functions connect to the same integration surface without becoming TOGAF phases.

**Recommended layout:** Three horizontal lanes with a narrow center bridge. Avoid overlapping circles that suggest equivalence.

```mermaid
flowchart LR
  subgraph T["TOGAF enterprise architecture"]
    T1["Business, data, application and technology views"] --> T2["Architecture decisions and target states"] --> T3["Roadmaps, implementation and change governance"]
  end
  subgraph I["Shared decision surface — EAA-RIF interpretation"]
    I1["Principles and requirements"] --> I2["Decision gates and exceptions"] --> I3["Traceability and evidence"]
  end
  subgraph N["NIST AI RMF"]
    N1["GOVERN<br/>cross-cutting policy and accountability"]
    N2["MAP<br/>context and impacts"]
    N3["MEASURE<br/>TEVV and monitoring"]
    N4["MANAGE<br/>prioritize and treat"]
    N1 -.-> N2
    N1 -.-> N3
    N1 -.-> N4
    N2 <--> N3
    N3 <--> N4
    N4 <--> N2
  end
  T2 --> I1
  T3 --> I2
  N1 --> I1
  N3 --> I3
  N4 --> I2
```

## 2. How TOGAF and AI RMF intersect

**Purpose:** Show AI-risk activities informing architecture decisions without depicting AI RMF as a TOGAF phase sequence.

**Components:** Enterprise change lifecycle; scope, architecture, release, and change gates; four AI RMF functions.

**Relationships:** GOVERN and MAP inform early gates; MEASURE and MANAGE provide evidence and treatment at release and runtime; all may recur.

**Recommended layout:** Architecture lifecycle across the top, risk functions below, dotted links to decision gates.

```mermaid
flowchart LR
  A1["Strategy and architecture intent"] --> G1{"Scope gate"}
  G1 --> A2["Domain and target architectures"] --> G2{"Architecture gate"}
  G2 --> A3["Roadmap and solution delivery"] --> G3{"Release gate"}
  G3 --> A4["Operate and change"] --> G4{"Change or retire gate"}
  G4 --> A1
  R1["GOVERN"] -. "risk appetite and roles" .-> G1
  R1 -. "accountability" .-> G2
  R2["MAP"] -. "context and impacts" .-> G1
  R2 -. "risk requirements" .-> G2
  R3["MEASURE"] -. "TEVV evidence" .-> G3
  R3 -. "runtime measures" .-> G4
  R4["MANAGE"] -. "treatment and residual risk" .-> G3
  R4 -. "respond, improve, deactivate" .-> G4
```

## 3. Integrated enterprise AI governance architecture

**Purpose:** Connect business strategy to runtime evidence and feedback.

**Components:** Seven EAA-RIF layers.

**Relationships:** Downstream layers refine intent into executable governance; evidence feeds strategy, architecture, risk, and controls.

**Recommended layout:** Seven stacked horizontal bands with feedback arrows on the side. Treat the layers as coupled responsibilities, not a waterfall.

```mermaid
flowchart TB
  L1["1 Business strategy and risk appetite<br/>value, accountability, permissible use"]
  L2["2 Enterprise architecture<br/>principles, target state, roadmap"]
  L3["3 AI system architecture<br/>models, data, RAG, agents, tools"]
  L4["4 AI risk and governance<br/>context, impacts, obligations, decisions"]
  L5["5 Control engineering<br/>policy, identity, gates, guardrails"]
  L6["6 Runtime assurance<br/>authorization, monitoring, response"]
  L7["7 Evidence and continuous governance<br/>traceability, assurance, exceptions, change"]
  L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7
  L7 -- "outcome and risk feedback" --> L1
  L7 -- "architecture change" --> L2
  L7 -- "control improvement" --> L5
```

## 4. Governance-as-Code lifecycle

**Purpose:** Show how human policy intent becomes enforceable and how evidence closes the loop.

**Components:** Principle, governance requirement, risk requirement, control objective, machine-readable specification, policy code, deployment gate, runtime guardrail, authoritative enforcement, telemetry, evidence, governance decision.

**Relationships:** Each stage implements or evidences the prior stage; continuous governance improves or restricts the system.

**Recommended layout:** A left-to-right chain that returns to requirements and enforcement.

```mermaid
flowchart LR
  P["Enterprise principle"] --> G["AI governance requirement"] --> R["Risk requirement"] --> C["Control objective"]
  C --> M["Machine-readable control specification"] --> PC["Policy-as-Code"] --> D["Deployment gate"]
  D --> U["Runtime guardrail"] --> A["Authoritative enforcement"] --> T["Telemetry"] --> E["Evidence"] --> CG["Continuous governance"]
  CG -- "improve" --> G
  CG -- "exception with expiry" --> D
  CG -- "restrict or suspend" --> A
```

## 5. Agentic AI control architecture

**Purpose:** Make the Deterministic Action Boundary and Evidence Spine visible.

**Components:** Channel, identity, deterministic orchestrator, reasoning plane, governed data plane, action boundary, assurance plane.

**Relationships:** The reasoning plane proposes; data access is entitlement-aware; the action boundary validates and authorizes; evidence correlates every stage; monitoring can disable orchestration or writes.

**Recommended layout:** Left-to-right request flow with three horizontal planes and a prominent vertical action boundary before enterprise APIs.

```mermaid
flowchart LR
  U["Customer or employee"] --> CH["Channel and API gateway"] --> ID["Identity, consent and session assurance"] --> OR["Deterministic orchestrator"]
  subgraph RP["Reasoning plane"]
    OR --> IC["Intent and impact classifier"] --> MG["Approved model gateway"] --> PL["Typed action proposal"]
  end
  subgraph DP["Governed data plane"]
    OR --> RG["Entitlement-aware retrieval gateway"]
    RG --> KB["Approved RAG corpus"]
    RG --> SR["Systems of record"]
    RG --> MG
  end
  subgraph AB["Deterministic Action Boundary"]
    PL --> PV["Plan and schema validator"] --> PDP["Policy decision point"] --> AP["Step-up and exact-plan approval"] --> TB["Tool broker<br/>single-use capability"] --> API["Enterprise APIs"]
  end
  subgraph AS["Assurance plane"]
    EV["Evidence Spine"] --> MON["Runtime monitoring and SIEM"] --> KS["Kill switch and safe fallback"]
  end
  ID -.-> EV
  RG -.-> EV
  MG -.-> EV
  PDP -.-> EV
  API -.-> EV
  KS -. "disable orchestration" .-> OR
  KS -. "disable writes" .-> TB
```

## 6. Control traceability chain

**Purpose:** Show how a business objective becomes a defensible residual-risk decision.

**Components:** Objective, principle, decision, risk, framework outcome, governance requirement, control, policy, enforcement, evidence, residual risk.

**Relationships:** Each node traces forward to implementation and backward to intent; runtime evidence can reopen the risk.

**Recommended layout:** A single horizontal chain with a feedback arrow from evidence/residual risk to the risk and control.

```mermaid
flowchart LR
  B["Business objective"] --> AP["Architecture principle"] --> AD["Architecture decision"] --> AR["AI risk"]
  AR --> NF["NIST AI RMF outcome"] --> GR["Governance requirement"] --> CO["Control objective"]
  CO --> PA["Technical policy or test"] --> EP["Enforcement point"] --> ER["Evidence record"] --> RR["Residual-risk decision"]
  RR -- "not acceptable" --> CO
  ER -- "runtime learning" --> AR
```

## 7. Enterprise decision-rights model

**Purpose:** Separate design, governance, implementation, monitoring, assurance, and risk acceptance.

**Components:** Business owner, EAB, AIGB, independent risk functions, product/architecture, engineering, operations, and evidence service.

**Relationships:** Teams propose and implement; boards decide within scope; evidence flows to independent challenge and the business owner; operations may suspend.

**Recommended layout:** Governance authorities at the top, design/engineering in the middle, operations/evidence at the bottom. Use distinct decision arrows.

```mermaid
flowchart TB
  BO["Business executive<br/>owns outcome and residual risk"]
  EAB["Enterprise Architecture Board<br/>approves architecture"]
  AGB["AI Governance Board<br/>sets tier and assurance baseline"]
  INDEP["CISO, Privacy, Compliance, Model Risk<br/>policy and independent challenge"]
  PROD["Product and architecture teams<br/>design and propose"]
  ENG["Platform, MLOps and engineering<br/>implement controls"]
  OPS["Operations and SOC<br/>monitor, respond and suspend"]
  EVID["Evidence Spine and assurance record"]
  PROD --> EAB
  PROD --> AGB
  INDEP --> EAB
  INDEP --> AGB
  BO --> AGB
  EAB --> ENG
  AGB --> ENG
  ENG --> OPS
  ENG --> EVID
  OPS --> EVID
  EVID --> INDEP
  EVID --> BO
  OPS -- "emergency suspension" --> ENG
  BO -- "risk acceptance within authority" --> EVID
```

## 8. Continuous AI assurance feedback loop

**Purpose:** Show authorization as a time-bound state maintained by evidence, not a one-time approval.

**Components:** Inventory/context, risk mapping, architecture/control design, independent TEVV, authorization, staged production, runtime measures, evidence review, improvement or suspension.

**Relationships:** Failed pre-production evidence returns to design; runtime evidence can continue, improve, revalidate, or suspend.

**Recommended layout:** Circular or left-to-right loop with a clearly marked authorization decision and incident branch.

```mermaid
flowchart LR
  I["Inventory and context"] --> R["Map risks and impacts"] --> C["Design architecture and controls"] --> V["Independent pre-deployment TEVV"] --> G{"Authorize?"}
  G -- "No" --> C
  G -- "Yes" --> P["Staged production"] --> M["Runtime measures and feedback"] --> E["Evidence and residual-risk review"] --> X{"Within tolerance?"}
  X -- "Yes" --> P
  X -- "Improve" --> C
  X -- "Material change" --> V
  X -- "Incident or invariant failure" --> S["Suspend, contain, recover"] --> R
```

## Rendering guidance

- Use the source labels in captions when diagrams appear outside this repository.
- Keep TOGAF and NIST names as text references; do not copy protected logos or source diagrams unless separately licensed.
- In decks, use native editable shapes for the required architecture diagrams.
- In code repositories, Mermaid is the canonical portable representation.
- Preserve the distinction between dotted informational relationships and solid control/decision paths.
