from datetime import UTC, datetime

from app.core.logging import logger
from app.embeddings.bge_m3_embedding import BGEM3Embedding
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.services.storage_service import StorageService
from app.dependencies.container import (
    get_embedding_service,
    get_storage_service,
)


class EmbeddingStage(BaseStage):
    """
    Generates embeddings for semantic chunks.
    """

    def __init__(self):
        self.embedding_model = get_embedding_service()
        self.storage = get_storage_service()

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info("Embedding stage started.")

        texts = [
            chunk.content
            for chunk in context.chunks
        ]

        embeddings = self.embedding_model.embed(
            texts
        )

        context.embeddings = embeddings

        self.storage.save_embeddings(
            embeddings,
            context.workspace,
        )

        context.manifest.embedding.completed = True
        context.manifest.embedding.timestamp = datetime.now(UTC)
        context.manifest.embedding.version = "bge-m3"

        self.storage.update_manifest(
            context.manifest,
            context.workspace,
        )

        logger.success(
            f"Generated {len(embeddings)} embeddings."
        )