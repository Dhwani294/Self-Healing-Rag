from fastapi import APIRouter

from app.database.db import (
SessionLocal
)

from app.database.models import (
QueryMetric
)

router = APIRouter()

@router.get("/metrics")
async def metrics():
    db = SessionLocal()

    count = db.query(
        QueryMetric
    ).count()

    avg_confidence = 0

    rows = db.query(
        QueryMetric
    ).all()

    if rows:
        avg_confidence = (
            sum(
                r.confidence
                for r in rows
            )
            / len(rows)
        )

    db.close()

    return {
        "requests": count,
        "avg_confidence": avg_confidence
    }

