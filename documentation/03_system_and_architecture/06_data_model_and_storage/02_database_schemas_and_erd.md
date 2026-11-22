# Database Schemas and ERD

## 1. Core entities

See `02_database_schemas_and_erd.png` for the visual ERD.

```
Banner (banner_id PK, retailer_id FK, name)
Store (store_id PK, banner_id FK, dma, region, income_quintile)
Product (sku_id PK, brand, category, pack_size)
Price (sku_id FK, store_id FK, week, price, promo_flag)
Distribution (sku_id FK, store_id FK, week, acv)
Sellout (sku_id FK, store_id FK, week, units, dollars)
Shipment (sku_id FK, banner_id FK, week, cases)
GLP1_Penetration (dma, month, penetration, income_quintile)
FeatureVector (entity_id FK, feature_name, value, as_of_date)
Forecast (run_id PK, sku_id FK, store_id FK, horizon, p10, p50, p90, model_version, created_at)
Attribution (run_id FK, driver, effect, confidence)
AuditEvent (event_id PK, user_id, action, entity, timestamp, run_id)
```

## 2. DDL examples (Iceberg)

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

CREATE TABLE forecast (
  run_id        STRING,
  sku_id        STRING,
  store_id      STRING,
  horizon       INT,
  p10           DOUBLE,
  p50           DOUBLE,
  p90           DOUBLE,
  model_version STRING,
  created_at    TIMESTAMP
) USING iceberg;
```

## 3. Indexing

| Table | Index / clustering |
|---|---|
| Sellout | Cluster by (store_id, week) |
| Forecast | Cluster by (run_id, sku_id) |
| FeatureVector | Partition by (as_of_date) |
| AuditEvent | Partition by (timestamp) |

## 4. Relationships (cardinality)

```
Banner 1──* Store
Store 1──* Sellout
Product 1──* Sellout
DMA 1──* Store
DMA 1──* GLP1_Penetration
Product 1──* Forecast
Forecast 1──* Attribution
AuditEvent *──1 Forecast
```

## 5. Constraints

- **Point-in-time correctness:** `as_of_date <= prediction_date`.
- **Referential integrity:** enforced in ETL.
- **Uniqueness:** (run_id, sku_id, store_id, horizon).

## 6. Partitioning & retention

- Partition by date.
- Retention per policy (see `03_storage_search_and_data_lifecycle.md`).

## 7. Related

- `02_database_schemas_and_erd.png` (visual)
- `01_client_normalized_and_offline_storage.md`
- `03_storage_search_and_data_lifecycle.md`