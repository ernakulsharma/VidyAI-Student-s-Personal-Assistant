from datetime import UTC, datetime

from app.core.logging import logger
from app.ingestion.metadata.extractor import MetadataExtractor
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.services.storage_service import StorageService


class MetadataStage(BaseStage):
    """
    Extracts metadata from parsed documents.
    """

    def __init__(self):

        self.extractor = MetadataExtractor()

        self.storage = StorageService()

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info("Metadata extraction started.")

        metadata = self.extractor.extract(
            context.parsed_document,
            context.document_path,
        )

        context.extracted_metadata = metadata

        context.manifest.updated_at = datetime.now(UTC)

        context.storage_metadata = metadata

        self.storage.save_json(
            metadata.model_dump(),
            context.workspace
              / "parsed"
              / "extracted_metadata.json"
        )

        context.manifest.metadata.completed = True

        context.manifest.metadata.timestamp = datetime.now(UTC)

        context.manifest.metadata.version = "1.0"

        self.storage.update_manifest(
            context.manifest,
            context.workspace,
        )

        logger.success("Metadata extraction completed.")