from app.core.exceptions import AppError


class PRODError(AppError):
    def __init__(self, message: str = "prod error"):
        super().__init__(message)
