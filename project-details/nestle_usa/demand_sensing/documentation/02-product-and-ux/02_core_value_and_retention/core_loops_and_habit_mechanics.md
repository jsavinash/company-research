# Core Loops and Habit Mechanics

## 1. Core value loops

### Loop 1 — The planning loop (weekly)

```
Planner asks scenario → gets calibrated answer → uses it in planning → returns next cycle
```

- **Trigger:** weekly planning cycle, variance review.
- **Action:** ask a scenario / review dashboard.
- **Reward:** defensible, explainable forecast.
- **Investment:** annotates / accepts forecasts → improves models.

### Loop 2 — The feedback loop (continuous)

```
Reviewer accept/adjust/reject → logged as label → retrains ranker → better forecasts
```

- Every human action is a training signal.
- Closes the loop between usage and model quality.

### Loop 3 — The trust loop (monthly)

```
Out-of-regime eval → published scorecard → planner trust → adoption
```

- Transparent evaluation builds trust.
- Trust drives adoption; adoption drives data.

## 2. Habit mechanics

| Mechanic | Application |
|---|---|
| **Cue** | Planning cycle, variance alert, meeting prep |
| **Routine** | Ask copilot / review dashboard |
| **Reward** | Time saved, defensible answer |
| **Investment** | Annotations, shared run IDs |
| **Streak** | Weekly active usage |
| **Social proof** | Shared forecasts / run IDs among planners |

## 3. Retention drivers

| Driver | Mechanism |
|---|---|
| **Habit** | Embedded in weekly planning |
| **Switching cost** | History, annotations, trust built over time |
| **Network** | Team shares run IDs / forecasts |
| **Value** | Accuracy + speed + auditability |

## 4. Retention metrics

| Metric | Target |
|---|---|
| Weekly active planners | ≥ 80% |
| Week-4 retention | ≥ 70% |
| Scenarios per planner / week | Report |
| Forecast acceptance rate | Report |

## 5. Anti-patterns (retention risks)

- **Trust erosion** — a wrong confident answer hurts; mitigated by intervals + "cannot assess".
- **Stale data** — freshness banners; degrade gracefully.
- **Over-automation** — planners want control; keep human-in-the-loop.

## 6. Instrumentation

See `06_analytics_and_experimentation/event_taxonomy_and_tracking_plan.md`.