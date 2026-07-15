from app.core.exceptions import AppError


class OMError(AppError):
    def __init__(self, message: str = "om error"):
        super().__init__(message)
