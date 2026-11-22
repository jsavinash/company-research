# Performance, Bundling, and Web Vitals

## 1. Web Vitals budgets

| Metric | Target |
|---|---|
| **LCP** | ≤ 2.5 s |
| **INP** | ≤ 200 ms |
| **CLS** | ≤ 0.1 |
| **TTFB** | ≤ 800 ms |
| **FCP** | ≤ 1.8 s |

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
- **Preload** critical assets.

## 4. Image/font optimization

- WebP/AVIF images.
- Font subsetting + `font-display: swap`.
- Lazy-load below-fold images.

## 5. Caching

- Long-term cache for hashed assets.
- HTML no-cache.
- CDN edge caching.

## 6. Performance testing

- Lighthouse CI.
- Bundle analyzer.
- WebPageTest for real-user metrics.

## 7. Monitoring

- Datadog RUM.
- Real-user monitoring for LCP/INP/CLS.
- Alerts on regression.

## 8. Optimization checklist

- [ ] Route-level code splitting
- [ ] Image optimization
- [ ] Font optimization
- [ ] CDN caching
- [ ] Preload critical resources
- [ ] Defer non-critical JS

## 9. Related

- `04_browser_runtime_and_web_workers.md`
- `../02_tech_choices_and_adrs/02_rendering_and_delivery_strategy.md`