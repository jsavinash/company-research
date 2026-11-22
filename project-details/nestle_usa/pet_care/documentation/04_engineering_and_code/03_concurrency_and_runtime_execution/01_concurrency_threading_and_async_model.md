# Concurrency, Threading, and Async Model

## 1. Concurrency model

| Component | Model |
|---|---|
| **Copilot BFF** | Async (FastAPI async, SSE streaming) |
| **Intake API** | Async |
| **Coaching API** | Async + queue |
| **RAG** | Async retrieval + generation |

## 2. Async / event loop

- **FastAPI** uses `asyncio`.
- **I/O-bound** calls (LLM, DB, vector) are `async`.
- **CPU-bound** (reranking) offloaded to process pool.

## 4. Worker pools

| Pool | Size | Use |
|---|---|---|
| **Coaching workers** | 2–10 | Generation |
| **Intake workers** | 2–10 | Extraction |
| **Eval workers** | 2–4 | Nightly eval |

## 5. Backpressure

- Bounded queues.
- Concurrency limits.
- Load shedding (429).

## 6. Temporal (durable execution)

- Long-running workflows (nightly eval, retraining).
- Automatic retries + timeouts.

## 7. Front-end concurrency

- **React 18** concurrent rendering.
- **AbortController** for cancellable requests.

## 8. Testing concurrency

See `../../05-quality-and-verification/`.