# North Star and Funnel Metrics

## 1. North Star metric

> **Weekly Active Planners with a trusted forecast** — planners who use the copilot/dashboard at least weekly and accept/act on a forecast.

Rationale: captures both adoption (active) and value (trusted/acted upon). A forecast that isn't used or trusted has no value.

## 2. Metric tree

```
North Star: Weekly Active Planners with Trusted Forecast
├── Activation
│   ├── Sign-up → first query
│   └── First query → aha (attribution viewed)
├── Engagement
│   ├── Scenarios per planner / week
│   ├── Dashboard views
│   └── Forecast acceptance rate
├── Quality
│   ├── Out-of-regime WMAPE
│   ├── Interval coverage
│   └── Bias by income quintile
├── Retention
│   ├── Week-4 retention
│   └── Weekly active
└── Governance
    ├── Audit completeness
    └── PII incidents
```

## 3. Funnel

| Stage | Event | Target |
|---|---|---|
| **Sign-up** | `signin` | 100% of invited |
| **Activation** | `scenario_submitted` | ≥ 80% |
| **Aha** | `scenario_attribution_viewed` | ≥ 60% |
| **Habit** | weekly active | ≥ 80% |
| **Value** | `forecast_accepted` | Report |
| **Advocacy** | `scenario_shared` | Report |

## 4. Metric definitions

| Metric | Definition | Target |
|---|---|---|
| **Weekly active planners** | ≥ 1 scenario or dashboard/week | ≥ 80% |
| **Time-to-first-query** | Sign-up → first scenario | < 5 min |
| **Scenario adoption** | Planners using copilot | ≥ 80% |
| **Forecast acceptance** | Accepted / total | Report |
| **Out-of-regime WMAPE** | Post-break accuracy | ≥ 15% rel. improvement |
| **Interval coverage** | P50/P90 coverage | Within tolerance |
| **Week-4 retention** | Active in week 4 | ≥ 70% |

## 5. Guardrail metrics

| Guardrail | Threshold |
|---|---|
| PII incidents | 0 |
| Error rate | < 1% |
| p95 latency | ≤ 5 s |
| "Cannot assess" rate | Monitor (not too high) |

## 6. Reporting cadence

| Report | Frequency | Audience |
|---|---|---|
| North Star + funnel | Weekly | Product |
| Quality scorecard | Weekly | DS + planners |
| Retention cohort | Monthly | Product |
| Business review | Quarterly | Steering |

## 7. Instrumentation

See `event_taxonomy_and_tracking_plan.md`.