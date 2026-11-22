# User Help Center Guides

## 1. What is the discovery platform?

It powers the search box and recommendation placements (home, category, cart, "similar items") on the storefront. It retrieves relevant products and ranks them using query, product, user, and session signals.

## 2. For merchandisers

- **Overrides:** boosts, pinning, and campaign rules layer on top of ranked output. The platform never silently overrides business rules.
- **Retrain approval:** client ML/eng counterparts approve candidate models; the platform surfaces a candidate, not an auto-deploy.

## 3. For client ML/eng

- **Shadow validation:** a candidate model is compared to live without changing UX. This is release safety, not lift proof.
- **Online experiment:** any conversion claim requires a randomized online test with a defined denominator and attribution window.

## 4. Understanding the metrics

| Metric | Meaning |
|---|---|
| **Recall@K** | Fraction of relevant items in top-K (retrieval) |
| **NDCG@K** | Ranking quality (per placement) |
| **ATC per impression** | Add-to-cart conversion (business) |
| **p95 / p99** | Latency percentiles |

## 5. Troubleshooting

| Issue | Fix |
|---|---|
| Results seem popularity-biased | Check position-bias controls; report |
| Cold-start items missing | Content/popularity fallback; report |
| Slow results | Check latency dashboard; contact on-call |
| Wrong recommendations | Report; merchandisers can override |

## 6. Best practices

- Keep search and reco labels separate.
- Never read raw click-through as unbiased relevance.
- Always pair a conversion claim with an experiment.