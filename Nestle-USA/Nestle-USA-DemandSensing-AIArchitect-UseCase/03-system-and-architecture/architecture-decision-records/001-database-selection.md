# ADR 001 — Database Selection

## Status

Accepted (2026-02)

## Context

The platform needs to store and process:
- High-volume retailer sell-out / shipment data.
- Semi-structured retailer feeds.
- Feature vectors for ML (online/offline parity).
- Vector embeddings for RAG.
- A knowledge graph for GraphRAG.

Nestlé USA is a Microsoft-centric enterprise with an existing Snowflake warehouse holding retailer data. Requirements include compliance, lineage, ABAC, and portability across clouds.

## Decision

Adopt a **polyglot persistence** strategy:

| Concern | Choice | Rationale |
|---|---|---|
| Lakehouse + ML + lineage | **Databricks (Unity Catalog)** | Feature store, ABAC, lineage, Mosaic AI |
| Warehouse + in-place AI | **Snowflake** (with Cortex) | Existing retailer data; keeps AI beside governed data |
| Open table format | **Apache Iceberg** | Portability across Snowflake/Databricks/Fabric |
| Feature store | **Feast** | Online/offline parity |
| Vector search | **Azure AI Search** + **pgvector/Qdrant** | Hybrid retrieval for RAG |
| Graph | **Neo4j** | GraphRAG (brand→category→DMA→banner) |

## Alternatives considered

| Option | Pros | Cons |
|---|---|---|
| Single warehouse (Snowflake only) | Simplicity | Weak ML/feature-store story; no graph |
| Databricks only | Strong ML | Doesn't reuse existing Snowflake retailer data |
| No Iceberg (separate stores) | Simpler ops | Vendor lock-in; hard to share data across engines |
| Pinecone only (no Azure AI Search) | Managed vectors | Misses hybrid keyword search + enterprise integration |

## Consequences

- **Positive:** Reuses existing Snowflake investment; open table format avoids lock-in; strong lineage and ABAC.
- **Negative:** Polyglot persistence adds operational complexity; requires skilled platform team.
- **Mitigation:** Standardize on Iceberg as the shared substrate; use Unity Catalog for governance across engines.

## References

- `03-system-and-architecture/system-design-document.md` §3.1
- `03-system-and-architecture/integration-and-data-strategy.md`