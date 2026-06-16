from app.self_healing.healing_loop import (
    self_healing_retrieve
)
from app.websearch.fallback_pipeline import (
    fallback_answer
)
from app.verification.verification_pipeline import (
    verify_answer
)

#Function:

def answer_query(
        query,
        threshold=0.4
):

#Retrieve:

    retrieval = (
        self_healing_retrieve(
            query
        )
    )

#Check quality:

    score = (
        retrieval["quality"]
        ["average_score"]
    )

#Good Retrieval

    if score >= threshold:

#Buildcontexts:

        contexts = [
            r["text"]
            for r in retrieval[
                "results"
            ]
        ]

#Generate answer:

        answer = (
            verify_answer(
                query,
                contexts
            )
        )

#Return:

        return {
            "source":
                "qdrant",

            "answer":
                answer,

            "contexts":
                contexts
        }

#Fallback

    return fallback_answer(
        query
    )