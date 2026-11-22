# Incident Runbook — Extraction Failure / Review Backlog

## When to use

- Extraction API error rate spikes.
- Review queue backlog exceeds threshold.
- OCR / model serving failure.

## Steps

1. **Detect** — alert fires (latency, error rate, queue depth).
2. **Assess** — which stage failed? (OCR / extraction / classification / calibration)
3. **Mitigate:**
   - **OCR failure:** route to cloud fallback; if cloud also fails, queue for manual entry.
   - **Model failure:** fall back to rules-based extraction; alert data science.
   - **Queue backlog:** add workers; adjust thresholds temporarily to reduce load.
   - **Cloud OCR cost spike:** tighten fallback threshold.
4. **Communicate** — notify operations + data science.
5. **Recover** — restore normal flow; re-run affected documents.
6. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model/config version.
- Re-run affected documents.

## Escalation

- Data science on-call → Engineering lead → Operations.