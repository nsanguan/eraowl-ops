from app.core.exceptions import AppError


class ARError(AppError):
    def __init__(self, message: str = "ar error"):
        super().__init__(message)
