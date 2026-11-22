# Core Workflows and Distributed Algorithms

## 1. Critical workflows

### 1.1 Intake → plan → coaching
```
Owner text → Intake Extractor → Profile → Solver + Adequacy Gate → Plan → RAG Coaching → Vet Summary
```

### 1.2 Vet endorsement
```
Vet Summary → Vet reviews → Endorse/Override → Label
```

### 1.3 Continuous eval
```
Nightly → eval harness → red-team → regression gates
```

## 2. Sagas

| Saga | Steps | Compensation |
|---|---|---|
| **Plan generation** | extract → solve → coach | Mark failed; retry |
| **Vet summary** | draft → endorse | Log override |
| **Model promotion** | eval → approve → deploy | Rollback |

## 3. Locks & concurrency

| Concern | Mechanism |
|---|---|
| **Profile lock** | Per-pet advisory lock |
| **Optimistic concurrency** | Version column |
| **Idempotency** | Idempotency-Key for POST |

## 4. Consensus & coordination

| Need | Mechanism |
|---|---|
| **Leader election** (batch) | Kubernetes lease / Temporal |
| **Distributed lock** | Redis / DB advisory |
| **Configuration** | GitOps |

## 5. Idempotency

- `Idempotency-Key` for POST.
- Dedup by (run_id, plan).

## 6. Consistency model

| Data | Consistency |
|---|---|
| **Plans** | Read-after-write |
| **Coaching** | Read-after-write |
| **Audit** | Strong (append-only) |

## 7. Failure handling

| Failure | Handling |
|---|---|
| Agent failure | Retry; fallback |
| Model failure | Fallback provider |
| Data failure | Degrade; alert |

## 8. Observability

- Trace every workflow (OpenTelemetry + LangSmith).
- Alert on stuck workflows.