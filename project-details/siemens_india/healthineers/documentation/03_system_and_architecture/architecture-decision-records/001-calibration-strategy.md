# ADR 001: Per-Site / Per-Prevalence Calibration

## Status

Accepted (2019-08)

## Context

Disease prevalence differs by 1–2 orders of magnitude between a symptomatic hospital cohort and a screening population. A model calibrated on the clinic is **confidently wrong** at a screening site — a direct patient-safety risk. Global calibration is therefore insufficient.

## Decision

Adopt a **per-site / per-prevalence calibration** layer:
- **Per-site temperature scaling** fitted on local labelled data.
- **Per-prevalence isotonic calibration** on top.
- Calibration slope + intercept reported per site.
- **Site-held-out validation** measures transfer before any score is shown.
- An uncalibrated score is treated as a **defect**, not a cosmetic issue.

## Consequences

**Positive:**
- The same image gets a different, correct probability at a clinic vs. a screening camp.
- Directly addresses prevalence shift — the central technical risk.
- Calibration becomes a release gate (ECE ≤ 0.05; slope 0.8–1.25).

**Negative:**
- Per-site calibration requires local labelled data.
- More complex to maintain across many sites.

**Mitigation:**
- Hierarchical calibration (global prior + local fit).
- Site-held-out validation.
- Drift monitoring triggers recalibration.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Global calibration only | Simplicity | Confidently wrong at screening sites |
| No calibration (raw scores) | Simplicity | Unsafe; uncalibrated |
| Per-site only (no prevalence) | Simpler | Misses clinic-vs-screening gap |

## Compliance / Governance

- Patient safety: calibration as a release gate.
- Regulatory: documented calibration per site.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-001