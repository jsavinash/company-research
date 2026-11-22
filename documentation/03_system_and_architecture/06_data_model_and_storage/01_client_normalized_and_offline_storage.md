# Client Normalized and Offline Storage

## 1. Client storage

| Store | Use | API |
|---|---|---|
| **Memory** | Server cache | React Query |
| **IndexedDB** | Offline / persistent | idb |
| **localStorage** | Preferences | localStorage |
| **Cache API** | Service Worker | Cache Storage |

## 2. Normalized store

- Normalize entities: `banners`, `stores`, `products`, `runs`.
- Reference by ID.
- Update in one place.

```
runs: { byId: {...}, allIds: [...] }
banners: { byId: {...} }
```

## 3. Offline storage

| Data | Cached |
|---|---|
| **Last-good forecasts** | IndexedDB |
| **App shell** | Service Worker |
| **User preferences** | localStorage |
| **Run history** | IndexedDB (LRU) |

## 4. Service Worker (PWA)

- **Cache-first** for static assets.
- **Network-first** for data.
- **Background sync** (optional).
- **Update prompt** for new versions.

## 5. PWA sync

- Queue mutations when offline.
- Replay on reconnect.
- Conflict resolution (last-write-wins / server-authoritative).

## 6. Data lifecycle

- **TTL** per cache type.
- **LRU eviction** for run history.
- **Clear on logout.**

## 7. Storage quotas

- Request persistent storage.
- Monitor quota; evict gracefully.

## 8. Testing

- Offline mode tests.
- Sync conflict tests.

## 9. Related

- `02_state_management_and_client_cache.md`
- `03_storage_search_and_data_lifecycle.md` (server-side)