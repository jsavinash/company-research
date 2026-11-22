# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Discovery down; data leak | 15 min |
| **S2 — High** | Major relevance/latency issue | 1 h |
| **S3 — Medium** | Partial degradation; workaround exists | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|
| **T1 — Service desk** | T-Systems support | Access, how-to |
| **T2 — Platform on-call** | T-Systems India SRE | Latency, availability, serving |
| **T3 — Data science** | DS lead | Relevance, ranking, bias |
| **T4 — Client ML/eng** | Client counterparts | Retrain approval, acceptance |
| **T5 — Security** | Security / DPO | Data boundary, privacy |
| **T6 — Leadership** | Delivery lead | S1 incidents, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Results wrong | T3 (with query + candidates) |
| Slow/down | T2 |
| Data concern | T5 |
| Retrain approval | T4 |

## 4. Contact

| Role | Channel |
|---|---|
| Service desk | T-Systems support portal |
| Platform on-call | Pager / #incidents |
| Data science | #data-science |
| Client ML/eng | Client channel |
| Security | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.