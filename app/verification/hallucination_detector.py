from nltk.tokenize import sent_tokenize

from .faithfulness_checker import (
    check_faithfulness
)



import nltk
nltk.download("punkt")



def detect_hallucinations(
        answer,
        contexts,
        threshold=0.6
):



    sentences = sent_tokenize(
        answer
    )



    verified = []

    hallucinated = []
    for sentence in sentences:



        score = (
            check_faithfulness(
                sentence,
                contexts
            )
        )



        if score >= threshold:

            verified.append(
                sentence
            )

        else:

            hallucinated.append(
                {
                    "sentence":
                        sentence,
                    "score":
                        score
                }
            )



    return {
        "verified":
            verified,
        "hallucinated":
            hallucinated
    }