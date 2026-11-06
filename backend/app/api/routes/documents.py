import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.application.upload_service import UploadService

router = APIRouter(prefix="/documents", tags=["Documents"])
service = UploadService()
MAX_UPLOAD_BYTES = 25 * 1024 * 1024


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload and index a PDF for academic question answering."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Uploaded file has no filename.")

    if Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(status_code=415, detail="Only PDF documents are supported.")

    content = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="PDF must be 25 MB or smaller.")

    if not content.startswith(b"%PDF-"):
        raise HTTPException(status_code=415, detail="The uploaded file is not a valid PDF.")

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(content)
            temp_path = Path(temp_file.name)

        metadata = service.upload_document(
            uploaded_file=temp_path,
            original_filename=file.filename,
            content_type="application/pdf",
        )

        return {
            "message": "Document uploaded and indexed successfully.",
            "document_id": str(metadata.document_id),
            "status": metadata.status,
            "filename": metadata.original_filename,
        }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Document processing failed. Check backend logs.") from exc
    finally:
        if temp_path and temp_path.exists():
            temp_path.unlink()
        await file.close()
