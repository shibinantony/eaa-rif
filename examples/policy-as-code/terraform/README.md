# Provider-free Terraform governance check

This root module has no cloud provider and creates no resources. Terraform variable validations implement a blocking, plan-time governance check over structured release facts. The same control objective can be implemented in OPA, Sentinel, another policy engine, or a release orchestrator.

Run with Terraform 1.6 or later:

```sh
terraform init -backend=false
terraform fmt -check -recursive
terraform validate
terraform plan -input=false -refresh=false -var-file=allow.tfvars.json
```

`deny.tfvars.json` is a negative fixture. Its plan is expected to fail because it exceeds the authority ceiling, changes the approved digest, has a failed control, and uses expired evidence.

```sh
terraform plan -input=false -refresh=false -var-file=deny.tfvars.json
```

Plan-time validation cannot observe model quality, prompt injection, data leakage, tool behavior, or operating effectiveness. Runtime controls and authoritative API authorization remain necessary.
