from app.embeddings.bge_m3_embedding import BGEM3Embedding
from app.vectorstore.chroma_store import ChromaStore
from app.dependencies.container import (
    get_embedding_service,
    get_vector_store,
)

class RetrievalService:
    """
    Retrieves the most relevant chunks for a query.
    """

    def __init__(self):
        self.embedding = get_embedding_service()
        self.store = get_vector_store()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_embedding = self.embedding.embed(
            [query]
        )[0]

        results = self.store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        return results