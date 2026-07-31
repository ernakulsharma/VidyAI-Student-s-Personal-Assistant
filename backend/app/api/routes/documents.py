import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.document_service import DocumentService
from app.application.upload_service import UploadService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


service = UploadService()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
):
    """
    Upload a document and start the complete ingestion pipeline.
    """

    if file.filename is None:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file has no filename.",
        )

    suffix = Path(file.filename).suffix

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp_file:

        content = await file.read()
        temp_file.write(content)

        temp_path = Path(temp_file.name)

    try:

        metadata = service.upload_document(
            uploaded_file=temp_path,
            original_filename=file.filename,
            content_type=file.content_type or "application/octet-stream",
        )

        return {
            "message": "Document uploaded successfully.",
            "document_id": str(metadata.document_id),
            "status": metadata.status,
            "filename": metadata.original_filename,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if temp_path.exists():
            temp_path.unlink()