# Bottlenecks, SPOFs, and Hotspots

## 1. Potential bottlenecks

| Bottleneck | Symptom | Mitigation |
|---|---|---|
| **Snowflake query time** | Slow forecasts | Clustering, result cache, pre-aggregation |
| **LLM latency (frontier)** | Slow copilot | Semantic cache; small-model routing; streaming |
| **Neo4j traversal** | Slow GraphRAG | Indexes, depth limits |
| **OPA policy checks** | Latency per request | Decision caching |
| **Feature store reads** | Slow scoring | Online store (Feast), caching |
| **Kafka consumer lag** | Stale data | Scale consumers, partitions |

## 2. Single points of failure (SPOFs)

| SPOF | Mitigation |
|---|---|
| **Snowflake** | Databricks replica; failover |
| **Databricks** | Snowflake / SageMaker fallback |
| **Neo4j** | Azure AI Search fallback (keyword-only) |
| **Kafka** | Multi-broker; DLQ; replay |
| **OPA** | HA deployment; cached decisions |

## 3. Hotspots / hot keys

| Hotspot | Problem | Mitigation |
|---|---|---|
| **Hot SKU/store** | Skewed forecast load | Shard by (sku, store); spread |
| **Celebrity query** | Repeated expensive scenario | Semantic cache |
| **Hot partition** | Kafka partition skew | Key by hashed entity; repartition |

## 4. Shard rebalancing

- **Iceberg:** partition evolution; compaction.
- **Kafka:** partition reassignment.
- **Neo4j:** shard by category/DMA (future).
- **Redis:** consistent hashing.

## 5. Backpressure

| Layer | Backpressure |
|---|---|
| **Gateway** | 429 + Retry-After |
| **Forecast API** | Queue limits; load shedding |
| **Kafka** | Consumer lag; pause/resume |
| **Agents** | Concurrency limits |

## 6. Thundering herd

- **Request coalescing** on cache miss.
- **Early recompute** (probabilistic).
- **Jittered retries.**

## 7. Hot-partition / skew mitigation

- **Salting** hot keys.
- **Two-level aggregation.**
- **Pre-aggregation** for common queries.

## 8. Monitoring

- Saturation (CPU, memory, queue depth).
- Hot-key detection.
- Consumer lag.

## 9. Related

- `02_load_balancing_and_auto_scaling.md`
- `../05_detailed_backend_and_async_design/`