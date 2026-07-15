from app.core.exceptions import NotFoundError


class OrgStructureNotFoundError(NotFoundError):
    def __init__(self, entity: str = "Org Structure resource"):
        super().__init__(entity=entity)
