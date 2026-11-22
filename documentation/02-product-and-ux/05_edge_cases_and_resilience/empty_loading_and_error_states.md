# Empty, Loading, and Error States

## 1. Empty states

| Context | Message | Action |
|---|---|---|
| No forecasts yet | "No forecasts yet. Run your first scenario." | CTA: Ask a question |
| No data for a banner | "No data available for this banner." | Request access / check freshness |
| No attribution | "Attribution unavailable for this run." | Re-run / contact DS |
| No search results | "No matches. Try a different brand/DMA." | Refine query |

## 2. Loading states

| Element | Loading UI |
|---|---|
| Copilot answer | Streaming tokens + "Running agents…" |
| Forecast chart | Skeleton + "Running forecast…" |
| Attribution | Spinner + "Estimating effects…" |
| Run detail | Skeleton rows |
| Export | Progress indicator |

## 3. Error states

| Error | Message | Action |
|---|---|---|
| **Permission denied** | "You don't have access to this banner/DMA." | Request access |
| **Data stale** | "Data is N days old; treat with caution." | Refresh / caveat |
| **Model degraded** | "Forecast degraded; last-good shown." | Retry later |
| **Pipeline failure** | "Forecast pipeline failed. Retry." | Retry / support |
| **LLM timeout** | "The copilot took too long. Retry." | Retry / use dashboard |
| **Rate limited** | "Too many requests; wait a moment." | Back off |
| **Upstream model error** | "Model provider unavailable; using fallback." | Automatic fallback |
| **Validation error** | "Couldn't understand the question. Try: brand + geography + horizon." | Refine query |

## 4. Error message principles

- **Actionable:** tell the user what to do.
- **Honest:** don't hide degradation.
- **Specific:** name the banner/DMA/run.
- **Non-technical:** avoid stack traces.

## 5. Partial / degraded results

| Case | Behavior |
|---|---|
| Some stores missing | Forecast with caveat + coverage indicator |
| Stockout censoring | Flag affected stores |
| Thin data | Wide intervals + "cannot assess" |
| One agent fails | Return partial + note |

## 6. Retry & recovery

- **Idempotent retries:** safe to re-run.
- **Backoff:** exponential for rate limits.
- **Last-good fallback:** serve previous forecast if pipeline fails.
- **Status banner:** global incident notice.

## 7. Observability

- Log every error with run ID.
- Alert on error-rate spikes.
- Track "cannot assess" rate as a quality signal.