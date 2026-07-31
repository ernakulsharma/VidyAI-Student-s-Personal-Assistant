from app.core.logging import logger
from app.vectorstore.chroma_store import ChromaStore
from app.dependencies.container import get_vector_store

class IndexingService:
    """
    Pushes document chunks into ChromaDB.
    """

    def __init__(self):
        self.store = get_vector_store()

    def index_document(
        self,
        context,
    ):

        logger.info("Indexing document...")

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk, embedding in zip(
            context.chunks,
            context.embeddings,
        ):

            ids.append(
                f"{context.document_id}_{chunk.chunk_id}"
            )

            documents.append(
                chunk.content
            )

            embeddings.append(
                embedding
            )

            metadatas.append(
                {
                    "document_id": str(context.document_id),
                    "chunk_id": chunk.chunk_id,
                    "heading": chunk.heading or "",
                }
            )

        self.store.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.success("Indexing completed.")