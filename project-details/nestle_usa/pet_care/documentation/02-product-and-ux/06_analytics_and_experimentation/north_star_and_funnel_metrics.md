# North Star and Funnel Metrics

## 1. North Star metric

> **Weekly active owners with a completed profile + coached plan** — owners who describe their pet, get a plan, and act on the coaching.

Rationale: captures adoption (active) and value (completed + coached).

## 2. Metric tree

```
North Star: Weekly Active Owners with Completed Profile + Coached Plan
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
│   ├── Week-4 retention
│   └── Weekly active
└── FinOps
    └── Cost per query
```

## 3. Funnel

| Stage | Event | Target |
|---|---|---|
| **Sign-up** | `signin` | 100% |
| **Activation** | `intake_completed` | ≥ 80% |
| **Aha** | `coaching_requested` | ≥ 60% |
| **Habit** | weekly active | ≥ 60% |
| **Advocacy** | `vet_endorsed` | Report |

## 4. Metric definitions

| Metric | Definition | Target |
|---|---|---|
| Weekly active owners | ≥ 1 coaching/week | ≥ 60% |
| Time-to-first-intake | Sign-up → first intake | < 2 min |
| Slot accuracy | Correct slots vs. human | ≥ 0.95 |
| Grounding faithfulness | Claims entailed by chunks | ≥ 0.95 |
| Hallucination rate | Ungrounded claims / 1k | ~0 |

## 5. Guardrails

| Guardrail | Threshold |
|---|---|
| Nutritional hallucination | 0 |
| Medical-escalation recall | ≥ 0.95 |
| p95 latency | ≤ 5 s |
| PII incidents | 0 |

## 6. Reporting

- Weekly North Star + funnel.
- Monthly safety review.
- Quarterly business review.