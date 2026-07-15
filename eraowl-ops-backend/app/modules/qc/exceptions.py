from app.core.exceptions import AppError


class QCError(AppError):
    def __init__(self, message: str = "qc error"):
        super().__init__(message)
