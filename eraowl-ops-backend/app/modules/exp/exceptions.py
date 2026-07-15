from app.core.exceptions import AppError


class EXPError(AppError):
    def __init__(self, message: str = "exp error"):
        super().__init__(message)
