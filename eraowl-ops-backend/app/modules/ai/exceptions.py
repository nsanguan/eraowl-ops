from app.core.exceptions import AppError


class AIError(AppError):
    def __init__(self, message: str = "ai error"):
        super().__init__(message)
