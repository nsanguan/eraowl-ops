from app.core.exceptions import AppError


class CollabNotFoundError(AppError):
    def __init__(self, entity: str = "Resource"):
        super().__init__(f"{entity} not found", status_code=404)
