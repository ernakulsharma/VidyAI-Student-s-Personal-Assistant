from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProcessingStage(BaseModel):
    completed: bool = False
    timestamp: datetime | None = None
    version: str | None = None


class DocumentManifest(BaseModel):
    document_id: UUID

    created_at: datetime

    updated_at: datetime

    parser: str = "docling"

    parser_version: str | None = None

    embedding_model: str | None = None

    chunking_strategy: str | None = None

    validation: ProcessingStage = ProcessingStage()

    parsing: ProcessingStage = ProcessingStage()

    metadata: ProcessingStage = ProcessingStage()

    chunking: ProcessingStage = ProcessingStage()

    embedding: ProcessingStage = ProcessingStage()

    chunk_count: int = 0

    embedding: ProcessingStage = ProcessingStage()

    indexing: ProcessingStage = ProcessingStage()

    vector_store: ProcessingStage = ProcessingStage()