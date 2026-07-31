from app.exceptions.base import AppException


class ParsingException(AppException):

    def __init__(self, message: str):

        super().__init__(
            status_code=422,
            error_code="PARSING_FAILED",
            message=message,
        )