from app.shared.module_base.crud import BaseCRUDService
from app.modules.admin.models import User, Role, Privilege
from sqlalchemy.ext.asyncio import AsyncSession


class UserService(BaseCRUDService[User]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, User)


class RoleService(BaseCRUDService[Role]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Role)


class PrivilegeService(BaseCRUDService[Privilege]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Privilege)
