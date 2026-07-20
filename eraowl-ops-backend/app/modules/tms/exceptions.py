from app.core.exceptions import AppError


class TMSError(AppError):
    def __init__(self, message: str = "tms error"):
        super().__init__(message)
