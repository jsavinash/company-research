# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Inference down; PHI leak | 15 min |
| **S2 — High** | Major accuracy/drift issue | 1 h |
| **S3 — Medium** | Partial degradation; workaround | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|
| **T1 — Service desk** | Support | Access, how-to |
| **T2 — Platform on-call** | SRE | Latency, availability, inference |
| **T3 — Data science** | DS lead | Accuracy, calibration, drift |
| **T4 — Clinical lead** | Clinical | Sign-off, reader study |
| **T5 — Regulatory** | Regulatory affairs | MDR/FDA/CDSCO |
| **T6 — Security/Privacy** | Security / DPO | PHI, DPDP |
| **T7 — Leadership** | Product leadership | S1, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Wrong finding | T3 (with study + heatmap) |
| Slow/down | T2 |
| PHI concern | T6 |
| Regulatory | T5 |

## 4. Contact

| Role | Channel |
|---|---|
| Service desk | Internal portal |
| Platform on-call | Pager / #incidents |
| Data science | #data-science |
| Clinical | #clinical |
| Regulatory | #regulatory |
| Security/Privacy | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.