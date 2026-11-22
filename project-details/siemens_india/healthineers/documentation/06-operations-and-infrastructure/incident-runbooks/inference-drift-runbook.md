# Incident Runbook — Inference Failure / Drift

## When to use

- Inference API error rate spikes.
- Calibration / drift alerts.
- Data-ingestion failure.

## Steps

1. **Detect** — alert fires (error rate, drift, calibration).
2. **Assess** — which stage? (ingestion / segmentation / classification / calibration)
3. **Mitigate:**
   - **Ingestion failure:** check DICOM feed; quarantine affected studies.
   - **Inference failure:** fall back to worklist-only; alert.
   - **Calibration drift:** roll back to previous calibration set; re-evaluate.
   - **Domain shift:** flag affected site/device; schedule recalibration.
6. **Communicate** — notify clinical lead + regulatory.
7. **Recover** — restore normal flow; re-run affected studies.
8. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model/calibration version.
- Re-run affected studies.

## Escalation

- Data science on-call → Clinical lead → Regulatory.