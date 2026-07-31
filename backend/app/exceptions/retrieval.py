from app.exceptions.base import AppException


class RetrievalException(AppException):

    def __init__(self, message: str):

        super().__init__(
            status_code=404,
            error_code="NO_CONTEXT_FOUND",
            message=message,
        )