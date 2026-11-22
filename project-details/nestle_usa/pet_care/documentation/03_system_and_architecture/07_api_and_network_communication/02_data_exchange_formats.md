# Data Exchange Formats

## 1. Formats

| Format | Use | Pros | Cons |
|---|---|---|---|
| **JSON** | REST / SSE | Human-readable | Verbose |
| **YAML** | Config / OpenAPI | Readable | Not for runtime |
| **CSV** | Exports | Universal | No schema |
| **Protobuf** | Internal RPC | Compact | Binary |
| **Avro** | Kafka | Schema evolution | Binary |

## 2. Format selection

| Context | Format |
|---|---|
| External API | JSON |
| Internal RPC | Protobuf |
| Streaming | Avro |
| Exports | CSV / XLSX |
| Config | YAML |

## 4. JSON conventions

- **UTF-8.**
- **ISO 8601** dates.
- **Snake_case** fields.
- **Explicit nulls.**

## 5. Schema evolution

- **Backward/forward compatible** changes.
- **Avro** schema registry for Kafka.
- **Protobuf** field numbers.

## 6. Large payloads

- **Pagination** for lists.
- **Compression** (gzip).
- **Streaming** for large exports.

## 7. Validation

- **JSON Schema** / **Protobuf** validation.
- Contract tests.

## 8. Example (JSON)

```json
{
  "session_id": "CS-...",
  "plan_id": "PL-...",
  "narrative": "Because he's a 3-yr-old lab...",
  "citations": ["AAFCO-..."]
}
```