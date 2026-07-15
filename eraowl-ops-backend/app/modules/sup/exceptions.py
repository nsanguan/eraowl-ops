from app.core.exceptions import AppError


class SUPError(AppError):
    def __init__(self, message: str = "sup error"):
        super().__init__(message)
