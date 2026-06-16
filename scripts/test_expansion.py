from app.retrieval.query_expansion import (
    expanded_retrieve
)

query = (
    "What benefits do employees receive?"
)

results = expanded_retrieve(
    query
)

print("\nRESULTS\n")

for result in results:

    print(
        f"\nScore: {result['score']:.4f}"
    )

    print(result["text"])