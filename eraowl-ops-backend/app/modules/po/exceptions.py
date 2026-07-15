from app.core.exceptions import NotFoundError, ConflictError, AppError


class PoNotFoundError(NotFoundError):
    def __init__(self, entity: str = "PO"):
        super().__init__(entity=entity)


class PoNumberAlreadyExistsError(ConflictError):
    def __init__(self):
        super().__init__(message="PO number already exists")


class PoValidationError(AppError):
    def __init__(self, message: str = "PO validation failed"):
        super().__init__(status_code=422, error_code="PO_VALIDATION_ERROR", message=message)
