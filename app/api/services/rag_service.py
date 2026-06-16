from app.websearch.router import answer_query


def run_rag(query: str):
    result = answer_query(query)

    answer_data = result["answer"]

    confidence = 1.0

    if answer_data["status"] == "low_confidence":
        confidence = 0.4

    return {
        "answer": answer_data["answer"],
        "confidence": confidence,
        "source": result["source"]
    }