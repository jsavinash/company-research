# Transfer and Streaming Protocols

## 1. Protocols

| Protocol | Use |
|---|---|
| **HTTP/3 (QUIC)** | External APIs |
| **HTTP/2** | Fallback |
| **WebSocket** | Live updates |
| **SSE** | Token streaming from coaching |
| **SFTP** | Batch files |

## 2. Streaming choices

| Need | Protocol |
|---|---|
| **LLM token streaming** | SSE (simple, one-way) |
| **Live updates** | WebSocket (bidirectional) |
| **Fallback** | Long-poll |

## 4. SSE example

```http
GET /v1/coaching/stream
event: token
data: {"text": "Because he's"}

event: done
data: {"session_id": "..."}
```

## 5. WebSocket

- **Heartbeat** / ping-pong.
- **Reconnect** with backoff.
- **Auth** via token.

## 6. File transfer

- **SFTP** for batch.
- **Resumable** uploads.

## 7. Compression

- **gzip / Brotli** for HTTP.
- **zstd** for internal.

## 8. Timeouts

| Call | Timeout |
|---|---|
| Copilot stream | 60 s idle |
| Forecast API | 30 s |