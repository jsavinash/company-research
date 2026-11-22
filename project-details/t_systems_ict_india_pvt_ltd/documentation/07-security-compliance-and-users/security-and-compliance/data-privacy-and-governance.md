# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | User/session data, PII-adjacent | Access logged, minimized |
| **Confidential** | Client event stream, catalog | Client-owned; single-client isolation |
| **Internal** | Model configs, features | Internal |
| **Public** | Public catalog | Unrestricted |

## 2. Privacy principles

- **Single-client isolation:** no cross-client training on raw behaviour.
- **Data minimization; purpose limitation.**
- **Consent/retention** per client policy.
- **Access control; audit.**

## 3. PII handling

- **Redaction** in logs.
- **Consent** verified per client.
- **Retention** per client policy.

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| Event stream | Per client policy | Secure delete |
| Interactions | 2 years | Secure delete |
| Model artifacts | Versioned, 2 years | Archive |
| Audit logs | Per policy | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| Client contract | Single-client isolation; data boundary |
| GDPR (EU client) | Consent, data subject rights, retention |
| ISO 27001 | Security controls |

## 6. Data subject requests

- Access / deletion via client governance workflow.

## 7. Cross-border

- Data stays in the client's region; no cross-border transfer without approval.

## 8. Roles

- Client data owner, T-Systems delivery, DPO.