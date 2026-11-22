# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Scoring down; data leak | 15 min |
| **S2 — High** | Major accuracy/drift issue | 1 h |
| **S3 — Medium** | Partial degradation; workaround | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|---|
| **T1 — Service desk** | Support | Access, how-to |
| **T2 — Platform on-call** | SRE | Latency, availability, scoring |
| **T3 — Data science** | DS lead | Accuracy, calibration, drift |
| **T4 — Model risk** | Model-risk | Validation, audit, bias |
| **T5 — Security/Privacy** | Security / DPO | Data boundary, DPDP |
| **T6 — Credit-risk owner** | Credit-risk leadership | S1, sign-off |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Score wrong | T3 (with account + reason codes) |
| Slow/down | T2 |
| Data concern | T5 |
| Model validation | T4 |

## 4. Contact

| Role | Channel |
|---|---|
| Service desk | Internal portal |
| Platform on-call | Pager / #incidents |
| Data science | #data-science |
| Model risk | #model-risk |
| Security/Privacy | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.