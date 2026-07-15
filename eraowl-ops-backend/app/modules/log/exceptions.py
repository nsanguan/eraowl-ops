from app.core.exceptions import AppError


class LOGError(AppError):
    def __init__(self, message: str = "log error"):
        super().__init__(message)
