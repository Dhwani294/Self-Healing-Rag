from app.retrieval.query_expansion import (
    expanded_retrieve
)


def retrieve_for_question(question: str):
    results = expanded_retrieve(
        question
    )

    return {
        "question": question,
        "results": results
    }