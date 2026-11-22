# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Coaching down; PII leak | 15 min |
| **S2 — High** | Major accuracy/hallucination issue | 1 h |
| **S3 — Medium** | Partial degradation; workaround | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|
| **T1 — Service desk** | Support | Access, how-to |
| **T2 — Platform on-call** | SRE | Latency, availability |
| **T3 — Data science** | DS lead | Accuracy, grounding, hallucination |
| **T4 — Nutrition science** | Nutrition | Adequacy, KB |
| **T5 — Security/Privacy** | Security / DPO | PII, injection |
| **T6 — Leadership** | Product leadership | S1, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Wrong plan | T3 (with profile + plan) |
| Slow/down | T2 |
| PII concern | T5 |
| Adequacy question | T4 |

## 4. Contact

| Role | Channel |
|---|---|
| Service desk | portal / #help |
| Platform on-call | Pager / #incidents |
| Data science | #data-science |
| Nutrition | #nutrition |
| Security | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.