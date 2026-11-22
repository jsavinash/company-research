# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Pet PII, owner data | AES-256, access logged |
| **Confidential** | Profiles, plans, coaching | Internal access |
| **Internal** | Model configs, schemas | Internal |
| **Public** | Product specs, AAFCO | Unrestricted |

## 2. Privacy principles

- **Data minimization; purpose limitation.**
- **Consent honored.**
- **PII never in prompts.**
- **Access control; audit.**

## 3. PII handling

- **Redaction** before prompts (Purview + custom).
- **Pet data separated from public KB.**
- **No PII in logs.**

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| Profiles | 3 years | Secure delete |
| Coaching | 2 years | Secure delete |
| Prompts / LLM logs | 90 days | Auto-delete |
| Audit logs | Per policy (7y) | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| Enterprise data policy | Purview DLP + retention |
| PII / consent | Redaction, consent |
| Audit requirements | Immutable log |

## 6. Data subject requests

- Access / deletion via governance workflow.
- Retention holds respected.

## 7. Cross-border

- Data stays in US regions.
- No cross-border transfer without approval.

## 8. Roles

- Data owner, data steward, DPO.