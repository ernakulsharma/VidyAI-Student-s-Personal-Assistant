from app.core.logging import logger
from app.services.rag_service import RAGService


class QueryService:
    """
    Coordinates the complete RAG workflow.
    """

    def __init__(self):

        self.rag = RAGService()

    def query(
        self,
        question: str,
    ):

        logger.info(
            f"Question: {question}"
        )

        answer = self.rag.answer(
            question,
        )

        logger.success(
            "Answer generated."
        )

        return answer