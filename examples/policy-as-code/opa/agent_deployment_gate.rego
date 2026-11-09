package eaa_rif.deployment

import rego.v1

# ORIGINAL IP: illustrative deployment-gate policy. It evaluates trusted,
# structured release metadata. It is not a compliance certification and does
# not replace runtime authorization in the target service.

default allow := false

authorizing_decisions := {
	"restricted_pilot",
	"authorized",
	"authorized_with_conditions",
}

high_consequence_tiers := {"high", "critical"}

supported_risk_tiers := {"low", "moderate", "high", "critical"}

supported_impact_tiers := {"low", "moderate", "high", "critical"}

supported_lifecycle_states := {
	"proposed",
	"sandbox",
	"development",
	"validation",
	"restricted_pilot",
	"production",
	"suspended",
	"retired",
}

authority_rank := {
	"A0": 0,
	"A1": 1,
	"A2": 2,
	"A3": 3,
	"A4": 4,
	"A5": 5,
	"not_applicable": 0,
}

allow if count(deny_reasons) == 0

deny_reasons contains "system.system_id is required" if {
	not input.system.system_id
}

deny_reasons contains "system.risk_tier is required" if {
	not input.system.risk_tier
}

deny_reasons contains "system.impact_tier is required" if {
	not input.system.impact_tier
}

deny_reasons contains "system.agent_authority is required" if {
	not input.system.agent_authority
}

deny_reasons contains "system.lifecycle_state is required" if {
	not input.system.lifecycle_state
}

deny_reasons contains "system.configuration_digest is required" if {
	not input.system.configuration_digest
}

deny_reasons contains "release.configuration_digest is required" if {
	not input.release.configuration_digest
}

deny_reasons contains "release.target_environment is required" if {
	not input.release.target_environment
}

deny_reasons contains "release.approved_configuration_digest is required" if {
	not input.release.approved_configuration_digest
}

deny_reasons contains "release.allowed_agent_authority is required" if {
	not input.release.allowed_agent_authority
}

deny_reasons contains "release.required_control_ids is required" if {
	not input.release.required_control_ids
}

deny_reasons contains "release.satisfied_control_ids is required" if {
	not input.release.satisfied_control_ids
}

deny_reasons contains "release.control_states is required" if {
	not input.release.control_states
}

deny_reasons contains "release.evidence is required" if {
	not input.release.evidence
}

deny_reasons contains "release.approval is required" if {
	not input.release.approval
}

deny_reasons contains "now is required" if {
	not input.now
}

deny_reasons contains "system.risk_tier uses an unsupported value" if {
	tier := object.get(input.system, "risk_tier", "")
	not supported_risk_tier(tier)
}

deny_reasons contains "system.impact_tier uses an unsupported value" if {
	tier := object.get(input.system, "impact_tier", "")
	not supported_impact_tier(tier)
}

deny_reasons contains "system.agent_authority uses an unsupported value" if {
	authority := object.get(input.system, "agent_authority", "")
	not supported_authority(authority)
}

deny_reasons contains "system.lifecycle_state uses an unsupported value" if {
	state := object.get(input.system, "lifecycle_state", "")
	not supported_lifecycle_state(state)
}

deny_reasons contains "release.allowed_agent_authority uses an unsupported value" if {
	authority := object.get(input.release, "allowed_agent_authority", "")
	not supported_authority(authority)
}

deny_reasons contains "the release configuration digest does not match the system configuration" if {
	input.release.configuration_digest != input.system.configuration_digest
}

deny_reasons contains "the release configuration digest is not the approved configuration" if {
	input.release.configuration_digest != input.release.approved_configuration_digest
}

deny_reasons contains "the approval is bound to a different configuration" if {
	input.release.approval.configuration_digest != input.release.configuration_digest
}

deny_reasons contains "a suspended or retired system cannot be deployed" if {
	input.system.lifecycle_state in {"suspended", "retired"}
}

deny_reasons contains "the configured agent authority exceeds the release ceiling" if {
	actual := authority_rank[input.system.agent_authority]
	ceiling := authority_rank[input.release.allowed_agent_authority]
	actual > ceiling
}

deny_reasons contains "at least one required control must be declared" if {
	count(input.release.required_control_ids) == 0
}

deny_reasons contains sprintf("required control is not satisfied: %s", [control_id]) if {
	some control_id in input.release.required_control_ids
	not control_satisfied(control_id)
}

deny_reasons contains sprintf("required control is not passing: %s", [control_id]) if {
	some control_id in input.release.required_control_ids
	state := object.get(input.release.control_states, control_id, "missing")
	state != "pass"
}

deny_reasons contains sprintf("required control lacks fresh configuration-matched evidence: %s", [control_id]) if {
	some control_id in input.release.required_control_ids
	not valid_evidence(control_id)
}

deny_reasons contains "the release decision is not authorizing" if {
	decision := object.get(input.release.approval, "decision", "")
	not authorizing_decision(decision)
}

deny_reasons contains "the release approval is expired or invalid" if {
	expires_at := object.get(input.release.approval, "expires_at", "")
	not unexpired(expires_at)
}

deny_reasons contains "high-consequence release lacks independent assurance approval" if {
	input.system.risk_tier in high_consequence_tiers
	object.get(input.release.approval, "independent_assurance", "") != "approved"
}

deny_reasons contains "high-consequence release lacks residual-risk acceptance" if {
	input.system.risk_tier in high_consequence_tiers
	decision := object.get(input.release.approval, "residual_risk", "")
	not residual_risk_accepted(decision)
}

deny_reasons contains sprintf("exception is invalid, expired, or bound to another configuration: %s", [exception_id]) if {
	exceptions := object.get(input.release, "exceptions", [])
	some exception in exceptions
	exception_id := object.get(exception, "exception_id", "unknown")
	not valid_exception(exception)
}

control_satisfied(control_id) if {
	some satisfied_id in input.release.satisfied_control_ids
	satisfied_id == control_id
}

authorizing_decision(decision) if {
	decision in authorizing_decisions
}

supported_risk_tier(tier) if {
	tier in supported_risk_tiers
}

supported_impact_tier(tier) if {
	tier in supported_impact_tiers
}

supported_authority(authority) if {
	rank := object.get(authority_rank, authority, -1)
	rank >= 0
}

supported_lifecycle_state(state) if {
	state in supported_lifecycle_states
}

residual_risk_accepted(decision) if {
	decision in {"accepted", "accepted_with_conditions"}
}

valid_evidence(control_id) if {
	evidence_records := object.get(input.release, "evidence", [])
	some evidence in evidence_records
	evidence.control_id == control_id
	evidence.state == "pass"
	evidence.configuration_digest == input.release.configuration_digest
	unexpired(evidence.expires_at)
}

valid_exception(exception) if {
	exception.status == "approved"
	exception.configuration_digest == input.release.configuration_digest
	exception.compensating_controls_verified == true
	unexpired(exception.expires_at)
}

unexpired(expires_at) if {
	expires_ns := time.parse_rfc3339_ns(expires_at)
	now_ns := time.parse_rfc3339_ns(input.now)
	expires_ns > now_ns
}
