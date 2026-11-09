# Azure Policy implementation example

`require-private-ai-service.json` illustrates where a cloud management-plane policy can enforce an infrastructure requirement. It is intentionally narrow: it audits or denies an Azure OpenAI account whose public network access is not explicitly disabled.

Before using it, verify the resource type, `kind`, and policy aliases in the target Azure environment, test with `Audit`, assess existing resources, and only then consider `Deny`. Azure resource schemas and aliases can change.

This example does **not**:

- authorize a user, workload, or agent;
- inspect prompts or model output;
- govern RAG entitlements or data purpose;
- evaluate model quality, safety, fairness, or security; or
- authorize a business transaction.

Azure Policy is shown as one possible infrastructure enforcement technology. Equivalent cloud, Kubernetes, admission-control, or configuration-policy mechanisms can implement the same control objective.
