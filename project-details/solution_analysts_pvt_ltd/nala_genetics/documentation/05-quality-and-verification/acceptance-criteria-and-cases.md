# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Triage
- **Given** a VCF + panel,
- **When** triage runs,
- **Then** it returns ranked variants with score, calibrated confidence, ACMG codes + provenance.

### AC-2 — No autonomous classification
- **Given** any result,
- **When** delivered,
- **Then** it is decision-support; a curator must sign off.

### AC-3 — Explicit abstention
- **Given** insufficient evidence,
- **When** routing runs,
- **Then** the variant is marked VUS / abstained (never confidently classified).

### AC-4 — Calibrated confidence
- **Given** the calibration model,
- **When** evaluated,
- **Then** ECE ≤ 0.05.

### AC-5 — Ancestry fairness
- **Given** the evaluation,
- **When** run per superpopulation,
- **Then** the transfer gap is reported as a headline.

### AC-6 — Curator efficiency
- **Given** a curator in the queue,
- **When** they process variants,
- **Then** median review time ≤ 90 s/variant.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | Known pathogenic variant | ClinVar P/LP | High score, top-20, P/LP code |
| TC-02 | Known benign variant | ClinVar B/LB | Low score, deprioritize |
| TC-03 | VUS | Conflicting/absent evidence | Abstain (VUS) |
| TC-04 | Gene-disjoint | Gene held out | Performance measured on unseen gene |
| TC-05 | Ancestry transfer | European vs. Asian calibrated | Gap reported |
| TC-06 | Curator action | Accept/override/reject | Logged as training label |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | Triage p95 latency | ≤ 3 s |
| NFR-AC2 | Availability | 99.5% |
| NFR-AC3 | Audit completeness | 100% of results |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and the release gates in `master-test-strategy.md` are green.