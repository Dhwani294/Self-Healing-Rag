from app.database.db import SessionLocal

from app.database.models import QueryMetric

def log_query(
query,
answer,
confidence,
source,
healing_triggered,
latency_ms
):
    db = SessionLocal()
    try:
        metric = QueryMetric(
            query=query,
            answer=answer,
            confidence=confidence,
            source=source,
            healing_triggered=healing_triggered,
            latency_ms=latency_ms,
        )

        db.add(metric)
        db.commit()
    finally:
        db.close()

