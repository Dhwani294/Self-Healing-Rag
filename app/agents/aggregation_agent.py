def aggregate_context(retrieval_outputs):
    seen = set()

    contexts = []

    for output in retrieval_outputs:
        for result in output["results"]:
            text = result["text"]

            if text not in seen:
                seen.add(text)
                contexts.append(text)

    return contexts