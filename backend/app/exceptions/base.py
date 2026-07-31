from fastapi import HTTPException


class AppException(HTTPException):
    """
    Base exception for VidyAI.
    """

    def __init__(
        self,
        status_code: int,
        error_code: str,
        message: str,
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "error": error_code,
                "message": message,
            },
        )

        self.error_code = error_code
        self.message = message