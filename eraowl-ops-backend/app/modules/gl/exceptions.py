from app.core.exceptions import AppError


class GLError(AppError):
    def __init__(self, message: str = "gl error"):
        super().__init__(message)
