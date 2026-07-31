from app.exceptions.base import AppException


class IndexingException(AppException):

    def __init__(self, message: str):

        super().__init__(
            status_code=500,
            error_code="INDEXING_FAILED",
            message=message,
        )