# Support Escalation Matrix

## 1. Severity levels

| Severity | Definition | Response time |
|---|---|---|
| **S1 — Critical** | Platform down; no forecasts; data breach | 15 min |
| **S2 — High** | Major feature broken; SLA at risk | 1 h |
| **S3 — Medium** | Partial degradation; workaround exists | 4 h |
| **S4 — Low** | Cosmetic; question | 1 business day |

## 2. Escalation matrix

| Tier | Who | Contact | Scope |
|---|---|---|---|
| **T1 — Service desk** | IT helpdesk | Portal / chat | Access, password, how-to |
| **T2 — Platform on-call** | SRE | Pager / #incidents | Latency, availability, pipeline |
| **T3 — Data science** | DS lead | #data-science | Model accuracy, attribution |
| **T4 — Security** | Security on-call | #security | Privacy, DLP, injection |
| **T5 — Leadership** | Head of Data / Platform | Phone | S1 incidents, comms |

## 3. Routing by issue type

| Issue | Route to |
|---|---|
| Can't log in | T1 |
| Copilot slow / down | T2 |
| Wrong forecast | T3 |
| Data leak / PII | T4 |
| Data permission | T2 (OPA) |
| Feature request | Product owner |

## 4. Incident process

1. **Triage** — T1 logs and classifies.
2. **Escalate** — route to tier; page on-call for S1/S2.
3. **Communicate** — status page; stakeholder updates.
4. **Resolve** — fix or mitigate.
5. **Review** — post-incident review for S1/S2.

## 5. Contact directory

| Role | Channel |
|---|---|
| Service desk | portal / #help |
| Platform on-call | PagerDuty / #incidents |
| Data science | #data-science |
| Security | #security |
| Product owner | #demand-sensing-product |

## 6. SLAs

See `../../01-business-and-strategy/01_project_overview_and_context.md` (§7 SLAs).