# Integration and Data Strategy

## 1. Data sources

| Source | Type | Freshness | Notes |
|---|---|---|---|
| Client event stream | Streaming | Real-time | Clicks, views, add-to-carts, orders |
| Catalog feed | Batch | Daily | Products, text, attributes, taxonomy |
| Session events | Streaming | Real-time | Browsing/cart context |
| Pricing / promotions | Batch | Daily | Consumed as features (client-owned) |
| Inventory | Batch | Daily | Availability feature (client-owned) |

## 2. Training record

One record associates: user/session, query or context, candidate product, impression position, model version, and a time-ordered outcome (click, add-to-cart, purchase). Event schema, consent/retention controls, deduplication, attribution rules documented from implementation.

## 3. The position-bias and negative-sampling problem

- Clicked items are easy positives; the difficulty is negatives.
- **Unclicked items are valid negatives only if actually exposed.** Impression logs + position are mandatory: an item shown at position 1 and ignored is a strong negative; an item never shown is *missing*, not negative.
- Training on "clicked vs. all catalog" silently teaches popularity and position, not relevance.

## 4. Leakage, freshness and bias controls

- **Chronological splits.** Train on months 1..N, evaluate on N+1; group repeated sessions/users.
- **Point-in-time correctness.** Every feature computed as of prediction time.
- **Freshness metrics.** Catalog/embedding freshness, OOV rate, duplicate/stale-SKU rate, feature nulls, online/offline parity.
- **Bias handling.** Impression policy + position recorded; position/popularity bias analysed explicitly.
- **Cold start.** New SKUs → content/rules; new/anonymous users → context/popularity; each fallback documented.

## 5. Single-client isolation

- Single-client engagement. **No cross-client training** on raw behaviour.
- Shared learning only through the ML/MLOps *method* (pipelines, registry, validation gates), never pooled data.

## 6. Integration architecture

```
Client storefront → Kafka (events) → Airflow (features) → Snowflake/Databricks → Feast → Train/Serve
Catalog feed → PIM (client) → Iceberg → features
Documents → Docling → vector store → RAG (n/a for ranking)
```

## 7. Integration with client systems

| System | Purpose | Protocol |
|---|---|---|
| Storefront | Event stream, result injection | REST / Kafka |
| PIM | Catalog system of record | API / SFTP |
| SAP / Salesforce / ServiceNow | ERP / CRM / ticketing | REST |
| Retailer APIs | Inventory / pricing | REST / SFTP |

Integration uses **MCP tools** for agents where applicable, but the core ranking path is deterministic (no LLM).

## 8. Data governance

- **Ownership:** client (data) + T-Systems India (platform).
- **Lineage:** MLflow + feature store.
- **Retention:** per client policy.
- **Access:** RBAC + client boundary.