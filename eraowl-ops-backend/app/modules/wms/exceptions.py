from app.core.exceptions import AppError


class WMSError(AppError):
    def __init__(self, message: str = "wms error"):
        super().__init__(message)
