# ADR 002: Database Selection

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

## Consequences

**Positive:**
- Reuses existing Snowflake investment.
- Open table format avoids lock-in.
- Strong lineage and ABAC.

**Negative:**
- Polyglot persistence adds operational complexity.
- Requires a skilled platform team.

**Mitigation:**
- Standardize on Iceberg as the shared substrate.
- Use Unity Catalog for governance across engines.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Single warehouse (Snowflake only) | Simplicity | Weak ML/feature-store story; no graph |
| Databricks only | Strong ML | Doesn't reuse existing Snowflake retailer data |
| No Iceberg (separate stores) | Simpler ops | Vendor lock-in; hard to share data across engines |
| Pinecone only (no Azure AI Search) | Managed vectors | Misses hybrid keyword search + enterprise integration |

## Compliance / Governance

- Retailer data: ABAC + contract-term parsing.
- Panel data: aggregate only.
- Audit: lineage via Unity Catalog.

## References

- `../01_full_stack_and_infra_tech_choices.md`
- `../../../Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/architecture-decision-records/001-database-selection.md`

## Metadata

| Field | Value |
|---|---|
| Author | AI Solutions Architect |
| Date | 2026-02 |
| Reviewers | Data Platform, Security |
| Supersedes | — |
| Superseded by | — |