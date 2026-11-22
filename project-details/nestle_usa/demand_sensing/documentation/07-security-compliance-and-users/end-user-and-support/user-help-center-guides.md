# User Help Center Guides

## 1. Getting started

### What is the Scenario Copilot?

A conversational assistant that answers demand questions ("if GLP-1 rises 5pp in the Southeast, what happens to DiGiorno by Q3?") with calibrated, causally-attributed forecasts.

### How do I ask a question?

Type in natural language in Teams or the web app. Be specific about:
- **Category/brand** (DiGiorno, Hot Pockets)
- **Geography** (Southeast, specific DMAs)
- **Driver** (GLP-1, price, distribution)
- **Horizon** (Q3, next 2 quarters)

### What does the answer contain?

- **Numbers:** P10/P50/P90 forecasts (not a single point).
- **Attribution:** which drivers explain the change.
- **Run ID:** for audit/reference.

## 2. Reading a forecast

| Term | Meaning |
|---|---|
| **P10** | 10th percentile — pessimistic case |
| **P50** | Median — most likely |
| **P90** | 90th percentile — optimistic case |
| **Run ID** | Reference for this forecast |

## 3. Common questions

**Q: Why is the interval so wide?**
A: New/thin data (new banner, reformulation) → wider intervals. The system tells you.

**Q: Can the copilot set prices?**
A: No. It explains demand; it never recommends or sets prices.

**Q: Why can't I see data for a banner?**
A: You may not have permission. Contact your data steward.

**Q: What if the data looks wrong (stockout)?**
A: The copilot flags stockout-censored stores; treat those with caution.

## 4. Troubleshooting

| Issue | Fix |
|---|---|
| Copilot slow | Check status page; retry |
| "No permission" | Request access via OPA workflow |
| Forecast looks stale | Check data freshness banner |
| Don't understand attribution | Read the "why" panel; contact data science |

## 5. Best practices

- Use specific DMAs/brands for better answers.
- Cross-check with your own judgment.
- Report issues via the support channel.

## 6. Glossary

See `00-glossary-and-terminology.md`.