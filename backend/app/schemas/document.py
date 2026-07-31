from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class DocumentMetadata(BaseModel):

    document_id: UUID

    original_filename: str

    stored_filename: str

    content_type: str

    file_size: int

    sha256: str

    uploaded_at: datetime

    parser: str

    status: str