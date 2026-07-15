from app.core.exceptions import NotFoundError


class PartyNotFoundError(NotFoundError):
    def __init__(self, entity: str = "Party resource"):
        super().__init__(entity=entity)
