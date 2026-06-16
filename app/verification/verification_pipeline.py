from .answer_generator import (
    generate_answer
)

from .hallucination_detector import (
    detect_hallucinations
)

from .answer_regenerator import (
    regenerate_answer
)

#Function:

def verify_answer(
        query,
        contexts,
        max_retries=3
):

#Generate:

    answer = generate_answer(
        query,
        contexts
    )

#Loop:

    retries = 0
    while retries < max_retries:

#Check:

        result = (
            detect_hallucinations(
                answer,
                contexts
            )
        )

#Pass:

        if (
            len(
                result[
                    "hallucinated"
                ]
            )
            == 0
        ):

#Return:

            return {
                "status":
                    "verified",
                "answer":
                    answer,
                "retries":
                    retries
            }

#Retry:

        answer = (
            regenerate_answer(
                query,
                contexts
            )
        )
        retries += 1



    return {
        "status":
            "low_confidence",
        "answer":
            answer,
        "retries":
            retries
    }