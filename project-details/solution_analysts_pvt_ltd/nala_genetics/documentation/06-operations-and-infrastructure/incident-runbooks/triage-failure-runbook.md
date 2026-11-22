# Incident Runbook — Triage Failure / Curator Backlog

## When to use

- Triage API error rate spikes.
- Curator queue backlog exceeds threshold.
- Annotation / model serving failure.

## Steps

1. **Detect** — alert fires (latency, error rate, queue depth).
2. **Assess** — which stage failed? (annotation / features / classify / calibrate / literature)
3. **Mitigate:**
   - **Annotation failure:** fall back to previous VEP/dbNSFP release; flag affected variants.
   - **Model failure:** abstain (VUS) rather than confidently classify; alert data science.
   - **Queue backlog:** add workers; adjust thresholds to reduce load.
   - **Calibration drift:** roll back to previous calibrator; re-evaluate.
4. **Communicate** — notify clinical + data science.
5. **Recover** — restore normal flow; re-run affected batches.
6. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model/config/annotation version.
- Re-run affected batches.

## Escalation

- Data science on-call → Clinical lead → Engineering lead.