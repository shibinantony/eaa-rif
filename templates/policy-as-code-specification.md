# Policy-as-Code Specification

## Policy identity

| Field | Value |
|---|---|
| Policy ID / Version / Status |  |
| Owner / Maintainer / Approver |  |
| System/control/risk/requirement IDs |  |
| Decision type and enforcement point |  |
| Effective date / Review / Expiry |  |

## Objective and scope

- Human-readable objective:
- Failure/risk scenario treated:
- Resources, actions, subjects, environments, and exclusions:
- Authoritative enforcement point and expected response:
- Default decision:

## Trusted input contract

| Input | Type/schema | Authoritative producer | Freshness/integrity | Required? | Sensitive? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Do not accept model-generated claims as authoritative identity, approval, ownership, or transaction state.

## Output contract

| Output | Meaning | Consumer/enforcement | Evidence field |
|---|---|---|---|
| `allow` | Boolean decision |  |  |
| `reasons` | Stable denial/condition reason codes |  |  |
| `obligations` | Required approval, masking, logging, rate limit, or escalation |  |  |
| `policy_id/version` | Exact logic evaluated |  |  |

## Rule logic

- Plain-language rules and precedence:
- Parameters, thresholds, data tables, and change authority:
- Conflict-resolution behavior:
- Exception/override lookup and scope:
- Time, replay, and concurrency behavior:

## Failure behavior

For policy service unavailable, malformed/missing input, stale data, unknown version, signature failure, and evidence sink failure specify:

`fail_closed | fail_safe_read_only | degrade_and_escalate | retry_with_bound | stop`

## Test cases

| Test ID | Positive/negative/boundary/replay/outage | Input fixture | Expected decision/reason/obligation | Result/evidence |
|---|---|---|---|---|
|  |  |  |  |  |

## Decision logging and privacy

- Event schema and correlation identifiers:
- Input values stored, hashed, redacted, or excluded:
- Classification, access, retention, integrity, and review:
- Alert and incident conditions:

## Lifecycle

- Repository, review, signing, bundle/distribution, deployment, compatibility:
- Rollback and last-known-good behavior:
- Material-change triggers:
- Superseded versions and historical evidence:

## Approval

- Policy/control-owner approval:
- Security/privacy/data/model-risk review as applicable:
- Independent test result:
- Deployment authorization:
