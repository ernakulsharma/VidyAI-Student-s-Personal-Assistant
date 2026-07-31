from app.core.logging import logger
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.chunking_stage import ChunkingStage
from app.ingestion.stages.metadata_stage import MetadataStage
from app.ingestion.stages.parsing_stage import ParsingStage
from app.ingestion.stages.validation_stage import ValidationStage
from app.ingestion.stages.embedding_stage import EmbeddingStage
from app.ingestion.stages.vector_store_stage import VectorStoreStage


class IngestionPipeline:
    """
    Executes all ingestion stages.
    """

    def __init__(self):

        self.stages = [

        ValidationStage(),

        ParsingStage(),

        MetadataStage(),

        ChunkingStage(),

        EmbeddingStage(),

        VectorStoreStage(),

    ]

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info(
            "Pipeline execution started."
        )

        for stage in self.stages:

            try:

                stage.process(context)

            except Exception as e:

                logger.exception(
                    f"{stage.__class__.__name__} failed."
                )

                context.errors.append(str(e))

                raise

        logger.success(
            "Pipeline execution completed."
        )