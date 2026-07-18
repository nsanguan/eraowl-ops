from app.core.exceptions import NotFoundError, ConflictError


class UserNotFoundError(NotFoundError):
    def __init__(self):
        super().__init__(entity="User")


class RoleNotFoundError(NotFoundError):
    def __init__(self):
        super().__init__(entity="Role")


class PrivilegeNotFoundError(NotFoundError):
    def __init__(self):
        super().__init__(entity="Privilege")


class UserAlreadyExistsError(ConflictError):
    def __init__(self):
        super().__init__(message="User already exists")


class RoleAlreadyExistsError(ConflictError):
    def __init__(self):
        super().__init__(message="Role already exists")
