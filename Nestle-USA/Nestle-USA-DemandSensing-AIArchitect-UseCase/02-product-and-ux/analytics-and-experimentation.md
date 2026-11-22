# Analytics and Experimentation

## 1. Metrics framework

### 1.1 Forecast quality

| Metric | Definition | Target |
|---|---|---|
| **Out-of-regime WMAPE** | WMAPE on post-break data (2024–26) | ≥ 15% relative improvement vs. incumbent |
| **MAPE** | Secondary accuracy | Report |
| **Bias** | Mean signed error | Near zero |
| **Interval coverage** | P50/P90 coverage vs. nominal | Within tolerance |
| **Bias by income quintile** | Systematic error across DMAs | None |

### 1.2 Causal attribution

| Metric | Definition | Target |
|---|---|---|
| **Sign consistency** | GLP-1 effect sign across rolling windows | Consistent |
| **Effect stability** | Variance of estimated effect | Low |
| **Counterfactual validity** | Pre-treatment fit of synthetic control | Good |

### 1.3 Product / adoption

| Metric | Definition | Target |
|---|---|---|
| **Copilot adoption** | Planners using copilot weekly | ≥ 80% |
| **Scenario usage** | What-if queries per planner | Report |
| **Decision acceptance** | Forecasts accepted vs. overridden | Report |

### 1.4 Platform / FinOps

| Metric | Definition | Target |
|---|---|---|
| **p95 latency** | Copilot / scenario | ≤ 5 s / ≤ 10 s |
| **Cache hit rate** | Semantic cache | Report |
| **Cost per query** | Token + compute | Trend down |
| **Availability** | Platform uptime | 99.9% |

## 2. Experimentation design

### 2.1 Forecast model comparison

- **Design:** rolling-origin backtesting (train ≤2022, test 2024–26).
- **Arms:** incumbent vs. regime-aware (GLP-1) vs. regime-aware + causal attribution.
- **Metric:** out-of-regime WMAPE, bias, interval coverage.

### 2.2 Copilot A/B

- **Design:** randomized planner groups (copilot vs. dashboard-only).
- **Metrics:** decision quality, time-to-decision, adoption.
- **Guardrail:** no degradation in forecast acceptance quality.

### 2.3 Causal validation

- **Design:** synthetic control per DMA + DiD on GLP-1 adoption ramp.
- **Validation:** placebo tests (pre-treatment), donor-pool sensitivity.

## 3. Guardrails & stop conditions

- Rollback if out-of-regime WMAPE degrades > 5% relative.
- Rollback if interval coverage falls outside tolerance.
- Rollback if bias by income quintile appears.
- Halt if any PII leakage detected.

## 4. Reporting cadence

| Report | Frequency | Audience |
|---|---|---|
| Forecast quality scorecard | Weekly | Demand planning |
| Causal attribution review | Monthly | RGM + finance |
| FinOps / cost review | Monthly | Platform + finance |
| Model drift alert | Continuous | Data science |