from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService
from app.modules.sup.models import PortalUser, RfqResponse, ShipmentAdvice


class PortalUserService(BaseCRUDService[PortalUser]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PortalUser)


class RfqResponseService(BaseCRUDService[RfqResponse]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RfqResponse)


class ShipmentAdviceService(BaseCRUDService[ShipmentAdvice]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentAdvice)
