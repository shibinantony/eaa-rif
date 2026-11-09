# ORIGINAL IP: provider-free Terraform implementation example.
#
# Variable validations are blocking preconditions for this example. They do not
# observe runtime AI behavior and do not replace authorization in a target API.

output "governance_gate_summary" {
  description = "Non-sensitive summary emitted only after all variable validations pass."
  value = {
    target_environment     = var.governance_release.target_environment
    impact_tier            = var.governance_release.impact_tier
    risk_tier              = var.governance_release.risk_tier
    agent_authority        = var.governance_release.agent_authority
    configuration_digest   = var.governance_release.configuration_digest
    required_control_count = length(var.governance_release.required_control_ids)
    approval_decision      = var.governance_release.approval.decision
    gate_result            = "pass"
  }
}
