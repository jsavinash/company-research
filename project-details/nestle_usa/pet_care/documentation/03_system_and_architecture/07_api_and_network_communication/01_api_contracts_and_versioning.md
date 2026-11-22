# API Contracts and Versioning

## 1. API styles

| Style | Use |
|---|---|
| **REST** | CRUD (profiles, plans) |
| **SSE** | Streaming coaching |
| **MCP** | Agent-to-tool |
| **A2A** | Agent-to-agent |

## 2. Versioning

- **URI versioning:** `/v1/...`.
- **SemVer** for breaking changes.
- **Deprecation:** N-2 support.

## 4. REST conventions

- **Naming:** plural nouns (`/profiles`, `/plans`).
- **Methods:** GET, POST, PUT, PATCH, DELETE.
- **Status codes:** 200, 201, 400, 401, 403, 404, 429, 500.
- **Errors:** RFC 7807 problem+json.

## 5. Pagination

- **Cursor-based** for lists.
- **Limits:** default 50, max 200.

## 6. Idempotency

- **Idempotency-Key** header for POST.
- Safe retries.

## 7. Example

```http
POST /v1/scenarios
{ "query": "GLP-1..." }
→ 200 { "run_id": "...", "narrative": "..." }
```

## 8. Contract testing

- Schemathesis / Pact.
- OpenAPI schema as source of truth.