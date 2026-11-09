variable "governance_release" {
  description = "Structured, authoritative release facts evaluated before infrastructure promotion."

  type = object({
    target_environment             = string
    impact_tier                    = string
    risk_tier                      = string
    agent_authority                = string
    allowed_agent_authority        = string
    configuration_digest           = string
    approved_configuration_digest  = string
    evaluation_time                = string
    required_control_ids           = set(string)
    satisfied_control_ids          = set(string)
    control_states                 = map(string)
    evidence_states                = map(string)
    evidence_configuration_digests = set(string)
    evidence_expires_at            = map(string)
    approval = object({
      decision              = string
      configuration_digest  = string
      expires_at            = string
      independent_assurance = string
      residual_risk         = string
    })
    active_exceptions = list(object({
      exception_id                   = string
      status                         = string
      configuration_digest           = string
      expires_at                     = string
      compensating_controls_verified = bool
    }))
  })

  validation {
    condition     = contains(["low", "moderate", "high", "critical"], var.governance_release.impact_tier)
    error_message = "impact_tier must use the approved EAA-RIF consequence-severity vocabulary."
  }

  validation {
    condition     = contains(["low", "moderate", "high", "critical"], var.governance_release.risk_tier)
    error_message = "risk_tier must use the approved EAA-RIF governance-classification vocabulary."
  }

  validation {
    condition     = contains(["A0", "A1", "A2", "A3", "A4", "A5", "not_applicable"], var.governance_release.agent_authority)
    error_message = "agent_authority must use the approved EAA-RIF authority vocabulary."
  }

  validation {
    condition = lookup(
      { A0 = 0, A1 = 1, A2 = 2, A3 = 3, A4 = 4, A5 = 5, not_applicable = 0 },
      var.governance_release.agent_authority,
      99
      ) <= lookup(
      { A0 = 0, A1 = 1, A2 = 2, A3 = 3, A4 = 4, A5 = 5, not_applicable = 0 },
      var.governance_release.allowed_agent_authority,
      -1
    )
    error_message = "The configured agent authority exceeds the approved release ceiling."
  }

  validation {
    condition = (
      var.governance_release.configuration_digest == var.governance_release.approved_configuration_digest &&
      var.governance_release.configuration_digest == var.governance_release.approval.configuration_digest
    )
    error_message = "The release, approved, and authorization configuration digests must match."
  }

  validation {
    condition     = length(var.governance_release.required_control_ids) > 0
    error_message = "At least one required control must be declared."
  }

  validation {
    condition     = length(setsubtract(var.governance_release.required_control_ids, var.governance_release.satisfied_control_ids)) == 0
    error_message = "Every required control must appear in satisfied_control_ids."
  }

  validation {
    condition = alltrue([
      for control_id in var.governance_release.required_control_ids :
      lookup(var.governance_release.control_states, control_id, "missing") == "pass"
    ])
    error_message = "Every required control must have a passing control state."
  }

  validation {
    condition = alltrue([
      for control_id in var.governance_release.required_control_ids :
      lookup(var.governance_release.evidence_states, control_id, "missing") == "pass"
    ])
    error_message = "Every required control must have passing evidence."
  }

  validation {
    condition = (
      length(var.governance_release.evidence_configuration_digests) > 0 &&
      alltrue([
        for digest in var.governance_release.evidence_configuration_digests :
        digest == var.governance_release.configuration_digest
      ])
    )
    error_message = "All release evidence must be bound to the release configuration digest."
  }

  validation {
    condition = alltrue([
      for control_id in var.governance_release.required_control_ids :
      timecmp(
        lookup(var.governance_release.evidence_expires_at, control_id, "1970-01-01T00:00:00Z"),
        var.governance_release.evaluation_time
      ) > 0
    ])
    error_message = "Every required control must have unexpired evidence."
  }

  validation {
    condition = contains(
      ["restricted_pilot", "authorized", "authorized_with_conditions"],
      var.governance_release.approval.decision
    )
    error_message = "The release decision is not authorizing."
  }

  validation {
    condition     = timecmp(var.governance_release.approval.expires_at, var.governance_release.evaluation_time) > 0
    error_message = "The release authorization is expired."
  }

  validation {
    condition = (
      !contains(["high", "critical"], var.governance_release.risk_tier) ||
      var.governance_release.approval.independent_assurance == "approved"
    )
    error_message = "A high-consequence release requires independent assurance approval."
  }

  validation {
    condition = (
      !contains(["high", "critical"], var.governance_release.risk_tier) ||
      contains(["accepted", "accepted_with_conditions"], var.governance_release.approval.residual_risk)
    )
    error_message = "A high-consequence release requires explicit residual-risk acceptance."
  }

  validation {
    condition = alltrue([
      for exception in var.governance_release.active_exceptions :
      exception.status == "approved" &&
      exception.configuration_digest == var.governance_release.configuration_digest &&
      exception.compensating_controls_verified &&
      timecmp(exception.expires_at, var.governance_release.evaluation_time) > 0
    ])
    error_message = "Every active exception must be approved, current, configuration-bound, and have verified compensating controls."
  }
}
