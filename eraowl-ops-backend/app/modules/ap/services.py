from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.ap.models import AccountingEntries
from app.modules.ap.models import AgingSnapshots
from app.modules.ap.models import AiAgentLogs
from app.modules.ap.models import AiDecisions
from app.modules.ap.models import AiWorkflowState
from app.modules.ap.models import ApInvoiceLines
from app.modules.ap.models import ApInvoices
from app.modules.ap.models import ApSupplierLocations
from app.modules.ap.models import ApSupplierSites
from app.modules.ap.models import ApSuppliers
from app.modules.ap.models import BankAccounts
from app.modules.ap.models import BankStatementLines
from app.modules.ap.models import BankStatements
from app.modules.ap.models import DiscountTracking
from app.modules.ap.models import ExpenseReportLines
from app.modules.ap.models import ExpenseReports
from app.modules.ap.models import GlMappingRules
from app.modules.ap.models import ImportErrorLog
from app.modules.ap.models import ImportInterface
from app.modules.ap.models import InvoiceAttachments
from app.modules.ap.models import InvoiceDistributions
from app.modules.ap.models import InvoiceHolds
from app.modules.ap.models import MatchExceptions
from app.modules.ap.models import MatchingRules
from app.modules.ap.models import PaymentBatches
from app.modules.ap.models import PaymentInstructions
from app.modules.ap.models import PaymentMethods
from app.modules.ap.models import PaymentTerms
from app.modules.ap.models import PeriodStatus
from app.modules.ap.models import PrepaymentApplications
from app.modules.ap.models import Prepayments
from app.modules.ap.models import TaxCodes
from app.modules.ap.models import WithholdingTax
from app.modules.ap.models import WorkflowDefinitions
from app.modules.ap.models import WorkflowTasks

class AccountingEntriesService(BaseCRUDService[AccountingEntries]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccountingEntries)

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

class ApInvoiceLinesService(BaseCRUDService[ApInvoiceLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApInvoiceLines)

class ApInvoicesService(BaseCRUDService[ApInvoices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApInvoices)

class ApSupplierLocationsService(BaseCRUDService[ApSupplierLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApSupplierLocations)

class ApSupplierSitesService(BaseCRUDService[ApSupplierSites]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApSupplierSites)

class ApSuppliersService(BaseCRUDService[ApSuppliers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ApSuppliers)

class BankAccountsService(BaseCRUDService[BankAccounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BankAccounts)

class BankStatementLinesService(BaseCRUDService[BankStatementLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BankStatementLines)

class BankStatementsService(BaseCRUDService[BankStatements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BankStatements)

class DiscountTrackingService(BaseCRUDService[DiscountTracking]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DiscountTracking)

class ExpenseReportLinesService(BaseCRUDService[ExpenseReportLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExpenseReportLines)

class ExpenseReportsService(BaseCRUDService[ExpenseReports]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExpenseReports)

class GlMappingRulesService(BaseCRUDService[GlMappingRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, GlMappingRules)

class ImportErrorLogService(BaseCRUDService[ImportErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportErrorLog)

class ImportInterfaceService(BaseCRUDService[ImportInterface]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ImportInterface)

class InvoiceAttachmentsService(BaseCRUDService[InvoiceAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvoiceAttachments)

class InvoiceDistributionsService(BaseCRUDService[InvoiceDistributions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvoiceDistributions)

class InvoiceHoldsService(BaseCRUDService[InvoiceHolds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InvoiceHolds)

class MatchExceptionsService(BaseCRUDService[MatchExceptions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MatchExceptions)

class MatchingRulesService(BaseCRUDService[MatchingRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MatchingRules)

class PaymentBatchesService(BaseCRUDService[PaymentBatches]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PaymentBatches)

class PaymentInstructionsService(BaseCRUDService[PaymentInstructions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PaymentInstructions)

class PaymentMethodsService(BaseCRUDService[PaymentMethods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PaymentMethods)

class PaymentTermsService(BaseCRUDService[PaymentTerms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PaymentTerms)

class PeriodStatusService(BaseCRUDService[PeriodStatus]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PeriodStatus)

class PrepaymentApplicationsService(BaseCRUDService[PrepaymentApplications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PrepaymentApplications)

class PrepaymentsService(BaseCRUDService[Prepayments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Prepayments)

class TaxCodesService(BaseCRUDService[TaxCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCodes)

class WithholdingTaxService(BaseCRUDService[WithholdingTax]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WithholdingTax)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)
