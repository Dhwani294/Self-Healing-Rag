from .multi_query import generate_queries
from .hyde import generate_hypothetical_document
from .hybrid import hybrid_retrieve


def expanded_retrieve(
        query,
        top_k=5
):

    queries = generate_queries(query)

    hyde_doc = generate_hypothetical_document(
        query
    )

    queries.append(hyde_doc)

    all_results = []

    for q in queries:

        try:

            results = hybrid_retrieve(
                q,
                top_k=5
            )

            all_results.extend(results)

        except Exception as e:

            print(
                f"Retrieval error: {e}"
            )

    unique = {}

    for result in all_results:

        text = result["text"]

        if text not in unique:

            unique[text] = result

    final_results = sorted(
        unique.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return final_results[:top_k]