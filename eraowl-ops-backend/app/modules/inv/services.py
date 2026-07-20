from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.inv.models import AbcAssignments
from app.modules.inv.models import AbcClasses
from app.modules.inv.models import AiAgentLogs
from app.modules.inv.models import AiDecisions
from app.modules.inv.models import AiWorkflowState
from app.modules.inv.models import CostTypes
from app.modules.inv.models import CycleCountSchedules
from app.modules.inv.models import ImportErrorLog
from app.modules.inv.models import ImportInterface
from app.modules.inv.models import InspectionPlans
from app.modules.inv.models import InspectionResults
from app.modules.inv.models import InvCycleCounts
from app.modules.inv.models import InvOnhandBalances
from app.modules.inv.models import InvReservations
from app.modules.inv.models import InvTransactionTypes
from app.modules.inv.models import ItemAttributes
from app.modules.inv.models import ItemCosts
from app.modules.inv.models import LotGenealogy
from app.modules.inv.models import LotMaster
from app.modules.inv.models import LotOnhand
from app.modules.inv.models import LpnContents
from app.modules.inv.models import LpnMaster
from app.modules.inv.models import MaterialTransactions
from app.modules.inv.models import MoveOrderHeaders
from app.modules.inv.models import MoveOrderLines
from app.modules.inv.models import PhysicalInventoryHeaders
from app.modules.inv.models import PhysicalInventoryLines
from app.modules.inv.models import ReplenishmentRules
from app.modules.inv.models import Serial
from app.modules.inv.models import SerialGenealogy
from app.modules.inv.models import TransferOrderLines
from app.modules.inv.models import TransferOrders
from app.modules.inv.models import WorkflowDefinitions
from app.modules.inv.models import WorkflowTasks

class AbcAssignmentsService(BaseCRUDService[AbcAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AbcAssignments)

class AbcClassesService(BaseCRUDService[AbcClasses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AbcClasses)

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class CostTypesService(BaseCRUDService[CostTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CostTypes)

class CycleCountSchedulesService(BaseCRUDService[CycleCountSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CycleCountSchedules)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class ImportInterfaceService(BaseCRUDService[ImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportInterface)

class InspectionPlansService(BaseCRUDService[InspectionPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionPlans)

class InspectionResultsService(BaseCRUDService[InspectionResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionResults)

class InvCycleCountsService(BaseCRUDService[InvCycleCounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvCycleCounts)

class InvOnhandBalancesService(BaseCRUDService[InvOnhandBalances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvOnhandBalances)

class InvReservationsService(BaseCRUDService[InvReservations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvReservations)

class InvTransactionTypesService(BaseCRUDService[InvTransactionTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvTransactionTypes)

class ItemAttributesService(BaseCRUDService[ItemAttributes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ItemAttributes)

class ItemCostsService(BaseCRUDService[ItemCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ItemCosts)

class LotGenealogyService(BaseCRUDService[LotGenealogy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LotGenealogy)

class LotMasterService(BaseCRUDService[LotMaster]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LotMaster)

class LotOnhandService(BaseCRUDService[LotOnhand]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LotOnhand)

class LpnContentsService(BaseCRUDService[LpnContents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LpnContents)

class LpnMasterService(BaseCRUDService[LpnMaster]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LpnMaster)

class MaterialTransactionsService(BaseCRUDService[MaterialTransactions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MaterialTransactions)

class MoveOrderHeadersService(BaseCRUDService[MoveOrderHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MoveOrderHeaders)

class MoveOrderLinesService(BaseCRUDService[MoveOrderLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MoveOrderLines)

class PhysicalInventoryHeadersService(BaseCRUDService[PhysicalInventoryHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PhysicalInventoryHeaders)

class PhysicalInventoryLinesService(BaseCRUDService[PhysicalInventoryLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PhysicalInventoryLines)

class ReplenishmentRulesService(BaseCRUDService[ReplenishmentRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ReplenishmentRules)

class SerialService(BaseCRUDService[Serial]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Serial)

class SerialGenealogyService(BaseCRUDService[SerialGenealogy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, SerialGenealogy)

class TransferOrderLinesService(BaseCRUDService[TransferOrderLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TransferOrderLines)

class TransferOrdersService(BaseCRUDService[TransferOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TransferOrders)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
