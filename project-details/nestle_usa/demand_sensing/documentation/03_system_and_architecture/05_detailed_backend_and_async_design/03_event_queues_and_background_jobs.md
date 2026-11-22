# Event Queues and Background Jobs

## 1. Messaging backbone

| Concern | Choice |
|---|---|
| **Streaming** | Apache Kafka |
| **Task queue** | RabbitMQ / SQS (optional) |
| **Durable workflows** | Temporal |
| **Scheduler** | Airflow / Dagster |

## 2. Kafka topics

| Topic | Purpose |
|---|---|
| `sellout` | Retailer sell-out events |
| `shipment` | Shipment events |
| `glp1` | GLP-1 prevalence updates |
| `forecast.completed` | Forecast run completion |
| `audit` | Audit events |

## 3. Event patterns

- **Event sourcing** for audit.
- **Outbox pattern** for reliable publishing.
- **CQRS** for read/write separation.

## 4. Outbox pattern

```
DB transaction → write event to outbox table → relay publishes to Kafka
```

- Guarantees at-least-once delivery.
- Idempotent consumers.

## 5. Dead-letter queues (DLQ)

- Failed messages → DLQ.
- Alert + replay tooling.
- Max retry before DLQ.

## 6. Background jobs

| Job | Schedule |
|---|---|
| **Nightly forecast** | 02:00 |
| **Feature refresh** | 01:00 |
| **Evaluation** | Weekly |
| **Cache warm** | Hourly |

## 7. Temporal workflows

- **Durable execution** for long-running flows.
- **Retries / timeouts** built in.
- **Visibility** into workflow state.

## 8. Delivery guarantees

| Pattern | Guarantee |
|---|---|
| **At-least-once** | Kafka default |
| **Exactly-once** | Kafka transactions (where needed) |
| **Idempotent consumers** | Dedup by key |

## 9. Monitoring

- Consumer lag.
- DLQ depth.
- Job success rate.

## 10. Related

- `01_cdn_edge_and_distributed_caching.md`
- `../08_bottlenecks_scalability_and_dr/`