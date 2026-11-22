# UX-to-System-State Mapping

## 1. UX state → system state

| UX state | System state | Trigger |
|---|---|---|
| **Idle** | No active query | User hasn't asked |
| **Loading** | Fetching data / running forecast | Scenario submitted |
| **Success** | Run complete; result ready | Agents finish |
| **Partial** | Some data missing / degraded | Data quality flag |
| **Permission denied** | OPA denied | Unauthorized banner/DMA |
| **Error** | Model/pipeline failure | Exception |
| **Stale** | Data older than SLA | Freshness check |

## 2. State transitions

```
Idle → Loading → Success
              ↘ Partial (data quality)
              ↘ Permission denied (OPA)
              ↘ Error (model/pipeline)
Success → Stale (if data ages)
```

## 3. UX ↔ system mapping table

| UX element | System source | Notes |
|---|---|---|
| Forecast numbers | Forecast Agent | P10/P50/P90 |
| Attribution | Attribution Agent | Driver effects |
| Run ID | Forecast run | Audit key |
| Freshness banner | Data Agent | Lag check |
| Permission error | OPA | Actionable message |
| "Cannot assess" | Forecast Agent | Thin-data fallback |
| Citations | RAG / KB | Grounded claims |

## 4. Error states → user messaging

| System state | User message | Action |
|---|---|---|
| Permission denied | "You don't have access to this banner." | Request access |
| Stale data | "Data is 3 days old; treat with caution." | Refresh / caveat |
| Model degraded | "Forecast is degraded; last-good shown." | Retry later |
| Thin data | "Limited data; wide intervals." | Provide more data |
| Pipeline error | "Something went wrong; retry." | Retry / contact support |

## 5. Loading & skeleton states

| Element | Loading state |
|---|---|
| Forecast chart | Skeleton + "Running forecast…" |
| Attribution | Spinner + "Estimating effects…" |
| Narrative | Streaming tokens |
| Run detail | Skeleton |

## 6. Trust & transparency

- Always show **run ID** and **model version**.
- Always show **freshness** and **data-quality caveats**.
- Never show a confident number without an interval.
- Never hide a "cannot assess" behind a blank.

## 7. Accessibility

- WCAG 2.1 AA.
- Keyboard navigation.
- Screen-reader labels for charts (P10/P50/P90 described in text).