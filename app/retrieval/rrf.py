def reciprocal_rank_fusion(
        dense_docs,
        sparse_docs,
        k=60
):

    scores = {}

    for rank, doc in enumerate(
            dense_docs
    ):

        text = doc["text"]

        scores[text] = (
            scores.get(text, 0)
            + 1 / (k + rank + 1)
        )

    for rank, (doc, _) in enumerate(
            sparse_docs
    ):

        text = doc["text"]

        scores[text] = (
            scores.get(text, 0)
            + 1 / (k + rank + 1)
        )

    fused = []

    for text, score in scores.items():

        fused.append(
            {
                "text": text,
                "rrf_score": score
            }
        )

    fused.sort(
        key=lambda x: x["rrf_score"],
        reverse=True
    )

    return fused