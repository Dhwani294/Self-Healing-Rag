from sqlalchemy.orm import declarative_base
from sqlalchemy import (
Column,
Integer,
String,
Float,
Boolean,
DateTime
)

from datetime import datetime

Base = declarative_base()

class QueryMetric(Base):
    __tablename__ = "query_metrics"

    id = Column(
        Integer,
        primary_key=True
    )

    query = Column(String)

    answer = Column(String)

    confidence = Column(Float)

    source = Column(String)

    healing_triggered = Column(Boolean)

    latency_ms = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

