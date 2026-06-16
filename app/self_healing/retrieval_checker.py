from sentence_transformers import CrossEncoder

checker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def score_retrieval(
    query,
    chunks
):
    pairs = [
        [query, chunk["text"]]
        for chunk in chunks
    ]

    scores = checker.predict(
        pairs
    )

    avg_score = (
        sum(scores)
        / len(scores)
    )

    return {
        "average_score": float(avg_score),
        "scores": [
            float(s)
            for s in scores
        ]
    }