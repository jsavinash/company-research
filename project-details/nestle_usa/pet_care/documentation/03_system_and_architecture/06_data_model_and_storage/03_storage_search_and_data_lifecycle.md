# Storage, Search, and Data Lifecycle

## 1. Storage tiers

| Tier | Store | Use |
|---|---|---|
| **Hot** | Snowflake / Databricks | Profiles, plans, coaching |
| **Warm** | Iceberg on ADLS/S3 | History |
| **Cold** | Archive | Compliance retention |
| **Vectors** | Azure AI Search / pgvector / Qdrant | Embeddings |
| **Graph** | Neo4j | Knowledge graph |
| **Object** | Blob / S3 | Documents |

## 2. Search

| Concern | Choice |
|---|---|
| **Keyword** | Azure AI Search (BM25) |
| **Vector** | pgvector / Qdrant |
| **Hybrid** | Combined |
| **Rerank** | Cross-encoder |

## 3. Data lifecycle

| Stage | Retention | Action |
|---|---|---|
| **Raw** | 90 days | Drop / archive |
| **Curated** | 3 years | Archive |
| **Coaching** | 2 years | Archive |
| **Audit** | Per policy (7y) | Archive |

## 4. TTLs

| Data | TTL |
|---|---|
| Cache | 5 min (memory) / session (IndexedDB) |
| Temp tables | 7 days |

## 5. Archival & deletion

- **Archive** to cold storage.
- **Secure delete** on expiry.
- **Legal hold** overrides.

## 6. Data quality

- Completeness, freshness, uniqueness checks.
- Quarantine on failure.

## 6. Backup

| Data | Backup |
|---|---|
| Iceberg | Snapshot + manifest |
| Snowflake | Time Travel |
| Neo4j | Snapshot |
| Audit | Immutable store |

## 8. Governance

- Ownership: data stewards.
- Lineage: Unity Catalog / OpenTelemetry.
- Access: ABAC.