from pydantic import BaseModel


class QueryResponse(BaseModel):
    answer: str
    confidence: float
    source: str
    healing_triggered: bool


class HealthResponse(BaseModel):
    status: str