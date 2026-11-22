# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Triage down; genomic data leak | 15 min |
| **S2 — High** | Major accuracy issue; queue backlog | 1 h |
| **S3 — Medium** | Partial degradation; workaround exists | 4 h |
| **S4 — Low** | Question / cosmetic | 1 business day |

## 2. Escalation matrix

| Tier | Who | Scope |
|---|---|---|---|
| **T1 — Support** | Support team | How-to, access |
| **T2 — Engineering** | Triage service on-call | Errors, latency, queue |
| **T3 — Data science** | DS lead | Accuracy, calibration, ancestry gap |
| **T4 — Clinical** | Clinical lead | Classification sign-off, QMS |
| **T5 — Security/Privacy** | Security / DPO | Genomic data, PDPA/UU PDP |
| **T6 — Leadership** | COO / CEO | S1 incidents, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Triage wrong | T3 (with variant + evidence) |
| Triage slow/down | T2 |
| Genomic data concern | T5 |
| Classification dispute | T4 |

## 4. Contact

| Role | Channel |
|---|---|
| Support | help@nalagenetics.com |
| Engineering on-call | Internal pager |
| Data science | #data-science |
| Clinical | #clinical |
| Security/Privacy | #security |

## 5. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.