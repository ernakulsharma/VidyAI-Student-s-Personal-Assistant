from datetime import UTC, datetime

from app.core.logging import logger
from app.dependencies.container import get_storage_service, get_vector_store
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage


class VectorStoreStage(BaseStage):
    def __init__(self):
        self.store = get_vector_store()
        self.storage = get_storage_service()

    def process(self, context: PipelineContext):
        logger.info("Storing vectors in ChromaDB...")

        ids = [
            f"{context.document_id}_{chunk.chunk_id}"
            for chunk in context.chunks
        ]
        documents = [chunk.content for chunk in context.chunks]
        metadatas = [
            {
                "document_id": str(context.document_id),
                "filename": context.metadata.original_filename,
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

        now = datetime.now(UTC)
        context.manifest.vector_store.completed = True
        context.manifest.vector_store.timestamp = now
        context.manifest.vector_store.version = "chromadb"
        context.manifest.indexing.completed = True
        context.manifest.indexing.timestamp = now
        context.manifest.indexing.version = "chromadb"

        self.storage.update_manifest(context.manifest, context.workspace)
        logger.success("Stored vectors successfully.")
