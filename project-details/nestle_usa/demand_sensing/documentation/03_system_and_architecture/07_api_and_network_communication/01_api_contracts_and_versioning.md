# API Contracts and Versioning

## 1. API styles

| Style | Use |
|---|---|
| **REST** | CRUD, resources (forecasts, runs) |
| **GraphQL** | Flexible queries (dashboards) |
| **gRPC** | Internal service-to-service |
| **MCP** | Agent-to-tool |
| **A2A** | Agent-to-agent |

## 2. Versioning

- **URI versioning:** `/v1/...`.
- **Semantic versioning** for breaking changes.
- **Deprecation policy:** N-2 support; sunset headers.

## 3. REST conventions

- **Naming:** plural nouns (`/forecasts`, `/scenarios`).
- **Methods:** GET, POST, PUT, PATCH, DELETE.
- **Status codes:** 200, 201, 400, 401, 403, 404, 429, 500.
- **Errors:** RFC 7807 problem+json.

## 4. Pagination

- **Cursor-based** for large lists.
- **Limits:** default 50, max 200.

## 5. Filtering & sorting

- Query params: `?banner=...&from=...&to=...`.
- Sort: `?sort=-created_at`.

## 6. Idempotency

- **Idempotency-Key** header for POST.
- Safe retries.

## 7. Contract examples

```http
POST /v1/forecasts
{
  "sku_id": "DGI-001",
  "store_ids": ["S1","S2"],
  "horizon_weeks": 12,
  "shocks": {"glp1": 0.05}
}
→ 200 { "run_id": "FR-...", "forecasts": [...], "warnings": [] }
```

## 8. Contract testing

- Schemathesis / Pact.
- OpenAPI schema as source of truth.

## 9. Related

- `../../04_engineering_and_code/api-contracts-and-specs.yaml`
- `02_data_exchange_formats.md`
- `04_network_resilience_and_rate_limiting.md`