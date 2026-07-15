from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.module_base.crud import BaseCRUDService
from app.modules.your_module.models import YourEntity


class YourEntityService(BaseCRUDService[YourEntity]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, YourEntity)
