from app.core.exceptions import AppError


class APError(AppError):
    def __init__(self, message: str = "ap error"):
        super().__init__(message)
