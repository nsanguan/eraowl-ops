from app.core.exceptions import AppError


class TAXError(AppError):
    def __init__(self, message: str = "tax error"):
        super().__init__(message)
