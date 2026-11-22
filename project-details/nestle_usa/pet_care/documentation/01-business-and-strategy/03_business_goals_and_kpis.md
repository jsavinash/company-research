# Business Goals and KPIs

## 1. Goals

| ID | Goal | Metric |
|---|---|---|
| G1 | Better intake | Slot accuracy ≥ 0.95 |
| G2 | Safe coaching | Grounding faithfulness ≥ 0.95; hallucination ~0 |
| G2 | Vet handoff | Vet endorsement ≥ 0.60 |
| G3 | Safety | Medical-escalation recall ≥ 0.95; injection resistance 100% |
| G4 | Adoption | Weekly active owners |
| G5 | Cost | Cost per query trend down |

## 2. KPI tree

```
North Star: weekly active owners with a completed profile + coached plan
├── Activation
│   ├── Sign-up → first intake
│   └── First intake → aha (coaching viewed)
├── Quality
│   ├── Slot accuracy
│   ├── Grounding faithfulness
│   └── Hallucination rate
├── Safety
│   ├── Medical-escalation recall
│   └── Injection resistance
├── Retention
│   └── Weekly active
└── FinOps
    └── Cost per query
```

## 3. Targets

| KPI | Target |
|---|---|
| Slot accuracy | ≥ 0.95 |
| Schema validity | 100% |
| Grounding faithfulness | ≥ 0.95 |
| Hallucination rate | ~0 |
| Medical-escalation recall | ≥ 0.95 |
| Injection resistance | 0 successful |

## 4. Reporting

- Weekly quality scorecard.
- Monthly safety review.
- Quarterly business review.