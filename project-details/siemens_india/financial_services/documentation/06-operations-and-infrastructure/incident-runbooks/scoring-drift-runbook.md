# Incident Runbook — Scoring Failure / Drift

## When to use

- Scoring API error rate spikes.
- Calibration / PSI drift alerts.
- Data-join failure.

## Steps

1. **Detect** — alert fires (error rate, PSI, calibration drift).
2. **Assess** — which stage? (data join / features / PD / survival / calibration)
3. **Mitigate:**
   - **Data-join error:** quarantine affected contracts; audit join accuracy.
   - **Calibration drift:** roll back to previous calibrator; re-evaluate.
   - **Concept drift (PSI):** trigger retrain; flag affected cohort.
   - **Model failure:** serve last-good; alert model risk.
4. **Communicate** — notify credit-risk owner + model risk.
5. **Recover** — restore normal flow; re-run affected batches.
6. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model/calibration version.
- Re-run affected batches.

## Escalation

- Data science on-call → Model risk → Credit-risk owner.