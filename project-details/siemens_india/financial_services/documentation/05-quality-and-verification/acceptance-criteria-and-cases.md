# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Scoring
- **Given** an account + as-of date,
- **When** scoring runs,
- **Then** it returns calibrated PD + survival P10/P50/P90 + reason codes + flag.

### AC-2 — No autonomous decision
- **Given** any score,
- **When** delivered,
- **Then** it is decision-support; a credit officer decides.

### AC-3 — Calibrated PD
- **Given** the calibration model,
- **When** evaluated,
- **Then** ECE ≤ 0.03.

### AC-4 — Operational lift
- **Given** the model,
- **When** compared to financial-only,
- **Then** operational lift ≥ +0.03 KS.

### AC-5 — Reason codes
- **Given** any score,
- **When** delivered,
- **Then** every PD carries SHAP reason codes (officer-rated ≥ 0.70).

### AC-6 — Early warning
- **Given** a deteriorating account,
- **When** scored,
- **Then** lead time ≥ 3 months; recall ≥ 0.60.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | Defaulting account | Deteriorating telemetry | Red flag, lead time ≥ 3 mo |
| TC-02 | Performing account | Stable telemetry | Green flag |
| TC-03 | Thin history | New contract | Reject inference / flag |
| TC-04 | Class imbalance | 2–5% defaulters | PR-AUC/KS, not accuracy |
| TC-05 | Censored loan | No default in window | Survival uses it |
| TC-06 | Drift | Economic shift | PSI alert |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | Scoring p95 | ≤ 5 s |
| NFR-AC2 | Availability | 99.5% |
| NFR-AC3 | Reason-code coverage | 100% of scores |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and the release gates in `master-test-strategy.md` are green.