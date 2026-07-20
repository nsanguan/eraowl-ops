from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService
from app.modules.exp.models import ClaimHeader, ClaimLine, ExpCategory


class ClaimHeaderService(BaseCRUDService[ClaimHeader]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ClaimHeader)


class ClaimLineService(BaseCRUDService[ClaimLine]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ClaimLine)


class ExpCategoryService(BaseCRUDService[ExpCategory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExpCategory)
