from fastapi import FastAPI

from app.api.routes.query import router as query_router
from app.api.routes.health import router as health_router
from app.api.routes.metrics import router as metrics_router
from app.api.routes.ingest import router as ingest_router

app = FastAPI(
    title="Self Healing RAG",
    version="1.0.0"
)

app.include_router(query_router)
app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(ingest_router)