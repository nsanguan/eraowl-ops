from app.modules.admin.services.admin import AdminService
from app.modules.admin.services.crud import UserService, RoleService, PrivilegeService
from app.modules.admin.services.generic import AdminGenericService

__all__ = [
    "AdminService",
    "UserService",
    "RoleService",
    "PrivilegeService",
    "AdminGenericService",
]
