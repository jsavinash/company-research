# Business Case and ROI

## 1. The problem

Three facts from `Nestle-USA-Research.md` define the business case:

1. **Volumes are structurally declining.** US food volume per person fell **0.6% in H1 2026**. Nestlé USA cannot grow on category expansion — it must defend share and price/mix.
2. **Frozen is the most exposed category.** GLP-1 adoption is associated with a **~3-point drop in dollar spend in year one** — the largest CPG category impact. Frozen is also where Nestlé is investing most (DiGiorno, Stouffer's, Hot Pockets, Lean Pockets, Lean Cuisine, CPK, Tombstone, Jack's, Buitoni).
3. **The old forecasting regime is dead.** Models trained on 2015–2022 history encode a world without meaningful GLP-1 penetration, without private label at **23.8% of units**, and without cocoa at **~$3,500/t**. Backtesting them on 2025–26 data produces confident, wrong numbers.

**The gap is predictive and causal:** not "what happened on the shelf" (descriptive, already covered by digital-shelf monitoring) but **"what will happen two to three quarters ahead, and why"**, when the demand process itself has changed.

## 2. The value proposition

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Avoided stockouts / overproduction** | Better store-level forecasts → right inventory in the right banner | Supply chain, retailers |
| **Trade-spend efficiency** | Causal attribution separates price/mix effects → less wasted promotion | Revenue growth management |
| **Faster response to regime shifts** | GLP-1 as a first-class driver → forecasts survive the break | Demand planning |
| **Audit-grade decisions** | Every number traceable to a forecast run + feature snapshot | Finance, compliance |
| **Reusable platform** | 6-layer architecture reused across Frozen, Coffee, Baking | Enterprise |

## 3. ROI model (illustrative)

| Component | Assumption | Annual value (illustrative) |
|---|---|---|
| Forecast accuracy improvement | ≥15% relative WMAPE reduction (out-of-regime) | Reduced safety stock + fewer lost sales |
| Trade-spend efficiency | Attribution-driven reallocation | Margin uplift |
| Analyst time saved | Copilot handles scenario analysis | Productivity |
| Avoided write-offs | Better shelf-life / promotion planning | Waste reduction |

> **Note:** all figures are illustrative and must be replaced with Nestlé USA's actual baseline before any business-case submission. The source ProjectDoc deliberately avoids unverified numbers.

## 4. Success criteria (business)

- Out-of-regime WMAPE improves **≥15% relative** vs. the incumbent on frozen.
- GLP-1 effect estimates are **sign-consistent** across rolling windows.
- Forecast intervals are **calibrated** (P50/P90 coverage within tolerance).
- **No systematic bias** by DMA income quintile.
- **Decision adoption ≥ 80%** among demand planners.
- **RIG contribution** (premiumization → registered innovation value) measurable and reported to finance.

## 5. Risks to the business case

| Risk | Mitigation |
|---|---|
| Data access (retailer contracts) | Degrade to first-party + panel; per-retailer governance |
| Regime shift outpaces model updates | Out-of-regime evaluation + scheduled re-estimation |
| Adoption resistance | Copilot UX, planner-in-the-loop, training |
| Overclaiming accuracy | Holdout + out-of-regime gates; no shadow-equals-lift claims |