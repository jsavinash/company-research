# Tenets and Guiding Principles

## 1. Tenets

1. **The LLM never forecasts.** It extracts structured signals and narrates grounded results. The constrained solver decides.
2. **Causal claims require causal evidence.** No "lift" without a holdout or a validated causal design.
3. **Point-in-time correctness is non-negotiable.** No feature may use future data.
4. **Governance is a feature.** Permission-aware retrieval and audit trails are first-class.
5. **Calibrated over confident.** A calibrated interval beats a confident point.
6. **Boring, auditable designs.** Prefer proven, inspectable systems over clever ones.
7. **Period-accurate tooling.** Match the toolchain to the era; no anachronisms.

## 2. Guiding principles

| Principle | Application |
|---|---|
| **Safety first** | Adequacy/accuracy gates; abstention over confident errors |
| **Human in the loop** | Planners/vets approve; system advises |
| **Least privilege** | ABAC; only the data you're entitled to |
| **Measure twice, cut once** | Out-of-regime evaluation before release |
| **Reuse over rebuild** | Hybrid cloud; managed services; open protocols |
| **Transparent by default** | Run IDs, citations, lineage |

## 3. Anti-patterns (what we avoid)

- LLM-authored forecasts or diets.
- Shadow validation presented as conversion lift.
- Cross-retailer pooling without permission.
- PII in prompts or logs.
- Anachronistic tooling (e.g., LLMs for forecasting in 2018).
- Overclaiming accuracy without out-of-regime evidence.

## 4. Decision framework

When trade-offs arise, default to:
- **Safety > speed**
- **Causal > correlational**
- **Governed > convenient**
- **Auditable > clever**