from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.scm.models import AgentProposals
from app.modules.scm.models import BusinessWeights
from app.modules.scm.models import Conflicts
from app.modules.scm.models import ControlTowerActivities
from app.modules.scm.models import ControlTowerAlerts
from app.modules.scm.models import DemandForecasts
from app.modules.scm.models import DisruptionScenarios
from app.modules.scm.models import EscalationTickets
from app.modules.scm.models import ExperienceLedger
from app.modules.scm.models import ExperienceLedgerCold
from app.modules.scm.models import LotSizePolicies
from app.modules.scm.models import MrpActionMessages
from app.modules.scm.models import MrpDemandRecords
from app.modules.scm.models import MrpExceptions
from app.modules.scm.models import MrpPegging
from app.modules.scm.models import MrpPlans
from app.modules.scm.models import MrpSupplyRecords
from app.modules.scm.models import PlanScenarios
from app.modules.scm.models import PlanningTimeFences
from app.modules.scm.models import ReplenishmentPlans
from app.modules.scm.models import ScmAiAgentExecutionLogs
from app.modules.scm.models import ScmAiCostTracking
from app.modules.scm.models import ScmAiDecisions
from app.modules.scm.models import ScmAiExperimentTracking
from app.modules.scm.models import ScmAiFeatureStore
from app.modules.scm.models import ScmAiModelRegistry
from app.modules.scm.models import ScmAiWorkflowState
from app.modules.scm.models import ScmAlertEscalations
from app.modules.scm.models import ScmAlertNotifications
from app.modules.scm.models import ScmAlertRules
from app.modules.scm.models import ScmAlertTypes
from app.modules.scm.models import ScmAlerts
from app.modules.scm.models import ScmAlgorithmTests
from app.modules.scm.models import ScmAlgorithmVersions
from app.modules.scm.models import ScmAlgorithms
from app.modules.scm.models import ScmBinPackingItems
from app.modules.scm.models import ScmBinPackingMetrics
from app.modules.scm.models import ScmBinPackingProblems
from app.modules.scm.models import ScmBinPackingResults
from app.modules.scm.models import ScmBinTypes
from app.modules.scm.models import ScmDemandClasses
from app.modules.scm.models import ScmDemandDrivers
from app.modules.scm.models import ScmDemandSources
from app.modules.scm.models import ScmDemandTimeSeries
from app.modules.scm.models import ScmDistributionAllocationRules
from app.modules.scm.models import ScmDistributionCostToServe
from app.modules.scm.models import ScmDistributionNetwork
from app.modules.scm.models import ScmDistributionPlanLines
from app.modules.scm.models import ScmDistributionPlans
from app.modules.scm.models import ScmDistributionServiceLevels
from app.modules.scm.models import ScmForecastAccuracy
from app.modules.scm.models import ScmForecastModels
from app.modules.scm.models import ScmForecastValues
from app.modules.scm.models import ScmForecastVersions
from app.modules.scm.models import ScmIntegrationConnections
from app.modules.scm.models import ScmIntegrationLogs
from app.modules.scm.models import ScmIntegrationMappings
from app.modules.scm.models import ScmInventoryAging
from app.modules.scm.models import ScmInventoryClassifications
from app.modules.scm.models import ScmInventoryHealth
from app.modules.scm.models import ScmInventoryOptimizationParams
from app.modules.scm.models import ScmInventoryPolicies
from app.modules.scm.models import ScmInventoryRecommendations
from app.modules.scm.models import ScmInventoryTargets
from app.modules.scm.models import ScmKpiAlerts
from app.modules.scm.models import ScmKpiBenchmarks
from app.modules.scm.models import ScmKpiDefinitions
from app.modules.scm.models import ScmKpiValues
from app.modules.scm.models import ScmLangchainAgentExecutions
from app.modules.scm.models import ScmLangchainAgents
from app.modules.scm.models import ScmLangchainChains
from app.modules.scm.models import ScmLangchainDocuments
from app.modules.scm.models import ScmLangchainExecutions
from app.modules.scm.models import ScmLangchainLlmConfigs
from app.modules.scm.models import ScmLangchainPromptTemplates
from app.modules.scm.models import ScmLangchainVectorStores
from app.modules.scm.models import ScmLanggraphEdges
from app.modules.scm.models import ScmLanggraphExecutions
from app.modules.scm.models import ScmLanggraphLogs
from app.modules.scm.models import ScmLanggraphNodes
from app.modules.scm.models import ScmLanggraphWorkflows
from app.modules.scm.models import ScmMlModelDeployments
from app.modules.scm.models import ScmMlModelTypes
from app.modules.scm.models import ScmMlModels
from app.modules.scm.models import ScmMlMonitoring
from app.modules.scm.models import ScmMlTrainingRuns
from app.modules.scm.models import ScmNetworkArcs
from app.modules.scm.models import ScmNetworkCapacities
from app.modules.scm.models import ScmNetworkCosts
from app.modules.scm.models import ScmNetworkFlows
from app.modules.scm.models import ScmNetworkNodes
from app.modules.scm.models import ScmNetworkRiskAssessment
from app.modules.scm.models import ScmNetworkScenarios
from app.modules.scm.models import ScmOptimizationExecutionLog
from app.modules.scm.models import ScmOptimizationProblems
from app.modules.scm.models import ScmOptimizationSensitivity
from app.modules.scm.models import ScmOptimizationSolutions
from app.modules.scm.models import ScmOrtoolsProblems
from app.modules.scm.models import ScmOrtoolsSolutions
from app.modules.scm.models import ScmPickPathLearning
from app.modules.scm.models import ScmPickPathProblems
from app.modules.scm.models import ScmPickPathSolutions
from app.modules.scm.models import ScmPredictionAccuracy
from app.modules.scm.models import ScmPredictionFeatures
from app.modules.scm.models import ScmPredictionOverrides
from app.modules.scm.models import ScmPredictionTypes
from app.modules.scm.models import ScmPredictions
from app.modules.scm.models import ScmProcurementContracts
from app.modules.scm.models import ScmProcurementRecommendations
from app.modules.scm.models import ScmProcurementSavings
from app.modules.scm.models import ScmProcurementScenarios
from app.modules.scm.models import ScmProcurementStrategies
from app.modules.scm.models import ScmProcurementTco
from app.modules.scm.models import ScmPromotionCalendars
from app.modules.scm.models import ScmRoutingDistanceMatrix
from app.modules.scm.models import ScmRoutingLocations
from app.modules.scm.models import ScmRoutingProblems
from app.modules.scm.models import ScmRoutingSolutions
from app.modules.scm.models import ScmRoutingVehicles
from app.modules.scm.models import ScmScenarioComparisons
from app.modules.scm.models import ScmScenarioResults
from app.modules.scm.models import ScmScenarioTemplates
from app.modules.scm.models import ScmScenarioTypes
from app.modules.scm.models import ScmScenarios
from app.modules.scm.models import ScmScipyProblems
from app.modules.scm.models import ScmScipyResults
from app.modules.scm.models import ScmScipyStatisticalTests
from app.modules.scm.models import ScmSeasonalityIndices
from app.modules.scm.models import ScmSolverBenchmarks
from app.modules.scm.models import ScmSolverInstances
from app.modules.scm.models import ScmSolverLogs
from app.modules.scm.models import ScmSolverParameters
from app.modules.scm.models import ScmSolverTypes
from app.modules.scm.models import ScmSopCycles
from app.modules.scm.models import ScmSopDecisions
from app.modules.scm.models import ScmSopDemandPlans
from app.modules.scm.models import ScmSopKpis
from app.modules.scm.models import ScmSopReconciliation
from app.modules.scm.models import ScmSopScenarios
from app.modules.scm.models import ScmSopSupplyPlans
from app.modules.scm.models import ScmSupplierForecasts
from app.modules.scm.models import ScmSupplierPerformance
from app.modules.scm.models import ScmSupplierProfiles
from app.modules.scm.models import ScmSupplierRiskAssessments
from app.modules.scm.models import ScmSupplierScorecards
from app.modules.scm.models import ScmSupplierSustainability
from app.modules.scm.models import ScmSupplyCalendarDates
from app.modules.scm.models import ScmSupplyCalendars
from app.modules.scm.models import ScmSupplyConstraints
from app.modules.scm.models import ScmSupplyLeadTimes
from app.modules.scm.models import ScmSupplyPlanLines
from app.modules.scm.models import ScmSupplyPlans
from app.modules.scm.models import ScmSupplyRisks
from app.modules.scm.models import ScmSupplySources
from app.modules.scm.models import ScmTransportationConstraints
from app.modules.scm.models import ScmTransportationCosts
from app.modules.scm.models import ScmTransportationModes
from app.modules.scm.models import ScmTransportationRecommendations
from app.modules.scm.models import ScmTransportationScenarios
from app.modules.scm.models import ScmTransportationServiceLevels
from app.modules.scm.models import ScmWarehouseAisles
from app.modules.scm.models import ScmWarehouseLocations
from app.modules.scm.models import ScmWarehousePickBatches
from app.modules.scm.models import ScmWarehousePickLines
from app.modules.scm.models import ScmWarehousePickOrders
from app.modules.scm.models import ScmWarehouseWaves
from app.modules.scm.models import ScmWarehouseZones

