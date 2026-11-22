# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Extraction down; PII leak | 15 min |
| **S2 — High** | Major accuracy issue; queue backlog | 1 h |
| **S3 — Medium** | Partial degradation; workaround exists | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|
| **T1 — Support** | Support team (knowledge base + tickets) | How-to, access |
| **T2 — Engineering** | Extraction service on-call | Errors, latency, queue |
| **T3 — Data science** | DS lead | Accuracy, calibration |
| **T4 — Security** | Security/compliance | PII, DLP, audit |
| **T5 — Leadership** | Operations manager | S1 incidents, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Extraction wrong | T3 (with document + field) |
| Extraction slow/down | T2 |
| PII concern | T4 |
| Data access | T2 |

## 4. Contact

| Role | Channel |
|---|---|
| Support | support@mytaxprepoffice.com / (307) 414-1211 |
| Engineering on-call | Internal pager |
| Data science | #data-science |
| Security | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.