from app.retrieval.query_expansion import (
    expanded_retrieve
)

from .retrieval_checker import (
    score_retrieval
)

from .query_rewriter import (
    rewrite_query
)


def self_healing_retrieve(
    query,
    threshold=0.4,
    max_retries=3
):
    results = expanded_retrieve(
        query
    )

    quality = score_retrieval(
        query,
        results
    )

    if quality["average_score"] >= threshold:
        return {
            "healed": False,
            "retries": 0,
            "results": results,
            "quality": quality
        }

    retry_count = 0

    best_results = results

    best_score = (
        quality["average_score"]
    )

    while retry_count < max_retries:

        rewrites = rewrite_query(
            query,
            f"score={best_score}"
        )

        for rewritten in rewrites:

            new_results = expanded_retrieve(
                rewritten
            )

            new_quality = score_retrieval(
                rewritten,
                new_results
            )

            if (
                new_quality["average_score"]
                > best_score
            ):

                best_score = (
                    new_quality[
                        "average_score"
                    ]
                )

                best_results = (
                    new_results
                )

        retry_count += 1

        if best_score >= threshold:
            break

    return {
        "healed": retry_count > 0,
        "retries": retry_count,
        "results": best_results,
        "quality": {
            "average_score": best_score
        }
    }