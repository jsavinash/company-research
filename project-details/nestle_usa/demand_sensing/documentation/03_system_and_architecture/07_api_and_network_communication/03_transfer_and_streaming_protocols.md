# Transfer and Streaming Protocols

## 1. Protocols

| Protocol | Use |
|---|---|
| **HTTP/3 (QUIC)** | External APIs, low latency |
| **HTTP/2** | Fallback |
| **WebSocket** | Live dashboard updates |
| **SSE** | Token streaming from copilot |
| **WebRTC** | (Future) real-time collaboration |
| **HLS / DASH** | (Not applicable — no video) |
| **SFTP** | Retailer batch files |

## 2. Streaming choices

| Need | Protocol |
|---|---|
| **LLM token streaming** | SSE (simple, one-way) |
| **Live dashboard** | WebSocket (bidirectional) |
| **Fallback** | Long-poll |

## 3. SSE example

```http
GET /v1/scenarios/stream
event: token
data: {"text": "By Q3"}

event: done
data: {"run_id": "FR-..."}
```

## 4. WebSocket

- **Heartbeat** / ping-pong.
- **Reconnect** with backoff.
- **Auth** via token.

## 5. File transfer

- **SFTP** for retailer files.
- **Large file** resumable uploads.

## 6. Compression

- **gzip / Brotli** for HTTP.
- **zstd** for internal.

## 7. Timeouts

| Call | Timeout |
|---|---|
| Copilot stream | 60 s idle |
| Forecast API | 30 s |
| Batch | N/A |

## 8. Related

- `01_api_contracts_and_versioning.md`
- `04_network_resilience_and_rate_limiting.md`