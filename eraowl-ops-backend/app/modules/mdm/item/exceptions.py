from app.core.exceptions import NotFoundError


class ItemNotFoundError(NotFoundError):
    def __init__(self, entity: str = "Item resource"):
        super().__init__(entity=entity)
