from app.agents.decomposition_agent import (
    decompose_query
)

from app.agents.retrieval_agent import (
    retrieve_for_question
)

from app.agents.aggregation_agent import (
    aggregate_context
)


def run_agentic_retrieval(query):
    questions = decompose_query(
        query
    )

    retrieval_outputs = []

    for question in questions:
        output = retrieve_for_question(
            question
        )

        retrieval_outputs.append(
            output
        )

    contexts = aggregate_context(
        retrieval_outputs
    )

    return {
        "original_query": query,
        "subquestions": questions,
        "contexts": contexts
    }