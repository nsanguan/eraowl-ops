from app.core.exceptions import AppError


class COREError(AppError):
    def __init__(self, message: str = "core error"):
        super().__init__(message)
