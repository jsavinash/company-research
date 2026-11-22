# Client Normalized and Offline Storage

## 1. Client storage

| Store | Use | API |
|---|---|---|
| **Memory** | Server cache | React Query |
| **IndexedDB** | Offline / persistent | idb |
| **localStorage** | Preferences | localStorage |
| **Cache API** | Service Worker | Cache Storage |

## 2. Normalized store

- Normalize entities: `pets`, `plans`, `coaching`.
- Reference by ID.

```
pets: { byId: {...}, allIds: [...] }
plans: { byId: {...} }
```

## 3. Offline storage

| Data | Cached |
|---|---|
| **Last-good plans** | IndexedDB |
| **App shell** | Service Worker |
| **User preferences** | localStorage |

## 4. Service Worker (PWA)

- **Cache-first** for static assets.
- **Network-first** for data.
- **Background sync** (optional).

## 5. PWA sync

- Queue mutations when offline.
- Replay on reconnect.
- Conflict resolution (last-write-wins / server-authoritative).

## 6. Data lifecycle

- **TTL** per cache type.
- **LRU eviction.**
- **Clear on logout.**

## 7. Storage quotas

- Request persistent storage.
- Monitor quota; evict gracefully.

## 8. Testing

- Offline mode tests.
- Sync conflict tests.