from app.exceptions.base import AppException


class DocumentUploadException(AppException):

    def __init__(self, message: str):

        super().__init__(
            status_code=400,
            error_code="DOCUMENT_UPLOAD_FAILED",
            message=message,
        )