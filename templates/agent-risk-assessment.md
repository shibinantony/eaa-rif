# Agent Risk Assessment

## 1. Identity and purpose

| Field | Value |
|---|---|
| Agent ID / System ID / Version |  |
| Goal and prohibited goals |  |
| Product owner / Business risk owner |  |
| Impact tier / Risk tier / Agent authority (`agent_authority`) A0–A5 |  |
| Environment / Geography / User population |  |

## 2. Authority inventory

| Tool/resource | Read/write | Actions and parameter bounds | Data class | Credential/capability | Reversible/idempotent | Human approval | Target authorization | Owner |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## 3. Agentic Action Envelope

- Verified purpose and user-intent binding:
- Allowed/prohibited data and environments:
- Tool and network allowlist:
- Maximum steps, duration, tokens, cost, calls, recursion, delegation depth:
- Transaction/amount/materiality limits:
- Approval points and exact-plan binding:
- Memory scope, retention, and cross-session rules:
- Reversibility, compensation, and finality:
- Safe modes, kill switch, and recovery objective:

## 4. Multi-agent topology

- Agents, orchestrator, supervisors, peers, and trust boundaries:
- Subject-chain propagation:
- Delegation authority and ceiling:
- Peer-output validation:
- Shared memory/state and race/conflict controls:
- Separation of duties:

## 5. Risk scenarios

| Risk ID | Cause-event-impact | Attack/failure path | Existing controls | Test/evidence | Residual risk | Owner |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

At minimum assess:

- direct/indirect prompt injection and RAG/tool poisoning;
- excessive agency, goal drift, loops, resource exhaustion, self-modification;
- unauthorized tool selection/parameters and arbitrary egress;
- identity, confused deputy, replay, stale authority, privilege amplification;
- data leakage, privacy, secret handling, and cross-session memory;
- confabulation and unsupported action-bearing claims;
- delegation, impersonation, peer trust, and emergent coordination;
- irreversible actions, duplicates, partial failure, and compensation;
- model/provider/tool/supply-chain change and drift; and
- human oversight, recourse, and emergency suspension.

## 6. Assurance scenarios

List representative intended, edge, misuse, prohibited, multi-turn, multi-agent, outage, concurrency, and adversarial cases. For each, define success, forbidden side effects, attempts, test environment, assessor independence, and evidence.

## 7. Decision

- Approved `agent_authority` and rationale:
- Mandatory controls and prohibited actions:
- Residual risks and acceptance authority:
- Deployment stage/limits:
- Reauthorization triggers and expiry:
