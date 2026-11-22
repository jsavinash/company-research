# Concurrency, Threading, and Async Model

## 1. Concurrency model

| Component | Model |
|---|---|
| **Copilot BFF** | Async (FastAPI async, SSE streaming) |
| **Forecast API** | Async workers + process pool for CPU-bound scoring |
| **Agents** | Async (LangGraph) + Temporal for durable steps |
| **Data pipeline** | Batch (Airflow) + streaming (Kafka consumers) |

## 2. Async / event loop

- **FastAPI** uses `asyncio` event loop.
- **I/O-bound** calls (DB, HTTP, LLM) are `async`.
- **CPU-bound** (LightGBM scoring) offloaded to process pool.

## 3. Threads & coroutines

| Task | Approach |
|---|---|
| **I/O-bound** (LLM, DB) | `async/await` |
| **CPU-bound** (scoring) | `ProcessPoolExecutor` |
| **Blocking libs** | `run_in_executor` |

## 4. Worker pools

| Pool | Size | Use |
|---|---|---|
| **Forecast workers** | CPU cores | Scoring |
| **Agent workers** | 2–10 | Orchestration |
| **Kafka consumers** | Per partition | Ingestion |

## 5. Backpressure

- Bounded queues.
- Concurrency limits per agent.
- Load shedding (429).

## 6. Temporal (durable execution)

- Long-running workflows (batch, backtesting).
- Automatic retries + timeouts.
- State persisted.

## 7. Front-end concurrency

- **React 18** concurrent rendering.
- **Web workers** for heavy computation (see frontend docs).
- **AbortController** for cancellable requests.

## 8. Testing concurrency

See `06_reference_implementation/tests/concurrency/`.

## 9. Related

- `02_memory_management_and_resource_pools.md`
- `03_synchronization_and_locking.md`