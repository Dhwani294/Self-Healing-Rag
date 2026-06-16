from sentence_transformers import (
    CrossEncoder
)


checker = CrossEncoder(
    "cross-encoder/nli-deberta-v3-small"
)



def check_faithfulness(
        sentence,
        contexts
):


    evidence = " ".join(
        contexts
    )



    score = checker.predict(
        [[evidence, sentence]]
    )[0]


    return float(score)