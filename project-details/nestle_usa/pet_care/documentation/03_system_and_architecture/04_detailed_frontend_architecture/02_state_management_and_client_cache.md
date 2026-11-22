# State Management and Client Cache

## 1. State categories

| Category | Tool | Examples |
|---|---|---|
| **Server state** | React Query | Profiles, plans, coaching |
| **UI state** | Zustand | Modals, selections |
| **Auth** | Context + Entra ID | User, token |
| **Feature flags** | LaunchDarkly / custom | Rollouts |

## 2. Server state (React Query)

- **Caching:** stale-while-revalidate.
- **Invalidation:** on new plan.
- **Pagination:** cursor-based.

## 3. Client cache

| Layer | Store | TTL |
|---|---|---|
| **Memory** | React Query | 5 min |
| **Session** | IndexedDB | Session |
| **Persistent** | IndexedDB | Configurable |

## 4. Cache keys

- `["profile", {petId}]`, `["plan", {planId}]`, `["coaching", {sessionId}]`.

## 5. Cache invalidation

| Event | Invalidate |
|---|---|
| New plan | Profile + plan |
| Model update | Coaching |

## 6. Offline cache

- Last-good plan cached in IndexedDB.
- Service Worker serves cached shell.

## 7. State persistence

- UI preferences in localStorage.
- Drafts in IndexedDB.