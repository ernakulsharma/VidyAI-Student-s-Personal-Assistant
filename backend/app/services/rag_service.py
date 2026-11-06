from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGService:
    """Retrieve document context and generate grounded academic answers."""

    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()

    def answer_with_sources(self, query: str) -> dict:
        results = self.retriever.retrieve(query)

        documents = (results.get("documents") or [[]])[0]
        metadatas = (results.get("metadatas") or [[]])[0]

        if not documents:
            return {
                "answer": "I couldn't find relevant information in the uploaded documents. Upload a study document and try again.",
                "sources": [],
            }

        context = "\n\n".join(documents)
        answer = self.llm.generate(question=query, context=context)

        sources = []
        seen = set()
        for metadata in metadatas:
            metadata = metadata or {}
            source_key = (
                metadata.get("document_id"),
                metadata.get("chunk_id"),
            )
            if source_key in seen:
                continue
            seen.add(source_key)
            sources.append(
                {
                    "document_id": metadata.get("document_id"),
                    "filename": metadata.get("filename") or "Uploaded document",
                    "heading": metadata.get("heading") or None,
                    "chunk_id": metadata.get("chunk_id"),
                }
            )

        return {"answer": answer, "sources": sources}

    def answer(self, query: str) -> str:
        """Backward-compatible text-only answer method."""
        return self.answer_with_sources(query)["answer"]
