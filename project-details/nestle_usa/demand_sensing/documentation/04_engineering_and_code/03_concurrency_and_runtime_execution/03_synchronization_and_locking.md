# Synchronization and Locking

## 1. Locking primitives

| Primitive | Use |
|---|---|
| **Mutex / Lock** | In-process critical sections |
| **Semaphore** | Concurrency limits |
| **Read-write lock** | Read-heavy data |
| **Advisory lock (DB)** | Cross-process coordination |
| **Distributed lock (Redis)** | Multi-instance coordination |

## 2. Deadlock avoidance

- **Lock ordering:** always acquire in the same order.
- **Timeouts:** `lock.acquire(timeout=...)`.
- **Try-lock** where contention is high.
- **Single lock** per resource where possible.

## 3. Distributed locks

| Use | Mechanism |
|---|---|
| **Forecast run lock** | DB advisory lock per (sku, store) |
| **Model promotion** | Redis lock / Temporal |
| **Cache rebuild** | Redis Redlock |

## 4. Atomic operations

- **Atomic counters** (Redis INCR).
- **Compare-and-swap** for optimistic concurrency.
- **Idempotency keys** for safe retries.

## 5. Optimistic concurrency

- **Version column** on mutable records.
- **ETag / If-Match** for HTTP.
- **Retry on conflict.**

## 6. Lock-free patterns

- **Immutable data** + copy-on-write.
- **Message queues** instead of shared state.
- **Actor model** (per-entity mailbox).

## 7. Testing

- **Concurrency tests** in `06_reference_implementation/tests/concurrency/`.
- **Race condition** detection (stress tests).
- **Deadlock** simulation.

## 8. Related

- `01_concurrency_threading_and_async_model.md`
- `06_reference_implementation/src/services/`