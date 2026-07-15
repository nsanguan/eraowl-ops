from app.core.exceptions import NotFoundError, ConflictError


class YourModuleNotFoundError(NotFoundError):
    def __init__(self, entity: str = "YourModule resource"):
        super().__init__(entity=entity)
