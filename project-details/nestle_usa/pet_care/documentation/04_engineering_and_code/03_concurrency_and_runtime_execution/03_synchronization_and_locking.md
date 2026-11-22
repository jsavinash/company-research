# Synchronization and Locking

## 1. Locking primitives

| Primitive | Use |
|---|---|
| **Mutex / Lock** | In-process critical sections |
| **Semaphore** | Concurrency limits |
| **Advisory lock (DB)** | Cross-process coordination |
| **Distributed lock (Redis)** | Multi-instance coordination |

## 2. Deadlock avoidance

- **Lock ordering:** always acquire in the same order.
- **Timeouts:** `lock.acquire(timeout=...)`.
- **Try-lock** where contention is high.

## 3. Distributed locks

| Use | Mechanism |
|---|---|
| **Profile lock** | DB advisory lock per pet |
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

## 7. Testing

- Concurrency tests.
- Race condition detection (stress tests).