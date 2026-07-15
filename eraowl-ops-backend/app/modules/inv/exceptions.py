from app.core.exceptions import AppError


class INVError(AppError):
    def __init__(self, message: str = "inv error"):
        super().__init__(message)
