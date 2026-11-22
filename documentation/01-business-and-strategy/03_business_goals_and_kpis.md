# Business Goals and KPIs

## 1. Business goals

| ID | Goal | Metric |
|---|---|---|
| G1 | Improve forecast accuracy under regime shift | Out-of-regime WMAPE ≥ 15% relative improvement |
| G2 | Explain demand changes | Causal attribution sign-consistent across windows |
| G3 | Improve trade-spend efficiency | Attribution-driven reallocation |
| G4 | Increase planner productivity | Time-to-decision; adoption ≥ 80% |
| G5 | Ensure governance & auditability | 100% of runs logged; zero PII leakage |
| G6 | Prove ROI / FinOps | Chargeback per business unit; cost per query trend |

## 2. KPI tree

```
Business outcome: defend share & price/mix in a declining-volume market
├── Forecast quality
│   ├── Out-of-regime WMAPE (primary)
│   ├── Bias (secondary)
│   ├── Interval coverage
│   └── Bias by income quintile
├── Causal attribution
│   ├── Sign consistency
│   └── Effect stability
├── Adoption
│   ├── Weekly active planners
│   └── Scenario usage
├── Platform
│   ├── p95 latency
│   ├── Availability 99.9%
│   └── Cost per query
└── Governance
    ├── Audit completeness 100%
    └── PII incidents 0
```

## 3. Targets & cadence

| KPI | Target | Cadence |
|---|---|---|
| Out-of-regime WMAPE | ≥ 15% rel. improvement | Weekly |
| Bias | ~0 | Weekly |
| Interval coverage | Within tolerance | Weekly |
| Sign consistency | Consistent | Monthly |
| Adoption | ≥ 80% | Monthly |
| Availability | 99.9% | Monthly |
| p95 latency | ≤ 5 s | Continuous |
| PII incidents | 0 | Continuous |

## 4. Reporting

- Weekly forecast quality scorecard → Demand Planning.
- Monthly causal attribution review → RGM + Finance.
- Monthly FinOps review → Platform + Finance.
- Quarterly business review → Steering Committee.