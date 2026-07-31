from datetime import UTC, datetime

from app.core.logging import logger
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.ingestion.validator import DocumentValidator
from app.services.storage_service import StorageService


class ValidationStage(BaseStage):
    """
    Validates uploaded documents before parsing.
    """

    def __init__(self):
        self.validator = DocumentValidator()
        self.storage = StorageService()

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info("Validation stage started.")

        self.validator.validate(
            context.document_path
        )

        context.manifest.validation.completed = True
        context.manifest.validation.timestamp = datetime.now(UTC)
        context.manifest.validation.version = "1.0"

        self.storage.update_manifest(
            context.manifest,
            context.workspace,
        )

        logger.success(
            "Validation completed."
        )