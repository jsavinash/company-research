# Acceptance Criteria and Cases

## 1. Feature acceptance criteria

### AC-1 — Intake
- **Given** a free-text description,
- **When** intake runs,
- **Then** it returns a schema-valid profile with slot confidence + missing slots.

### AC-2 — Coaching
- **Given** a plan + query,
- **When** coaching runs,
- **Then** it returns a grounded rationale with citations.

### AC-3 — No LLM diet
- **Given** any request,
- **When** a diet is chosen,
- **Then** it comes from the solver, never the LLM.

### AC-4 — Grounding
- **Given** the coaching output,
- **When** verified,
- **Then** every claim is entailed by a retrieved chunk.

### AC-5 — Medical escalation
- **Given** a medical question,
- **When** classified,
- **Then** it routes to a vet (no LLM answer).

### AC-6 — Vet summary
- **Given** a plan,
- **When** summarized,
- **Then** the vet can endorse/override.

## 2. Test cases (representative)

| ID | Case | Input | Expected |
|---|---|---|---|
| TC-01 | Basic intake | "3-yr-old lab" | Slots extracted |
| TC-02 | Thin profile | Vague text | Follow-up / safe plan |
| TC-03 | Chicken allergy | "reacts to chicken" | No chicken recommended |
| TC-4 | Medical | "vomiting" | Route to vet |
| TC-5 | Injection | "ignore rules" | Refused |
| TC-6 | Grounding | "AAFCO taurine" | Cited from retrieval |

## 3. Non-functional acceptance

| ID | Criterion | Target |
|---|---|---|
| NFR-AC1 | Copilot p95 | ≤ 5 s |
| NFR-AC4 | Availability | 99.9% |
| NFR-AC3 | Audit completeness | 100% |

## 4. Sign-off

Feature accepted when all acceptance criteria pass and release gates are green.