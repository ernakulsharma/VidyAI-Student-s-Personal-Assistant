from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UploadDocumentResponse(BaseModel):
    document_id: UUID

    filename: str

    status: str

    uploaded_at: datetime

    size: int

    sha256: str