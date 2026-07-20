from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.ar.models import AccountingEntries
from app.modules.ar.models import Adjustments
from app.modules.ar.models import AgingSnapshots
from app.modules.ar.models import AiAgentLogs
from app.modules.ar.models import AiDecisions
from app.modules.ar.models import AiWorkflowState
from app.modules.ar.models import ArCustomerLocations
from app.modules.ar.models import ArCustomerSites
from app.modules.ar.models import ArCustomers
from app.modules.ar.models import ArInvoiceLines
from app.modules.ar.models import ArInvoices
from app.modules.ar.models import BankAccounts
from app.modules.ar.models import CashReceipts
from app.modules.ar.models import CollectionTasks
from app.modules.ar.models import CreditHolds
from app.modules.ar.models import CreditProfiles
from app.modules.ar.models import CustSiteUses
from app.modules.ar.models import CustomerDeposits
from app.modules.ar.models import DepositApplications
from app.modules.ar.models import DunningHistory
from app.modules.ar.models import DunningPlans
from app.modules.ar.models import ImportErrorLog
from app.modules.ar.models import ImportInterface
from app.modules.ar.models import InvoiceDistributions
from app.modules.ar.models import PaymentSchedules
from app.modules.ar.models import PeriodStatus
from app.modules.ar.models import ReceiptApplications
from app.modules.ar.models import ReceiptBatches
from app.modules.ar.models import RevenueSchedules
from app.modules.ar.models import TaxCodes
from app.modules.ar.models import TransactionTypes
from app.modules.ar.models import WorkflowDefinitions
from app.modules.ar.models import WorkflowTasks

class AccountingEntriesService(BaseCRUDService[AccountingEntries]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccountingEntries)

class AdjustmentsService(BaseCRUDService[Adjustments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Adjustments)

class AgingSnapshotsService(BaseCRUDService[AgingSnapshots]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AgingSnapshots)

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class ArCustomerLocationsService(BaseCRUDService[ArCustomerLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ArCustomerLocations)

class ArCustomerSitesService(BaseCRUDService[ArCustomerSites]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ArCustomerSites)

class ArCustomersService(BaseCRUDService[ArCustomers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ArCustomers)

class ArInvoiceLinesService(BaseCRUDService[ArInvoiceLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ArInvoiceLines)

class ArInvoicesService(BaseCRUDService[ArInvoices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ArInvoices)

class BankAccountsService(BaseCRUDService[BankAccounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BankAccounts)

class CashReceiptsService(BaseCRUDService[CashReceipts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CashReceipts)

class CollectionTasksService(BaseCRUDService[CollectionTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CollectionTasks)

class CreditHoldsService(BaseCRUDService[CreditHolds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CreditHolds)

class CreditProfilesService(BaseCRUDService[CreditProfiles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CreditProfiles)

class CustSiteUsesService(BaseCRUDService[CustSiteUses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CustSiteUses)

class CustomerDepositsService(BaseCRUDService[CustomerDeposits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CustomerDeposits)

class DepositApplicationsService(BaseCRUDService[DepositApplications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DepositApplications)

class DunningHistoryService(BaseCRUDService[DunningHistory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DunningHistory)

class DunningPlansService(BaseCRUDService[DunningPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DunningPlans)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class ImportInterfaceService(BaseCRUDService[ImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportInterface)

class InvoiceDistributionsService(BaseCRUDService[InvoiceDistributions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvoiceDistributions)

class PaymentSchedulesService(BaseCRUDService[PaymentSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PaymentSchedules)

class PeriodStatusService(BaseCRUDService[PeriodStatus]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PeriodStatus)

class ReceiptApplicationsService(BaseCRUDService[ReceiptApplications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ReceiptApplications)

class ReceiptBatchesService(BaseCRUDService[ReceiptBatches]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ReceiptBatches)

class RevenueSchedulesService(BaseCRUDService[RevenueSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RevenueSchedules)

class TaxCodesService(BaseCRUDService[TaxCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCodes)

class TransactionTypesService(BaseCRUDService[TransactionTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TransactionTypes)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
