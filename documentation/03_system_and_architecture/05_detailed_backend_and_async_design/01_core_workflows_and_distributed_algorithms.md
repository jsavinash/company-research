# Core Workflows and Distributed Algorithms

Deep dive into the critical paths, sagas, locks, and consensus used by the platform.

## 1. Critical workflows

### 1.1 Scenario what-if (interactive)

```
Planner → Copilot → Gateway → Scenario Agent
  → Attribution Agent (A2A) → Forecast Agent
  → Data Agent (MCP) → Governance Agent
  → narrated answer
```

- **Latency budget:** p95 ≤ 10 s.
- **Parallelism:** Attribution + Forecast run concurrently where independent.
- **Fallback:** cached / last-good on failure.

### 1.2 Nightly forecast batch

```
02:00 → fetch features → train/score → reconcile (MinT) → publish → notify
```

- **Durable:** Temporal workflow (resumable).
- **Idempotent:** reruns safe.
- **SLA:** complete by 06:00.

### 1.3 Data ingestion

```
Producer → Kafka → consumer → Iceberg/Snowflake → dbt → Feast
```

- **At-least-once** + idempotent consumers.
- **Outbox pattern** for reliable publishing.

## 2. Sagas

| Saga | Steps | Compensation |
|---|---|---|
| **Forecast publish** | score → reconcile → write → notify | Mark run failed; alert |
| **Model promotion** | eval → approve → deploy → verify | Rollback to previous |
| **Data backfill** | extract → transform → load → verify | Quarantine on failure |

- **Choreography** for simple flows; **orchestration** (Temporal) for complex.

## 3. Locks & concurrency

| Concern | Mechanism |
|---|---|
| **Forecast run lock** | Per (sku, store) advisory lock to avoid duplicate runs |
| **Optimistic concurrency** | Version column on config/models |
| **Pessimistic** | Rare; only for critical config |

## 4. Consensus & coordination

| Need | Mechanism |
|---|---|
| **Leader election** (batch) | Kubernetes lease / Temporal |
| **Distributed lock** | Redis (Redlock) or DB advisory lock |
| **Configuration** | GitOps (single source of truth) |

## 5. Idempotency

- **Idempotency-Key** for POST.
- **Dedup** by (run_id, sku, store).
- **Exactly-once** via Kafka transactions where needed.

## 6. Consistency model

| Data | Consistency |
|---|---|
| **Forecasts** | Read-after-write (session) |
| **Features** | Eventual (nightly) |
| **Attribution** | Read-after-write |
| **Audit** | Strong (append-only) |

## 7. Failure handling

| Failure | Handling |
|---|---|
| Agent failure | Retry; fallback to last-good |
| Model failure | Route to fallback provider |
| Data failure | Degrade; alert |
| Partial result | Return partial + caveat |

## 8. Observability

- Trace every workflow (OpenTelemetry + LangSmith).
- Step-level status (Temporal).
- Alert on stuck workflows.

## 9. Related

- `02_cdn_edge_and_distributed_caching.md`
- `03_event_queues_and_background_jobs.md`
- `../03_high_level_design_hld/03_backend_and_bff_service_boundaries.md`