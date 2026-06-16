from fastapi import APIRouter

from app.schemas.request import QueryRequest
from app.services.rag_service import run_rag

router = APIRouter()


@router.post("/query")
async def query_rag(
    req: QueryRequest
):
    result = run_rag(req.query)

    return {
        "answer": result["answer"],
        "confidence": result["confidence"],
        "source": result["source"]
    }