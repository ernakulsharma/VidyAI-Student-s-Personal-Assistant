from app.exceptions.base import AppException


class EmbeddingException(AppException):

    def __init__(self, message: str):

        super().__init__(
            status_code=500,
            error_code="EMBEDDING_FAILED",
            message=message,
        )