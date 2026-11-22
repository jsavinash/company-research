# Performance, Bundling, and Web Vitals

## 1. Web Vitals budgets

| Metric | Target |
|---|---|
| **LCP** | ≤ 2.5 s |
| **INP** | ≤ 200 ms |
| **CLS** | ≤ 0.1 |
| **TTFB** | ≤ 800 ms |

## 2. Bundle budgets

| Bundle | Budget (gzipped) |
|---|---|
| **Initial** | ≤ 200 KB |
| **Per route** | ≤ 100 KB |
| **Total (app)** | ≤ 1 MB |

## 3. Bundling strategy

- **Code splitting** per route/MFE.
- **Tree shaking** (ES modules).
- **Compression** (Brotli/Gzip).
- **CDN** for static assets.

## 4. Image/font optimization

- WebP/AVIF.
- Font subsetting + `font-display: swap`.

## 5. Caching

- Long-term cache for hashed assets.
- HTML no-cache.

## 6. Performance testing

- Lighthouse CI.
- Bundle analyzer.

## 7. Monitoring

- Datadog RUM.
- Real-user monitoring for LCP/INP/CLS.