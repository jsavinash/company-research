# Browser Runtime and Web Workers

## 1. Main-thread budget

| Task | Budget |
|---|---|
| Initial JS | ≤ 200 KB (gzipped) |
| Interaction (INP) | ≤ 200 ms |
| Long tasks | Avoid > 50 ms |

## 2. Web workers

| Worker | Purpose |
|---|---|
| **Parsing** | Large JSON/CSV parsing |
| **Computation** | Client-side aggregation |
| **Export** | Excel/CSV generation |

## 3. Virtualization

- **Tables:** virtualized (react-window) for large forecast lists.
- **Lists:** infinite scroll.

## 4. Rendering performance

- **Code splitting** per route/MFE.
- **Lazy loading** components.
- **Memoization** (React.memo, useMemo).
- **Debouncing** search inputs.

## 5. Memory management

- Avoid leaks: clean up subscriptions/observers.
- Release large blobs after export.

## 6. Service worker

- Cache shell + static assets.
- Background sync (optional).
- Update strategy: skip-waiting / prompt.

## 7. Monitoring

- Web Vitals (LCP, INP, CLS).
- Long-task observer.
- Error tracking (Datadog RUM).

## 8. Related

- `06_performance_bundling_and_web_vitals.md`
- `../06_data_model_and_storage/01_client_normalized_and_offline_storage.md`