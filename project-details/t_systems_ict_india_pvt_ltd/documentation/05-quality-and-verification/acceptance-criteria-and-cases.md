# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Search
- **Given** a query,
- **When** search runs,
- **Then** it returns ranked results with scores + positions.

### AC-2 — Recommendations
- **Given** a session context (no query),
- **When** recommendations run,
- **Then** it returns placement-appropriate recommendations.

### AC-3 — Separate labels
- **Given** search and reco,
- **When** training,
- **Then** they use separate datasets/labels/metrics.

### AC-4 — Position-bias control
- **Given** impression logs,
- **When** training,
- **Then** only exposed items are negatives; position is recorded.

### AC-4 — Cold start
- **Given** a new SKU / new user,
- **When** discovery runs,
- **Then** it uses content/popularity fallback (documented).

### AC-5 — No un-evidenced lift
- **Given** a conversion claim,
- **When** published,
- **Then** it rests on a controlled online experiment (not shadow).

### AC-6 — Latency
- **Given** peak load,
- **When** measured,
- **Then** p95 ≤ target within the benchmark boundary.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | Search relevance | Query + candidates | NDCG@K vs. baseline |
| TC-02 | Recommendation | Session context | Placement-appropriate items |
| TC-03 | Cold start SKU | New SKU | Content/popularity fallback |
| TC-04 | Cold start user | New user | Context/popularity fallback |
| TC-05 | Position bias | Impression at position 1 | Recorded; bias-corrected |
| TC-06 | Timeout | Slow upstream | Safe fallback |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | p95 latency | ≤ target (boundary defined) |
| NFR-AC2 | Availability | 99.9% |
| NFR-AC3 | Guardrails | No no-results/latency regression |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and the release gates in `master-test-strategy.md` are green.