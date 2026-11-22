# User Personas and Empathy Mapping

## 1. Personas

### Persona 1 — Demand Planner (primary)

| Attribute | Detail |
|---|---|
| **Name** | "Priya" — Demand Planner, Frozen |
| **Goals** | Accurate 2–3 quarter forecasts; defend share; explain variances to leadership |
| **Frustrations** | Spreadsheet drudgery; models blind to GLP-1; can't answer "why" |
| **Tools** | Excel, Power BI, Teams, Snowflake |
| **Success looks like** | Walks into Monday meeting with a defensible, explainable forecast |
| **Quote** | "I need to know what happens next quarter, and why — not a 40-tab spreadsheet." |

### Persona 2 — RGM Analyst

| Attribute | Detail |
|---|---|
| **Name** | "Arjun" — Revenue Growth Management |
| **Goals** | Separate price/mix/GLP-1 effects; optimize trade spend |
| **Frustrations** | Can't isolate drivers; correlational deltas mislead |
| **Success looks like** | Defensible causal decomposition of a demand change |

### Persona 3 — Supply Planner

| Attribute | Detail |
|---|---|
| **Name** | "Meera" — Supply Planning |
| **Goals** | Store/banner numbers by production/procurement lead time |
| **Frustrations** | Manual reconciliation; late data |
| **Success looks like** | Right inventory in the right banner; fewer stockouts |

### Persona 4 — Data Steward

| Attribute | Detail |
|---|---|
| **Name** | "Vikram" — Data Governance |
| **Goals** | Lineage, permissions, quality |
| **Frustrations** | Ad-hoc access requests; over-sharing risk |
| **Success looks like** | Auditable access; no data leaks |

## 2. Empathy map (Demand Planner)

| | |
|---|---|
| **Says** | "The old model is wrong again." |
| **Thinks** | "I don't trust the number; I'll rebuild it in Excel." |
| **Does** | Pulls data, reconciles manually, adjusts by judgment |
| **Feels** | Overwhelmed, accountable, time-pressed |

| Pain | Gain |
|---|---|
| Regime blindness | A model that survives the break |
| Manual work | Conversational what-ifs in seconds |
| No "why" | Causal attribution |
| Audit risk | Run IDs + lineage |

## 3. Needs → features

| Need | Feature |
|---|---|
| Trustworthy forward view | Regime-aware forecast + intervals |
| Explanation | Causal attribution |
| Speed | Copilot |
| Compliance | Permission-aware retrieval + audit |
| Confidence | Out-of-regime evaluation |

## 4. Jobs-to-be-done summary

See `jobs_to_be_done_and_value_prop.md`.