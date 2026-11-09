# OPA/Rego deployment-gate example

This example implements `POL-DEPLOY-001` and supports `CTRL-RELEASE-001`. It is intentionally implementation-neutral in its governance model: OPA is one example policy decision point, and another policy engine can implement the same control contract.

The policy evaluates structured facts supplied by authoritative registries and release services. It does not infer approval, identity, or evidence from model-generated text. The CI/CD system remains the policy enforcement point and must block when the policy returns deny or cannot be evaluated.

Run locally with OPA 1.x:

```sh
opa fmt --fail agent_deployment_gate.rego agent_deployment_gate_test.rego
opa test . -v
opa eval --format=pretty --data agent_deployment_gate.rego --input input-allow.json 'data.eaa_rif.deployment'
opa eval --format=pretty --data agent_deployment_gate.rego --input input-deny.json 'data.eaa_rif.deployment'
```

`input-allow.json` must evaluate to `allow: true`; `input-deny.json` demonstrates configuration, control-state, and evidence failures. These examples are control-engineering illustrations, not proof of regulatory compliance or runtime authorization.
