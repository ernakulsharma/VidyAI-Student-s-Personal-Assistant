from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from app.core.logging import logger
from app.models.document_status import DocumentStatus
from app.schemas.document import DocumentMetadata
from app.services.storage_service import StorageService
from app.utils.hash import calculate_sha256
from app.schemas.manifest import (
    DocumentManifest,
)
from app.ingestion.ingestion_pipeline import IngestionPipeline
from app.ingestion.pipeline_context import PipelineContext
from app.services.indexing_service import IndexingService
from app.dependencies.container import get_storage_service
from app.database.repositories.document_repository import DocumentRepository
from app.database.session import SessionLocal
from app.application.workspace_service import WorkspaceService

class DocumentService:
    """
    Handles document registration and metadata creation.
    """

    def __init__(self):
        self.storage = get_storage_service()
        self.pipeline = IngestionPipeline()
        self.indexing = IndexingService()
        self.workspace_service = WorkspaceService()

        # Database
        self.db = SessionLocal()
        self.document_repository = DocumentRepository(
            self.db
        )

    def register_document(
        self,
        uploaded_file: Path,
        original_filename: str,
        content_type: str,
    ) -> DocumentMetadata:

        logger.info(
            f"Starting document registration: {original_filename}"
        )

        document_id = uuid4()

        workspace, stored_file, sha256 = self._store_document(
            document_id,
            uploaded_file,
        )

        metadata = self._create_metadata(
            document_id=document_id,
            original_filename=original_filename,
            content_type=content_type,
            stored_file=stored_file,
            sha256=sha256,
        )

        self._persist_document(
            metadata,
        )

        manifest = self._create_manifest(
            document_id,
        )

        context = self._build_pipeline_context(
            document_id,
            workspace,
            stored_file,
            metadata,
            manifest,
        )

        self._run_pipeline(
            context,
        )

        logger.success(
            f"Document registration completed: {document_id}"
        )

        return metadata
    
    def _store_document(
        self,
        document_id,
        uploaded_file,
    ):

        workspace = self.storage.create_workspace(
            document_id,
        )

        logger.info(
            f"Workspace created: {workspace}"
        )

        stored_file = self.storage.save_original_file(
            uploaded_file,
            workspace,
        )

        logger.info(
            f"Original file stored: {stored_file.name}"
        )

        sha256 = calculate_sha256(
            stored_file,
        )

        logger.info(
            f"SHA256: {sha256}"
        )

        return (
            workspace,
            stored_file,
            sha256,
        )
    
    def _create_metadata(
        self,
        document_id,
        original_filename,
        content_type,
        stored_file,
        sha256,
    ):

        metadata = DocumentMetadata(
            document_id=document_id,
            original_filename=original_filename,
            stored_filename=stored_file.name,
            content_type=content_type,
            file_size=stored_file.stat().st_size,
            sha256=sha256,
            uploaded_at=datetime.now(UTC),
            parser="docling",
            status=DocumentStatus.UPLOADED.value,
        )

        return metadata
    
    def _persist_document(
        self,
        metadata,
    ):
        """
        Persist document metadata into PostgreSQL.
        Automatically creates the default workspace
        if it does not already exist.
        """

        # Get or create the default workspace
        workspace = self.workspace_service.get_or_create_default_workspace()

        # Save document in PostgreSQL
        document = self.document_repository.create(

            workspace_id=workspace.id,

            title=metadata.original_filename,

            filename=metadata.stored_filename,

            sha256=metadata.sha256,

            parser=metadata.parser,

            status=metadata.status,

            file_size=metadata.file_size,
        )

        logger.info(
            f"Document persisted to PostgreSQL "
            f"(Workspace: {workspace.name}, "
            f"Document ID: {document.public_id})"
        )

        return document

    def _create_manifest(
        self,
        document_id,
    ):

        manifest = DocumentManifest(
            document_id=document_id,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
            parser="docling",
        )

        return manifest
    
    def _build_pipeline_context(
        self,
        document_id,
        workspace,
        stored_file,
        metadata,
        manifest,
    ):

        self.storage.save_metadata(
            metadata,
            workspace,
        )

        self.storage.save_manifest(
            manifest,
            workspace,
        )

        return PipelineContext(
            document_id=document_id,
            workspace=workspace,
            document_path=stored_file,
            metadata=metadata,
            manifest=manifest,
        )
    
    def _run_pipeline(
        self,
        context,
    ):

        self.pipeline.process(
            context,
        )

        self.indexing.index_document(
            context,
        )