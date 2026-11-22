# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Credit book, telemetry, PII | AES-256, access logged, per-entity isolation |
| **Confidential** | PD scores, reason codes | Internal access |
| **Internal** | Model configs, features | Internal |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- **Per-entity and per-contract data isolation.**
- **De-identification** where telemetry links to identity.
- **India DPDP Act** obligations; regional processing where required.
- **Data minimization; purpose limitation.**

## 3. PII handling

- **Encryption:** AES-256 at rest, TLS in transit.
- **De-identification** before analysis.
- **Access control:** ABAC + per-entity.

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| Credit book | Per policy | Secure delete |
| Telemetry | Per policy | Secure delete |
| Scores | 2 years | Secure delete |
| Audit logs | Per policy (7y) | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| India DPDP Act | Consent, residency, data subject rights |
| IFRS 9 | Forward-looking ECL (feeds accounting) |
| SR 11-7 (model risk) | Versioned, validated, documented models |
| GDPR (if applicable) | Consent, retention |

## 6. Model risk governance

- Versioned models; independent validation.
- Documented reason codes.
- Bias/fairness checks across customer segments.
- Audit-grade lineage.

## 7. Roles

- Data owner (SFS), data steward (Corporate Units), DPO, model risk.