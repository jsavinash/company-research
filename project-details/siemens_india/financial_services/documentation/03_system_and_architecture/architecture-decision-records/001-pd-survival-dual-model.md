# ADR 001: PD + Survival Dual-Model Architecture

## Status

Accepted (2019-09)

## Context

The system must predict both **whether** a B2B borrower will default and **when** (time-to-delinquency), on a book where defaults are 2–5% and most loans do not default within the observation window (right-censoring). A single binary classifier cannot use censored data correctly and gives no timing.

## Decision

Adopt a **dual-model architecture**:
- **PD model** (XGBoost / LightGBM, cost-sensitive) → probability of default.
- **Survival model** (Cox PH / AFT, lifelines) → time-to-delinquency with censoring, reported as P10/P50/P90 months to event.
- **WoE scorecard** as a regulatory-friendly companion (not the production model).

## Consequences

**Positive:**
- Uses censored data correctly (survival).
- PD answers "how likely"; survival answers "when" — together they drive early warning.
- Scorecard provides regulatory interpretability.

**Negative:**
- Two models to train/validate.
- Survival models are less familiar to some stakeholders.

**Mitigation:**
- Shared feature pipeline; joint evaluation.
- Scorecard as the audit companion.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Single binary classifier | Simplicity | Can't use censored data; no timing |
| Logistic regression only | Interpretable | Weaker; no censoring |
| Survival only | Timing | No headline PD for provisioning |

## Compliance / Governance

- Model risk (SR 11-7): versioned, validated, documented.
- Reason codes for every PD.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-002