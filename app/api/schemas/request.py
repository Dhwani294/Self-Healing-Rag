from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str
    top_k: int = 5
    max_retries: int = 3


class IngestRequest(BaseModel):
    path: str