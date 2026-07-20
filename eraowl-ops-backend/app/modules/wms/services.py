from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService
from app.modules.wms.models import (
    CycleCount,
    PackingTask,
    PickingTask,
    PutawayTask,
    ReceivingSchedule,
    ShipmentHeader,
    WarehouseZone,
)


class CycleCountService(BaseCRUDService[CycleCount]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CycleCount)


class PackingTaskService(BaseCRUDService[PackingTask]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PackingTask)


class PickingTaskService(BaseCRUDService[PickingTask]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PickingTask)


class PutawayTaskService(BaseCRUDService[PutawayTask]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PutawayTask)


class ReceivingScheduleService(BaseCRUDService[ReceivingSchedule]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ReceivingSchedule)


class ShipmentHeaderService(BaseCRUDService[ShipmentHeader]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentHeader)


class WarehouseZoneService(BaseCRUDService[WarehouseZone]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WarehouseZone)
