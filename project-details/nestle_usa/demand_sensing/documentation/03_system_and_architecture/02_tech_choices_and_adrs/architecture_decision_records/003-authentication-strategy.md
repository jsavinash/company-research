# ADR 003: Authentication Strategy

## Status

Accepted (2026-02)

## Context

The platform serves internal Nestlé USA planners, RGM analysts, supply planners, and data stewards, and integrates with enterprise systems (SAP, Salesforce, ServiceNow). It must enforce **permission-aware retrieval** — a planner must only retrieve data for the banners/DMAs they are entitled to — and comply with enterprise identity and data-privacy policy.

Nestlé is a Microsoft-centric enterprise (Entra ID), with Okta for partner collaboration and AWS IAM for cloud resources.

## Decision

Adopt a **federated identity + externalized authorization** model:

| Concern | Choice | Rationale |
|---|---|---|
| Enterprise SSO | **Microsoft Entra ID** (OIDC) | Corporate identity, MFA, conditional access |
| Partner / retailer access | **Okta** | External collaboration |
| Cloud IAM | **AWS IAM** | Bedrock/S3-resident assets |
| Authorization (ABAC) | **OPA (Open Policy Agent)** | Externalized policy: planner → banner/DMA/role |
| AI guardrails | **NeMo Guardrails + Lakera** | Prompt-injection defense, content policy |
| DLP | **Microsoft Purview** | PII / confidential data protection |
| Secrets | **HashiCorp Vault** | No secrets in code |

**Key principle:** authentication is federated (Entra ID), but **authorization is externalized to OPA** so data-access policy is centrally managed and auditable, and enforced at both the AI gateway and the data layer.

## Consequences

**Positive:**
- Fine-grained, auditable, centrally-managed access.
- Satisfies retailer-contract and panel-privacy constraints.
- No PII in prompts (Purview + redaction).

**Negative:**
- OPA policy authoring and testing requires discipline.
- Policy-check latency must be managed (cache decisions).

**Mitigation:**
- Policy-as-code with unit tests.
- Decision caching.
- Regular access reviews.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| App-level RBAC only | Simple | Coarse; can't express banner/DMA ABAC; policy drift |
| Entra ID groups only | Native | Hard to express fine-grained ABAC; not portable to data layer |
| OAuth2 + custom policy service | Flexible | Reinventing OPA; slower to audit |

## Compliance / Governance

- Retailer contracts: no pooling without permission.
- Panel privacy: aggregate only.
- Audit: every access decision logged.

## References

- `../../09_security_and_compliance/01_authn_authz_and_identity.md`
- `../../../Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/architecture-decision-records/002-authentication-strategy.md`

## Metadata

| Field | Value |
|---|---|
| Author | AI Solutions Architect |
| Date | 2026-02 |
| Reviewers | Security & Compliance, IT |
| Supersedes | — |
| Superseded by | — |