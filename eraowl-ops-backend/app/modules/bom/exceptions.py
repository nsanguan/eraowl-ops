from app.core.exceptions import AppError, NotFoundError


class BomNotFoundError(NotFoundError):
    def __init__(self, entity: str = "BOM resource"):
        super().__init__(entity=entity)


class BomCircularReferenceError(AppError):
    def __init__(self, item_id: str, ancestor_id: str):
        super().__init__(
            status_code=422,
            error_code="CIRCULAR_REFERENCE",
            message=f"Item {item_id} would create circular reference with ancestor {ancestor_id}",
        )
