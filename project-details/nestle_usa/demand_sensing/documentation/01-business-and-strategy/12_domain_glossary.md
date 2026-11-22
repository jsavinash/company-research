# Domain Glossary

Ubiquitous business terminology for the Demand Sensing project. (Technical terms live in the platform glossary; this is the business-facing vocabulary.)

## 1. Business & category

| Term | Definition |
|---|---|
| **Banner** | A retail banner (specific grocery chain) within a retailer group. |
| **DMA** | Designated Market Area — a geographic market (Nielsen). |
| **Category** | Product grouping (Frozen, Coffee, Baking). |
| **SKU** | Stock Keeping Unit — a specific product/pack. |
| **Brand** | Consumer-facing brand (DiGiorno, Stouffer's, Coffee mate). |
| **ACV** | All Commodity Volume — distribution weighting. |
| **Distribution** | Presence of a product in stores (ACV / points). |
| **Sell-in** | Nestlé shipments to the retailer. |
| **Sell-out** | Retailer sales to consumers (scanner/loyalty). |
| **Panel data** | Household-level purchase panel (Circana/Nielsen). |
| **Private label** | Retailer-owned brands (23.8% of units). |
| **Trade spend** | Promotional / trade investment. |
| **Mix** | Product/channel mix effect on value. |
| **RGM** | Revenue Growth Management. |
| **RIG** | Registered/Recognised Innovation Governance — value-reporting mechanism to finance. |

## 2. Demand & forecasting

| Term | Definition |
|---|---|
| **Demand sensing** | Using near-real-time signals to forecast demand. |
| **Regime shift / structural break** | A change in the demand process (GLP-1, private label, input costs) that invalidates history-based models. |
| **GLP-1** | Glucagon-like peptide-1 receptor agonists — weight-loss/diabetes drugs associated with reduced food-basket spend. |
| **Forecast horizon** | How far ahead the forecast looks (1–2 quarters). |
| **Interval (P10/P50/P90)** | Prediction range; P10 pessimistic, P50 median, P90 optimistic. |
| **Bias** | Systematic over/under-forecast. |
| **Out-of-regime** | Testing on data beyond the training regime. |
| **Analog forecasting** | Forecasting a new/reformulated product using a comparable historical product. |
| **Hierarchical reconciliation** | Making store → banner → DMA → national forecasts consistent. |

## 3. Causal & measurement

| Term | Definition |
|---|---|
| **Causal attribution** | Decomposing a demand delta into drivers (GLP-1, price, mix, private label). |
| **Synthetic control** | Constructing a weighted counterfactual from a donor pool. |
| **DiD** | Difference-in-differences — causal design comparing exposed vs. control pre/post. |
| **Counterfactual** | What would have happened without the driver. |
| **Placebo test** | Sanity check applying the method where no effect should exist. |
| **Point-in-time correctness** | Using only data available at prediction time. |

## 4. Governance & value

| Term | Definition |
|---|---|
| **ABAC** | Attribute-Based Access Control (banner/DMA/role). |
| **OPA** | Open Policy Agent — policy decision point. |
| **DLP** | Data Loss Prevention. |
| **Audit trail** | Immutable record of every forecast/scenario run. |
| **Chargeback** | Attributing cost to a business unit. |
| **FinOps** | Financial operations for cloud/AI cost. |
| **SLA** | Service Level Agreement. |
| **RIG contribution** | Reported innovation value to finance. |

## 5. Abbreviations

| Abbreviation | Expansion |
|---|---|
| SKU | Stock Keeping Unit |
| ACV | All Commodity Volume |
| DMA | Designated Market Area |
| RGM | Revenue Growth Management |
| RIG | Registered/Recognised Innovation Governance |
| GLP-1 | Glucagon-like peptide-1 |
| ABAC | Attribute-Based Access Control |
| OPA | Open Policy Agent |
| DLP | Data Loss Prevention |
| SLA | Service Level Agreement |
| FinOps | Financial Operations |
| DiD | Difference-in-differences |