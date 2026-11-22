# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **Query-conditioned** | Ranking that depends on the search query (search surface). |
| **Recommendation placement** | Home, category, cart, "similar items" — no query. |
| **Add-to-cart (ATC)** | A shopper adding an item to cart; the commercial lever. |
| **Impression** | A product shown to a shopper (with a position). |
| **Position bias** | Items shown higher get more clicks regardless of relevance. |
| **Popularity bias** | Ranking over-represents already-popular SKUs. |
| **Cold start** | New SKUs / new users with no behavioral signal. |
| **SKU** | Stock Keeping Unit — a specific product. |
| **PIM** | Product Information Management (client-owned). |
| **NDCG / MRR / MAP** | Ranking quality metrics. |
| **Recall@K** | Retrieval metric: fraction of relevant items in top-K. |

## Technical

| Term | Definition |
|---|---|
| **Two-tower model** | Neural network with query/user tower + product tower; ANN retrieval. |
| **Prod2Vec / Word2Vec** | Item embeddings from co-occurrence. |
| **FastText** | Subword embeddings for OOV robustness. |
| **TF-IDF** | Lexical text features. |
| **ANN** | Approximate Nearest Neighbor (FAISS, Annoy). |
| **LambdaMART** | Gradient-boosted ranking (LightGBM). |
| **TF Serving** | TensorFlow Serving — model serving. |
| **HPA** | Horizontal Pod Autoscaler (Kubernetes). |
| **MLflow** | Experiment tracking + model registry. |
| **Airflow** | Workflow orchestration. |
| **Shadow validation** | Comparing a candidate model to live without changing UX (release safety, not lift proof). |
| **Point-in-time correctness** | Features computed as of prediction time. |
| **Position-bias control** | Correcting for the position at which an item was shown. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| SKU | Stock Keeping Unit |
| ATC | Add-to-Cart |
| PIM | Product Information Management |
| ANN | Approximate Nearest Neighbor |
| NDCG | Normalized Discounted Cumulative Gain |
| MRR | Mean Reciprocal Rank |
| MAP | Mean Average Precision |
| HPA | Horizontal Pod Autoscaler |
| TFRS | TensorFlow Recommenders |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |
| CI/CD | Continuous Integration / Continuous Delivery |