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
| `intake` | Owner messages |
| `coaching` | Coaching requests |
| `vet_summary` | Vet summary requests |
| `eval` | Eval results |
| `audit` | Audit events |

## 3. Event patterns

- **Outbox pattern** for reliable publishing.
- **CQRS** for read/write separation.

## 4. Dead-letter queues (DLQ)

- Failed messages → DLQ.
- Alert + replay tooling.

## 5. Background jobs

| Job | Schedule |
|---|---|
| **Nightly eval** | Daily |
| **Red-team** | Weekly |
| **Cache warm** | Hourly |

## 6. Temporal workflows

- **Durable execution** for long-running flows.
- **Retries / timeouts** built in.

## 5. Delivery guarantees

| Pattern | Guarantee |
|---|---|
| **At-least-once** | Kafka default |
| **Exactly-once** | Kafka transactions (where needed) |
| **Idempotent consumers** | Dedup by key |

## 8. Monitoring

- Consumer lag.
- DLQ depth.
- Job success rate.