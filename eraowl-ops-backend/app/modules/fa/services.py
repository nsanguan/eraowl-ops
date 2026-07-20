from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.fa.models import AiAgentLogs
from app.modules.fa.models import AiDecisions
from app.modules.fa.models import AiModelRegistry
from app.modules.fa.models import AiWorkflowState
from app.modules.fa.models import FaAdditions
from app.modules.fa.models import FaAdjustments
from app.modules.fa.models import FaAgentDefinitions
from app.modules.fa.models import FaAlgorithms
from app.modules.fa.models import FaAssetAttachments
from app.modules.fa.models import FaAssetBookAssignments
from app.modules.fa.models import FaAssetCategories
from app.modules.fa.models import FaAssetCategoryHierarchy
from app.modules.fa.models import FaAssetComponents
from app.modules.fa.models import FaAssetCustomAttributes
from app.modules.fa.models import FaAssetPhotos
from app.modules.fa.models import FaAssetStorage
from app.modules.fa.models import FaAssetTags
from app.modules.fa.models import FaAssetTypes
from app.modules.fa.models import FaAssets
from app.modules.fa.models import FaBonusDepreciation
from app.modules.fa.models import FaBookTypes
from app.modules.fa.models import FaCipCosts
from app.modules.fa.models import FaCipProjects
from app.modules.fa.models import FaCountLines
from app.modules.fa.models import FaCountRoutes
from app.modules.fa.models import FaCountSheets
from app.modules.fa.models import FaCountVariances
from app.modules.fa.models import FaCustodians
from app.modules.fa.models import FaDeprnBookPeriods
from app.modules.fa.models import FaDeprnBooks
from app.modules.fa.models import FaDeprnCalculation
from app.modules.fa.models import FaDeprnConventions
from app.modules.fa.models import FaDeprnMethods
from app.modules.fa.models import FaGroupAssetMembers
from app.modules.fa.models import FaGroupAssets
from app.modules.fa.models import FaImpairments
from app.modules.fa.models import FaInsuranceClaims
from app.modules.fa.models import FaInsurancePolicies
from app.modules.fa.models import FaIntegrationConnections
from app.modules.fa.models import FaIntegrationLogs
from app.modules.fa.models import FaLanggraphExecutions
from app.modules.fa.models import FaLanggraphStates
from app.modules.fa.models import FaLanggraphWorkflows
from app.modules.fa.models import FaLeaseAssets
from app.modules.fa.models import FaLeaseSchedules
from app.modules.fa.models import FaLeases
from app.modules.fa.models import FaLlmConfigs
from app.modules.fa.models import FaLocations
from app.modules.fa.models import FaMlModels
from app.modules.fa.models import FaMobileDevices
from app.modules.fa.models import FaMobileScans
from app.modules.fa.models import FaMobileSyncBatches
from app.modules.fa.models import FaMobileUsers
from app.modules.fa.models import FaOptimizationProblems
from app.modules.fa.models import FaOrtoolsProblems
from app.modules.fa.models import FaPhotos
from app.modules.fa.models import FaPhysicalCounts
from app.modules.fa.models import FaPredictionActuals
from app.modules.fa.models import FaPredictions
from app.modules.fa.models import FaPromptTemplates
from app.modules.fa.models import FaReinstatements
from app.modules.fa.models import FaReportSchedules
from app.modules.fa.models import FaReports
from app.modules.fa.models import FaRetirements
from app.modules.fa.models import FaRevaluations
from app.modules.fa.models import FaScenarios
from app.modules.fa.models import FaScipyAnalyses
from app.modules.fa.models import FaSignatures
from app.modules.fa.models import FaSolverConfigs
from app.modules.fa.models import FaTaxPayments
from app.modules.fa.models import FaTaxRecords
from app.modules.fa.models import FaTransactions
from app.modules.fa.models import FaTransfers
from app.modules.fa.models import FaVectorDocuments
from app.modules.fa.models import FaWarranties
from app.modules.fa.models import FaWarrantyClaims

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiModelRegistryService(BaseCRUDService[AiModelRegistry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiModelRegistry)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class FaAdditionsService(BaseCRUDService[FaAdditions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAdditions)

class FaAdjustmentsService(BaseCRUDService[FaAdjustments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAdjustments)

class FaAgentDefinitionsService(BaseCRUDService[FaAgentDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAgentDefinitions)

class FaAlgorithmsService(BaseCRUDService[FaAlgorithms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAlgorithms)

class FaAssetAttachmentsService(BaseCRUDService[FaAssetAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetAttachments)

class FaAssetBookAssignmentsService(BaseCRUDService[FaAssetBookAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetBookAssignments)

class FaAssetCategoriesService(BaseCRUDService[FaAssetCategories]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetCategories)

class FaAssetCategoryHierarchyService(BaseCRUDService[FaAssetCategoryHierarchy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetCategoryHierarchy)

class FaAssetComponentsService(BaseCRUDService[FaAssetComponents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetComponents)

class FaAssetCustomAttributesService(BaseCRUDService[FaAssetCustomAttributes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetCustomAttributes)

class FaAssetPhotosService(BaseCRUDService[FaAssetPhotos]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetPhotos)

class FaAssetStorageService(BaseCRUDService[FaAssetStorage]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetStorage)

class FaAssetTagsService(BaseCRUDService[FaAssetTags]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetTags)

class FaAssetTypesService(BaseCRUDService[FaAssetTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssetTypes)

class FaAssetsService(BaseCRUDService[FaAssets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaAssets)

class FaBonusDepreciationService(BaseCRUDService[FaBonusDepreciation]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaBonusDepreciation)

class FaBookTypesService(BaseCRUDService[FaBookTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaBookTypes)

class FaCipCostsService(BaseCRUDService[FaCipCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCipCosts)

class FaCipProjectsService(BaseCRUDService[FaCipProjects]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCipProjects)

class FaCountLinesService(BaseCRUDService[FaCountLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCountLines)

class FaCountRoutesService(BaseCRUDService[FaCountRoutes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCountRoutes)

class FaCountSheetsService(BaseCRUDService[FaCountSheets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCountSheets)

class FaCountVariancesService(BaseCRUDService[FaCountVariances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCountVariances)

class FaCustodiansService(BaseCRUDService[FaCustodians]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaCustodians)

class FaDeprnBookPeriodsService(BaseCRUDService[FaDeprnBookPeriods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaDeprnBookPeriods)

class FaDeprnBooksService(BaseCRUDService[FaDeprnBooks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaDeprnBooks)

class FaDeprnCalculationService(BaseCRUDService[FaDeprnCalculation]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaDeprnCalculation)

class FaDeprnConventionsService(BaseCRUDService[FaDeprnConventions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaDeprnConventions)

class FaDeprnMethodsService(BaseCRUDService[FaDeprnMethods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaDeprnMethods)

class FaGroupAssetMembersService(BaseCRUDService[FaGroupAssetMembers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaGroupAssetMembers)

class FaGroupAssetsService(BaseCRUDService[FaGroupAssets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaGroupAssets)

class FaImpairmentsService(BaseCRUDService[FaImpairments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaImpairments)

class FaInsuranceClaimsService(BaseCRUDService[FaInsuranceClaims]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaInsuranceClaims)

class FaInsurancePoliciesService(BaseCRUDService[FaInsurancePolicies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaInsurancePolicies)

class FaIntegrationConnectionsService(BaseCRUDService[FaIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaIntegrationConnections)

class FaIntegrationLogsService(BaseCRUDService[FaIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaIntegrationLogs)

class FaLanggraphExecutionsService(BaseCRUDService[FaLanggraphExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLanggraphExecutions)

class FaLanggraphStatesService(BaseCRUDService[FaLanggraphStates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLanggraphStates)

class FaLanggraphWorkflowsService(BaseCRUDService[FaLanggraphWorkflows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLanggraphWorkflows)

class FaLeaseAssetsService(BaseCRUDService[FaLeaseAssets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLeaseAssets)

class FaLeaseSchedulesService(BaseCRUDService[FaLeaseSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLeaseSchedules)

class FaLeasesService(BaseCRUDService[FaLeases]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLeases)

class FaLlmConfigsService(BaseCRUDService[FaLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLlmConfigs)

class FaLocationsService(BaseCRUDService[FaLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaLocations)

class FaMlModelsService(BaseCRUDService[FaMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaMlModels)

class FaMobileDevicesService(BaseCRUDService[FaMobileDevices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaMobileDevices)

class FaMobileScansService(BaseCRUDService[FaMobileScans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaMobileScans)

class FaMobileSyncBatchesService(BaseCRUDService[FaMobileSyncBatches]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaMobileSyncBatches)

class FaMobileUsersService(BaseCRUDService[FaMobileUsers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaMobileUsers)

class FaOptimizationProblemsService(BaseCRUDService[FaOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaOptimizationProblems)

class FaOrtoolsProblemsService(BaseCRUDService[FaOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaOrtoolsProblems)

class FaPhotosService(BaseCRUDService[FaPhotos]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaPhotos)

class FaPhysicalCountsService(BaseCRUDService[FaPhysicalCounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaPhysicalCounts)

class FaPredictionActualsService(BaseCRUDService[FaPredictionActuals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaPredictionActuals)

class FaPredictionsService(BaseCRUDService[FaPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaPredictions)

class FaPromptTemplatesService(BaseCRUDService[FaPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaPromptTemplates)

class FaReinstatementsService(BaseCRUDService[FaReinstatements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaReinstatements)

class FaReportSchedulesService(BaseCRUDService[FaReportSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaReportSchedules)

class FaReportsService(BaseCRUDService[FaReports]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaReports)

class FaRetirementsService(BaseCRUDService[FaRetirements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaRetirements)

class FaRevaluationsService(BaseCRUDService[FaRevaluations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaRevaluations)

class FaScenariosService(BaseCRUDService[FaScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaScenarios)

class FaScipyAnalysesService(BaseCRUDService[FaScipyAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaScipyAnalyses)

class FaSignaturesService(BaseCRUDService[FaSignatures]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaSignatures)

class FaSolverConfigsService(BaseCRUDService[FaSolverConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaSolverConfigs)

class FaTaxPaymentsService(BaseCRUDService[FaTaxPayments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaTaxPayments)

class FaTaxRecordsService(BaseCRUDService[FaTaxRecords]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaTaxRecords)

class FaTransactionsService(BaseCRUDService[FaTransactions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaTransactions)

class FaTransfersService(BaseCRUDService[FaTransfers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaTransfers)

class FaVectorDocumentsService(BaseCRUDService[FaVectorDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaVectorDocuments)

class FaWarrantiesService(BaseCRUDService[FaWarranties]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaWarranties)

class FaWarrantyClaimsService(BaseCRUDService[FaWarrantyClaims]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FaWarrantyClaims)
