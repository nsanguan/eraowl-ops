from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.prd.models import AiAgentLogs
from app.modules.prd.models import AiDecisions
from app.modules.prd.models import AiWorkflowState
from app.modules.prd.models import BomComponentsExt
from app.modules.prd.models import EngineeringChangeOrders
from app.modules.prd.models import ImportErrorLog
from app.modules.prd.models import ImportInterface
from app.modules.prd.models import MpsEntries
from app.modules.prd.models import MrpRecommendations
from app.modules.prd.models import ProdWorkOrders
from app.modules.prd.models import ProductionCalendar
from app.modules.prd.models import Resources
from app.modules.prd.models import RoutingHeaders
from app.modules.prd.models import RoutingOperations
from app.modules.prd.models import WipMovements
from app.modules.prd.models import WorkCenters
from app.modules.prd.models import WorkOrderOperations
from app.modules.prd.models import WorkOrderRequirements
from app.modules.prd.models import WorkflowDefinitions
from app.modules.prd.models import WorkflowTasks

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class BomComponentsExtService(BaseCRUDService[BomComponentsExt]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BomComponentsExt)

class EngineeringChangeOrdersService(BaseCRUDService[EngineeringChangeOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EngineeringChangeOrders)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class ImportInterfaceService(BaseCRUDService[ImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportInterface)

class MpsEntriesService(BaseCRUDService[MpsEntries]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MpsEntries)

class MrpRecommendationsService(BaseCRUDService[MrpRecommendations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpRecommendations)

class ProdWorkOrdersService(BaseCRUDService[ProdWorkOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ProdWorkOrders)

class ProductionCalendarService(BaseCRUDService[ProductionCalendar]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ProductionCalendar)

class ResourcesService(BaseCRUDService[Resources]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Resources)

class RoutingHeadersService(BaseCRUDService[RoutingHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RoutingHeaders)

class RoutingOperationsService(BaseCRUDService[RoutingOperations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RoutingOperations)

class WipMovementsService(BaseCRUDService[WipMovements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WipMovements)

class WorkCentersService(BaseCRUDService[WorkCenters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkCenters)

class WorkOrderOperationsService(BaseCRUDService[WorkOrderOperations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkOrderOperations)

class WorkOrderRequirementsService(BaseCRUDService[WorkOrderRequirements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkOrderRequirements)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
