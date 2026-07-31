from datetime import UTC, datetime

from app.core.logging import logger
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.vectorstore.chroma_store import ChromaStore


class VectorStoreStage(BaseStage):

    def __init__(self):
        self.store = ChromaStore()

    def process(
        self,
        context: PipelineContext,
    ):

        logger.info("Storing vectors in ChromaDB...")

        ids = [
            f"{context.document_id}_{chunk.chunk_id}"
            for chunk in context.chunks
        ]

        documents = [
            chunk.content
            for chunk in context.chunks
        ]

        metadatas = [
            {
                "document_id": str(context.document_id),
                "chunk_id": chunk.chunk_id,
                "heading": chunk.heading or "",
            }
            for chunk in context.chunks
        ]

        self.store.add(
            ids=ids,
            documents=documents,
            embeddings=context.embeddings,
            metadatas=metadatas,
        )

        context.manifest.vector_store.completed = True
        context.manifest.vector_store.timestamp = datetime.now(UTC)
        context.manifest.vector_store.version = "chromadb"

        logger.success("Stored vectors successfully.")