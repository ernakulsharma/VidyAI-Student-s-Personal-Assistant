from pathlib import Path

from app.core.logging import logger
from app.services.document_service import DocumentService


class UploadService:
    """
    Coordinates the complete upload workflow.
    """

    def __init__(self):

        self.document_service = DocumentService()

    def upload_document(
        self,
        uploaded_file: Path,
        original_filename: str,
        content_type: str,
    ):

        logger.info(
            f"Upload started: {original_filename}"
        )

        metadata = self.document_service.register_document(
            uploaded_file=uploaded_file,
            original_filename=original_filename,
            content_type=content_type,
        )

        logger.success(
            "Upload completed successfully."
        )

        return metadata