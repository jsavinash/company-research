# High Availability, Backups, and Disaster Recovery

## 1. Availability targets

| Metric | Target |
|---|---|
| **Availability** | 99.9% monthly |
| **RPO** | ≤ 24 h |
| **RTO** | ≤ 4 h |

## 2. High availability

- **Multi-AZ** within region.
- **Redundant** services (HPA).
- **Health checks** + auto-restart.
- **Circuit breakers** + fallbacks.

## 4. Backups

| Data | Backup | Frequency | Retention |
|---|---|---|---|---|
| Iceberg | Snapshot + manifest | Continuous + daily | 90 days |
| Snowflake | Time Travel | Continuous | 90 days |
| Neo4j | Snapshot | Daily | 30 days |
| Audit | Immutable store | Continuous | Per policy |

## 5. Disaster recovery

| Scenario | Response |
|---|---|
| **Snowflake outage** | Fail over to Databricks replica |
| **Databricks outage** | Fail over to Snowflake/SageMaker |
| **Region outage** | Fail over to secondary region |
| **Kafka outage** | Buffer in DLQ; replay |

## 6. DR runbook (summary)

1. Detect → assess → fail over → communicate → recover → review.

## 7. Chaos testing

- Quarterly game days.
- Kill LLM, pipeline, DB.
- Validate degradation.

## 8. Backup restore tests

- Monthly restore test.
- Verify RPO/RTO.

## 9. Multi-region

- Active-passive (current).
- Active-active (future).