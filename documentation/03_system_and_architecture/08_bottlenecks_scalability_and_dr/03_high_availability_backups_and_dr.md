# High Availability, Backups, and Disaster Recovery

## 1. Availability targets

| Metric | Target |
|---|---|
| **Availability** | 99.9% monthly |
| **RPO** | ≤ 24 h (≤ 1 h critical) |
| **RTO** | ≤ 4 h (copilot); ≤ 12 h (batch) |

## 2. High availability

- **Multi-AZ** within region.
- **Redundant** services (HPA).
- **Health checks** + auto-restart.
- **Circuit breakers** + fallbacks.

## 3. Backups

| Data | Backup | Frequency | Retention |
|---|---|---|---|
| Iceberg | Snapshot + manifest | Continuous + daily | 90 days |
| Snowflake | Time Travel + clone | Continuous | 90 days |
| Neo4j | Snapshot | Daily | 30 days |
| Audit | Immutable store | Continuous | Per policy |

## 4. Disaster recovery

| Scenario | Response |
|---|---|
| **Snowflake outage** | Fail over to Databricks replica |
| **Databricks outage** | Fail over to Snowflake/SageMaker |
| **Region outage** | Fail over to secondary region |
| **Kafka outage** | Buffer in DLQ; replay |

## 5. DR runbook (summary)

1. Detect → assess → fail over → communicate → recover → review.

See `Nestle-USA-DemandSensing-AIArchitect-UseCase/06-operations-and-infrastructure/incident-runbooks/`.

## 6. Chaos testing

- Quarterly game days.
- Kill LLM, pipeline, DB.
- Validate degradation.

## 7. Backup restore tests

- Monthly restore test.
- Verify RPO/RTO.

## 8. Multi-region

- Active-passive (current).
- Active-active (future).

## 9. Related

- `02_load_balancing_and_auto_scaling.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/06-operations-and-infrastructure/disaster-recovery-plan.md`