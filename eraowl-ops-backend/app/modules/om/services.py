from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.om.models import AiAgentLogs
from app.modules.om.models import AiDecisions
from app.modules.om.models import AiWorkflowState
from app.modules.om.models import CustomerAttributes
from app.modules.om.models import ImportErrorLog
from app.modules.om.models import LineTypes
from app.modules.om.models import OmHeaders
from app.modules.om.models import OmLines
from app.modules.om.models import OmShipments
from app.modules.om.models import OrderImportInterface
from app.modules.om.models import OrderTypes
from app.modules.om.models import ShipmentTracking
from app.modules.om.models import WmsCallbacks
from app.modules.om.models import WmsTaskQueue
from app.modules.om.models import WorkflowAssignments
from app.modules.om.models import WorkflowDefinitions
from app.modules.om.models import WorkflowTasks

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class CustomerAttributesService(BaseCRUDService[CustomerAttributes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CustomerAttributes)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class LineTypesService(BaseCRUDService[LineTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LineTypes)

class OmHeadersService(BaseCRUDService[OmHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, OmHeaders)

class OmLinesService(BaseCRUDService[OmLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, OmLines)

class OmShipmentsService(BaseCRUDService[OmShipments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, OmShipments)

class OrderImportInterfaceService(BaseCRUDService[OrderImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, OrderImportInterface)

class OrderTypesService(BaseCRUDService[OrderTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, OrderTypes)

class ShipmentTrackingService(BaseCRUDService[ShipmentTracking]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentTracking)

class WmsCallbacksService(BaseCRUDService[WmsCallbacks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WmsCallbacks)

class WmsTaskQueueService(BaseCRUDService[WmsTaskQueue]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WmsTaskQueue)

class WorkflowAssignmentsService(BaseCRUDService[WorkflowAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowAssignments)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
