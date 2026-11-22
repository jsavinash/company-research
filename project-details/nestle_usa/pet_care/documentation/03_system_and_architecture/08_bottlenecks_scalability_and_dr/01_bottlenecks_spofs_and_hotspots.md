# Bottlenecks, SPOFs, and Hotspots

## 1. Potential bottlenecks

| Bottleneck | Symptom | Mitigation |
|---|---|---|
| **LLM latency (frontier)** | Slow coaching | Semantic cache; small-model routing; streaming |
| **Vector search** | Slow retrieval | HNSW index; caching |
| **Snowflake query** | Slow features | Clustering; result cache |
| **OPA policy checks** | Latency per request | Decision caching |

## 2. Single points of failure (SPOFs)

| SPOF | Mitigation |
|---|---|
| **Snowflake** | Databricks replica |
| **Databricks** | Snowflake / SageMaker fallback |
| **Neo4j** | Azure AI Search fallback |
| **Kafka** | Multi-broker; DLQ |

## 3. Hotspots / hot keys

| Hotspot | Problem | Mitigation |
|---|---|---|
| **Hot pet profile** | Repeated queries | Semantic cache |
| **Celebrity query** | Expensive scenario | Cache |
| **Hot partition** | Kafka partition skew | Key by hashed entity |

## 4. Shard rebalancing

- **Iceberg:** partition evolution; compaction.
- **Kafka:** partition reassignment.
- **Redis:** consistent hashing.

## 5. Backpressure

| Layer | Backpressure |
|---|---|
| **Gateway** | 429 + Retry-After |
| **Coaching API** | Queue limits |
| **Kafka** | Consumer lag; pause/resume |

## 6. Hot-partition / skew

- **Salting** hot keys.
- **Two-level aggregation.**
- **Pre-aggregation.**

## 7. Monitoring

- Saturation (CPU, memory, queue depth).
- Hot-key detection.
- Consumer lag.