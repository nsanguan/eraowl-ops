from app.core.exceptions import AppError


class PRDError(AppError):
    def __init__(self, message: str = "prd error"):
        super().__init__(message)
