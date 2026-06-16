User Query
|
v
FastAPI
|
v
Query Expansion
(Multi Query + HyDE)
|
v
Hybrid Retrieval
(Dense + BM25)
|
v
RRF Fusion
|
v
Cross Encoder Reranker
|
+----> Low Score?
|
v
Query Rewrite
|
v
Retry Retrieval

```
 |
 v
```

Generator
|
v
Hallucination Detection
(NLI)
|
+----> Hallucinated?
|
v
Regenerate

```
 |
 v
```

Answer

```
 |
 +----> PostgreSQL Metrics

 |
 +----> Grafana Dashboard

 |
 +----> Tavily Fallback
```
