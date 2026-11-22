# Data Privacy and Retention

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Tax documents, TIN, DOB | AES-256, access logged, no third-party training |
| **Confidential** | Extracted fields, review actions | Internal access |
| **Internal** | Model configs, schemas | Internal |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- **Data minimization:** only collect what's needed.
- **Purpose limitation:** documents used only for extraction.
- **No third-party training:** vendor OCR only, no vendor model training.
- **Access control:** named reviewers; logged.

## 3. PII handling

- **Encryption:** AES-256 at rest, TLS in transit.
- **Redaction:** PII/TIN masked in logs and prompts.
- **Retention:** per WISP schedule; extraction artifacts purged.

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| Documents | Per WISP schedule | Secure delete |
| Extracted fields | 3 years | Secure delete |
| Review actions | 3 years | Secure delete |
| Audit logs | Per policy (7y) | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| IRS WISP | Retention, access logging, encryption |
| PII / TIN | Encryption, redaction, access control |
| No third-party training | Vendor contracts; local-first OCR |

## 6. Data subject requests

- Access / deletion via data platform workflow.
- Retention holds respected.

## 7. Cross-border

- Data stays in US regions.
- No cross-border transfer without approval.

## 8. Roles

- Data owner (operations), data steward (compliance), DLP (Purview-equivalent).