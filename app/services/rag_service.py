from time import time

from app.websearch.router import answer_query

from app.monitoring.logger import (
log_query
)

def run_rag(query: str):
    start = time()

    result = answer_query(query)

    answer_data = result["answer"]

    confidence = 1.0

    if answer_data["status"] == "low_confidence":
        confidence = 0.4

    latency = (
        time() - start
    ) * 1000

    log_query(
        query=query,
        answer=answer_data["answer"],
        confidence=confidence,
        source=result["source"],
        healing_triggered=True,
        latency_ms=latency
    )

    return {
        "answer": answer_data["answer"],
        "confidence": confidence,
        "source": result["source"]
    }

