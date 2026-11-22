# State Management and Client Cache

## 1. State categories

| Category | Tool | Examples |
|---|---|---|
| **Server state** | React Query | Forecasts, attribution, runs |
| **UI state** | Zustand / Redux Toolkit | Modals, filters, selections |
| **Auth** | Context + Entra ID | User, roles, tokens |
| **Feature flags** | LaunchDarkly / custom | Rollouts |
| **Form state** | React Hook Form | Scenario input |

## 2. Server state (React Query)

- **Caching:** stale-while-revalidate.
- **Invalidation:** on run completion.
- **Pagination:** cursor-based.
- **Optimistic updates:** where safe.

## 3. Client cache

| Layer | Store | TTL |
|---|---|---|
| **Memory** | React Query | 5 min |
| **Session** | IndexedDB | Session |
| **Persistent** | IndexedDB | Configurable |

## 4. Cache keys

- Structured: `["forecast", {runId}]`, `["attribution", {runId}]`.
- Include permissions scope.

## 5. Cache invalidation

| Event | Invalidate |
|---|---|
| New run | Forecast list |
| Model update | Run detail |
| Permission change | All queries |

## 6. Offline cache

- Last-good forecasts cached in IndexedDB.
- Service Worker serves cached shell.
- Queued queries (optional).

## 7. State persistence

- UI preferences in localStorage.
- Drafts in IndexedDB.

## 8. Testing

- Mock React Query.
- Test cache invalidation.

## 9. Related

- `../06_data_model_and_storage/01_client_normalized_and_offline_storage.md`