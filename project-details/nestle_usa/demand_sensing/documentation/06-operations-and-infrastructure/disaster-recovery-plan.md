# Disaster Recovery Plan

## 1. Recovery objectives

| Metric | Target |
|---|---|
| **RPO** (data loss) | ≤ 24 h (daily); ≤ 1 h for critical streams |
| **RTO** (downtime) | ≤ 4 h for copilot; ≤ 12 h for forecast batch |
| **Availability** | 99.9% monthly |

## 2. Scenarios & responses

| Scenario | Response |
|---|---|
| **Snowflake outage** | Fail over to Databricks replica; degrade to last-good forecast |
| **Databricks outage** | Fail over to Snowflake / SageMaker |
| **Azure region outage** | Fail over to secondary region (US) |
| **Kafka outage** | Buffer in DLQ; replay from retained log |
| **Neo4j outage** | Degrade to Azure AI Search (keyword) only |
| **Model serving outage** | Fall back to last-good forecast; alert |

## 3. Backup & restore

| Data | Backup | Frequency | Retention |
|---|---|---|---|
| Iceberg tables | Snapshot + manifest | Continuous + daily | 90 days |
| Snowflake | Time Travel + clone | Continuous | 90 days |
| Neo4j | Snapshot | Daily | 30 days |
| Audit logs | Immutable store | Continuous | Per policy |

## 4. Failover runbook (summary)

1. **Detect** — alert fires (Datadog).
2. **Assess** — on-call confirms severity.
3. **Fail over** — promote replica / shift traffic.
4. **Communicate** — status page + stakeholders.
5. **Recover** — restore primary; reconcile data.
6. **Review** — post-incident review.

See `incident-runbooks/db-failover-runbook.md` and `incident-runbooks/high-latency-troubleshooting.md`.

## 5. Testing

- DR drill **quarterly**.
- Game day **twice a year**.
- Backup restore test **monthly**.

## 6. Roles

- **Incident commander:** on-call SRE.
- **Comms lead:** platform lead.
- **Data lead:** data platform.