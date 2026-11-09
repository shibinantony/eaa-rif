# Authoritative references and source-version register

Research baseline: **9 November 2026**.

> **Current-version notice:** NIST's official AI RMF page states that AI RMF 1.0 is being revised. EAA-RIF 0.1.0 therefore version-pins its baseline to **NIST AI 100-1 / AI RMF 1.0** and records a review trigger for the revised release. The Playbook page also states that it will be updated after the AI RMF revision.

## The Open Group

1. The Open Group, [Understanding the TOGAF Standard](https://help.opengroup.org/hc/en-us/articles/32726995273362-Understanding-the-TOGAF-Standard), official overview updated 21 January 2026. Supports the TOGAF Standard, 10th Edition structure: Fundamental Content covering core concepts, ADM, techniques/application, architecture content, and EA capability/governance, plus contextual Series Guides.
2. The Open Group, [Competency-to-Role Mapping — TOGAF Enterprise Architecture Practitioner](https://help.opengroup.org/hc/en-us/articles/32127544219026-Competency-to-Role-Mapping-TOGAF-Enterprise-Architecture-Practitioner), updated December 2025. Publicly confirms ADM tailoring and iteration, Architecture Vision, domain architectures, implementation/migration work, change management, requirements, and content.
3. The Open Group, [How the ArchiMate Language and the TOGAF Standard Complement Each Other](https://help.opengroup.org/hc/en-us/articles/32115987894930-How-the-ArchiMate-Language-and-the-TOGAF-Standard-Complement-Each-Other), updated December 2025. Publicly describes Phase A; Phases B–D; Phases E–F; Phase G; Phase H; domains; and traceability concepts.
4. The Open Group, [Commercial-use guidance for the TOGAF Standard](https://help.opengroup.org/hc/en-us/articles/4416348999057-What-do-I-need-to-do-in-order-to-use-the-TOGAF-Standard-commercially-with-my-clients), updated 27 December 2025, and [licensing guidance](https://www.opengroup.org/licensing-commercial-and-non-commercial). Supports the licensing caution for commercial/client use and incorporation of protected materials.
5. The Open Group, [TOGAF Standard, 10th Edition template deliverables information](https://help.opengroup.org/hc/en-us/articles/21726647171730-Are-There-Any-Template-Deliverables-for-the-TOGAF-Standard), updated December 2025. Cited only to distinguish official templates from original EAA-RIF templates; this repository does not reproduce them.

## NIST AI risk and assurance

6. Tabassi, E., [Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1), NIST AI 100-1, 26 January 2023. Primary source for purpose, voluntary/rights-preserving/non-sector-specific positioning, trustworthiness characteristics, and GOVERN/MAP/MEASURE/MANAGE.
7. NIST AI Resource Center, [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Accessible official presentation of Core categories/subcategories.
8. NIST, [AI Risk Management Framework status page](https://www.nist.gov/itl/ai-risk-management-framework). Current official status, publication timeline, GenAI Profile link, and notice that AI RMF 1.0 is being revised.
9. NIST AI Resource Center, [AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/). Suggested actions aligned to Core subcategories; explicitly voluntary and neither a checklist nor an ordered implementation sequence; current revision notice.
10. Autio, C. et al., [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1), NIST AI 600-1, 26 July 2024. Primary source for GenAI risks and suggested actions.
11. Vassilev, A. et al., [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://doi.org/10.6028/NIST.AI.100-2e2025), NIST AI 100-2e2025, March 2025, with the [CSRC publication and errata landing page](https://csrc.nist.gov/pubs/ai/100/2/e2025/final). Primary source for predictive/GenAI adversarial-ML attacks, lifecycle, attacker capabilities, and mitigation limitations.
12. NIST, [Lessons Learned from the Consortium: Tool Use in Agent Systems](https://www.nist.gov/news-events/news/2025/08/lessons-learned-consortium-tool-use-agent-systems), 2025. Supports tool-risk considerations including permission, trust environment, reversibility, monitoring, reliability, and autonomy.
13. NIST, [Building Evaluation Probes into Agentic AI](https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai), active research page. Supports evidence-linked evaluation and machine-readable audit trail research; used as direction, not a finalized control standard.
14. NIST, [Zero Trust Architecture](https://doi.org/10.6028/NIST.SP.800-207), SP 800-207, August 2020. Source for no implicit trust and per-resource authentication/authorization principles.

## NIST cybersecurity

15. Pascoe, C., Quinn, S., and Scarfone, K., [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29), NIST CSWP 29, 26 February 2024. Primary source for GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, and RECOVER and the non-prescriptive cybersecurity outcome taxonomy.

## ISO/IEC

16. ISO, [ISO/IEC 42001:2023 — Artificial intelligence management system](https://www.iso.org/standard/42001), Edition 1, December 2023. Public metadata and overview for the requirements to establish, implement, maintain, and continually improve an AI management system.
17. ISO, [ISO/IEC 23894:2023 — Artificial intelligence — Guidance on risk management](https://www.iso.org/standard/77304.html), Edition 1, February 2023. Public metadata and abstract for integrating AI-specific risk management into organizational activities.

ISO/IEC standards are copyrighted. EAA-RIF cites only public metadata and high-level descriptions; practitioners must obtain licensed copies for clause-level implementation or conformity work.

## MITRE

18. MITRE, [MITRE ATLAS](https://atlas.mitre.org/), living knowledge base accessed 9 November 2026. Source for empirically informed tactics, techniques, mitigations, and case studies spanning predictive, generative, agentic, and enterprise AI.

ATLAS informs threat scenarios and control/evaluation design. It is not a complete governance or enterprise-risk framework.

## Governance-as-Code implementation references

19. Open Policy Agent, [OPA documentation](https://www.openpolicyagent.org/docs) and [deployment guidance](https://www.openpolicyagent.org/docs/deploy). Source for general-purpose policy decisions, Rego, policy-decision-point separation, and placement near enforcement points.
20. Open Policy Agent, [Policy testing](https://www.openpolicyagent.org/docs/policy-testing). Source for Rego unit-test practices.
21. Microsoft, [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) and [policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics). Source for management-plane resource evaluation, audit/deny/modify-style effects, and policy-as-code workflow guidance.
22. Microsoft, [PyRIT documentation](https://azure.github.io/PyRIT/). Source for automated and human-led generative-AI red teaming and scenario-based testing.
23. NVIDIA, [NeMo Guardrails v0.24.1 release](https://github.com/NVIDIA-NeMo/Guardrails/releases/tag/v0.24.1) and [version-pinned documentation source tree](https://github.com/NVIDIA-NeMo/Guardrails/tree/v0.24.1/docs). Source baseline for input, retrieval, dialog, execution/tool, and output rail placement. Revalidate placement and configuration when adopting another release.
24. OpenTelemetry, [GenAI semantic-conventions project](https://github.com/open-telemetry/semantic-conventions-genai) and [GenAI attributes notice](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/). Source for model, agent, retrieval, tool, and MCP observability conventions and sensitivity warnings. Conventions are evolving; implementations should version-pin them.

## Governance operating model

25. The Institute of Internal Auditors, [Three Lines Model: Assurance and Advice in Support of Effective Governance](https://www.theiia.org/globalassets/site/resources/statements-of-position/tlm_assurance_advice_support_effective_gov_en.pdf), Statement of Position, 8 July 2026. Source for the distinction and coordination of first-line management, second-line expertise/support/monitoring/challenge, and third-line independent assurance. EAA-RIF's AI-specific role allocation remains an original adaptation.

## Reference-use rules

- Facts about source frameworks use **SOURCE FRAMEWORK** and an authoritative citation.
- Relationships between frameworks use **DERIVED MAPPING** and an explicit non-official disclaimer.
- EAA-RIF methods, names, schemas, controls, and diagrams use **ORIGINAL IP**.
- A tool is cited only where its enforcement, evaluation, observability, or evidence function is precise.
- A framework update triggers a mapping impact assessment; historical approvals retain the version against which they were made.
