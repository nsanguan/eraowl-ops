from app.core.exceptions import AppError


class FAError(AppError):
    def __init__(self, message: str = "fa error"):
        super().__init__(message)
