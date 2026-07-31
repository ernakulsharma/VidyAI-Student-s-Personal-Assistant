from datetime import UTC, datetime

from app.core.logging import logger
from app.ingestion.chunking.academic_chunker import AcademicChunker
from app.ingestion.chunking.graph_builder import GraphBuilder
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.services.storage_service import StorageService


class ChunkingStage(BaseStage):
    """
    Splits parsed markdown into semantic chunks.
    """

    def __init__(self):
        self.chunker = AcademicChunker()
        self.graph_builder = GraphBuilder()
        self.storage = StorageService()

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info("Chunking stage started.")

        chunks = self.chunker.chunk(
            context.markdown,
        )

        context.chunks = chunks

        self.storage.save_chunks(
            [chunk.model_dump() for chunk in chunks],
            context.workspace,
        )

        graph = self.graph_builder.build(
            chunks,
        )

        self.storage.save_chunk_graph(
            graph,
            context.workspace,
        )

        context.manifest.chunking.completed = True
        context.manifest.chunking.timestamp = datetime.now(UTC)
        context.manifest.chunking.version = "academic-v1"
        context.manifest.chunk_count = len(chunks)

        self.storage.update_manifest(
            context.manifest,
            context.workspace,
        )

        logger.success(
            f"Chunking completed. Generated {len(chunks)} chunks."
        )