# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Analysis
- **Given** a chest X-ray study,
- **When** analyzed,
- **Then** it returns a triage category + findings + heatmaps + site-calibrated confidence.

### AC-2 — No autonomous diagnosis
- **Given** any analysis,
- **When** delivered,
- **Then** it is decision-support; the radiologist signs.

### AC-3 — Calibrated confidence
- **Given** the calibration layer,
- **When** evaluated per site,
- **Then** ECE ≤ 0.05; slope 0.8–1.25.

### AC-4 — Localization
- **Given** a finding,
- **When** localized,
- **Then** a Grad-CAM heatmap is present (IoU vs. radiologist boxes reported).

### AC-5 — Abstention
- **Given** poor quality / OOD,
- **When** analyzed,
- **Then** it returns "cannot assess" (never confident wrong).

### AC-6 — Radiologist acceptance
- **Given** a reader study,
- **When** measured,
- **Then** acceptance ≥ 0.70; read-time ↓ ≥ 15%.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | TB-suggestive X-ray | Abnormal | Urgent/priority; heatmap; calibrated conf |
| TC-02 | Normal X-ray | Normal | Routine |
| TC-03 | Poor quality | Motion artifact | "Cannot assess" |
| TC-04 | Portable device | Portable | Device-class handled |
| TC-05 | Rare finding | Subtle | "Cannot assess" if unsure |
| TC-06 | Screening site | Low prevalence | Calibrated for screening |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | Inference p95 | ≤ 3 s |
| NFR-AC2 | Availability | 99.5% |
| NFR-AC3 | Audit completeness | 100% of studies |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and the release gates in `master-test-strategy.md` are green.