# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Extraction
- **Given** a valid tax document upload,
- **When** extraction runs,
- **Then** it returns structured fields with per-field confidence + provenance.

### AC-2 — Never silently accept low confidence
- **Given** a field with confidence < τ,
- **When** routing runs,
- **Then** the field enters the review queue (never auto-filled).

### AC-3 — Calibrated confidence
- **Given** the calibration model,
- **When** evaluated on a held-out set,
- **Then** ECE ≤ 0.05.

### AC-4 — Review efficiency
- **Given** a reviewer in the queue,
- **When** they process fields,
- **Then** median review time ≤ 8 s/field.

### AC-5 — Audit trail
- **Given** any field,
- **When** committed,
- **Then** an audit event records field → confidence → provenance.

### AC-6 — Downstream reject reduction
- **Given** shadow deployment,
- **When** compared to baseline,
- **Then** downstream reject rate ↓ ≥ 50%.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | Clean W-2 | High-quality scan | High confidence, auto-fill |
| TC-02 | Degraded scan | Fax/low DPI | Lower confidence → review |
| TC-03 | Unknown layout | Unrecognized form | Review queue |
| TC-04 | Low-confidence field | Ambiguous value | Review queue |
| TC-05 | Review action | Accept/correct/reject | Logged as training label |
| TC-06 | PII in document | TIN/DOB | Redacted/masked in logs |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | Extraction p95 latency | ≤ 2 s |
| NFR-AC2 | Availability | 99.5% |
| NFR-AC3 | Audit completeness | 100% of fields |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and the release gates in `master-test-strategy.md` are green.