# Database Schema and ERD

## 1. Core entities

```
Store (store_id, banner_id, dma, region, income_quintile)
Banner (banner_id, retailer_id, name)
Product (sku_id, brand, category, pack_size)
Price (sku_id, store_id, week, price, promo_flag)
Distribution (sku_id, store_id, week, acv)
Sellout (sku_id, store_id, week, units, dollars)
Shipment (sku_id, banner_id, week, cases)
GLP1_Penetration (dma, month, penetration, income_quintile)
FeatureVector (entity_id, feature_name, value, as_of_date)
Forecast (run_id, sku_id, store_id, horizon, p10, p50, p90, model_version, created_at)
Attribution (run_id, sku_id, driver, effect, confidence)
AuditEvent (event_id, user_id, action, entity, timestamp, run_id)
```

## 2. ERD (text)

```
Banner ||--o{ Store : has
Store  ||--o{ Sellout : records
Product||--o{ Sellout : sold_as
Store  ||--o{ Price : prices
Store  ||--o{ Distribution : distributes
DMA    ||--o{ Store : contains
DMA    ||--o{ GLP1_Penetration : has
Product||--o{ FeatureVector : features
Product||--o{ Forecast : forecasts
Forecast||--o{ Attribution : decomposes
AuditEvent }o--|| Forecast : references
```

## 3. Key design points

- **Point-in-time correctness:** every feature row carries `as_of_date`; training queries filter `as_of_date <= prediction_date`.
- **Hierarchical reconciliation:** store → banner → DMA → national via MinT.
- **Forecast run metadata:** `run_id` links forecast → attribution → audit.
- **Partitioning:** Iceberg partitions by `date`/`sku_id`; Snowflake clustering by `store_id`/`week`.

## 4. Example DDL (Iceberg)

```sql
CREATE TABLE sellout (
  sku_id      STRING,
  store_id    STRING,
  week        DATE,
  units       DOUBLE,
  dollars     DOUBLE,
  promo_flag  BOOLEAN
) USING iceberg
PARTITIONED BY (days(week));
```

## 5. Governance

- Row/column-level security in Snowflake + Unity Catalog ABAC.
- OPA policies enforce per-banner/DMA access.
- Audit log is append-only.