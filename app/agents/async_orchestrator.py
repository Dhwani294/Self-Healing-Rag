import asyncio

from app.agents.decomposition_agent import decompose_query
from app.agents.retrieval_agent import retrieve_for_question
from app.agents.aggregation_agent import aggregate_context


async def retrieve_async(question):
    return retrieve_for_question(question)


async def run_agentic_retrieval(query):
    questions = decompose_query(query)

    tasks = [
        retrieve_async(q)
        for q in questions
    ]

    retrieval_outputs = await asyncio.gather(
        *tasks
    )

    contexts = aggregate_context(
        retrieval_outputs
    )

    return {
        "original_query": query,
        "subquestions": questions,
        "contexts": contexts
    }