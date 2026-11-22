# Data Privacy and Retention

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Household panel PII, retailer-confidential data | Aggregate only; ABAC; no cross-retailer pooling |
| **Confidential** | GLP-1 Rx prevalence, sell-out | Per-retailer governance; least privilege |
| **Internal** | Forecasts, attribution | Internal access |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- **Data minimization:** only collect what's needed.
- **Purpose limitation:** retailer data used only per contract.
- **Aggregate panel:** no household-level PII; minimum cell sizes.
- **Consent:** honored for panel data.
- **No cross-retailer pooling** without explicit permission.

## 3. Retention

| Data | Retention | Disposal |
|---|---|---|
| Sell-out / shipment | 3 years | Secure delete |
| Panel (aggregate) | 3 years | Secure delete |
| Forecasts | 2 years | Secure delete |
| Audit logs | Per policy (e.g., 7 years) | Archive |
| Prompts / LLM logs | 90 days | Auto-delete |
| Model artifacts | Versioned, 2 years | Archive |

## 4. PII handling

- **Redaction** before prompts (Purview + custom redactor).
- **Tokenization** for analytics where possible.
- **No PII in logs** — scrubbed at ingestion.
- **Access reviews** quarterly.

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| Retailer contracts | ABAC + contract-term parsing + no pooling |
| Household panel licensing | Aggregate-only + consent |
| Enterprise data policy | Purview DLP + retention |
| Audit requirements | Immutable audit log |

## 6. Data subject requests

- Access / deletion requests handled via data platform workflow.
- Retention holds respected.

## 7. Cross-border

- Data stays in **US regions**.
- No cross-border transfer without approval.

## 8. Roles

- **Data owner:** business domain.
- **Data steward:** quality + policy.
- **Privacy officer:** compliance.