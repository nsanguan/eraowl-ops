from app.core.exceptions import AppError


class EAMError(AppError):
    def __init__(self, message: str = "eam error"):
        super().__init__(message)
