from fastapi import APIRouter

from app.schemas.query import QueryRequest
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

service = RAGService()


@router.post("/query")
async def query(request: QueryRequest):
    result = service.answer_with_sources(request.query)
    return {
        "question": request.query,
        **result,
    }
