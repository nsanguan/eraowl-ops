from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.gl.models import AccountCombinations
from app.modules.gl.models import AccountingBooks
from app.modules.gl.models import AiAgentLogs
from app.modules.gl.models import AiDecisions
from app.modules.gl.models import AiWorkflowCheckpoints
from app.modules.gl.models import AiWorkflowState
from app.modules.gl.models import Balances
from app.modules.gl.models import BudgetBalances
from app.modules.gl.models import BudgetVersions
from app.modules.gl.models import ChartOfAccounts
from app.modules.gl.models import ExchangeRates
from app.modules.gl.models import FiscalPeriods
from app.modules.gl.models import ImportErrorLog
from app.modules.gl.models import ImportInterface
from app.modules.gl.models import JournalCategories
from app.modules.gl.models import JournalHeaders
from app.modules.gl.models import JournalLines
from app.modules.gl.models import JournalSources
from app.modules.gl.models import Ledgers
from app.modules.gl.models import PeriodStatuses
from app.modules.gl.models import WorkflowDefinitions
from app.modules.gl.models import WorkflowTasks

class AccountCombinationsService(BaseCRUDService[AccountCombinations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccountCombinations)

class AccountingBooksService(BaseCRUDService[AccountingBooks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccountingBooks)

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowCheckpointsService(BaseCRUDService[AiWorkflowCheckpoints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowCheckpoints)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class BalancesService(BaseCRUDService[Balances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Balances)

class BudgetBalancesService(BaseCRUDService[BudgetBalances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BudgetBalances)

class BudgetVersionsService(BaseCRUDService[BudgetVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BudgetVersions)

class ChartOfAccountsService(BaseCRUDService[ChartOfAccounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ChartOfAccounts)

class ExchangeRatesService(BaseCRUDService[ExchangeRates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExchangeRates)

class FiscalPeriodsService(BaseCRUDService[FiscalPeriods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FiscalPeriods)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class ImportInterfaceService(BaseCRUDService[ImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportInterface)

class JournalCategoriesService(BaseCRUDService[JournalCategories]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, JournalCategories)

class JournalHeadersService(BaseCRUDService[JournalHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, JournalHeaders)

class JournalLinesService(BaseCRUDService[JournalLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, JournalLines)

class JournalSourcesService(BaseCRUDService[JournalSources]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, JournalSources)

class LedgersService(BaseCRUDService[Ledgers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Ledgers)

class PeriodStatusesService(BaseCRUDService[PeriodStatuses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PeriodStatuses)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
