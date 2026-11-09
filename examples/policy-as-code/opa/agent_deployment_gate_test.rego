package eaa_rif.deployment_test

import rego.v1

base_input := {
	"system": {
		"system_id": "SYS-BANK-AGENT-001",
		"impact_tier": "high",
		"risk_tier": "high",
		"agent_authority": "A3",
		"lifecycle_state": "restricted_pilot",
		"configuration_digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
	},
	"release": {
		"target_environment": "production",
		"configuration_digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
		"approved_configuration_digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
		"allowed_agent_authority": "A3",
		"required_control_ids": ["CTRL-RELEASE-001"],
		"satisfied_control_ids": ["CTRL-RELEASE-001"],
		"control_states": {"CTRL-RELEASE-001": "pass"},
		"evidence": [{
			"evidence_id": "EVID-RELEASE-001",
			"control_id": "CTRL-RELEASE-001",
			"state": "pass",
			"configuration_digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
			"expires_at": "2027-02-07T10:00:00Z",
		}],
		"approval": {
			"decision": "restricted_pilot",
			"configuration_digest": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
			"expires_at": "2027-02-07T10:15:00Z",
			"independent_assurance": "approved",
			"residual_risk": "accepted_with_conditions",
		},
		"exceptions": [],
	},
	"now": "2026-11-09T10:30:00Z",
}

test_allows_complete_configuration_bound_release if {
	data.eaa_rif.deployment.allow with input as base_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as base_input
	count(reasons) == 0
}

test_denies_configuration_digest_mismatch if {
	changed_release := object.union(base_input.release, {"configuration_digest": "sha256:2222222222222222222222222222222222222222222222222222222222222222"})
	changed_input := object.union(base_input, {"release": changed_release})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"the release configuration digest does not match the system configuration" in reasons
}

test_denies_missing_required_control if {
	changed_release := object.union(base_input.release, {"required_control_ids": ["CTRL-RELEASE-001", "CTRL-MISSING-001"]})
	changed_input := object.union(base_input, {"release": changed_release})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"required control is not satisfied: CTRL-MISSING-001" in reasons
}

test_denies_expired_evidence if {
	expired_evidence := [object.union(base_input.release.evidence[0], {"expires_at": "2026-11-01T00:00:00Z"})]
	changed_release := object.union(base_input.release, {"evidence": expired_evidence})
	changed_input := object.union(base_input, {"release": changed_release})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"required control lacks fresh configuration-matched evidence: CTRL-RELEASE-001" in reasons
}

test_denies_failed_control_state if {
	changed_release := object.union(base_input.release, {"control_states": {"CTRL-RELEASE-001": "fail"}})
	changed_input := object.union(base_input, {"release": changed_release})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"required control is not passing: CTRL-RELEASE-001" in reasons
}

test_denies_unsupported_agent_authority if {
	changed_system := object.union(base_input.system, {"agent_authority": "A99"})
	changed_input := object.union(base_input, {"system": changed_system})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"system.agent_authority uses an unsupported value" in reasons
}

test_denies_unsupported_impact_tier if {
	changed_system := object.union(base_input.system, {"impact_tier": "extreme"})
	changed_input := object.union(base_input, {"system": changed_system})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"system.impact_tier uses an unsupported value" in reasons
}

test_denies_unverified_exception if {
	invalid_exception := [{
		"exception_id": "EXC-001",
		"status": "approved",
		"configuration_digest": base_input.release.configuration_digest,
		"expires_at": "2027-01-01T00:00:00Z",
		"compensating_controls_verified": false,
	}]
	changed_release := object.union(base_input.release, {"exceptions": invalid_exception})
	changed_input := object.union(base_input, {"release": changed_release})

	not data.eaa_rif.deployment.allow with input as changed_input
	reasons := data.eaa_rif.deployment.deny_reasons with input as changed_input
	"exception is invalid, expired, or bound to another configuration: EXC-001" in reasons
}
