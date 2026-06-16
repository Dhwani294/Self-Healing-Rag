from app.websearch.tavily_search import (
    web_search,
    build_web_context
)
from app.verification.verification_pipeline import (
    verify_answer
)

#Function:

def fallback_answer(
        query
):

#Search:

    results = web_search(
        query
    )

#Build context:

    contexts = (
        build_web_context(
            results
        )
    )

#Generate answer:

    answer = verify_answer(
        query,
        contexts
    )

#Return:

    return {
        "source":
            "web",

        "contexts":
            contexts,

        "answer":
            answer
    }