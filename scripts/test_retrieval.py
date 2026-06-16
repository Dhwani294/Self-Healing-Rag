from app.retrieval.hybrid import (
    hybrid_retrieve
)

query = (
    "How many leave days do employees get?"
)

results = hybrid_retrieve(query)

print("\nRESULTS\n")

for result in results:

    print(
        f"\nScore: {result['score']:.4f}"
    )

    print(
        result["text"]
    )