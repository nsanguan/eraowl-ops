from app.core.exceptions import AppError


class MESError(AppError):
    def __init__(self, message: str = "mes error"):
        super().__init__(message)
