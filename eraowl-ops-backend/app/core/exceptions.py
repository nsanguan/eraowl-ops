from fastapi import HTTPException, status


class AppError(HTTPException):
    def __init__(
        self,
        status_code: int = 400,
        error_code: str = "UNKNOWN_ERROR",
        message: str = "An error occurred",
        detail: dict | None = None,
    ):
        self.error_code = error_code
        self.detail = detail
        super().__init__(
            status_code=status_code,
            detail={"error_code": error_code, "message": message, "detail": detail or {}},
        )


class UnauthorizedError(AppError):
    def __init__(self, message: str = "Not authenticated"):
        super().__init__(status_code=401, error_code="UNAUTHORIZED", message=message)


class ForbiddenError(AppError):
    def __init__(self, message: str = "Insufficient privileges"):
        super().__init__(status_code=403, error_code="FORBIDDEN", message=message)


class NotFoundError(AppError):
    def __init__(self, entity: str = "Resource"):
        super().__init__(status_code=404, error_code="NOT_FOUND", message=f"{entity} not found")


class ConflictError(AppError):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(status_code=409, error_code="CONFLICT", message=message)


class ValidationError(AppError):
    def __init__(self, message: str = "Validation failed", detail: dict | None = None):
        super().__init__(status_code=422, error_code="VALIDATION_ERROR", message=message, detail=detail)
