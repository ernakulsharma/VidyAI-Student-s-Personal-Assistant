from pathlib import Path
from uuid import UUID

from app.schemas.document import DocumentMetadata
from app.schemas.manifest import DocumentManifest
from app.schemas.chunk import Chunk


class PipelineContext:
    """
    Shared context passed through all ingestion stages.
    """

    def __init__(
        self,
        document_id: UUID,
        workspace: Path,
        document_path: Path,
        metadata: DocumentMetadata,
        manifest: DocumentManifest,
    ):
        # Core document information
        self.document_id = document_id
        self.workspace = workspace
        self.document_path = document_path

        # Persistent information
        self.metadata = metadata
        self.manifest = manifest

        # Filled during processing
        self.parsed_document = None
        self.markdown = None

        # Document Intelligence Engine

        self.document_tree = None

        self.sections = []

        self.relationships = []

        self.keywords = []

        self.entities = []

        self.document_info = None

        self.chunks: list[Chunk] = []

        self.embeddings: list[list[float]] = []

        self.index_id: str | None = None

        self.errors: list[str] = []