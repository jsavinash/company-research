# Data Exchange Formats

## 1. Formats

| Format | Use | Pros | Cons |
|---|---|---|---|
| **JSON** | REST / GraphQL | Human-readable | Verbose |
| **YAML** | Config / OpenAPI | Readable | Not for runtime |
| **CSV** | Exports / bulk | Universal | No schema |
| **Protobuf** | gRPC (internal) | Compact, fast | Binary |
| **Avro** | Kafka / data lake | Schema evolution | Binary |
| **Thrift** | RPC (legacy) | Compact | Less common |

## 2. Format selection

| Context | Format |
|---|---|
| External API | JSON |
| Internal RPC | Protobuf |
| Streaming | Avro |
| Exports | CSV / XLSX |
| Config | YAML |

## 3. JSON conventions

- **UTF-8.**
- **ISO 8601** dates.
- **Snake_case** fields.
- **Explicit nulls** (not missing).

## 4. Schema evolution

- **Backward/forward compatible** changes.
- **Avro** schema registry for Kafka.
- **Protobuf** field numbers.

## 5. Large payloads

- **Pagination** for lists.
- **Compression** (gzip).
- **Streaming** for large exports.

## 6. Validation

- **JSON Schema** / **Protobuf** validation.
- Contract tests.

## 7. Example (JSON)

```json
{
  "run_id": "FR-2026-11-22-0142",
  "model_version": "1.0.0",
  "forecasts": [
    {"sku_id":"DGI-001","store_id":"S1","week":"2026-09-01","p10":100,"p50":110,"p90":120}
  ]
}
```

## 8. Related

- `01_api_contracts_and_versioning.md`
- `03_transfer_and_streaming_protocols.md`