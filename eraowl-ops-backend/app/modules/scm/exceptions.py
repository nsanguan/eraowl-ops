from app.core.exceptions import AppError


class SCMError(AppError):
    def __init__(self, message: str = "scm error"):
        super().__init__(message)
