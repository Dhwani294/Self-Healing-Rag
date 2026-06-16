from sentence_transformers import (
    CrossEncoder
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(
        query,
        chunks
):

    pairs = [
        [query, chunk["text"]]
        for chunk in chunks
    ]

    scores = reranker.predict(
        pairs
    )

    results = []

    for chunk, score in zip(
            chunks,
            scores
    ):

        results.append(
            {
                "text": chunk["text"],
                "score": float(score)
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results