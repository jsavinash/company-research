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
| **Parsing** | Large JSON parsing |
| **Computation** | Client-side aggregation |
| **Export** | CSV/PDF generation |

## 3. Virtualization

- **Tables:** virtualized for large plan lists.
- **Chat:** windowed message list.

## 4. Rendering performance

- **Code splitting** per route/MFE.
- **Lazy loading** components.
- **Memoization** (React.memo, useMemo).
- **Debouncing** search inputs.

## 5. Memory management

- Clean up subscriptions/observers.
- Release large blobs after export.

## 6. Service worker

- Cache shell + static assets.
- Background sync (optional).

## 5. Monitoring

- Web Vitals (LCP, INP, CLS).
- Long-task observer.