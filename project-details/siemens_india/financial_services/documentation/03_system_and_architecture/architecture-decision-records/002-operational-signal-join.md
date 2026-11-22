# ADR 002: Operational-Signal Join (the Moat)

## Status

Accepted (2019-08)

## Context

SFS's differentiator is that it can see how the financed machine is operated (utilization, downtime, service-deferral, energy), while a generic lender sees only financials. Realizing this requires joining credit data (SFS), operational telemetry (Siemens service/ops), and finance data (Corporate) — across different systems, keys, and legal entities, under time-correct and privacy-preserving constraints.

## Decision

Adopt a **governed operational-signal join**:
- **Risk-data platform** (Kafka → Spark → time-aware feature store) joins credit + telemetry + finance.
- **Per-entity, per-contract isolation** with de-identification.
- **Operational features** (utilization, downtime, service-deferral, energy) computed as windowed, lagged features and **attributed separately** from financial signals.
- **Operational-signal lift measured as a release gate** vs. a financial-only baseline.

## Consequences

**Positive:**
- Realizes the moat: a leading operational signal beyond lagging financials.
- Attribution ("operational vs. financial") justifies SFS's existence as lender.
- Governed join satisfies DPDP / cross-entity constraints.

**Negative:**
- The join is partial in reality — not every asset is connected, not every contract permits data sharing.
- Complex engineering + governance.

**Mitigation:**
- State the *achievable* coverage honestly.
- Audited join accuracy; per-contract keys.
- De-identification + per-entity isolation.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Financial-only model | Simpler | No moat; matches any bank |
| Un-governed data pooling | More signal | Violates DPDP / contracts |
| No operational join | Simple | Concedes the differentiator |

## Compliance / Governance

- India DPDP; per-entity isolation; de-identification.
- Operational-signal lift as a gate (if no lift, the moat claim fails).

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-001, D-008