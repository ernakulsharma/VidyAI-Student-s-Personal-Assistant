from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGService:

    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()

    def answer(
        self,
        query: str,
    ) -> str:

        results = self.retriever.retrieve(query)

        if (
            not results
            or "documents" not in results
            or not results["documents"]
        ):
            return "No relevant information found."

        context = "\n\n".join(
            results["documents"][0]
        )

        answer = self.llm.generate(
            question=query,
            context=context,
        )

        return context