class AgentProposalsService(BaseCRUDService[AgentProposals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AgentProposals)

class BusinessWeightsService(BaseCRUDService[BusinessWeights]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, BusinessWeights)

class ConflictsService(BaseCRUDService[Conflicts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Conflicts)

class ControlTowerActivitiesService(BaseCRUDService[ControlTowerActivities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ControlTowerActivities)

class ControlTowerAlertsService(BaseCRUDService[ControlTowerAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ControlTowerAlerts)

class DemandForecastsService(BaseCRUDService[DemandForecasts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DemandForecasts)

class DisruptionScenariosService(BaseCRUDService[DisruptionScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DisruptionScenarios)

class EscalationTicketsService(BaseCRUDService[EscalationTickets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EscalationTickets)

class ExperienceLedgerService(BaseCRUDService[ExperienceLedger]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExperienceLedger)

class ExperienceLedgerColdService(BaseCRUDService[ExperienceLedgerCold]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ExperienceLedgerCold)

class LotSizePoliciesService(BaseCRUDService[LotSizePolicies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LotSizePolicies)

class MrpActionMessagesService(BaseCRUDService[MrpActionMessages]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpActionMessages)

class MrpDemandRecordsService(BaseCRUDService[MrpDemandRecords]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpDemandRecords)

class MrpExceptionsService(BaseCRUDService[MrpExceptions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpExceptions)

class MrpPeggingService(BaseCRUDService[MrpPegging]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpPegging)

class MrpPlansService(BaseCRUDService[MrpPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpPlans)

class MrpSupplyRecordsService(BaseCRUDService[MrpSupplyRecords]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MrpSupplyRecords)

class PlanScenariosService(BaseCRUDService[PlanScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PlanScenarios)

class PlanningTimeFencesService(BaseCRUDService[PlanningTimeFences]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PlanningTimeFences)

class ReplenishmentPlansService(BaseCRUDService[ReplenishmentPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ReplenishmentPlans)

class ScmAiAgentExecutionLogsService(BaseCRUDService[ScmAiAgentExecutionLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiAgentExecutionLogs)

class ScmAiCostTrackingService(BaseCRUDService[ScmAiCostTracking]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiCostTracking)

class ScmAiDecisionsService(BaseCRUDService[ScmAiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiDecisions)

class ScmAiExperimentTrackingService(BaseCRUDService[ScmAiExperimentTracking]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiExperimentTracking)

class ScmAiFeatureStoreService(BaseCRUDService[ScmAiFeatureStore]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiFeatureStore)

class ScmAiModelRegistryService(BaseCRUDService[ScmAiModelRegistry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiModelRegistry)

class ScmAiWorkflowStateService(BaseCRUDService[ScmAiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAiWorkflowState)

class ScmAlertEscalationsService(BaseCRUDService[ScmAlertEscalations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlertEscalations)

class ScmAlertNotificationsService(BaseCRUDService[ScmAlertNotifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlertNotifications)

class ScmAlertRulesService(BaseCRUDService[ScmAlertRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlertRules)

class ScmAlertTypesService(BaseCRUDService[ScmAlertTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlertTypes)

class ScmAlertsService(BaseCRUDService[ScmAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlerts)

class ScmAlgorithmTestsService(BaseCRUDService[ScmAlgorithmTests]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlgorithmTests)

class ScmAlgorithmVersionsService(BaseCRUDService[ScmAlgorithmVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlgorithmVersions)

class ScmAlgorithmsService(BaseCRUDService[ScmAlgorithms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmAlgorithms)

class ScmBinPackingItemsService(BaseCRUDService[ScmBinPackingItems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmBinPackingItems)

class ScmBinPackingMetricsService(BaseCRUDService[ScmBinPackingMetrics]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmBinPackingMetrics)

class ScmBinPackingProblemsService(BaseCRUDService[ScmBinPackingProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmBinPackingProblems)

class ScmBinPackingResultsService(BaseCRUDService[ScmBinPackingResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmBinPackingResults)

class ScmBinTypesService(BaseCRUDService[ScmBinTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmBinTypes)

class ScmDemandClassesService(BaseCRUDService[ScmDemandClasses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDemandClasses)

class ScmDemandDriversService(BaseCRUDService[ScmDemandDrivers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDemandDrivers)

class ScmDemandSourcesService(BaseCRUDService[ScmDemandSources]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDemandSources)

class ScmDemandTimeSeriesService(BaseCRUDService[ScmDemandTimeSeries]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDemandTimeSeries)

class ScmDistributionAllocationRulesService(BaseCRUDService[ScmDistributionAllocationRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionAllocationRules)

class ScmDistributionCostToServeService(BaseCRUDService[ScmDistributionCostToServe]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionCostToServe)

class ScmDistributionNetworkService(BaseCRUDService[ScmDistributionNetwork]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionNetwork)

class ScmDistributionPlanLinesService(BaseCRUDService[ScmDistributionPlanLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionPlanLines)

class ScmDistributionPlansService(BaseCRUDService[ScmDistributionPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionPlans)

class ScmDistributionServiceLevelsService(BaseCRUDService[ScmDistributionServiceLevels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmDistributionServiceLevels)

class ScmForecastAccuracyService(BaseCRUDService[ScmForecastAccuracy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmForecastAccuracy)

class ScmForecastModelsService(BaseCRUDService[ScmForecastModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmForecastModels)

class ScmForecastValuesService(BaseCRUDService[ScmForecastValues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmForecastValues)

class ScmForecastVersionsService(BaseCRUDService[ScmForecastVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmForecastVersions)

class ScmIntegrationConnectionsService(BaseCRUDService[ScmIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmIntegrationConnections)

class ScmIntegrationLogsService(BaseCRUDService[ScmIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmIntegrationLogs)

class ScmIntegrationMappingsService(BaseCRUDService[ScmIntegrationMappings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmIntegrationMappings)

class ScmInventoryAgingService(BaseCRUDService[ScmInventoryAging]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryAging)

class ScmInventoryClassificationsService(BaseCRUDService[ScmInventoryClassifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryClassifications)

class ScmInventoryHealthService(BaseCRUDService[ScmInventoryHealth]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryHealth)

class ScmInventoryOptimizationParamsService(BaseCRUDService[ScmInventoryOptimizationParams]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryOptimizationParams)

class ScmInventoryPoliciesService(BaseCRUDService[ScmInventoryPolicies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryPolicies)

class ScmInventoryRecommendationsService(BaseCRUDService[ScmInventoryRecommendations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryRecommendations)

class ScmInventoryTargetsService(BaseCRUDService[ScmInventoryTargets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmInventoryTargets)

class ScmKpiAlertsService(BaseCRUDService[ScmKpiAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmKpiAlerts)

class ScmKpiBenchmarksService(BaseCRUDService[ScmKpiBenchmarks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmKpiBenchmarks)

class ScmKpiDefinitionsService(BaseCRUDService[ScmKpiDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmKpiDefinitions)

class ScmKpiValuesService(BaseCRUDService[ScmKpiValues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmKpiValues)

class ScmLangchainAgentExecutionsService(BaseCRUDService[ScmLangchainAgentExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainAgentExecutions)

class ScmLangchainAgentsService(BaseCRUDService[ScmLangchainAgents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainAgents)

class ScmLangchainChainsService(BaseCRUDService[ScmLangchainChains]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainChains)

class ScmLangchainDocumentsService(BaseCRUDService[ScmLangchainDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainDocuments)

class ScmLangchainExecutionsService(BaseCRUDService[ScmLangchainExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainExecutions)

class ScmLangchainLlmConfigsService(BaseCRUDService[ScmLangchainLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainLlmConfigs)

class ScmLangchainPromptTemplatesService(BaseCRUDService[ScmLangchainPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainPromptTemplates)

class ScmLangchainVectorStoresService(BaseCRUDService[ScmLangchainVectorStores]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLangchainVectorStores)

class ScmLanggraphEdgesService(BaseCRUDService[ScmLanggraphEdges]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLanggraphEdges)

class ScmLanggraphExecutionsService(BaseCRUDService[ScmLanggraphExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLanggraphExecutions)

class ScmLanggraphLogsService(BaseCRUDService[ScmLanggraphLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLanggraphLogs)

class ScmLanggraphNodesService(BaseCRUDService[ScmLanggraphNodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLanggraphNodes)

class ScmLanggraphWorkflowsService(BaseCRUDService[ScmLanggraphWorkflows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmLanggraphWorkflows)

class ScmMlModelDeploymentsService(BaseCRUDService[ScmMlModelDeployments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmMlModelDeployments)

class ScmMlModelTypesService(BaseCRUDService[ScmMlModelTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmMlModelTypes)

class ScmMlModelsService(BaseCRUDService[ScmMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmMlModels)

class ScmMlMonitoringService(BaseCRUDService[ScmMlMonitoring]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmMlMonitoring)

class ScmMlTrainingRunsService(BaseCRUDService[ScmMlTrainingRuns]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmMlTrainingRuns)

class ScmNetworkArcsService(BaseCRUDService[ScmNetworkArcs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkArcs)

class ScmNetworkCapacitiesService(BaseCRUDService[ScmNetworkCapacities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkCapacities)

class ScmNetworkCostsService(BaseCRUDService[ScmNetworkCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkCosts)

class ScmNetworkFlowsService(BaseCRUDService[ScmNetworkFlows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkFlows)

class ScmNetworkNodesService(BaseCRUDService[ScmNetworkNodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkNodes)

class ScmNetworkRiskAssessmentService(BaseCRUDService[ScmNetworkRiskAssessment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkRiskAssessment)

class ScmNetworkScenariosService(BaseCRUDService[ScmNetworkScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmNetworkScenarios)

class ScmOptimizationExecutionLogService(BaseCRUDService[ScmOptimizationExecutionLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOptimizationExecutionLog)

class ScmOptimizationProblemsService(BaseCRUDService[ScmOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOptimizationProblems)

class ScmOptimizationSensitivityService(BaseCRUDService[ScmOptimizationSensitivity]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOptimizationSensitivity)

class ScmOptimizationSolutionsService(BaseCRUDService[ScmOptimizationSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOptimizationSolutions)

class ScmOrtoolsProblemsService(BaseCRUDService[ScmOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOrtoolsProblems)

class ScmOrtoolsSolutionsService(BaseCRUDService[ScmOrtoolsSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmOrtoolsSolutions)

class ScmPickPathLearningService(BaseCRUDService[ScmPickPathLearning]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPickPathLearning)

class ScmPickPathProblemsService(BaseCRUDService[ScmPickPathProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPickPathProblems)

class ScmPickPathSolutionsService(BaseCRUDService[ScmPickPathSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPickPathSolutions)

class ScmPredictionAccuracyService(BaseCRUDService[ScmPredictionAccuracy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPredictionAccuracy)

class ScmPredictionFeaturesService(BaseCRUDService[ScmPredictionFeatures]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPredictionFeatures)

class ScmPredictionOverridesService(BaseCRUDService[ScmPredictionOverrides]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPredictionOverrides)

class ScmPredictionTypesService(BaseCRUDService[ScmPredictionTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPredictionTypes)

class ScmPredictionsService(BaseCRUDService[ScmPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPredictions)

class ScmProcurementContractsService(BaseCRUDService[ScmProcurementContracts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementContracts)

class ScmProcurementRecommendationsService(BaseCRUDService[ScmProcurementRecommendations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementRecommendations)

class ScmProcurementSavingsService(BaseCRUDService[ScmProcurementSavings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementSavings)

class ScmProcurementScenariosService(BaseCRUDService[ScmProcurementScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementScenarios)

class ScmProcurementStrategiesService(BaseCRUDService[ScmProcurementStrategies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementStrategies)

class ScmProcurementTcoService(BaseCRUDService[ScmProcurementTco]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmProcurementTco)

class ScmPromotionCalendarsService(BaseCRUDService[ScmPromotionCalendars]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmPromotionCalendars)

class ScmRoutingDistanceMatrixService(BaseCRUDService[ScmRoutingDistanceMatrix]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmRoutingDistanceMatrix)

class ScmRoutingLocationsService(BaseCRUDService[ScmRoutingLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmRoutingLocations)

class ScmRoutingProblemsService(BaseCRUDService[ScmRoutingProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmRoutingProblems)

class ScmRoutingSolutionsService(BaseCRUDService[ScmRoutingSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmRoutingSolutions)

class ScmRoutingVehiclesService(BaseCRUDService[ScmRoutingVehicles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmRoutingVehicles)

class ScmScenarioComparisonsService(BaseCRUDService[ScmScenarioComparisons]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScenarioComparisons)

class ScmScenarioResultsService(BaseCRUDService[ScmScenarioResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScenarioResults)

class ScmScenarioTemplatesService(BaseCRUDService[ScmScenarioTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScenarioTemplates)

class ScmScenarioTypesService(BaseCRUDService[ScmScenarioTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScenarioTypes)

class ScmScenariosService(BaseCRUDService[ScmScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScenarios)

class ScmScipyProblemsService(BaseCRUDService[ScmScipyProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScipyProblems)

class ScmScipyResultsService(BaseCRUDService[ScmScipyResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScipyResults)

class ScmScipyStatisticalTestsService(BaseCRUDService[ScmScipyStatisticalTests]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmScipyStatisticalTests)

class ScmSeasonalityIndicesService(BaseCRUDService[ScmSeasonalityIndices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSeasonalityIndices)

class ScmSolverBenchmarksService(BaseCRUDService[ScmSolverBenchmarks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSolverBenchmarks)

class ScmSolverInstancesService(BaseCRUDService[ScmSolverInstances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSolverInstances)

class ScmSolverLogsService(BaseCRUDService[ScmSolverLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSolverLogs)

class ScmSolverParametersService(BaseCRUDService[ScmSolverParameters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSolverParameters)

class ScmSolverTypesService(BaseCRUDService[ScmSolverTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSolverTypes)

class ScmSopCyclesService(BaseCRUDService[ScmSopCycles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopCycles)

class ScmSopDecisionsService(BaseCRUDService[ScmSopDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopDecisions)

class ScmSopDemandPlansService(BaseCRUDService[ScmSopDemandPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopDemandPlans)

class ScmSopKpisService(BaseCRUDService[ScmSopKpis]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopKpis)

class ScmSopReconciliationService(BaseCRUDService[ScmSopReconciliation]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopReconciliation)

class ScmSopScenariosService(BaseCRUDService[ScmSopScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopScenarios)

class ScmSopSupplyPlansService(BaseCRUDService[ScmSopSupplyPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSopSupplyPlans)

class ScmSupplierForecastsService(BaseCRUDService[ScmSupplierForecasts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierForecasts)

class ScmSupplierPerformanceService(BaseCRUDService[ScmSupplierPerformance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierPerformance)

class ScmSupplierProfilesService(BaseCRUDService[ScmSupplierProfiles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierProfiles)

class ScmSupplierRiskAssessmentsService(BaseCRUDService[ScmSupplierRiskAssessments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierRiskAssessments)

class ScmSupplierScorecardsService(BaseCRUDService[ScmSupplierScorecards]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierScorecards)

class ScmSupplierSustainabilityService(BaseCRUDService[ScmSupplierSustainability]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplierSustainability)

class ScmSupplyCalendarDatesService(BaseCRUDService[ScmSupplyCalendarDates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyCalendarDates)

class ScmSupplyCalendarsService(BaseCRUDService[ScmSupplyCalendars]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyCalendars)

class ScmSupplyConstraintsService(BaseCRUDService[ScmSupplyConstraints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyConstraints)

class ScmSupplyLeadTimesService(BaseCRUDService[ScmSupplyLeadTimes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyLeadTimes)

class ScmSupplyPlanLinesService(BaseCRUDService[ScmSupplyPlanLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyPlanLines)

class ScmSupplyPlansService(BaseCRUDService[ScmSupplyPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyPlans)

class ScmSupplyRisksService(BaseCRUDService[ScmSupplyRisks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplyRisks)

class ScmSupplySourcesService(BaseCRUDService[ScmSupplySources]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmSupplySources)

class ScmTransportationConstraintsService(BaseCRUDService[ScmTransportationConstraints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationConstraints)

class ScmTransportationCostsService(BaseCRUDService[ScmTransportationCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationCosts)

class ScmTransportationModesService(BaseCRUDService[ScmTransportationModes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationModes)

class ScmTransportationRecommendationsService(BaseCRUDService[ScmTransportationRecommendations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationRecommendations)

class ScmTransportationScenariosService(BaseCRUDService[ScmTransportationScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationScenarios)

class ScmTransportationServiceLevelsService(BaseCRUDService[ScmTransportationServiceLevels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmTransportationServiceLevels)

class ScmWarehouseAislesService(BaseCRUDService[ScmWarehouseAisles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehouseAisles)

class ScmWarehouseLocationsService(BaseCRUDService[ScmWarehouseLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehouseLocations)

class ScmWarehousePickBatchesService(BaseCRUDService[ScmWarehousePickBatches]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehousePickBatches)

class ScmWarehousePickLinesService(BaseCRUDService[ScmWarehousePickLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehousePickLines)

class ScmWarehousePickOrdersService(BaseCRUDService[ScmWarehousePickOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehousePickOrders)

class ScmWarehouseWavesService(BaseCRUDService[ScmWarehouseWaves]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehouseWaves)

class ScmWarehouseZonesService(BaseCRUDService[ScmWarehouseZones]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ScmWarehouseZones)
