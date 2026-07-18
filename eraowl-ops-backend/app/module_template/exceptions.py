from app.core.exceptions import NotFoundError


class YourModuleNotFoundError(NotFoundError):
    def __init__(self, entity: str = "YourModule resource"):
        super().__init__(entity=entity)
