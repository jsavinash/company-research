# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Household panel PII, retailer-confidential | Aggregate only; ABAC |
| **Confidential** | GLP-1 Rx, sell-out | Per-retailer governance |
| **Internal** | Forecasts, attribution | Internal access |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- Data minimization.
- Purpose limitation.
- Aggregate panel only.
- Consent honored.
- No cross-retailer pooling without permission.

## 3. PII masking

- **Redaction** before prompts (Purview + custom).
- **Tokenization** for analytics.
- **No PII in logs.**
- **Minimum cell sizes** for panel.

## 4. Retention

| Data | Retention |
|---|---|
| Sell-out / shipment | 3 years |
| Panel (aggregate) | 3 years |
| Forecasts | 2 years |
| Audit logs | Per policy (7y) |
| Prompts / LLM logs | 90 days |

## 5. Audit logs

- **Immutable, append-only.**
- **Every run** logged with run ID.
- **Retention** per policy.
- **Access** restricted.

## 6. Compliance mapping

| Regulation / policy | Control |
|---|---|
| Retailer contracts | ABAC + contract-term parsing |
| Panel licensing | Aggregate + consent |
| Enterprise data policy | Purview DLP + retention |
| Audit requirements | Immutable log |

## 7. Data subject requests

- Access / deletion via workflow.
- Retention holds respected.

## 8. Cross-border

- Data stays in **US regions.**
- No cross-border transfer without approval.

## 9. Roles

- Data owner, data steward, privacy officer.

## 10. Related

- `01_authn_authz_and_identity.md`
- `02_appsec_and_data_protection.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/07-security-compliance-and-users/security-and-compliance/data-privacy-and-retention.md`