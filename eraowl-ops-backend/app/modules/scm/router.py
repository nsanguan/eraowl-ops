import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.scm.services import (
    AgentProposalsService,
    BusinessWeightsService,
    ConflictsService,
    ControlTowerActivitiesService,
    ControlTowerAlertsService,
    DemandForecastsService,
    DisruptionScenariosService,
    EscalationTicketsService,
    ExperienceLedgerService,
    ExperienceLedgerColdService,
    LotSizePoliciesService,
    MrpActionMessagesService,
    MrpDemandRecordsService,
    MrpExceptionsService,
    MrpPeggingService,
    MrpPlansService,
    MrpSupplyRecordsService,
    PlanScenariosService,
    PlanningTimeFencesService,
    ReplenishmentPlansService,
    ScmAiAgentExecutionLogsService,
    ScmAiCostTrackingService,
    ScmAiDecisionsService,
    ScmAiExperimentTrackingService,
    ScmAiFeatureStoreService,
    ScmAiModelRegistryService,
    ScmAiWorkflowStateService,
    ScmAlertEscalationsService,
    ScmAlertNotificationsService,
    ScmAlertRulesService,
    ScmAlertTypesService,
    ScmAlertsService,
    ScmAlgorithmTestsService,
    ScmAlgorithmVersionsService,
    ScmAlgorithmsService,
    ScmBinPackingItemsService,
    ScmBinPackingMetricsService,
    ScmBinPackingProblemsService,
    ScmBinPackingResultsService,
    ScmBinTypesService,
    ScmDemandClassesService,
    ScmDemandDriversService,
    ScmDemandSourcesService,
    ScmDemandTimeSeriesService,
    ScmDistributionAllocationRulesService,
    ScmDistributionCostToServeService,
    ScmDistributionNetworkService,
    ScmDistributionPlanLinesService,
    ScmDistributionPlansService,
    ScmDistributionServiceLevelsService,
    ScmForecastAccuracyService,
    ScmForecastModelsService,
    ScmForecastValuesService,
    ScmForecastVersionsService,
    ScmIntegrationConnectionsService,
    ScmIntegrationLogsService,
    ScmIntegrationMappingsService,
    ScmInventoryAgingService,
    ScmInventoryClassificationsService,
    ScmInventoryHealthService,
    ScmInventoryOptimizationParamsService,
    ScmInventoryPoliciesService,
    ScmInventoryRecommendationsService,
    ScmInventoryTargetsService,
    ScmKpiAlertsService,
    ScmKpiBenchmarksService,
    ScmKpiDefinitionsService,
    ScmKpiValuesService,
    ScmLangchainAgentExecutionsService,
    ScmLangchainAgentsService,
    ScmLangchainChainsService,
    ScmLangchainDocumentsService,
    ScmLangchainExecutionsService,
    ScmLangchainLlmConfigsService,
    ScmLangchainPromptTemplatesService,
    ScmLangchainVectorStoresService,
    ScmLanggraphEdgesService,
    ScmLanggraphExecutionsService,
    ScmLanggraphLogsService,
    ScmLanggraphNodesService,
    ScmLanggraphWorkflowsService,
    ScmMlModelDeploymentsService,
    ScmMlModelTypesService,
    ScmMlModelsService,
    ScmMlMonitoringService,
    ScmMlTrainingRunsService,
    ScmNetworkArcsService,
    ScmNetworkCapacitiesService,
    ScmNetworkCostsService,
    ScmNetworkFlowsService,
    ScmNetworkNodesService,
    ScmNetworkRiskAssessmentService,
    ScmNetworkScenariosService,
    ScmOptimizationExecutionLogService,
    ScmOptimizationProblemsService,
    ScmOptimizationSensitivityService,
    ScmOptimizationSolutionsService,
    ScmOrtoolsProblemsService,
    ScmOrtoolsSolutionsService,
    ScmPickPathLearningService,
    ScmPickPathProblemsService,
    ScmPickPathSolutionsService,
    ScmPredictionAccuracyService,
    ScmPredictionFeaturesService,
    ScmPredictionOverridesService,
    ScmPredictionTypesService,
    ScmPredictionsService,
    ScmProcurementContractsService,
    ScmProcurementRecommendationsService,
    ScmProcurementSavingsService,
    ScmProcurementScenariosService,
    ScmProcurementStrategiesService,
    ScmProcurementTcoService,
    ScmPromotionCalendarsService,
    ScmRoutingDistanceMatrixService,
    ScmRoutingLocationsService,
    ScmRoutingProblemsService,
    ScmRoutingSolutionsService,
    ScmRoutingVehiclesService,
    ScmScenarioComparisonsService,
    ScmScenarioResultsService,
    ScmScenarioTemplatesService,
    ScmScenarioTypesService,
    ScmScenariosService,
    ScmScipyProblemsService,
    ScmScipyResultsService,
    ScmScipyStatisticalTestsService,
    ScmSeasonalityIndicesService,
    ScmSolverBenchmarksService,
    ScmSolverInstancesService,
    ScmSolverLogsService,
    ScmSolverParametersService,
    ScmSolverTypesService,
    ScmSopCyclesService,
    ScmSopDecisionsService,
    ScmSopDemandPlansService,
    ScmSopKpisService,
    ScmSopReconciliationService,
    ScmSopScenariosService,
    ScmSopSupplyPlansService,
    ScmSupplierForecastsService,
    ScmSupplierPerformanceService,
    ScmSupplierProfilesService,
    ScmSupplierRiskAssessmentsService,
    ScmSupplierScorecardsService,
    ScmSupplierSustainabilityService,
    ScmSupplyCalendarDatesService,
    ScmSupplyCalendarsService,
    ScmSupplyConstraintsService,
    ScmSupplyLeadTimesService,
    ScmSupplyPlanLinesService,
    ScmSupplyPlansService,
    ScmSupplyRisksService,
    ScmSupplySourcesService,
    ScmTransportationConstraintsService,
    ScmTransportationCostsService,
    ScmTransportationModesService,
    ScmTransportationRecommendationsService,
    ScmTransportationScenariosService,
    ScmTransportationServiceLevelsService,
    ScmWarehouseAislesService,
    ScmWarehouseLocationsService,
    ScmWarehousePickBatchesService,
    ScmWarehousePickLinesService,
    ScmWarehousePickOrdersService,
    ScmWarehouseWavesService,
    ScmWarehouseZonesService,
)
from app.modules.scm.schemas import (
    AgentProposalsCreate,
    AgentProposalsUpdate,
    AgentProposalsOut,
    BusinessWeightsCreate,
    BusinessWeightsUpdate,
    BusinessWeightsOut,
    ConflictsCreate,
    ConflictsUpdate,
    ConflictsOut,
    ControlTowerActivitiesCreate,
    ControlTowerActivitiesUpdate,
    ControlTowerActivitiesOut,
    ControlTowerAlertsCreate,
    ControlTowerAlertsUpdate,
    ControlTowerAlertsOut,
    DemandForecastsCreate,
    DemandForecastsUpdate,
    DemandForecastsOut,
    DisruptionScenariosCreate,
    DisruptionScenariosUpdate,
    DisruptionScenariosOut,
    EscalationTicketsCreate,
    EscalationTicketsUpdate,
    EscalationTicketsOut,
    ExperienceLedgerCreate,
    ExperienceLedgerUpdate,
    ExperienceLedgerOut,
    ExperienceLedgerColdCreate,
    ExperienceLedgerColdUpdate,
    ExperienceLedgerColdOut,
    LotSizePoliciesCreate,
    LotSizePoliciesUpdate,
    LotSizePoliciesOut,
    MrpActionMessagesCreate,
    MrpActionMessagesUpdate,
    MrpActionMessagesOut,
    MrpDemandRecordsCreate,
    MrpDemandRecordsUpdate,
    MrpDemandRecordsOut,
    MrpExceptionsCreate,
    MrpExceptionsUpdate,
    MrpExceptionsOut,
    MrpPeggingCreate,
    MrpPeggingUpdate,
    MrpPeggingOut,
    MrpPlansCreate,
    MrpPlansUpdate,
    MrpPlansOut,
    MrpSupplyRecordsCreate,
    MrpSupplyRecordsUpdate,
    MrpSupplyRecordsOut,
    PlanScenariosCreate,
    PlanScenariosUpdate,
    PlanScenariosOut,
    PlanningTimeFencesCreate,
    PlanningTimeFencesUpdate,
    PlanningTimeFencesOut,
    ReplenishmentPlansCreate,
    ReplenishmentPlansUpdate,
    ReplenishmentPlansOut,
    ScmAiAgentExecutionLogsCreate,
    ScmAiAgentExecutionLogsUpdate,
    ScmAiAgentExecutionLogsOut,
    ScmAiCostTrackingCreate,
    ScmAiCostTrackingUpdate,
    ScmAiCostTrackingOut,
    ScmAiDecisionsCreate,
    ScmAiDecisionsUpdate,
    ScmAiDecisionsOut,
    ScmAiExperimentTrackingCreate,
    ScmAiExperimentTrackingUpdate,
    ScmAiExperimentTrackingOut,
    ScmAiFeatureStoreCreate,
    ScmAiFeatureStoreUpdate,
    ScmAiFeatureStoreOut,
    ScmAiModelRegistryCreate,
    ScmAiModelRegistryUpdate,
    ScmAiModelRegistryOut,
    ScmAiWorkflowStateCreate,
    ScmAiWorkflowStateUpdate,
    ScmAiWorkflowStateOut,
    ScmAlertEscalationsCreate,
    ScmAlertEscalationsUpdate,
    ScmAlertEscalationsOut,
    ScmAlertNotificationsCreate,
    ScmAlertNotificationsUpdate,
    ScmAlertNotificationsOut,
    ScmAlertRulesCreate,
    ScmAlertRulesUpdate,
    ScmAlertRulesOut,
    ScmAlertTypesCreate,
    ScmAlertTypesUpdate,
    ScmAlertTypesOut,
    ScmAlertsCreate,
    ScmAlertsUpdate,
    ScmAlertsOut,
    ScmAlgorithmTestsCreate,
    ScmAlgorithmTestsUpdate,
    ScmAlgorithmTestsOut,
    ScmAlgorithmVersionsCreate,
    ScmAlgorithmVersionsUpdate,
    ScmAlgorithmVersionsOut,
    ScmAlgorithmsCreate,
    ScmAlgorithmsUpdate,
    ScmAlgorithmsOut,
    ScmBinPackingItemsCreate,
    ScmBinPackingItemsUpdate,
    ScmBinPackingItemsOut,
    ScmBinPackingMetricsCreate,
    ScmBinPackingMetricsUpdate,
    ScmBinPackingMetricsOut,
    ScmBinPackingProblemsCreate,
    ScmBinPackingProblemsUpdate,
    ScmBinPackingProblemsOut,
    ScmBinPackingResultsCreate,
    ScmBinPackingResultsUpdate,
    ScmBinPackingResultsOut,
    ScmBinTypesCreate,
    ScmBinTypesUpdate,
    ScmBinTypesOut,
    ScmDemandClassesCreate,
    ScmDemandClassesUpdate,
    ScmDemandClassesOut,
    ScmDemandDriversCreate,
    ScmDemandDriversUpdate,
    ScmDemandDriversOut,
    ScmDemandSourcesCreate,
    ScmDemandSourcesUpdate,
    ScmDemandSourcesOut,
    ScmDemandTimeSeriesCreate,
    ScmDemandTimeSeriesUpdate,
    ScmDemandTimeSeriesOut,
    ScmDistributionAllocationRulesCreate,
    ScmDistributionAllocationRulesUpdate,
    ScmDistributionAllocationRulesOut,
    ScmDistributionCostToServeCreate,
    ScmDistributionCostToServeUpdate,
    ScmDistributionCostToServeOut,
    ScmDistributionNetworkCreate,
    ScmDistributionNetworkUpdate,
    ScmDistributionNetworkOut,
    ScmDistributionPlanLinesCreate,
    ScmDistributionPlanLinesUpdate,
    ScmDistributionPlanLinesOut,
    ScmDistributionPlansCreate,
    ScmDistributionPlansUpdate,
    ScmDistributionPlansOut,
    ScmDistributionServiceLevelsCreate,
    ScmDistributionServiceLevelsUpdate,
    ScmDistributionServiceLevelsOut,
    ScmForecastAccuracyCreate,
    ScmForecastAccuracyUpdate,
    ScmForecastAccuracyOut,
    ScmForecastModelsCreate,
    ScmForecastModelsUpdate,
    ScmForecastModelsOut,
    ScmForecastValuesCreate,
    ScmForecastValuesUpdate,
    ScmForecastValuesOut,
    ScmForecastVersionsCreate,
    ScmForecastVersionsUpdate,
    ScmForecastVersionsOut,
    ScmIntegrationConnectionsCreate,
    ScmIntegrationConnectionsUpdate,
    ScmIntegrationConnectionsOut,
    ScmIntegrationLogsCreate,
    ScmIntegrationLogsUpdate,
    ScmIntegrationLogsOut,
    ScmIntegrationMappingsCreate,
    ScmIntegrationMappingsUpdate,
    ScmIntegrationMappingsOut,
    ScmInventoryAgingCreate,
    ScmInventoryAgingUpdate,
    ScmInventoryAgingOut,
    ScmInventoryClassificationsCreate,
    ScmInventoryClassificationsUpdate,
    ScmInventoryClassificationsOut,
    ScmInventoryHealthCreate,
    ScmInventoryHealthUpdate,
    ScmInventoryHealthOut,
    ScmInventoryOptimizationParamsCreate,
    ScmInventoryOptimizationParamsUpdate,
    ScmInventoryOptimizationParamsOut,
    ScmInventoryPoliciesCreate,
    ScmInventoryPoliciesUpdate,
    ScmInventoryPoliciesOut,
    ScmInventoryRecommendationsCreate,
    ScmInventoryRecommendationsUpdate,
    ScmInventoryRecommendationsOut,
    ScmInventoryTargetsCreate,
    ScmInventoryTargetsUpdate,
    ScmInventoryTargetsOut,
    ScmKpiAlertsCreate,
    ScmKpiAlertsUpdate,
    ScmKpiAlertsOut,
    ScmKpiBenchmarksCreate,
    ScmKpiBenchmarksUpdate,
    ScmKpiBenchmarksOut,
    ScmKpiDefinitionsCreate,
    ScmKpiDefinitionsUpdate,
    ScmKpiDefinitionsOut,
    ScmKpiValuesCreate,
    ScmKpiValuesUpdate,
    ScmKpiValuesOut,
    ScmLangchainAgentExecutionsCreate,
    ScmLangchainAgentExecutionsUpdate,
    ScmLangchainAgentExecutionsOut,
    ScmLangchainAgentsCreate,
    ScmLangchainAgentsUpdate,
    ScmLangchainAgentsOut,
    ScmLangchainChainsCreate,
    ScmLangchainChainsUpdate,
    ScmLangchainChainsOut,
    ScmLangchainDocumentsCreate,
    ScmLangchainDocumentsUpdate,
    ScmLangchainDocumentsOut,
    ScmLangchainExecutionsCreate,
    ScmLangchainExecutionsUpdate,
    ScmLangchainExecutionsOut,
    ScmLangchainLlmConfigsCreate,
    ScmLangchainLlmConfigsUpdate,
    ScmLangchainLlmConfigsOut,
    ScmLangchainPromptTemplatesCreate,
    ScmLangchainPromptTemplatesUpdate,
    ScmLangchainPromptTemplatesOut,
    ScmLangchainVectorStoresCreate,
    ScmLangchainVectorStoresUpdate,
    ScmLangchainVectorStoresOut,
    ScmLanggraphEdgesCreate,
    ScmLanggraphEdgesUpdate,
    ScmLanggraphEdgesOut,
    ScmLanggraphExecutionsCreate,
    ScmLanggraphExecutionsUpdate,
    ScmLanggraphExecutionsOut,
    ScmLanggraphLogsCreate,
    ScmLanggraphLogsUpdate,
    ScmLanggraphLogsOut,
    ScmLanggraphNodesCreate,
    ScmLanggraphNodesUpdate,
    ScmLanggraphNodesOut,
    ScmLanggraphWorkflowsCreate,
    ScmLanggraphWorkflowsUpdate,
    ScmLanggraphWorkflowsOut,
    ScmMlModelDeploymentsCreate,
    ScmMlModelDeploymentsUpdate,
    ScmMlModelDeploymentsOut,
    ScmMlModelTypesCreate,
    ScmMlModelTypesUpdate,
    ScmMlModelTypesOut,
    ScmMlModelsCreate,
    ScmMlModelsUpdate,
    ScmMlModelsOut,
    ScmMlMonitoringCreate,
    ScmMlMonitoringUpdate,
    ScmMlMonitoringOut,
    ScmMlTrainingRunsCreate,
    ScmMlTrainingRunsUpdate,
    ScmMlTrainingRunsOut,
    ScmNetworkArcsCreate,
    ScmNetworkArcsUpdate,
    ScmNetworkArcsOut,
    ScmNetworkCapacitiesCreate,
    ScmNetworkCapacitiesUpdate,
    ScmNetworkCapacitiesOut,
    ScmNetworkCostsCreate,
    ScmNetworkCostsUpdate,
    ScmNetworkCostsOut,
    ScmNetworkFlowsCreate,
    ScmNetworkFlowsUpdate,
    ScmNetworkFlowsOut,
    ScmNetworkNodesCreate,
    ScmNetworkNodesUpdate,
    ScmNetworkNodesOut,
    ScmNetworkRiskAssessmentCreate,
    ScmNetworkRiskAssessmentUpdate,
    ScmNetworkRiskAssessmentOut,
    ScmNetworkScenariosCreate,
    ScmNetworkScenariosUpdate,
    ScmNetworkScenariosOut,
    ScmOptimizationExecutionLogCreate,
    ScmOptimizationExecutionLogUpdate,
    ScmOptimizationExecutionLogOut,
    ScmOptimizationProblemsCreate,
    ScmOptimizationProblemsUpdate,
    ScmOptimizationProblemsOut,
    ScmOptimizationSensitivityCreate,
    ScmOptimizationSensitivityUpdate,
    ScmOptimizationSensitivityOut,
    ScmOptimizationSolutionsCreate,
    ScmOptimizationSolutionsUpdate,
    ScmOptimizationSolutionsOut,
    ScmOrtoolsProblemsCreate,
    ScmOrtoolsProblemsUpdate,
    ScmOrtoolsProblemsOut,
    ScmOrtoolsSolutionsCreate,
    ScmOrtoolsSolutionsUpdate,
    ScmOrtoolsSolutionsOut,
    ScmPickPathLearningCreate,
    ScmPickPathLearningUpdate,
    ScmPickPathLearningOut,
    ScmPickPathProblemsCreate,
    ScmPickPathProblemsUpdate,
    ScmPickPathProblemsOut,
    ScmPickPathSolutionsCreate,
    ScmPickPathSolutionsUpdate,
    ScmPickPathSolutionsOut,
    ScmPredictionAccuracyCreate,
    ScmPredictionAccuracyUpdate,
    ScmPredictionAccuracyOut,
    ScmPredictionFeaturesCreate,
    ScmPredictionFeaturesUpdate,
    ScmPredictionFeaturesOut,
    ScmPredictionOverridesCreate,
    ScmPredictionOverridesUpdate,
    ScmPredictionOverridesOut,
    ScmPredictionTypesCreate,
    ScmPredictionTypesUpdate,
    ScmPredictionTypesOut,
    ScmPredictionsCreate,
    ScmPredictionsUpdate,
    ScmPredictionsOut,
    ScmProcurementContractsCreate,
    ScmProcurementContractsUpdate,
    ScmProcurementContractsOut,
    ScmProcurementRecommendationsCreate,
    ScmProcurementRecommendationsUpdate,
    ScmProcurementRecommendationsOut,
    ScmProcurementSavingsCreate,
    ScmProcurementSavingsUpdate,
    ScmProcurementSavingsOut,
    ScmProcurementScenariosCreate,
    ScmProcurementScenariosUpdate,
    ScmProcurementScenariosOut,
    ScmProcurementStrategiesCreate,
    ScmProcurementStrategiesUpdate,
    ScmProcurementStrategiesOut,
    ScmProcurementTcoCreate,
    ScmProcurementTcoUpdate,
    ScmProcurementTcoOut,
    ScmPromotionCalendarsCreate,
    ScmPromotionCalendarsUpdate,
    ScmPromotionCalendarsOut,
    ScmRoutingDistanceMatrixCreate,
    ScmRoutingDistanceMatrixUpdate,
    ScmRoutingDistanceMatrixOut,
    ScmRoutingLocationsCreate,
    ScmRoutingLocationsUpdate,
    ScmRoutingLocationsOut,
    ScmRoutingProblemsCreate,
    ScmRoutingProblemsUpdate,
    ScmRoutingProblemsOut,
    ScmRoutingSolutionsCreate,
    ScmRoutingSolutionsUpdate,
    ScmRoutingSolutionsOut,
    ScmRoutingVehiclesCreate,
    ScmRoutingVehiclesUpdate,
    ScmRoutingVehiclesOut,
    ScmScenarioComparisonsCreate,
    ScmScenarioComparisonsUpdate,
    ScmScenarioComparisonsOut,
    ScmScenarioResultsCreate,
    ScmScenarioResultsUpdate,
    ScmScenarioResultsOut,
    ScmScenarioTemplatesCreate,
    ScmScenarioTemplatesUpdate,
    ScmScenarioTemplatesOut,
    ScmScenarioTypesCreate,
    ScmScenarioTypesUpdate,
    ScmScenarioTypesOut,
    ScmScenariosCreate,
    ScmScenariosUpdate,
    ScmScenariosOut,
    ScmScipyProblemsCreate,
    ScmScipyProblemsUpdate,
    ScmScipyProblemsOut,
    ScmScipyResultsCreate,
    ScmScipyResultsUpdate,
    ScmScipyResultsOut,
    ScmScipyStatisticalTestsCreate,
    ScmScipyStatisticalTestsUpdate,
    ScmScipyStatisticalTestsOut,
    ScmSeasonalityIndicesCreate,
    ScmSeasonalityIndicesUpdate,
    ScmSeasonalityIndicesOut,
    ScmSolverBenchmarksCreate,
    ScmSolverBenchmarksUpdate,
    ScmSolverBenchmarksOut,
    ScmSolverInstancesCreate,
    ScmSolverInstancesUpdate,
    ScmSolverInstancesOut,
    ScmSolverLogsCreate,
    ScmSolverLogsUpdate,
    ScmSolverLogsOut,
    ScmSolverParametersCreate,
    ScmSolverParametersUpdate,
    ScmSolverParametersOut,
    ScmSolverTypesCreate,
    ScmSolverTypesUpdate,
    ScmSolverTypesOut,
    ScmSopCyclesCreate,
    ScmSopCyclesUpdate,
    ScmSopCyclesOut,
    ScmSopDecisionsCreate,
    ScmSopDecisionsUpdate,
    ScmSopDecisionsOut,
    ScmSopDemandPlansCreate,
    ScmSopDemandPlansUpdate,
    ScmSopDemandPlansOut,
    ScmSopKpisCreate,
    ScmSopKpisUpdate,
    ScmSopKpisOut,
    ScmSopReconciliationCreate,
    ScmSopReconciliationUpdate,
    ScmSopReconciliationOut,
    ScmSopScenariosCreate,
    ScmSopScenariosUpdate,
    ScmSopScenariosOut,
    ScmSopSupplyPlansCreate,
    ScmSopSupplyPlansUpdate,
    ScmSopSupplyPlansOut,
    ScmSupplierForecastsCreate,
    ScmSupplierForecastsUpdate,
    ScmSupplierForecastsOut,
    ScmSupplierPerformanceCreate,
    ScmSupplierPerformanceUpdate,
    ScmSupplierPerformanceOut,
    ScmSupplierProfilesCreate,
    ScmSupplierProfilesUpdate,
    ScmSupplierProfilesOut,
    ScmSupplierRiskAssessmentsCreate,
    ScmSupplierRiskAssessmentsUpdate,
    ScmSupplierRiskAssessmentsOut,
    ScmSupplierScorecardsCreate,
    ScmSupplierScorecardsUpdate,
    ScmSupplierScorecardsOut,
    ScmSupplierSustainabilityCreate,
    ScmSupplierSustainabilityUpdate,
    ScmSupplierSustainabilityOut,
    ScmSupplyCalendarDatesCreate,
    ScmSupplyCalendarDatesUpdate,
    ScmSupplyCalendarDatesOut,
    ScmSupplyCalendarsCreate,
    ScmSupplyCalendarsUpdate,
    ScmSupplyCalendarsOut,
    ScmSupplyConstraintsCreate,
    ScmSupplyConstraintsUpdate,
    ScmSupplyConstraintsOut,
    ScmSupplyLeadTimesCreate,
    ScmSupplyLeadTimesUpdate,
    ScmSupplyLeadTimesOut,
    ScmSupplyPlanLinesCreate,
    ScmSupplyPlanLinesUpdate,
    ScmSupplyPlanLinesOut,
    ScmSupplyPlansCreate,
    ScmSupplyPlansUpdate,
    ScmSupplyPlansOut,
    ScmSupplyRisksCreate,
    ScmSupplyRisksUpdate,
    ScmSupplyRisksOut,
    ScmSupplySourcesCreate,
    ScmSupplySourcesUpdate,
    ScmSupplySourcesOut,
    ScmTransportationConstraintsCreate,
    ScmTransportationConstraintsUpdate,
    ScmTransportationConstraintsOut,
    ScmTransportationCostsCreate,
    ScmTransportationCostsUpdate,
    ScmTransportationCostsOut,
    ScmTransportationModesCreate,
    ScmTransportationModesUpdate,
    ScmTransportationModesOut,
    ScmTransportationRecommendationsCreate,
    ScmTransportationRecommendationsUpdate,
    ScmTransportationRecommendationsOut,
    ScmTransportationScenariosCreate,
    ScmTransportationScenariosUpdate,
    ScmTransportationScenariosOut,
    ScmTransportationServiceLevelsCreate,
    ScmTransportationServiceLevelsUpdate,
    ScmTransportationServiceLevelsOut,
    ScmWarehouseAislesCreate,
    ScmWarehouseAislesUpdate,
    ScmWarehouseAislesOut,
    ScmWarehouseLocationsCreate,
    ScmWarehouseLocationsUpdate,
    ScmWarehouseLocationsOut,
    ScmWarehousePickBatchesCreate,
    ScmWarehousePickBatchesUpdate,
    ScmWarehousePickBatchesOut,
    ScmWarehousePickLinesCreate,
    ScmWarehousePickLinesUpdate,
    ScmWarehousePickLinesOut,
    ScmWarehousePickOrdersCreate,
    ScmWarehousePickOrdersUpdate,
    ScmWarehousePickOrdersOut,
    ScmWarehouseWavesCreate,
    ScmWarehouseWavesUpdate,
    ScmWarehouseWavesOut,
    ScmWarehouseZonesCreate,
    ScmWarehouseZonesUpdate,
    ScmWarehouseZonesOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/agent_proposals", response_model=PaginatedResponse[AgentProposalsOut])
async def list_agent_proposals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = AgentProposalsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/agent_proposals/{entity_id}", response_model=AgentProposalsOut)
async def get_agent_proposals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await AgentProposalsService(db).get(entity_id)

@router.post("/agent_proposals", response_model=AgentProposalsOut, status_code=status.HTTP_201_CREATED)
async def create_agent_proposals(
    data: AgentProposalsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await AgentProposalsService(db).create(data)

@router.put("/agent_proposals/{entity_id}", response_model=AgentProposalsOut)
async def update_agent_proposals(
    entity_id: uuid.UUID,
    data: AgentProposalsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await AgentProposalsService(db).update(entity_id, data)

@router.delete("/agent_proposals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_agent_proposals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await AgentProposalsService(db).delete(entity_id)

@router.get("/business_weights", response_model=PaginatedResponse[BusinessWeightsOut])
async def list_business_weights(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = BusinessWeightsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/business_weights/{entity_id}", response_model=BusinessWeightsOut)
async def get_business_weights(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await BusinessWeightsService(db).get(entity_id)

@router.post("/business_weights", response_model=BusinessWeightsOut, status_code=status.HTTP_201_CREATED)
async def create_business_weights(
    data: BusinessWeightsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await BusinessWeightsService(db).create(data)

@router.put("/business_weights/{entity_id}", response_model=BusinessWeightsOut)
async def update_business_weights(
    entity_id: uuid.UUID,
    data: BusinessWeightsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await BusinessWeightsService(db).update(entity_id, data)

@router.delete("/business_weights/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_business_weights(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await BusinessWeightsService(db).delete(entity_id)

@router.get("/conflicts", response_model=PaginatedResponse[ConflictsOut])
async def list_conflicts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ConflictsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/conflicts/{entity_id}", response_model=ConflictsOut)
async def get_conflicts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ConflictsService(db).get(entity_id)

@router.post("/conflicts", response_model=ConflictsOut, status_code=status.HTTP_201_CREATED)
async def create_conflicts(
    data: ConflictsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ConflictsService(db).create(data)

@router.put("/conflicts/{entity_id}", response_model=ConflictsOut)
async def update_conflicts(
    entity_id: uuid.UUID,
    data: ConflictsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ConflictsService(db).update(entity_id, data)

@router.delete("/conflicts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conflicts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ConflictsService(db).delete(entity_id)

@router.get("/control_tower_activities", response_model=PaginatedResponse[ControlTowerActivitiesOut])
async def list_control_tower_activities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ControlTowerActivitiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/control_tower_activities/{entity_id}", response_model=ControlTowerActivitiesOut)
async def get_control_tower_activities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ControlTowerActivitiesService(db).get(entity_id)

@router.post("/control_tower_activities", response_model=ControlTowerActivitiesOut, status_code=status.HTTP_201_CREATED)
async def create_control_tower_activities(
    data: ControlTowerActivitiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ControlTowerActivitiesService(db).create(data)

@router.put("/control_tower_activities/{entity_id}", response_model=ControlTowerActivitiesOut)
async def update_control_tower_activities(
    entity_id: uuid.UUID,
    data: ControlTowerActivitiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ControlTowerActivitiesService(db).update(entity_id, data)

@router.delete("/control_tower_activities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_control_tower_activities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ControlTowerActivitiesService(db).delete(entity_id)

@router.get("/control_tower_alerts", response_model=PaginatedResponse[ControlTowerAlertsOut])
async def list_control_tower_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ControlTowerAlertsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/control_tower_alerts/{entity_id}", response_model=ControlTowerAlertsOut)
async def get_control_tower_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ControlTowerAlertsService(db).get(entity_id)

@router.post("/control_tower_alerts", response_model=ControlTowerAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_control_tower_alerts(
    data: ControlTowerAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ControlTowerAlertsService(db).create(data)

@router.put("/control_tower_alerts/{entity_id}", response_model=ControlTowerAlertsOut)
async def update_control_tower_alerts(
    entity_id: uuid.UUID,
    data: ControlTowerAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ControlTowerAlertsService(db).update(entity_id, data)

@router.delete("/control_tower_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_control_tower_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ControlTowerAlertsService(db).delete(entity_id)

@router.get("/demand_forecasts", response_model=PaginatedResponse[DemandForecastsOut])
async def list_demand_forecasts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = DemandForecastsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/demand_forecasts/{entity_id}", response_model=DemandForecastsOut)
async def get_demand_forecasts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await DemandForecastsService(db).get(entity_id)

@router.post("/demand_forecasts", response_model=DemandForecastsOut, status_code=status.HTTP_201_CREATED)
async def create_demand_forecasts(
    data: DemandForecastsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await DemandForecastsService(db).create(data)

@router.put("/demand_forecasts/{entity_id}", response_model=DemandForecastsOut)
async def update_demand_forecasts(
    entity_id: uuid.UUID,
    data: DemandForecastsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await DemandForecastsService(db).update(entity_id, data)

@router.delete("/demand_forecasts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_demand_forecasts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await DemandForecastsService(db).delete(entity_id)

@router.get("/disruption_scenarios", response_model=PaginatedResponse[DisruptionScenariosOut])
async def list_disruption_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = DisruptionScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/disruption_scenarios/{entity_id}", response_model=DisruptionScenariosOut)
async def get_disruption_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await DisruptionScenariosService(db).get(entity_id)

@router.post("/disruption_scenarios", response_model=DisruptionScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_disruption_scenarios(
    data: DisruptionScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await DisruptionScenariosService(db).create(data)

@router.put("/disruption_scenarios/{entity_id}", response_model=DisruptionScenariosOut)
async def update_disruption_scenarios(
    entity_id: uuid.UUID,
    data: DisruptionScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await DisruptionScenariosService(db).update(entity_id, data)

@router.delete("/disruption_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_disruption_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await DisruptionScenariosService(db).delete(entity_id)

@router.get("/escalation_tickets", response_model=PaginatedResponse[EscalationTicketsOut])
async def list_escalation_tickets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = EscalationTicketsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/escalation_tickets/{entity_id}", response_model=EscalationTicketsOut)
async def get_escalation_tickets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await EscalationTicketsService(db).get(entity_id)

@router.post("/escalation_tickets", response_model=EscalationTicketsOut, status_code=status.HTTP_201_CREATED)
async def create_escalation_tickets(
    data: EscalationTicketsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await EscalationTicketsService(db).create(data)

@router.put("/escalation_tickets/{entity_id}", response_model=EscalationTicketsOut)
async def update_escalation_tickets(
    entity_id: uuid.UUID,
    data: EscalationTicketsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await EscalationTicketsService(db).update(entity_id, data)

@router.delete("/escalation_tickets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_escalation_tickets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await EscalationTicketsService(db).delete(entity_id)

@router.get("/experience_ledger", response_model=PaginatedResponse[ExperienceLedgerOut])
async def list_experience_ledger(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ExperienceLedgerService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/experience_ledger/{entity_id}", response_model=ExperienceLedgerOut)
async def get_experience_ledger(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ExperienceLedgerService(db).get(entity_id)

@router.post("/experience_ledger", response_model=ExperienceLedgerOut, status_code=status.HTTP_201_CREATED)
async def create_experience_ledger(
    data: ExperienceLedgerCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ExperienceLedgerService(db).create(data)

@router.put("/experience_ledger/{entity_id}", response_model=ExperienceLedgerOut)
async def update_experience_ledger(
    entity_id: uuid.UUID,
    data: ExperienceLedgerUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ExperienceLedgerService(db).update(entity_id, data)

@router.delete("/experience_ledger/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience_ledger(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ExperienceLedgerService(db).delete(entity_id)

@router.get("/experience_ledger_cold", response_model=PaginatedResponse[ExperienceLedgerColdOut])
async def list_experience_ledger_cold(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ExperienceLedgerColdService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/experience_ledger_cold/{entity_id}", response_model=ExperienceLedgerColdOut)
async def get_experience_ledger_cold(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ExperienceLedgerColdService(db).get(entity_id)

@router.post("/experience_ledger_cold", response_model=ExperienceLedgerColdOut, status_code=status.HTTP_201_CREATED)
async def create_experience_ledger_cold(
    data: ExperienceLedgerColdCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ExperienceLedgerColdService(db).create(data)

@router.put("/experience_ledger_cold/{entity_id}", response_model=ExperienceLedgerColdOut)
async def update_experience_ledger_cold(
    entity_id: uuid.UUID,
    data: ExperienceLedgerColdUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ExperienceLedgerColdService(db).update(entity_id, data)

@router.delete("/experience_ledger_cold/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience_ledger_cold(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ExperienceLedgerColdService(db).delete(entity_id)

@router.get("/lot_size_policies", response_model=PaginatedResponse[LotSizePoliciesOut])
async def list_lot_size_policies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = LotSizePoliciesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/lot_size_policies/{entity_id}", response_model=LotSizePoliciesOut)
async def get_lot_size_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await LotSizePoliciesService(db).get(entity_id)

@router.post("/lot_size_policies", response_model=LotSizePoliciesOut, status_code=status.HTTP_201_CREATED)
async def create_lot_size_policies(
    data: LotSizePoliciesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await LotSizePoliciesService(db).create(data)

@router.put("/lot_size_policies/{entity_id}", response_model=LotSizePoliciesOut)
async def update_lot_size_policies(
    entity_id: uuid.UUID,
    data: LotSizePoliciesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await LotSizePoliciesService(db).update(entity_id, data)

@router.delete("/lot_size_policies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lot_size_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await LotSizePoliciesService(db).delete(entity_id)

@router.get("/mrp_action_messages", response_model=PaginatedResponse[MrpActionMessagesOut])
async def list_mrp_action_messages(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpActionMessagesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_action_messages/{entity_id}", response_model=MrpActionMessagesOut)
async def get_mrp_action_messages(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpActionMessagesService(db).get(entity_id)

@router.post("/mrp_action_messages", response_model=MrpActionMessagesOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_action_messages(
    data: MrpActionMessagesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpActionMessagesService(db).create(data)

@router.put("/mrp_action_messages/{entity_id}", response_model=MrpActionMessagesOut)
async def update_mrp_action_messages(
    entity_id: uuid.UUID,
    data: MrpActionMessagesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpActionMessagesService(db).update(entity_id, data)

@router.delete("/mrp_action_messages/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_action_messages(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpActionMessagesService(db).delete(entity_id)

@router.get("/mrp_demand_records", response_model=PaginatedResponse[MrpDemandRecordsOut])
async def list_mrp_demand_records(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpDemandRecordsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_demand_records/{entity_id}", response_model=MrpDemandRecordsOut)
async def get_mrp_demand_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpDemandRecordsService(db).get(entity_id)

@router.post("/mrp_demand_records", response_model=MrpDemandRecordsOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_demand_records(
    data: MrpDemandRecordsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpDemandRecordsService(db).create(data)

@router.put("/mrp_demand_records/{entity_id}", response_model=MrpDemandRecordsOut)
async def update_mrp_demand_records(
    entity_id: uuid.UUID,
    data: MrpDemandRecordsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpDemandRecordsService(db).update(entity_id, data)

@router.delete("/mrp_demand_records/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_demand_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpDemandRecordsService(db).delete(entity_id)

@router.get("/mrp_exceptions", response_model=PaginatedResponse[MrpExceptionsOut])
async def list_mrp_exceptions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpExceptionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_exceptions/{entity_id}", response_model=MrpExceptionsOut)
async def get_mrp_exceptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpExceptionsService(db).get(entity_id)

@router.post("/mrp_exceptions", response_model=MrpExceptionsOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_exceptions(
    data: MrpExceptionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpExceptionsService(db).create(data)

@router.put("/mrp_exceptions/{entity_id}", response_model=MrpExceptionsOut)
async def update_mrp_exceptions(
    entity_id: uuid.UUID,
    data: MrpExceptionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpExceptionsService(db).update(entity_id, data)

@router.delete("/mrp_exceptions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_exceptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpExceptionsService(db).delete(entity_id)

@router.get("/mrp_pegging", response_model=PaginatedResponse[MrpPeggingOut])
async def list_mrp_pegging(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpPeggingService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_pegging/{entity_id}", response_model=MrpPeggingOut)
async def get_mrp_pegging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpPeggingService(db).get(entity_id)

@router.post("/mrp_pegging", response_model=MrpPeggingOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_pegging(
    data: MrpPeggingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpPeggingService(db).create(data)

@router.put("/mrp_pegging/{entity_id}", response_model=MrpPeggingOut)
async def update_mrp_pegging(
    entity_id: uuid.UUID,
    data: MrpPeggingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpPeggingService(db).update(entity_id, data)

@router.delete("/mrp_pegging/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_pegging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpPeggingService(db).delete(entity_id)

@router.get("/mrp_plans", response_model=PaginatedResponse[MrpPlansOut])
async def list_mrp_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpPlansService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_plans/{entity_id}", response_model=MrpPlansOut)
async def get_mrp_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpPlansService(db).get(entity_id)

@router.post("/mrp_plans", response_model=MrpPlansOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_plans(
    data: MrpPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpPlansService(db).create(data)

@router.put("/mrp_plans/{entity_id}", response_model=MrpPlansOut)
async def update_mrp_plans(
    entity_id: uuid.UUID,
    data: MrpPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpPlansService(db).update(entity_id, data)

@router.delete("/mrp_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpPlansService(db).delete(entity_id)

@router.get("/mrp_supply_records", response_model=PaginatedResponse[MrpSupplyRecordsOut])
async def list_mrp_supply_records(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = MrpSupplyRecordsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_supply_records/{entity_id}", response_model=MrpSupplyRecordsOut)
async def get_mrp_supply_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await MrpSupplyRecordsService(db).get(entity_id)

@router.post("/mrp_supply_records", response_model=MrpSupplyRecordsOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_supply_records(
    data: MrpSupplyRecordsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpSupplyRecordsService(db).create(data)

@router.put("/mrp_supply_records/{entity_id}", response_model=MrpSupplyRecordsOut)
async def update_mrp_supply_records(
    entity_id: uuid.UUID,
    data: MrpSupplyRecordsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await MrpSupplyRecordsService(db).update(entity_id, data)

@router.delete("/mrp_supply_records/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_supply_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await MrpSupplyRecordsService(db).delete(entity_id)

@router.get("/plan_scenarios", response_model=PaginatedResponse[PlanScenariosOut])
async def list_plan_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = PlanScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/plan_scenarios/{entity_id}", response_model=PlanScenariosOut)
async def get_plan_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await PlanScenariosService(db).get(entity_id)

@router.post("/plan_scenarios", response_model=PlanScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_plan_scenarios(
    data: PlanScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await PlanScenariosService(db).create(data)

@router.put("/plan_scenarios/{entity_id}", response_model=PlanScenariosOut)
async def update_plan_scenarios(
    entity_id: uuid.UUID,
    data: PlanScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await PlanScenariosService(db).update(entity_id, data)

@router.delete("/plan_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plan_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await PlanScenariosService(db).delete(entity_id)

@router.get("/planning_time_fences", response_model=PaginatedResponse[PlanningTimeFencesOut])
async def list_planning_time_fences(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = PlanningTimeFencesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/planning_time_fences/{entity_id}", response_model=PlanningTimeFencesOut)
async def get_planning_time_fences(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await PlanningTimeFencesService(db).get(entity_id)

@router.post("/planning_time_fences", response_model=PlanningTimeFencesOut, status_code=status.HTTP_201_CREATED)
async def create_planning_time_fences(
    data: PlanningTimeFencesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await PlanningTimeFencesService(db).create(data)

@router.put("/planning_time_fences/{entity_id}", response_model=PlanningTimeFencesOut)
async def update_planning_time_fences(
    entity_id: uuid.UUID,
    data: PlanningTimeFencesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await PlanningTimeFencesService(db).update(entity_id, data)

@router.delete("/planning_time_fences/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_planning_time_fences(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await PlanningTimeFencesService(db).delete(entity_id)

@router.get("/replenishment_plans", response_model=PaginatedResponse[ReplenishmentPlansOut])
async def list_replenishment_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ReplenishmentPlansService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/replenishment_plans/{entity_id}", response_model=ReplenishmentPlansOut)
async def get_replenishment_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ReplenishmentPlansService(db).get(entity_id)

@router.post("/replenishment_plans", response_model=ReplenishmentPlansOut, status_code=status.HTTP_201_CREATED)
async def create_replenishment_plans(
    data: ReplenishmentPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ReplenishmentPlansService(db).create(data)

@router.put("/replenishment_plans/{entity_id}", response_model=ReplenishmentPlansOut)
async def update_replenishment_plans(
    entity_id: uuid.UUID,
    data: ReplenishmentPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ReplenishmentPlansService(db).update(entity_id, data)

@router.delete("/replenishment_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_replenishment_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ReplenishmentPlansService(db).delete(entity_id)

@router.get("/scm_ai_agent_execution_logs", response_model=PaginatedResponse[ScmAiAgentExecutionLogsOut])
async def list_scm_ai_agent_execution_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiAgentExecutionLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_agent_execution_logs/{entity_id}", response_model=ScmAiAgentExecutionLogsOut)
async def get_scm_ai_agent_execution_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiAgentExecutionLogsService(db).get(entity_id)

@router.post("/scm_ai_agent_execution_logs", response_model=ScmAiAgentExecutionLogsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_agent_execution_logs(
    data: ScmAiAgentExecutionLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiAgentExecutionLogsService(db).create(data)

@router.put("/scm_ai_agent_execution_logs/{entity_id}", response_model=ScmAiAgentExecutionLogsOut)
async def update_scm_ai_agent_execution_logs(
    entity_id: uuid.UUID,
    data: ScmAiAgentExecutionLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiAgentExecutionLogsService(db).update(entity_id, data)

@router.delete("/scm_ai_agent_execution_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_agent_execution_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiAgentExecutionLogsService(db).delete(entity_id)

@router.get("/scm_ai_cost_tracking", response_model=PaginatedResponse[ScmAiCostTrackingOut])
async def list_scm_ai_cost_tracking(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiCostTrackingService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_cost_tracking/{entity_id}", response_model=ScmAiCostTrackingOut)
async def get_scm_ai_cost_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiCostTrackingService(db).get(entity_id)

@router.post("/scm_ai_cost_tracking", response_model=ScmAiCostTrackingOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_cost_tracking(
    data: ScmAiCostTrackingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiCostTrackingService(db).create(data)

@router.put("/scm_ai_cost_tracking/{entity_id}", response_model=ScmAiCostTrackingOut)
async def update_scm_ai_cost_tracking(
    entity_id: uuid.UUID,
    data: ScmAiCostTrackingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiCostTrackingService(db).update(entity_id, data)

@router.delete("/scm_ai_cost_tracking/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_cost_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiCostTrackingService(db).delete(entity_id)

@router.get("/scm_ai_decisions", response_model=PaginatedResponse[ScmAiDecisionsOut])
async def list_scm_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_decisions/{entity_id}", response_model=ScmAiDecisionsOut)
async def get_scm_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiDecisionsService(db).get(entity_id)

@router.post("/scm_ai_decisions", response_model=ScmAiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_decisions(
    data: ScmAiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiDecisionsService(db).create(data)

@router.put("/scm_ai_decisions/{entity_id}", response_model=ScmAiDecisionsOut)
async def update_scm_ai_decisions(
    entity_id: uuid.UUID,
    data: ScmAiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiDecisionsService(db).update(entity_id, data)

@router.delete("/scm_ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiDecisionsService(db).delete(entity_id)

@router.get("/scm_ai_experiment_tracking", response_model=PaginatedResponse[ScmAiExperimentTrackingOut])
async def list_scm_ai_experiment_tracking(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiExperimentTrackingService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["experiment_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_experiment_tracking/{entity_id}", response_model=ScmAiExperimentTrackingOut)
async def get_scm_ai_experiment_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiExperimentTrackingService(db).get(entity_id)

@router.post("/scm_ai_experiment_tracking", response_model=ScmAiExperimentTrackingOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_experiment_tracking(
    data: ScmAiExperimentTrackingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiExperimentTrackingService(db).create(data)

@router.put("/scm_ai_experiment_tracking/{entity_id}", response_model=ScmAiExperimentTrackingOut)
async def update_scm_ai_experiment_tracking(
    entity_id: uuid.UUID,
    data: ScmAiExperimentTrackingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiExperimentTrackingService(db).update(entity_id, data)

@router.delete("/scm_ai_experiment_tracking/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_experiment_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiExperimentTrackingService(db).delete(entity_id)

@router.get("/scm_ai_feature_store", response_model=PaginatedResponse[ScmAiFeatureStoreOut])
async def list_scm_ai_feature_store(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiFeatureStoreService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["feature_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_feature_store/{entity_id}", response_model=ScmAiFeatureStoreOut)
async def get_scm_ai_feature_store(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiFeatureStoreService(db).get(entity_id)

@router.post("/scm_ai_feature_store", response_model=ScmAiFeatureStoreOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_feature_store(
    data: ScmAiFeatureStoreCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiFeatureStoreService(db).create(data)

@router.put("/scm_ai_feature_store/{entity_id}", response_model=ScmAiFeatureStoreOut)
async def update_scm_ai_feature_store(
    entity_id: uuid.UUID,
    data: ScmAiFeatureStoreUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiFeatureStoreService(db).update(entity_id, data)

@router.delete("/scm_ai_feature_store/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_feature_store(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiFeatureStoreService(db).delete(entity_id)

@router.get("/scm_ai_model_registry", response_model=PaginatedResponse[ScmAiModelRegistryOut])
async def list_scm_ai_model_registry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiModelRegistryService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_model_registry/{entity_id}", response_model=ScmAiModelRegistryOut)
async def get_scm_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiModelRegistryService(db).get(entity_id)

@router.post("/scm_ai_model_registry", response_model=ScmAiModelRegistryOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_model_registry(
    data: ScmAiModelRegistryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiModelRegistryService(db).create(data)

@router.put("/scm_ai_model_registry/{entity_id}", response_model=ScmAiModelRegistryOut)
async def update_scm_ai_model_registry(
    entity_id: uuid.UUID,
    data: ScmAiModelRegistryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiModelRegistryService(db).update(entity_id, data)

@router.delete("/scm_ai_model_registry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiModelRegistryService(db).delete(entity_id)

@router.get("/scm_ai_workflow_state", response_model=PaginatedResponse[ScmAiWorkflowStateOut])
async def list_scm_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ai_workflow_state/{entity_id}", response_model=ScmAiWorkflowStateOut)
async def get_scm_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAiWorkflowStateService(db).get(entity_id)

@router.post("/scm_ai_workflow_state", response_model=ScmAiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ai_workflow_state(
    data: ScmAiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiWorkflowStateService(db).create(data)

@router.put("/scm_ai_workflow_state/{entity_id}", response_model=ScmAiWorkflowStateOut)
async def update_scm_ai_workflow_state(
    entity_id: uuid.UUID,
    data: ScmAiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAiWorkflowStateService(db).update(entity_id, data)

@router.delete("/scm_ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAiWorkflowStateService(db).delete(entity_id)

@router.get("/scm_alert_escalations", response_model=PaginatedResponse[ScmAlertEscalationsOut])
async def list_scm_alert_escalations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlertEscalationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_alert_escalations/{entity_id}", response_model=ScmAlertEscalationsOut)
async def get_scm_alert_escalations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlertEscalationsService(db).get(entity_id)

@router.post("/scm_alert_escalations", response_model=ScmAlertEscalationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_alert_escalations(
    data: ScmAlertEscalationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertEscalationsService(db).create(data)

@router.put("/scm_alert_escalations/{entity_id}", response_model=ScmAlertEscalationsOut)
async def update_scm_alert_escalations(
    entity_id: uuid.UUID,
    data: ScmAlertEscalationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertEscalationsService(db).update(entity_id, data)

@router.delete("/scm_alert_escalations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_alert_escalations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlertEscalationsService(db).delete(entity_id)

@router.get("/scm_alert_notifications", response_model=PaginatedResponse[ScmAlertNotificationsOut])
async def list_scm_alert_notifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlertNotificationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_alert_notifications/{entity_id}", response_model=ScmAlertNotificationsOut)
async def get_scm_alert_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlertNotificationsService(db).get(entity_id)

@router.post("/scm_alert_notifications", response_model=ScmAlertNotificationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_alert_notifications(
    data: ScmAlertNotificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertNotificationsService(db).create(data)

@router.put("/scm_alert_notifications/{entity_id}", response_model=ScmAlertNotificationsOut)
async def update_scm_alert_notifications(
    entity_id: uuid.UUID,
    data: ScmAlertNotificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertNotificationsService(db).update(entity_id, data)

@router.delete("/scm_alert_notifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_alert_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlertNotificationsService(db).delete(entity_id)

@router.get("/scm_alert_rules", response_model=PaginatedResponse[ScmAlertRulesOut])
async def list_scm_alert_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlertRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_alert_rules/{entity_id}", response_model=ScmAlertRulesOut)
async def get_scm_alert_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlertRulesService(db).get(entity_id)

@router.post("/scm_alert_rules", response_model=ScmAlertRulesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_alert_rules(
    data: ScmAlertRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertRulesService(db).create(data)

@router.put("/scm_alert_rules/{entity_id}", response_model=ScmAlertRulesOut)
async def update_scm_alert_rules(
    entity_id: uuid.UUID,
    data: ScmAlertRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertRulesService(db).update(entity_id, data)

@router.delete("/scm_alert_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_alert_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlertRulesService(db).delete(entity_id)

@router.get("/scm_alert_types", response_model=PaginatedResponse[ScmAlertTypesOut])
async def list_scm_alert_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlertTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_alert_types/{entity_id}", response_model=ScmAlertTypesOut)
async def get_scm_alert_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlertTypesService(db).get(entity_id)

@router.post("/scm_alert_types", response_model=ScmAlertTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_alert_types(
    data: ScmAlertTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertTypesService(db).create(data)

@router.put("/scm_alert_types/{entity_id}", response_model=ScmAlertTypesOut)
async def update_scm_alert_types(
    entity_id: uuid.UUID,
    data: ScmAlertTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertTypesService(db).update(entity_id, data)

@router.delete("/scm_alert_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_alert_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlertTypesService(db).delete(entity_id)

@router.get("/scm_alerts", response_model=PaginatedResponse[ScmAlertsOut])
async def list_scm_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlertsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_alerts/{entity_id}", response_model=ScmAlertsOut)
async def get_scm_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlertsService(db).get(entity_id)

@router.post("/scm_alerts", response_model=ScmAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_alerts(
    data: ScmAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertsService(db).create(data)

@router.put("/scm_alerts/{entity_id}", response_model=ScmAlertsOut)
async def update_scm_alerts(
    entity_id: uuid.UUID,
    data: ScmAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlertsService(db).update(entity_id, data)

@router.delete("/scm_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlertsService(db).delete(entity_id)

@router.get("/scm_algorithm_tests", response_model=PaginatedResponse[ScmAlgorithmTestsOut])
async def list_scm_algorithm_tests(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlgorithmTestsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["test_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_algorithm_tests/{entity_id}", response_model=ScmAlgorithmTestsOut)
async def get_scm_algorithm_tests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlgorithmTestsService(db).get(entity_id)

@router.post("/scm_algorithm_tests", response_model=ScmAlgorithmTestsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_algorithm_tests(
    data: ScmAlgorithmTestsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmTestsService(db).create(data)

@router.put("/scm_algorithm_tests/{entity_id}", response_model=ScmAlgorithmTestsOut)
async def update_scm_algorithm_tests(
    entity_id: uuid.UUID,
    data: ScmAlgorithmTestsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmTestsService(db).update(entity_id, data)

@router.delete("/scm_algorithm_tests/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_algorithm_tests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlgorithmTestsService(db).delete(entity_id)

@router.get("/scm_algorithm_versions", response_model=PaginatedResponse[ScmAlgorithmVersionsOut])
async def list_scm_algorithm_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlgorithmVersionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["version_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_algorithm_versions/{entity_id}", response_model=ScmAlgorithmVersionsOut)
async def get_scm_algorithm_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlgorithmVersionsService(db).get(entity_id)

@router.post("/scm_algorithm_versions", response_model=ScmAlgorithmVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_algorithm_versions(
    data: ScmAlgorithmVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmVersionsService(db).create(data)

@router.put("/scm_algorithm_versions/{entity_id}", response_model=ScmAlgorithmVersionsOut)
async def update_scm_algorithm_versions(
    entity_id: uuid.UUID,
    data: ScmAlgorithmVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmVersionsService(db).update(entity_id, data)

@router.delete("/scm_algorithm_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_algorithm_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlgorithmVersionsService(db).delete(entity_id)

@router.get("/scm_algorithms", response_model=PaginatedResponse[ScmAlgorithmsOut])
async def list_scm_algorithms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmAlgorithmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["algorithm_code", "algorithm_name", "code_repository_url"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_algorithms/{entity_id}", response_model=ScmAlgorithmsOut)
async def get_scm_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmAlgorithmsService(db).get(entity_id)

@router.post("/scm_algorithms", response_model=ScmAlgorithmsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_algorithms(
    data: ScmAlgorithmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmsService(db).create(data)

@router.put("/scm_algorithms/{entity_id}", response_model=ScmAlgorithmsOut)
async def update_scm_algorithms(
    entity_id: uuid.UUID,
    data: ScmAlgorithmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmAlgorithmsService(db).update(entity_id, data)

@router.delete("/scm_algorithms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmAlgorithmsService(db).delete(entity_id)

@router.get("/scm_bin_packing_items", response_model=PaginatedResponse[ScmBinPackingItemsOut])
async def list_scm_bin_packing_items(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmBinPackingItemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_bin_packing_items/{entity_id}", response_model=ScmBinPackingItemsOut)
async def get_scm_bin_packing_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmBinPackingItemsService(db).get(entity_id)

@router.post("/scm_bin_packing_items", response_model=ScmBinPackingItemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_bin_packing_items(
    data: ScmBinPackingItemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingItemsService(db).create(data)

@router.put("/scm_bin_packing_items/{entity_id}", response_model=ScmBinPackingItemsOut)
async def update_scm_bin_packing_items(
    entity_id: uuid.UUID,
    data: ScmBinPackingItemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingItemsService(db).update(entity_id, data)

@router.delete("/scm_bin_packing_items/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_bin_packing_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmBinPackingItemsService(db).delete(entity_id)

@router.get("/scm_bin_packing_metrics", response_model=PaginatedResponse[ScmBinPackingMetricsOut])
async def list_scm_bin_packing_metrics(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmBinPackingMetricsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_bin_packing_metrics/{entity_id}", response_model=ScmBinPackingMetricsOut)
async def get_scm_bin_packing_metrics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmBinPackingMetricsService(db).get(entity_id)

@router.post("/scm_bin_packing_metrics", response_model=ScmBinPackingMetricsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_bin_packing_metrics(
    data: ScmBinPackingMetricsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingMetricsService(db).create(data)

@router.put("/scm_bin_packing_metrics/{entity_id}", response_model=ScmBinPackingMetricsOut)
async def update_scm_bin_packing_metrics(
    entity_id: uuid.UUID,
    data: ScmBinPackingMetricsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingMetricsService(db).update(entity_id, data)

@router.delete("/scm_bin_packing_metrics/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_bin_packing_metrics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmBinPackingMetricsService(db).delete(entity_id)

@router.get("/scm_bin_packing_problems", response_model=PaginatedResponse[ScmBinPackingProblemsOut])
async def list_scm_bin_packing_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmBinPackingProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_bin_packing_problems/{entity_id}", response_model=ScmBinPackingProblemsOut)
async def get_scm_bin_packing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmBinPackingProblemsService(db).get(entity_id)

@router.post("/scm_bin_packing_problems", response_model=ScmBinPackingProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_bin_packing_problems(
    data: ScmBinPackingProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingProblemsService(db).create(data)

@router.put("/scm_bin_packing_problems/{entity_id}", response_model=ScmBinPackingProblemsOut)
async def update_scm_bin_packing_problems(
    entity_id: uuid.UUID,
    data: ScmBinPackingProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingProblemsService(db).update(entity_id, data)

@router.delete("/scm_bin_packing_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_bin_packing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmBinPackingProblemsService(db).delete(entity_id)

@router.get("/scm_bin_packing_results", response_model=PaginatedResponse[ScmBinPackingResultsOut])
async def list_scm_bin_packing_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmBinPackingResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_bin_packing_results/{entity_id}", response_model=ScmBinPackingResultsOut)
async def get_scm_bin_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmBinPackingResultsService(db).get(entity_id)

@router.post("/scm_bin_packing_results", response_model=ScmBinPackingResultsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_bin_packing_results(
    data: ScmBinPackingResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingResultsService(db).create(data)

@router.put("/scm_bin_packing_results/{entity_id}", response_model=ScmBinPackingResultsOut)
async def update_scm_bin_packing_results(
    entity_id: uuid.UUID,
    data: ScmBinPackingResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinPackingResultsService(db).update(entity_id, data)

@router.delete("/scm_bin_packing_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_bin_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmBinPackingResultsService(db).delete(entity_id)

@router.get("/scm_bin_types", response_model=PaginatedResponse[ScmBinTypesOut])
async def list_scm_bin_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmBinTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["bin_type_code", "bin_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_bin_types/{entity_id}", response_model=ScmBinTypesOut)
async def get_scm_bin_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmBinTypesService(db).get(entity_id)

@router.post("/scm_bin_types", response_model=ScmBinTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_bin_types(
    data: ScmBinTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinTypesService(db).create(data)

@router.put("/scm_bin_types/{entity_id}", response_model=ScmBinTypesOut)
async def update_scm_bin_types(
    entity_id: uuid.UUID,
    data: ScmBinTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmBinTypesService(db).update(entity_id, data)

@router.delete("/scm_bin_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_bin_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmBinTypesService(db).delete(entity_id)

@router.get("/scm_demand_classes", response_model=PaginatedResponse[ScmDemandClassesOut])
async def list_scm_demand_classes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDemandClassesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["class_code", "class_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_demand_classes/{entity_id}", response_model=ScmDemandClassesOut)
async def get_scm_demand_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDemandClassesService(db).get(entity_id)

@router.post("/scm_demand_classes", response_model=ScmDemandClassesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_demand_classes(
    data: ScmDemandClassesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandClassesService(db).create(data)

@router.put("/scm_demand_classes/{entity_id}", response_model=ScmDemandClassesOut)
async def update_scm_demand_classes(
    entity_id: uuid.UUID,
    data: ScmDemandClassesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandClassesService(db).update(entity_id, data)

@router.delete("/scm_demand_classes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_demand_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDemandClassesService(db).delete(entity_id)

@router.get("/scm_demand_drivers", response_model=PaginatedResponse[ScmDemandDriversOut])
async def list_scm_demand_drivers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDemandDriversService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["driver_code", "driver_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_demand_drivers/{entity_id}", response_model=ScmDemandDriversOut)
async def get_scm_demand_drivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDemandDriversService(db).get(entity_id)

@router.post("/scm_demand_drivers", response_model=ScmDemandDriversOut, status_code=status.HTTP_201_CREATED)
async def create_scm_demand_drivers(
    data: ScmDemandDriversCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandDriversService(db).create(data)

@router.put("/scm_demand_drivers/{entity_id}", response_model=ScmDemandDriversOut)
async def update_scm_demand_drivers(
    entity_id: uuid.UUID,
    data: ScmDemandDriversUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandDriversService(db).update(entity_id, data)

@router.delete("/scm_demand_drivers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_demand_drivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDemandDriversService(db).delete(entity_id)

@router.get("/scm_demand_sources", response_model=PaginatedResponse[ScmDemandSourcesOut])
async def list_scm_demand_sources(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDemandSourcesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["source_code", "source_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_demand_sources/{entity_id}", response_model=ScmDemandSourcesOut)
async def get_scm_demand_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDemandSourcesService(db).get(entity_id)

@router.post("/scm_demand_sources", response_model=ScmDemandSourcesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_demand_sources(
    data: ScmDemandSourcesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandSourcesService(db).create(data)

@router.put("/scm_demand_sources/{entity_id}", response_model=ScmDemandSourcesOut)
async def update_scm_demand_sources(
    entity_id: uuid.UUID,
    data: ScmDemandSourcesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandSourcesService(db).update(entity_id, data)

@router.delete("/scm_demand_sources/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_demand_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDemandSourcesService(db).delete(entity_id)

@router.get("/scm_demand_time_series", response_model=PaginatedResponse[ScmDemandTimeSeriesOut])
async def list_scm_demand_time_series(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDemandTimeSeriesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_demand_time_series/{entity_id}", response_model=ScmDemandTimeSeriesOut)
async def get_scm_demand_time_series(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDemandTimeSeriesService(db).get(entity_id)

@router.post("/scm_demand_time_series", response_model=ScmDemandTimeSeriesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_demand_time_series(
    data: ScmDemandTimeSeriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandTimeSeriesService(db).create(data)

@router.put("/scm_demand_time_series/{entity_id}", response_model=ScmDemandTimeSeriesOut)
async def update_scm_demand_time_series(
    entity_id: uuid.UUID,
    data: ScmDemandTimeSeriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDemandTimeSeriesService(db).update(entity_id, data)

@router.delete("/scm_demand_time_series/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_demand_time_series(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDemandTimeSeriesService(db).delete(entity_id)

@router.get("/scm_distribution_allocation_rules", response_model=PaginatedResponse[ScmDistributionAllocationRulesOut])
async def list_scm_distribution_allocation_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionAllocationRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_allocation_rules/{entity_id}", response_model=ScmDistributionAllocationRulesOut)
async def get_scm_distribution_allocation_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionAllocationRulesService(db).get(entity_id)

@router.post("/scm_distribution_allocation_rules", response_model=ScmDistributionAllocationRulesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_allocation_rules(
    data: ScmDistributionAllocationRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionAllocationRulesService(db).create(data)

@router.put("/scm_distribution_allocation_rules/{entity_id}", response_model=ScmDistributionAllocationRulesOut)
async def update_scm_distribution_allocation_rules(
    entity_id: uuid.UUID,
    data: ScmDistributionAllocationRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionAllocationRulesService(db).update(entity_id, data)

@router.delete("/scm_distribution_allocation_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_allocation_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionAllocationRulesService(db).delete(entity_id)

@router.get("/scm_distribution_cost_to_serve", response_model=PaginatedResponse[ScmDistributionCostToServeOut])
async def list_scm_distribution_cost_to_serve(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionCostToServeService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_cost_to_serve/{entity_id}", response_model=ScmDistributionCostToServeOut)
async def get_scm_distribution_cost_to_serve(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionCostToServeService(db).get(entity_id)

@router.post("/scm_distribution_cost_to_serve", response_model=ScmDistributionCostToServeOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_cost_to_serve(
    data: ScmDistributionCostToServeCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionCostToServeService(db).create(data)

@router.put("/scm_distribution_cost_to_serve/{entity_id}", response_model=ScmDistributionCostToServeOut)
async def update_scm_distribution_cost_to_serve(
    entity_id: uuid.UUID,
    data: ScmDistributionCostToServeUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionCostToServeService(db).update(entity_id, data)

@router.delete("/scm_distribution_cost_to_serve/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_cost_to_serve(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionCostToServeService(db).delete(entity_id)

@router.get("/scm_distribution_network", response_model=PaginatedResponse[ScmDistributionNetworkOut])
async def list_scm_distribution_network(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionNetworkService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["node_code", "node_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_network/{entity_id}", response_model=ScmDistributionNetworkOut)
async def get_scm_distribution_network(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionNetworkService(db).get(entity_id)

@router.post("/scm_distribution_network", response_model=ScmDistributionNetworkOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_network(
    data: ScmDistributionNetworkCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionNetworkService(db).create(data)

@router.put("/scm_distribution_network/{entity_id}", response_model=ScmDistributionNetworkOut)
async def update_scm_distribution_network(
    entity_id: uuid.UUID,
    data: ScmDistributionNetworkUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionNetworkService(db).update(entity_id, data)

@router.delete("/scm_distribution_network/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_network(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionNetworkService(db).delete(entity_id)

@router.get("/scm_distribution_plan_lines", response_model=PaginatedResponse[ScmDistributionPlanLinesOut])
async def list_scm_distribution_plan_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionPlanLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_plan_lines/{entity_id}", response_model=ScmDistributionPlanLinesOut)
async def get_scm_distribution_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionPlanLinesService(db).get(entity_id)

@router.post("/scm_distribution_plan_lines", response_model=ScmDistributionPlanLinesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_plan_lines(
    data: ScmDistributionPlanLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionPlanLinesService(db).create(data)

@router.put("/scm_distribution_plan_lines/{entity_id}", response_model=ScmDistributionPlanLinesOut)
async def update_scm_distribution_plan_lines(
    entity_id: uuid.UUID,
    data: ScmDistributionPlanLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionPlanLinesService(db).update(entity_id, data)

@router.delete("/scm_distribution_plan_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionPlanLinesService(db).delete(entity_id)

@router.get("/scm_distribution_plans", response_model=PaginatedResponse[ScmDistributionPlansOut])
async def list_scm_distribution_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionPlansService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_plans/{entity_id}", response_model=ScmDistributionPlansOut)
async def get_scm_distribution_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionPlansService(db).get(entity_id)

@router.post("/scm_distribution_plans", response_model=ScmDistributionPlansOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_plans(
    data: ScmDistributionPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionPlansService(db).create(data)

@router.put("/scm_distribution_plans/{entity_id}", response_model=ScmDistributionPlansOut)
async def update_scm_distribution_plans(
    entity_id: uuid.UUID,
    data: ScmDistributionPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionPlansService(db).update(entity_id, data)

@router.delete("/scm_distribution_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionPlansService(db).delete(entity_id)

@router.get("/scm_distribution_service_levels", response_model=PaginatedResponse[ScmDistributionServiceLevelsOut])
async def list_scm_distribution_service_levels(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmDistributionServiceLevelsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_distribution_service_levels/{entity_id}", response_model=ScmDistributionServiceLevelsOut)
async def get_scm_distribution_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmDistributionServiceLevelsService(db).get(entity_id)

@router.post("/scm_distribution_service_levels", response_model=ScmDistributionServiceLevelsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_distribution_service_levels(
    data: ScmDistributionServiceLevelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionServiceLevelsService(db).create(data)

@router.put("/scm_distribution_service_levels/{entity_id}", response_model=ScmDistributionServiceLevelsOut)
async def update_scm_distribution_service_levels(
    entity_id: uuid.UUID,
    data: ScmDistributionServiceLevelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmDistributionServiceLevelsService(db).update(entity_id, data)

@router.delete("/scm_distribution_service_levels/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_distribution_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmDistributionServiceLevelsService(db).delete(entity_id)

@router.get("/scm_forecast_accuracy", response_model=PaginatedResponse[ScmForecastAccuracyOut])
async def list_scm_forecast_accuracy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmForecastAccuracyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_forecast_accuracy/{entity_id}", response_model=ScmForecastAccuracyOut)
async def get_scm_forecast_accuracy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmForecastAccuracyService(db).get(entity_id)

@router.post("/scm_forecast_accuracy", response_model=ScmForecastAccuracyOut, status_code=status.HTTP_201_CREATED)
async def create_scm_forecast_accuracy(
    data: ScmForecastAccuracyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastAccuracyService(db).create(data)

@router.put("/scm_forecast_accuracy/{entity_id}", response_model=ScmForecastAccuracyOut)
async def update_scm_forecast_accuracy(
    entity_id: uuid.UUID,
    data: ScmForecastAccuracyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastAccuracyService(db).update(entity_id, data)

@router.delete("/scm_forecast_accuracy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_forecast_accuracy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmForecastAccuracyService(db).delete(entity_id)

@router.get("/scm_forecast_models", response_model=PaginatedResponse[ScmForecastModelsOut])
async def list_scm_forecast_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmForecastModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_forecast_models/{entity_id}", response_model=ScmForecastModelsOut)
async def get_scm_forecast_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmForecastModelsService(db).get(entity_id)

@router.post("/scm_forecast_models", response_model=ScmForecastModelsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_forecast_models(
    data: ScmForecastModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastModelsService(db).create(data)

@router.put("/scm_forecast_models/{entity_id}", response_model=ScmForecastModelsOut)
async def update_scm_forecast_models(
    entity_id: uuid.UUID,
    data: ScmForecastModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastModelsService(db).update(entity_id, data)

@router.delete("/scm_forecast_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_forecast_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmForecastModelsService(db).delete(entity_id)

@router.get("/scm_forecast_values", response_model=PaginatedResponse[ScmForecastValuesOut])
async def list_scm_forecast_values(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmForecastValuesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_forecast_values/{entity_id}", response_model=ScmForecastValuesOut)
async def get_scm_forecast_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmForecastValuesService(db).get(entity_id)

@router.post("/scm_forecast_values", response_model=ScmForecastValuesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_forecast_values(
    data: ScmForecastValuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastValuesService(db).create(data)

@router.put("/scm_forecast_values/{entity_id}", response_model=ScmForecastValuesOut)
async def update_scm_forecast_values(
    entity_id: uuid.UUID,
    data: ScmForecastValuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastValuesService(db).update(entity_id, data)

@router.delete("/scm_forecast_values/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_forecast_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmForecastValuesService(db).delete(entity_id)

@router.get("/scm_forecast_versions", response_model=PaginatedResponse[ScmForecastVersionsOut])
async def list_scm_forecast_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmForecastVersionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["version_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_forecast_versions/{entity_id}", response_model=ScmForecastVersionsOut)
async def get_scm_forecast_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmForecastVersionsService(db).get(entity_id)

@router.post("/scm_forecast_versions", response_model=ScmForecastVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_forecast_versions(
    data: ScmForecastVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastVersionsService(db).create(data)

@router.put("/scm_forecast_versions/{entity_id}", response_model=ScmForecastVersionsOut)
async def update_scm_forecast_versions(
    entity_id: uuid.UUID,
    data: ScmForecastVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmForecastVersionsService(db).update(entity_id, data)

@router.delete("/scm_forecast_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_forecast_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmForecastVersionsService(db).delete(entity_id)

@router.get("/scm_integration_connections", response_model=PaginatedResponse[ScmIntegrationConnectionsOut])
async def list_scm_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmIntegrationConnectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["connection_code", "connection_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_integration_connections/{entity_id}", response_model=ScmIntegrationConnectionsOut)
async def get_scm_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmIntegrationConnectionsService(db).get(entity_id)

@router.post("/scm_integration_connections", response_model=ScmIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_integration_connections(
    data: ScmIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationConnectionsService(db).create(data)

@router.put("/scm_integration_connections/{entity_id}", response_model=ScmIntegrationConnectionsOut)
async def update_scm_integration_connections(
    entity_id: uuid.UUID,
    data: ScmIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/scm_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmIntegrationConnectionsService(db).delete(entity_id)

@router.get("/scm_integration_logs", response_model=PaginatedResponse[ScmIntegrationLogsOut])
async def list_scm_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmIntegrationLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_integration_logs/{entity_id}", response_model=ScmIntegrationLogsOut)
async def get_scm_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmIntegrationLogsService(db).get(entity_id)

@router.post("/scm_integration_logs", response_model=ScmIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_integration_logs(
    data: ScmIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationLogsService(db).create(data)

@router.put("/scm_integration_logs/{entity_id}", response_model=ScmIntegrationLogsOut)
async def update_scm_integration_logs(
    entity_id: uuid.UUID,
    data: ScmIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationLogsService(db).update(entity_id, data)

@router.delete("/scm_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmIntegrationLogsService(db).delete(entity_id)

@router.get("/scm_integration_mappings", response_model=PaginatedResponse[ScmIntegrationMappingsOut])
async def list_scm_integration_mappings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmIntegrationMappingsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["mapping_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_integration_mappings/{entity_id}", response_model=ScmIntegrationMappingsOut)
async def get_scm_integration_mappings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmIntegrationMappingsService(db).get(entity_id)

@router.post("/scm_integration_mappings", response_model=ScmIntegrationMappingsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_integration_mappings(
    data: ScmIntegrationMappingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationMappingsService(db).create(data)

@router.put("/scm_integration_mappings/{entity_id}", response_model=ScmIntegrationMappingsOut)
async def update_scm_integration_mappings(
    entity_id: uuid.UUID,
    data: ScmIntegrationMappingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmIntegrationMappingsService(db).update(entity_id, data)

@router.delete("/scm_integration_mappings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_integration_mappings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmIntegrationMappingsService(db).delete(entity_id)

@router.get("/scm_inventory_aging", response_model=PaginatedResponse[ScmInventoryAgingOut])
async def list_scm_inventory_aging(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryAgingService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_aging/{entity_id}", response_model=ScmInventoryAgingOut)
async def get_scm_inventory_aging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryAgingService(db).get(entity_id)

@router.post("/scm_inventory_aging", response_model=ScmInventoryAgingOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_aging(
    data: ScmInventoryAgingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryAgingService(db).create(data)

@router.put("/scm_inventory_aging/{entity_id}", response_model=ScmInventoryAgingOut)
async def update_scm_inventory_aging(
    entity_id: uuid.UUID,
    data: ScmInventoryAgingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryAgingService(db).update(entity_id, data)

@router.delete("/scm_inventory_aging/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_aging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryAgingService(db).delete(entity_id)

@router.get("/scm_inventory_classifications", response_model=PaginatedResponse[ScmInventoryClassificationsOut])
async def list_scm_inventory_classifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryClassificationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_classifications/{entity_id}", response_model=ScmInventoryClassificationsOut)
async def get_scm_inventory_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryClassificationsService(db).get(entity_id)

@router.post("/scm_inventory_classifications", response_model=ScmInventoryClassificationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_classifications(
    data: ScmInventoryClassificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryClassificationsService(db).create(data)

@router.put("/scm_inventory_classifications/{entity_id}", response_model=ScmInventoryClassificationsOut)
async def update_scm_inventory_classifications(
    entity_id: uuid.UUID,
    data: ScmInventoryClassificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryClassificationsService(db).update(entity_id, data)

@router.delete("/scm_inventory_classifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryClassificationsService(db).delete(entity_id)

@router.get("/scm_inventory_health", response_model=PaginatedResponse[ScmInventoryHealthOut])
async def list_scm_inventory_health(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryHealthService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_health/{entity_id}", response_model=ScmInventoryHealthOut)
async def get_scm_inventory_health(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryHealthService(db).get(entity_id)

@router.post("/scm_inventory_health", response_model=ScmInventoryHealthOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_health(
    data: ScmInventoryHealthCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryHealthService(db).create(data)

@router.put("/scm_inventory_health/{entity_id}", response_model=ScmInventoryHealthOut)
async def update_scm_inventory_health(
    entity_id: uuid.UUID,
    data: ScmInventoryHealthUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryHealthService(db).update(entity_id, data)

@router.delete("/scm_inventory_health/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_health(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryHealthService(db).delete(entity_id)

@router.get("/scm_inventory_optimization_params", response_model=PaginatedResponse[ScmInventoryOptimizationParamsOut])
async def list_scm_inventory_optimization_params(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryOptimizationParamsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_optimization_params/{entity_id}", response_model=ScmInventoryOptimizationParamsOut)
async def get_scm_inventory_optimization_params(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryOptimizationParamsService(db).get(entity_id)

@router.post("/scm_inventory_optimization_params", response_model=ScmInventoryOptimizationParamsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_optimization_params(
    data: ScmInventoryOptimizationParamsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryOptimizationParamsService(db).create(data)

@router.put("/scm_inventory_optimization_params/{entity_id}", response_model=ScmInventoryOptimizationParamsOut)
async def update_scm_inventory_optimization_params(
    entity_id: uuid.UUID,
    data: ScmInventoryOptimizationParamsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryOptimizationParamsService(db).update(entity_id, data)

@router.delete("/scm_inventory_optimization_params/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_optimization_params(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryOptimizationParamsService(db).delete(entity_id)

@router.get("/scm_inventory_policies", response_model=PaginatedResponse[ScmInventoryPoliciesOut])
async def list_scm_inventory_policies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryPoliciesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["policy_code", "policy_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_policies/{entity_id}", response_model=ScmInventoryPoliciesOut)
async def get_scm_inventory_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryPoliciesService(db).get(entity_id)

@router.post("/scm_inventory_policies", response_model=ScmInventoryPoliciesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_policies(
    data: ScmInventoryPoliciesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryPoliciesService(db).create(data)

@router.put("/scm_inventory_policies/{entity_id}", response_model=ScmInventoryPoliciesOut)
async def update_scm_inventory_policies(
    entity_id: uuid.UUID,
    data: ScmInventoryPoliciesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryPoliciesService(db).update(entity_id, data)

@router.delete("/scm_inventory_policies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryPoliciesService(db).delete(entity_id)

@router.get("/scm_inventory_recommendations", response_model=PaginatedResponse[ScmInventoryRecommendationsOut])
async def list_scm_inventory_recommendations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryRecommendationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["reason_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_recommendations/{entity_id}", response_model=ScmInventoryRecommendationsOut)
async def get_scm_inventory_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryRecommendationsService(db).get(entity_id)

@router.post("/scm_inventory_recommendations", response_model=ScmInventoryRecommendationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_recommendations(
    data: ScmInventoryRecommendationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryRecommendationsService(db).create(data)

@router.put("/scm_inventory_recommendations/{entity_id}", response_model=ScmInventoryRecommendationsOut)
async def update_scm_inventory_recommendations(
    entity_id: uuid.UUID,
    data: ScmInventoryRecommendationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryRecommendationsService(db).update(entity_id, data)

@router.delete("/scm_inventory_recommendations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryRecommendationsService(db).delete(entity_id)

@router.get("/scm_inventory_targets", response_model=PaginatedResponse[ScmInventoryTargetsOut])
async def list_scm_inventory_targets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmInventoryTargetsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_inventory_targets/{entity_id}", response_model=ScmInventoryTargetsOut)
async def get_scm_inventory_targets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmInventoryTargetsService(db).get(entity_id)

@router.post("/scm_inventory_targets", response_model=ScmInventoryTargetsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_inventory_targets(
    data: ScmInventoryTargetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryTargetsService(db).create(data)

@router.put("/scm_inventory_targets/{entity_id}", response_model=ScmInventoryTargetsOut)
async def update_scm_inventory_targets(
    entity_id: uuid.UUID,
    data: ScmInventoryTargetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmInventoryTargetsService(db).update(entity_id, data)

@router.delete("/scm_inventory_targets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_inventory_targets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmInventoryTargetsService(db).delete(entity_id)

@router.get("/scm_kpi_alerts", response_model=PaginatedResponse[ScmKpiAlertsOut])
async def list_scm_kpi_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmKpiAlertsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_kpi_alerts/{entity_id}", response_model=ScmKpiAlertsOut)
async def get_scm_kpi_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmKpiAlertsService(db).get(entity_id)

@router.post("/scm_kpi_alerts", response_model=ScmKpiAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_kpi_alerts(
    data: ScmKpiAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiAlertsService(db).create(data)

@router.put("/scm_kpi_alerts/{entity_id}", response_model=ScmKpiAlertsOut)
async def update_scm_kpi_alerts(
    entity_id: uuid.UUID,
    data: ScmKpiAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiAlertsService(db).update(entity_id, data)

@router.delete("/scm_kpi_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_kpi_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmKpiAlertsService(db).delete(entity_id)

@router.get("/scm_kpi_benchmarks", response_model=PaginatedResponse[ScmKpiBenchmarksOut])
async def list_scm_kpi_benchmarks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmKpiBenchmarksService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_kpi_benchmarks/{entity_id}", response_model=ScmKpiBenchmarksOut)
async def get_scm_kpi_benchmarks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmKpiBenchmarksService(db).get(entity_id)

@router.post("/scm_kpi_benchmarks", response_model=ScmKpiBenchmarksOut, status_code=status.HTTP_201_CREATED)
async def create_scm_kpi_benchmarks(
    data: ScmKpiBenchmarksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiBenchmarksService(db).create(data)

@router.put("/scm_kpi_benchmarks/{entity_id}", response_model=ScmKpiBenchmarksOut)
async def update_scm_kpi_benchmarks(
    entity_id: uuid.UUID,
    data: ScmKpiBenchmarksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiBenchmarksService(db).update(entity_id, data)

@router.delete("/scm_kpi_benchmarks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_kpi_benchmarks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmKpiBenchmarksService(db).delete(entity_id)

@router.get("/scm_kpi_definitions", response_model=PaginatedResponse[ScmKpiDefinitionsOut])
async def list_scm_kpi_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmKpiDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "kpi_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_kpi_definitions/{entity_id}", response_model=ScmKpiDefinitionsOut)
async def get_scm_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmKpiDefinitionsService(db).get(entity_id)

@router.post("/scm_kpi_definitions", response_model=ScmKpiDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_kpi_definitions(
    data: ScmKpiDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiDefinitionsService(db).create(data)

@router.put("/scm_kpi_definitions/{entity_id}", response_model=ScmKpiDefinitionsOut)
async def update_scm_kpi_definitions(
    entity_id: uuid.UUID,
    data: ScmKpiDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiDefinitionsService(db).update(entity_id, data)

@router.delete("/scm_kpi_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmKpiDefinitionsService(db).delete(entity_id)

@router.get("/scm_kpi_values", response_model=PaginatedResponse[ScmKpiValuesOut])
async def list_scm_kpi_values(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmKpiValuesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_kpi_values/{entity_id}", response_model=ScmKpiValuesOut)
async def get_scm_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmKpiValuesService(db).get(entity_id)

@router.post("/scm_kpi_values", response_model=ScmKpiValuesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_kpi_values(
    data: ScmKpiValuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiValuesService(db).create(data)

@router.put("/scm_kpi_values/{entity_id}", response_model=ScmKpiValuesOut)
async def update_scm_kpi_values(
    entity_id: uuid.UUID,
    data: ScmKpiValuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmKpiValuesService(db).update(entity_id, data)

@router.delete("/scm_kpi_values/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmKpiValuesService(db).delete(entity_id)

@router.get("/scm_langchain_agent_executions", response_model=PaginatedResponse[ScmLangchainAgentExecutionsOut])
async def list_scm_langchain_agent_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainAgentExecutionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["execution_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_agent_executions/{entity_id}", response_model=ScmLangchainAgentExecutionsOut)
async def get_scm_langchain_agent_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainAgentExecutionsService(db).get(entity_id)

@router.post("/scm_langchain_agent_executions", response_model=ScmLangchainAgentExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_agent_executions(
    data: ScmLangchainAgentExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainAgentExecutionsService(db).create(data)

@router.put("/scm_langchain_agent_executions/{entity_id}", response_model=ScmLangchainAgentExecutionsOut)
async def update_scm_langchain_agent_executions(
    entity_id: uuid.UUID,
    data: ScmLangchainAgentExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainAgentExecutionsService(db).update(entity_id, data)

@router.delete("/scm_langchain_agent_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_agent_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainAgentExecutionsService(db).delete(entity_id)

@router.get("/scm_langchain_agents", response_model=PaginatedResponse[ScmLangchainAgentsOut])
async def list_scm_langchain_agents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainAgentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_code", "agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_agents/{entity_id}", response_model=ScmLangchainAgentsOut)
async def get_scm_langchain_agents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainAgentsService(db).get(entity_id)

@router.post("/scm_langchain_agents", response_model=ScmLangchainAgentsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_agents(
    data: ScmLangchainAgentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainAgentsService(db).create(data)

@router.put("/scm_langchain_agents/{entity_id}", response_model=ScmLangchainAgentsOut)
async def update_scm_langchain_agents(
    entity_id: uuid.UUID,
    data: ScmLangchainAgentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainAgentsService(db).update(entity_id, data)

@router.delete("/scm_langchain_agents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_agents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainAgentsService(db).delete(entity_id)

@router.get("/scm_langchain_chains", response_model=PaginatedResponse[ScmLangchainChainsOut])
async def list_scm_langchain_chains(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainChainsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["chain_code", "chain_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_chains/{entity_id}", response_model=ScmLangchainChainsOut)
async def get_scm_langchain_chains(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainChainsService(db).get(entity_id)

@router.post("/scm_langchain_chains", response_model=ScmLangchainChainsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_chains(
    data: ScmLangchainChainsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainChainsService(db).create(data)

@router.put("/scm_langchain_chains/{entity_id}", response_model=ScmLangchainChainsOut)
async def update_scm_langchain_chains(
    entity_id: uuid.UUID,
    data: ScmLangchainChainsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainChainsService(db).update(entity_id, data)

@router.delete("/scm_langchain_chains/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_chains(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainChainsService(db).delete(entity_id)

@router.get("/scm_langchain_documents", response_model=PaginatedResponse[ScmLangchainDocumentsOut])
async def list_scm_langchain_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainDocumentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_documents/{entity_id}", response_model=ScmLangchainDocumentsOut)
async def get_scm_langchain_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainDocumentsService(db).get(entity_id)

@router.post("/scm_langchain_documents", response_model=ScmLangchainDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_documents(
    data: ScmLangchainDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainDocumentsService(db).create(data)

@router.put("/scm_langchain_documents/{entity_id}", response_model=ScmLangchainDocumentsOut)
async def update_scm_langchain_documents(
    entity_id: uuid.UUID,
    data: ScmLangchainDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainDocumentsService(db).update(entity_id, data)

@router.delete("/scm_langchain_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainDocumentsService(db).delete(entity_id)

@router.get("/scm_langchain_executions", response_model=PaginatedResponse[ScmLangchainExecutionsOut])
async def list_scm_langchain_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainExecutionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["execution_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_executions/{entity_id}", response_model=ScmLangchainExecutionsOut)
async def get_scm_langchain_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainExecutionsService(db).get(entity_id)

@router.post("/scm_langchain_executions", response_model=ScmLangchainExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_executions(
    data: ScmLangchainExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainExecutionsService(db).create(data)

@router.put("/scm_langchain_executions/{entity_id}", response_model=ScmLangchainExecutionsOut)
async def update_scm_langchain_executions(
    entity_id: uuid.UUID,
    data: ScmLangchainExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainExecutionsService(db).update(entity_id, data)

@router.delete("/scm_langchain_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainExecutionsService(db).delete(entity_id)

@router.get("/scm_langchain_llm_configs", response_model=PaginatedResponse[ScmLangchainLlmConfigsOut])
async def list_scm_langchain_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_code", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_llm_configs/{entity_id}", response_model=ScmLangchainLlmConfigsOut)
async def get_scm_langchain_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainLlmConfigsService(db).get(entity_id)

@router.post("/scm_langchain_llm_configs", response_model=ScmLangchainLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_llm_configs(
    data: ScmLangchainLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainLlmConfigsService(db).create(data)

@router.put("/scm_langchain_llm_configs/{entity_id}", response_model=ScmLangchainLlmConfigsOut)
async def update_scm_langchain_llm_configs(
    entity_id: uuid.UUID,
    data: ScmLangchainLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainLlmConfigsService(db).update(entity_id, data)

@router.delete("/scm_langchain_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainLlmConfigsService(db).delete(entity_id)

@router.get("/scm_langchain_prompt_templates", response_model=PaginatedResponse[ScmLangchainPromptTemplatesOut])
async def list_scm_langchain_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_code", "template_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_prompt_templates/{entity_id}", response_model=ScmLangchainPromptTemplatesOut)
async def get_scm_langchain_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainPromptTemplatesService(db).get(entity_id)

@router.post("/scm_langchain_prompt_templates", response_model=ScmLangchainPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_prompt_templates(
    data: ScmLangchainPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainPromptTemplatesService(db).create(data)

@router.put("/scm_langchain_prompt_templates/{entity_id}", response_model=ScmLangchainPromptTemplatesOut)
async def update_scm_langchain_prompt_templates(
    entity_id: uuid.UUID,
    data: ScmLangchainPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainPromptTemplatesService(db).update(entity_id, data)

@router.delete("/scm_langchain_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainPromptTemplatesService(db).delete(entity_id)

@router.get("/scm_langchain_vector_stores", response_model=PaginatedResponse[ScmLangchainVectorStoresOut])
async def list_scm_langchain_vector_stores(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLangchainVectorStoresService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["store_code", "store_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langchain_vector_stores/{entity_id}", response_model=ScmLangchainVectorStoresOut)
async def get_scm_langchain_vector_stores(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLangchainVectorStoresService(db).get(entity_id)

@router.post("/scm_langchain_vector_stores", response_model=ScmLangchainVectorStoresOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langchain_vector_stores(
    data: ScmLangchainVectorStoresCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainVectorStoresService(db).create(data)

@router.put("/scm_langchain_vector_stores/{entity_id}", response_model=ScmLangchainVectorStoresOut)
async def update_scm_langchain_vector_stores(
    entity_id: uuid.UUID,
    data: ScmLangchainVectorStoresUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLangchainVectorStoresService(db).update(entity_id, data)

@router.delete("/scm_langchain_vector_stores/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langchain_vector_stores(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLangchainVectorStoresService(db).delete(entity_id)

@router.get("/scm_langgraph_edges", response_model=PaginatedResponse[ScmLanggraphEdgesOut])
async def list_scm_langgraph_edges(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLanggraphEdgesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langgraph_edges/{entity_id}", response_model=ScmLanggraphEdgesOut)
async def get_scm_langgraph_edges(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLanggraphEdgesService(db).get(entity_id)

@router.post("/scm_langgraph_edges", response_model=ScmLanggraphEdgesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langgraph_edges(
    data: ScmLanggraphEdgesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphEdgesService(db).create(data)

@router.put("/scm_langgraph_edges/{entity_id}", response_model=ScmLanggraphEdgesOut)
async def update_scm_langgraph_edges(
    entity_id: uuid.UUID,
    data: ScmLanggraphEdgesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphEdgesService(db).update(entity_id, data)

@router.delete("/scm_langgraph_edges/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langgraph_edges(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLanggraphEdgesService(db).delete(entity_id)

@router.get("/scm_langgraph_executions", response_model=PaginatedResponse[ScmLanggraphExecutionsOut])
async def list_scm_langgraph_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLanggraphExecutionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["execution_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langgraph_executions/{entity_id}", response_model=ScmLanggraphExecutionsOut)
async def get_scm_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLanggraphExecutionsService(db).get(entity_id)

@router.post("/scm_langgraph_executions", response_model=ScmLanggraphExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langgraph_executions(
    data: ScmLanggraphExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphExecutionsService(db).create(data)

@router.put("/scm_langgraph_executions/{entity_id}", response_model=ScmLanggraphExecutionsOut)
async def update_scm_langgraph_executions(
    entity_id: uuid.UUID,
    data: ScmLanggraphExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphExecutionsService(db).update(entity_id, data)

@router.delete("/scm_langgraph_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLanggraphExecutionsService(db).delete(entity_id)

@router.get("/scm_langgraph_logs", response_model=PaginatedResponse[ScmLanggraphLogsOut])
async def list_scm_langgraph_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLanggraphLogsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langgraph_logs/{entity_id}", response_model=ScmLanggraphLogsOut)
async def get_scm_langgraph_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLanggraphLogsService(db).get(entity_id)

@router.post("/scm_langgraph_logs", response_model=ScmLanggraphLogsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langgraph_logs(
    data: ScmLanggraphLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphLogsService(db).create(data)

@router.put("/scm_langgraph_logs/{entity_id}", response_model=ScmLanggraphLogsOut)
async def update_scm_langgraph_logs(
    entity_id: uuid.UUID,
    data: ScmLanggraphLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphLogsService(db).update(entity_id, data)

@router.delete("/scm_langgraph_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langgraph_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLanggraphLogsService(db).delete(entity_id)

@router.get("/scm_langgraph_nodes", response_model=PaginatedResponse[ScmLanggraphNodesOut])
async def list_scm_langgraph_nodes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLanggraphNodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["function_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langgraph_nodes/{entity_id}", response_model=ScmLanggraphNodesOut)
async def get_scm_langgraph_nodes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLanggraphNodesService(db).get(entity_id)

@router.post("/scm_langgraph_nodes", response_model=ScmLanggraphNodesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langgraph_nodes(
    data: ScmLanggraphNodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphNodesService(db).create(data)

@router.put("/scm_langgraph_nodes/{entity_id}", response_model=ScmLanggraphNodesOut)
async def update_scm_langgraph_nodes(
    entity_id: uuid.UUID,
    data: ScmLanggraphNodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphNodesService(db).update(entity_id, data)

@router.delete("/scm_langgraph_nodes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langgraph_nodes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLanggraphNodesService(db).delete(entity_id)

@router.get("/scm_langgraph_workflows", response_model=PaginatedResponse[ScmLanggraphWorkflowsOut])
async def list_scm_langgraph_workflows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmLanggraphWorkflowsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_langgraph_workflows/{entity_id}", response_model=ScmLanggraphWorkflowsOut)
async def get_scm_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmLanggraphWorkflowsService(db).get(entity_id)

@router.post("/scm_langgraph_workflows", response_model=ScmLanggraphWorkflowsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_langgraph_workflows(
    data: ScmLanggraphWorkflowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphWorkflowsService(db).create(data)

@router.put("/scm_langgraph_workflows/{entity_id}", response_model=ScmLanggraphWorkflowsOut)
async def update_scm_langgraph_workflows(
    entity_id: uuid.UUID,
    data: ScmLanggraphWorkflowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmLanggraphWorkflowsService(db).update(entity_id, data)

@router.delete("/scm_langgraph_workflows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmLanggraphWorkflowsService(db).delete(entity_id)

@router.get("/scm_ml_model_deployments", response_model=PaginatedResponse[ScmMlModelDeploymentsOut])
async def list_scm_ml_model_deployments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmMlModelDeploymentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ml_model_deployments/{entity_id}", response_model=ScmMlModelDeploymentsOut)
async def get_scm_ml_model_deployments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmMlModelDeploymentsService(db).get(entity_id)

@router.post("/scm_ml_model_deployments", response_model=ScmMlModelDeploymentsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ml_model_deployments(
    data: ScmMlModelDeploymentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelDeploymentsService(db).create(data)

@router.put("/scm_ml_model_deployments/{entity_id}", response_model=ScmMlModelDeploymentsOut)
async def update_scm_ml_model_deployments(
    entity_id: uuid.UUID,
    data: ScmMlModelDeploymentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelDeploymentsService(db).update(entity_id, data)

@router.delete("/scm_ml_model_deployments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ml_model_deployments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmMlModelDeploymentsService(db).delete(entity_id)

@router.get("/scm_ml_model_types", response_model=PaginatedResponse[ScmMlModelTypesOut])
async def list_scm_ml_model_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmMlModelTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ml_model_types/{entity_id}", response_model=ScmMlModelTypesOut)
async def get_scm_ml_model_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmMlModelTypesService(db).get(entity_id)

@router.post("/scm_ml_model_types", response_model=ScmMlModelTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ml_model_types(
    data: ScmMlModelTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelTypesService(db).create(data)

@router.put("/scm_ml_model_types/{entity_id}", response_model=ScmMlModelTypesOut)
async def update_scm_ml_model_types(
    entity_id: uuid.UUID,
    data: ScmMlModelTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelTypesService(db).update(entity_id, data)

@router.delete("/scm_ml_model_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ml_model_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmMlModelTypesService(db).delete(entity_id)

@router.get("/scm_ml_models", response_model=PaginatedResponse[ScmMlModelsOut])
async def list_scm_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ml_models/{entity_id}", response_model=ScmMlModelsOut)
async def get_scm_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmMlModelsService(db).get(entity_id)

@router.post("/scm_ml_models", response_model=ScmMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ml_models(
    data: ScmMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelsService(db).create(data)

@router.put("/scm_ml_models/{entity_id}", response_model=ScmMlModelsOut)
async def update_scm_ml_models(
    entity_id: uuid.UUID,
    data: ScmMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlModelsService(db).update(entity_id, data)

@router.delete("/scm_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmMlModelsService(db).delete(entity_id)

@router.get("/scm_ml_monitoring", response_model=PaginatedResponse[ScmMlMonitoringOut])
async def list_scm_ml_monitoring(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmMlMonitoringService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ml_monitoring/{entity_id}", response_model=ScmMlMonitoringOut)
async def get_scm_ml_monitoring(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmMlMonitoringService(db).get(entity_id)

@router.post("/scm_ml_monitoring", response_model=ScmMlMonitoringOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ml_monitoring(
    data: ScmMlMonitoringCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlMonitoringService(db).create(data)

@router.put("/scm_ml_monitoring/{entity_id}", response_model=ScmMlMonitoringOut)
async def update_scm_ml_monitoring(
    entity_id: uuid.UUID,
    data: ScmMlMonitoringUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlMonitoringService(db).update(entity_id, data)

@router.delete("/scm_ml_monitoring/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ml_monitoring(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmMlMonitoringService(db).delete(entity_id)

@router.get("/scm_ml_training_runs", response_model=PaginatedResponse[ScmMlTrainingRunsOut])
async def list_scm_ml_training_runs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmMlTrainingRunsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["run_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ml_training_runs/{entity_id}", response_model=ScmMlTrainingRunsOut)
async def get_scm_ml_training_runs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmMlTrainingRunsService(db).get(entity_id)

@router.post("/scm_ml_training_runs", response_model=ScmMlTrainingRunsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ml_training_runs(
    data: ScmMlTrainingRunsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlTrainingRunsService(db).create(data)

@router.put("/scm_ml_training_runs/{entity_id}", response_model=ScmMlTrainingRunsOut)
async def update_scm_ml_training_runs(
    entity_id: uuid.UUID,
    data: ScmMlTrainingRunsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmMlTrainingRunsService(db).update(entity_id, data)

@router.delete("/scm_ml_training_runs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ml_training_runs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmMlTrainingRunsService(db).delete(entity_id)

@router.get("/scm_network_arcs", response_model=PaginatedResponse[ScmNetworkArcsOut])
async def list_scm_network_arcs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkArcsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["arc_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_arcs/{entity_id}", response_model=ScmNetworkArcsOut)
async def get_scm_network_arcs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkArcsService(db).get(entity_id)

@router.post("/scm_network_arcs", response_model=ScmNetworkArcsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_arcs(
    data: ScmNetworkArcsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkArcsService(db).create(data)

@router.put("/scm_network_arcs/{entity_id}", response_model=ScmNetworkArcsOut)
async def update_scm_network_arcs(
    entity_id: uuid.UUID,
    data: ScmNetworkArcsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkArcsService(db).update(entity_id, data)

@router.delete("/scm_network_arcs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_arcs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkArcsService(db).delete(entity_id)

@router.get("/scm_network_capacities", response_model=PaginatedResponse[ScmNetworkCapacitiesOut])
async def list_scm_network_capacities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkCapacitiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_capacities/{entity_id}", response_model=ScmNetworkCapacitiesOut)
async def get_scm_network_capacities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkCapacitiesService(db).get(entity_id)

@router.post("/scm_network_capacities", response_model=ScmNetworkCapacitiesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_capacities(
    data: ScmNetworkCapacitiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkCapacitiesService(db).create(data)

@router.put("/scm_network_capacities/{entity_id}", response_model=ScmNetworkCapacitiesOut)
async def update_scm_network_capacities(
    entity_id: uuid.UUID,
    data: ScmNetworkCapacitiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkCapacitiesService(db).update(entity_id, data)

@router.delete("/scm_network_capacities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_capacities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkCapacitiesService(db).delete(entity_id)

@router.get("/scm_network_costs", response_model=PaginatedResponse[ScmNetworkCostsOut])
async def list_scm_network_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_costs/{entity_id}", response_model=ScmNetworkCostsOut)
async def get_scm_network_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkCostsService(db).get(entity_id)

@router.post("/scm_network_costs", response_model=ScmNetworkCostsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_costs(
    data: ScmNetworkCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkCostsService(db).create(data)

@router.put("/scm_network_costs/{entity_id}", response_model=ScmNetworkCostsOut)
async def update_scm_network_costs(
    entity_id: uuid.UUID,
    data: ScmNetworkCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkCostsService(db).update(entity_id, data)

@router.delete("/scm_network_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkCostsService(db).delete(entity_id)

@router.get("/scm_network_flows", response_model=PaginatedResponse[ScmNetworkFlowsOut])
async def list_scm_network_flows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkFlowsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_flows/{entity_id}", response_model=ScmNetworkFlowsOut)
async def get_scm_network_flows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkFlowsService(db).get(entity_id)

@router.post("/scm_network_flows", response_model=ScmNetworkFlowsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_flows(
    data: ScmNetworkFlowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkFlowsService(db).create(data)

@router.put("/scm_network_flows/{entity_id}", response_model=ScmNetworkFlowsOut)
async def update_scm_network_flows(
    entity_id: uuid.UUID,
    data: ScmNetworkFlowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkFlowsService(db).update(entity_id, data)

@router.delete("/scm_network_flows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_flows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkFlowsService(db).delete(entity_id)

@router.get("/scm_network_nodes", response_model=PaginatedResponse[ScmNetworkNodesOut])
async def list_scm_network_nodes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkNodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["node_code", "node_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_nodes/{entity_id}", response_model=ScmNetworkNodesOut)
async def get_scm_network_nodes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkNodesService(db).get(entity_id)

@router.post("/scm_network_nodes", response_model=ScmNetworkNodesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_nodes(
    data: ScmNetworkNodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkNodesService(db).create(data)

@router.put("/scm_network_nodes/{entity_id}", response_model=ScmNetworkNodesOut)
async def update_scm_network_nodes(
    entity_id: uuid.UUID,
    data: ScmNetworkNodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkNodesService(db).update(entity_id, data)

@router.delete("/scm_network_nodes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_nodes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkNodesService(db).delete(entity_id)

@router.get("/scm_network_risk_assessment", response_model=PaginatedResponse[ScmNetworkRiskAssessmentOut])
async def list_scm_network_risk_assessment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkRiskAssessmentService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_risk_assessment/{entity_id}", response_model=ScmNetworkRiskAssessmentOut)
async def get_scm_network_risk_assessment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkRiskAssessmentService(db).get(entity_id)

@router.post("/scm_network_risk_assessment", response_model=ScmNetworkRiskAssessmentOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_risk_assessment(
    data: ScmNetworkRiskAssessmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkRiskAssessmentService(db).create(data)

@router.put("/scm_network_risk_assessment/{entity_id}", response_model=ScmNetworkRiskAssessmentOut)
async def update_scm_network_risk_assessment(
    entity_id: uuid.UUID,
    data: ScmNetworkRiskAssessmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkRiskAssessmentService(db).update(entity_id, data)

@router.delete("/scm_network_risk_assessment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_risk_assessment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkRiskAssessmentService(db).delete(entity_id)

@router.get("/scm_network_scenarios", response_model=PaginatedResponse[ScmNetworkScenariosOut])
async def list_scm_network_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmNetworkScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_network_scenarios/{entity_id}", response_model=ScmNetworkScenariosOut)
async def get_scm_network_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmNetworkScenariosService(db).get(entity_id)

@router.post("/scm_network_scenarios", response_model=ScmNetworkScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_scm_network_scenarios(
    data: ScmNetworkScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkScenariosService(db).create(data)

@router.put("/scm_network_scenarios/{entity_id}", response_model=ScmNetworkScenariosOut)
async def update_scm_network_scenarios(
    entity_id: uuid.UUID,
    data: ScmNetworkScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmNetworkScenariosService(db).update(entity_id, data)

@router.delete("/scm_network_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_network_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmNetworkScenariosService(db).delete(entity_id)

@router.get("/scm_optimization_execution_log", response_model=PaginatedResponse[ScmOptimizationExecutionLogOut])
async def list_scm_optimization_execution_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOptimizationExecutionLogService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_optimization_execution_log/{entity_id}", response_model=ScmOptimizationExecutionLogOut)
async def get_scm_optimization_execution_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOptimizationExecutionLogService(db).get(entity_id)

@router.post("/scm_optimization_execution_log", response_model=ScmOptimizationExecutionLogOut, status_code=status.HTTP_201_CREATED)
async def create_scm_optimization_execution_log(
    data: ScmOptimizationExecutionLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationExecutionLogService(db).create(data)

@router.put("/scm_optimization_execution_log/{entity_id}", response_model=ScmOptimizationExecutionLogOut)
async def update_scm_optimization_execution_log(
    entity_id: uuid.UUID,
    data: ScmOptimizationExecutionLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationExecutionLogService(db).update(entity_id, data)

@router.delete("/scm_optimization_execution_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_optimization_execution_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOptimizationExecutionLogService(db).delete(entity_id)

@router.get("/scm_optimization_problems", response_model=PaginatedResponse[ScmOptimizationProblemsOut])
async def list_scm_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOptimizationProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_code", "problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_optimization_problems/{entity_id}", response_model=ScmOptimizationProblemsOut)
async def get_scm_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOptimizationProblemsService(db).get(entity_id)

@router.post("/scm_optimization_problems", response_model=ScmOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_optimization_problems(
    data: ScmOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationProblemsService(db).create(data)

@router.put("/scm_optimization_problems/{entity_id}", response_model=ScmOptimizationProblemsOut)
async def update_scm_optimization_problems(
    entity_id: uuid.UUID,
    data: ScmOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/scm_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOptimizationProblemsService(db).delete(entity_id)

@router.get("/scm_optimization_sensitivity", response_model=PaginatedResponse[ScmOptimizationSensitivityOut])
async def list_scm_optimization_sensitivity(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOptimizationSensitivityService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["parameter_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_optimization_sensitivity/{entity_id}", response_model=ScmOptimizationSensitivityOut)
async def get_scm_optimization_sensitivity(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOptimizationSensitivityService(db).get(entity_id)

@router.post("/scm_optimization_sensitivity", response_model=ScmOptimizationSensitivityOut, status_code=status.HTTP_201_CREATED)
async def create_scm_optimization_sensitivity(
    data: ScmOptimizationSensitivityCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationSensitivityService(db).create(data)

@router.put("/scm_optimization_sensitivity/{entity_id}", response_model=ScmOptimizationSensitivityOut)
async def update_scm_optimization_sensitivity(
    entity_id: uuid.UUID,
    data: ScmOptimizationSensitivityUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationSensitivityService(db).update(entity_id, data)

@router.delete("/scm_optimization_sensitivity/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_optimization_sensitivity(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOptimizationSensitivityService(db).delete(entity_id)

@router.get("/scm_optimization_solutions", response_model=PaginatedResponse[ScmOptimizationSolutionsOut])
async def list_scm_optimization_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOptimizationSolutionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solution_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_optimization_solutions/{entity_id}", response_model=ScmOptimizationSolutionsOut)
async def get_scm_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOptimizationSolutionsService(db).get(entity_id)

@router.post("/scm_optimization_solutions", response_model=ScmOptimizationSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_optimization_solutions(
    data: ScmOptimizationSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationSolutionsService(db).create(data)

@router.put("/scm_optimization_solutions/{entity_id}", response_model=ScmOptimizationSolutionsOut)
async def update_scm_optimization_solutions(
    entity_id: uuid.UUID,
    data: ScmOptimizationSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOptimizationSolutionsService(db).update(entity_id, data)

@router.delete("/scm_optimization_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOptimizationSolutionsService(db).delete(entity_id)

@router.get("/scm_ortools_problems", response_model=PaginatedResponse[ScmOrtoolsProblemsOut])
async def list_scm_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOrtoolsProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_code", "problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ortools_problems/{entity_id}", response_model=ScmOrtoolsProblemsOut)
async def get_scm_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOrtoolsProblemsService(db).get(entity_id)

@router.post("/scm_ortools_problems", response_model=ScmOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ortools_problems(
    data: ScmOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOrtoolsProblemsService(db).create(data)

@router.put("/scm_ortools_problems/{entity_id}", response_model=ScmOrtoolsProblemsOut)
async def update_scm_ortools_problems(
    entity_id: uuid.UUID,
    data: ScmOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/scm_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOrtoolsProblemsService(db).delete(entity_id)

@router.get("/scm_ortools_solutions", response_model=PaginatedResponse[ScmOrtoolsSolutionsOut])
async def list_scm_ortools_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmOrtoolsSolutionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solution_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_ortools_solutions/{entity_id}", response_model=ScmOrtoolsSolutionsOut)
async def get_scm_ortools_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmOrtoolsSolutionsService(db).get(entity_id)

@router.post("/scm_ortools_solutions", response_model=ScmOrtoolsSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_ortools_solutions(
    data: ScmOrtoolsSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOrtoolsSolutionsService(db).create(data)

@router.put("/scm_ortools_solutions/{entity_id}", response_model=ScmOrtoolsSolutionsOut)
async def update_scm_ortools_solutions(
    entity_id: uuid.UUID,
    data: ScmOrtoolsSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmOrtoolsSolutionsService(db).update(entity_id, data)

@router.delete("/scm_ortools_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_ortools_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmOrtoolsSolutionsService(db).delete(entity_id)

@router.get("/scm_pick_path_learning", response_model=PaginatedResponse[ScmPickPathLearningOut])
async def list_scm_pick_path_learning(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPickPathLearningService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_pick_path_learning/{entity_id}", response_model=ScmPickPathLearningOut)
async def get_scm_pick_path_learning(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPickPathLearningService(db).get(entity_id)

@router.post("/scm_pick_path_learning", response_model=ScmPickPathLearningOut, status_code=status.HTTP_201_CREATED)
async def create_scm_pick_path_learning(
    data: ScmPickPathLearningCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathLearningService(db).create(data)

@router.put("/scm_pick_path_learning/{entity_id}", response_model=ScmPickPathLearningOut)
async def update_scm_pick_path_learning(
    entity_id: uuid.UUID,
    data: ScmPickPathLearningUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathLearningService(db).update(entity_id, data)

@router.delete("/scm_pick_path_learning/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_pick_path_learning(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPickPathLearningService(db).delete(entity_id)

@router.get("/scm_pick_path_problems", response_model=PaginatedResponse[ScmPickPathProblemsOut])
async def list_scm_pick_path_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPickPathProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_pick_path_problems/{entity_id}", response_model=ScmPickPathProblemsOut)
async def get_scm_pick_path_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPickPathProblemsService(db).get(entity_id)

@router.post("/scm_pick_path_problems", response_model=ScmPickPathProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_pick_path_problems(
    data: ScmPickPathProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathProblemsService(db).create(data)

@router.put("/scm_pick_path_problems/{entity_id}", response_model=ScmPickPathProblemsOut)
async def update_scm_pick_path_problems(
    entity_id: uuid.UUID,
    data: ScmPickPathProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathProblemsService(db).update(entity_id, data)

@router.delete("/scm_pick_path_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_pick_path_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPickPathProblemsService(db).delete(entity_id)

@router.get("/scm_pick_path_solutions", response_model=PaginatedResponse[ScmPickPathSolutionsOut])
async def list_scm_pick_path_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPickPathSolutionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_pick_path_solutions/{entity_id}", response_model=ScmPickPathSolutionsOut)
async def get_scm_pick_path_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPickPathSolutionsService(db).get(entity_id)

@router.post("/scm_pick_path_solutions", response_model=ScmPickPathSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_pick_path_solutions(
    data: ScmPickPathSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathSolutionsService(db).create(data)

@router.put("/scm_pick_path_solutions/{entity_id}", response_model=ScmPickPathSolutionsOut)
async def update_scm_pick_path_solutions(
    entity_id: uuid.UUID,
    data: ScmPickPathSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPickPathSolutionsService(db).update(entity_id, data)

@router.delete("/scm_pick_path_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_pick_path_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPickPathSolutionsService(db).delete(entity_id)

@router.get("/scm_prediction_accuracy", response_model=PaginatedResponse[ScmPredictionAccuracyOut])
async def list_scm_prediction_accuracy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPredictionAccuracyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_prediction_accuracy/{entity_id}", response_model=ScmPredictionAccuracyOut)
async def get_scm_prediction_accuracy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPredictionAccuracyService(db).get(entity_id)

@router.post("/scm_prediction_accuracy", response_model=ScmPredictionAccuracyOut, status_code=status.HTTP_201_CREATED)
async def create_scm_prediction_accuracy(
    data: ScmPredictionAccuracyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionAccuracyService(db).create(data)

@router.put("/scm_prediction_accuracy/{entity_id}", response_model=ScmPredictionAccuracyOut)
async def update_scm_prediction_accuracy(
    entity_id: uuid.UUID,
    data: ScmPredictionAccuracyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionAccuracyService(db).update(entity_id, data)

@router.delete("/scm_prediction_accuracy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_prediction_accuracy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPredictionAccuracyService(db).delete(entity_id)

@router.get("/scm_prediction_features", response_model=PaginatedResponse[ScmPredictionFeaturesOut])
async def list_scm_prediction_features(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPredictionFeaturesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["feature_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_prediction_features/{entity_id}", response_model=ScmPredictionFeaturesOut)
async def get_scm_prediction_features(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPredictionFeaturesService(db).get(entity_id)

@router.post("/scm_prediction_features", response_model=ScmPredictionFeaturesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_prediction_features(
    data: ScmPredictionFeaturesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionFeaturesService(db).create(data)

@router.put("/scm_prediction_features/{entity_id}", response_model=ScmPredictionFeaturesOut)
async def update_scm_prediction_features(
    entity_id: uuid.UUID,
    data: ScmPredictionFeaturesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionFeaturesService(db).update(entity_id, data)

@router.delete("/scm_prediction_features/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_prediction_features(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPredictionFeaturesService(db).delete(entity_id)

@router.get("/scm_prediction_overrides", response_model=PaginatedResponse[ScmPredictionOverridesOut])
async def list_scm_prediction_overrides(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPredictionOverridesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_prediction_overrides/{entity_id}", response_model=ScmPredictionOverridesOut)
async def get_scm_prediction_overrides(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPredictionOverridesService(db).get(entity_id)

@router.post("/scm_prediction_overrides", response_model=ScmPredictionOverridesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_prediction_overrides(
    data: ScmPredictionOverridesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionOverridesService(db).create(data)

@router.put("/scm_prediction_overrides/{entity_id}", response_model=ScmPredictionOverridesOut)
async def update_scm_prediction_overrides(
    entity_id: uuid.UUID,
    data: ScmPredictionOverridesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionOverridesService(db).update(entity_id, data)

@router.delete("/scm_prediction_overrides/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_prediction_overrides(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPredictionOverridesService(db).delete(entity_id)

@router.get("/scm_prediction_types", response_model=PaginatedResponse[ScmPredictionTypesOut])
async def list_scm_prediction_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPredictionTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_prediction_types/{entity_id}", response_model=ScmPredictionTypesOut)
async def get_scm_prediction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPredictionTypesService(db).get(entity_id)

@router.post("/scm_prediction_types", response_model=ScmPredictionTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_prediction_types(
    data: ScmPredictionTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionTypesService(db).create(data)

@router.put("/scm_prediction_types/{entity_id}", response_model=ScmPredictionTypesOut)
async def update_scm_prediction_types(
    entity_id: uuid.UUID,
    data: ScmPredictionTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionTypesService(db).update(entity_id, data)

@router.delete("/scm_prediction_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_prediction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPredictionTypesService(db).delete(entity_id)

@router.get("/scm_predictions", response_model=PaginatedResponse[ScmPredictionsOut])
async def list_scm_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPredictionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_predictions/{entity_id}", response_model=ScmPredictionsOut)
async def get_scm_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPredictionsService(db).get(entity_id)

@router.post("/scm_predictions", response_model=ScmPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_predictions(
    data: ScmPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionsService(db).create(data)

@router.put("/scm_predictions/{entity_id}", response_model=ScmPredictionsOut)
async def update_scm_predictions(
    entity_id: uuid.UUID,
    data: ScmPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPredictionsService(db).update(entity_id, data)

@router.delete("/scm_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPredictionsService(db).delete(entity_id)

@router.get("/scm_procurement_contracts", response_model=PaginatedResponse[ScmProcurementContractsOut])
async def list_scm_procurement_contracts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementContractsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["contract_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_contracts/{entity_id}", response_model=ScmProcurementContractsOut)
async def get_scm_procurement_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementContractsService(db).get(entity_id)

@router.post("/scm_procurement_contracts", response_model=ScmProcurementContractsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_contracts(
    data: ScmProcurementContractsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementContractsService(db).create(data)

@router.put("/scm_procurement_contracts/{entity_id}", response_model=ScmProcurementContractsOut)
async def update_scm_procurement_contracts(
    entity_id: uuid.UUID,
    data: ScmProcurementContractsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementContractsService(db).update(entity_id, data)

@router.delete("/scm_procurement_contracts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementContractsService(db).delete(entity_id)

@router.get("/scm_procurement_recommendations", response_model=PaginatedResponse[ScmProcurementRecommendationsOut])
async def list_scm_procurement_recommendations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementRecommendationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_recommendations/{entity_id}", response_model=ScmProcurementRecommendationsOut)
async def get_scm_procurement_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementRecommendationsService(db).get(entity_id)

@router.post("/scm_procurement_recommendations", response_model=ScmProcurementRecommendationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_recommendations(
    data: ScmProcurementRecommendationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementRecommendationsService(db).create(data)

@router.put("/scm_procurement_recommendations/{entity_id}", response_model=ScmProcurementRecommendationsOut)
async def update_scm_procurement_recommendations(
    entity_id: uuid.UUID,
    data: ScmProcurementRecommendationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementRecommendationsService(db).update(entity_id, data)

@router.delete("/scm_procurement_recommendations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementRecommendationsService(db).delete(entity_id)

@router.get("/scm_procurement_savings", response_model=PaginatedResponse[ScmProcurementSavingsOut])
async def list_scm_procurement_savings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementSavingsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_savings/{entity_id}", response_model=ScmProcurementSavingsOut)
async def get_scm_procurement_savings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementSavingsService(db).get(entity_id)

@router.post("/scm_procurement_savings", response_model=ScmProcurementSavingsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_savings(
    data: ScmProcurementSavingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementSavingsService(db).create(data)

@router.put("/scm_procurement_savings/{entity_id}", response_model=ScmProcurementSavingsOut)
async def update_scm_procurement_savings(
    entity_id: uuid.UUID,
    data: ScmProcurementSavingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementSavingsService(db).update(entity_id, data)

@router.delete("/scm_procurement_savings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_savings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementSavingsService(db).delete(entity_id)

@router.get("/scm_procurement_scenarios", response_model=PaginatedResponse[ScmProcurementScenariosOut])
async def list_scm_procurement_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_scenarios/{entity_id}", response_model=ScmProcurementScenariosOut)
async def get_scm_procurement_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementScenariosService(db).get(entity_id)

@router.post("/scm_procurement_scenarios", response_model=ScmProcurementScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_scenarios(
    data: ScmProcurementScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementScenariosService(db).create(data)

@router.put("/scm_procurement_scenarios/{entity_id}", response_model=ScmProcurementScenariosOut)
async def update_scm_procurement_scenarios(
    entity_id: uuid.UUID,
    data: ScmProcurementScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementScenariosService(db).update(entity_id, data)

@router.delete("/scm_procurement_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementScenariosService(db).delete(entity_id)

@router.get("/scm_procurement_strategies", response_model=PaginatedResponse[ScmProcurementStrategiesOut])
async def list_scm_procurement_strategies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementStrategiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_strategies/{entity_id}", response_model=ScmProcurementStrategiesOut)
async def get_scm_procurement_strategies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementStrategiesService(db).get(entity_id)

@router.post("/scm_procurement_strategies", response_model=ScmProcurementStrategiesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_strategies(
    data: ScmProcurementStrategiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementStrategiesService(db).create(data)

@router.put("/scm_procurement_strategies/{entity_id}", response_model=ScmProcurementStrategiesOut)
async def update_scm_procurement_strategies(
    entity_id: uuid.UUID,
    data: ScmProcurementStrategiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementStrategiesService(db).update(entity_id, data)

@router.delete("/scm_procurement_strategies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_strategies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementStrategiesService(db).delete(entity_id)

@router.get("/scm_procurement_tco", response_model=PaginatedResponse[ScmProcurementTcoOut])
async def list_scm_procurement_tco(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmProcurementTcoService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_procurement_tco/{entity_id}", response_model=ScmProcurementTcoOut)
async def get_scm_procurement_tco(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmProcurementTcoService(db).get(entity_id)

@router.post("/scm_procurement_tco", response_model=ScmProcurementTcoOut, status_code=status.HTTP_201_CREATED)
async def create_scm_procurement_tco(
    data: ScmProcurementTcoCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementTcoService(db).create(data)

@router.put("/scm_procurement_tco/{entity_id}", response_model=ScmProcurementTcoOut)
async def update_scm_procurement_tco(
    entity_id: uuid.UUID,
    data: ScmProcurementTcoUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmProcurementTcoService(db).update(entity_id, data)

@router.delete("/scm_procurement_tco/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_procurement_tco(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmProcurementTcoService(db).delete(entity_id)

@router.get("/scm_promotion_calendars", response_model=PaginatedResponse[ScmPromotionCalendarsOut])
async def list_scm_promotion_calendars(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmPromotionCalendarsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["promotion_code", "promotion_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_promotion_calendars/{entity_id}", response_model=ScmPromotionCalendarsOut)
async def get_scm_promotion_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmPromotionCalendarsService(db).get(entity_id)

@router.post("/scm_promotion_calendars", response_model=ScmPromotionCalendarsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_promotion_calendars(
    data: ScmPromotionCalendarsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPromotionCalendarsService(db).create(data)

@router.put("/scm_promotion_calendars/{entity_id}", response_model=ScmPromotionCalendarsOut)
async def update_scm_promotion_calendars(
    entity_id: uuid.UUID,
    data: ScmPromotionCalendarsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmPromotionCalendarsService(db).update(entity_id, data)

@router.delete("/scm_promotion_calendars/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_promotion_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmPromotionCalendarsService(db).delete(entity_id)

@router.get("/scm_routing_distance_matrix", response_model=PaginatedResponse[ScmRoutingDistanceMatrixOut])
async def list_scm_routing_distance_matrix(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmRoutingDistanceMatrixService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_routing_distance_matrix/{entity_id}", response_model=ScmRoutingDistanceMatrixOut)
async def get_scm_routing_distance_matrix(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmRoutingDistanceMatrixService(db).get(entity_id)

@router.post("/scm_routing_distance_matrix", response_model=ScmRoutingDistanceMatrixOut, status_code=status.HTTP_201_CREATED)
async def create_scm_routing_distance_matrix(
    data: ScmRoutingDistanceMatrixCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingDistanceMatrixService(db).create(data)

@router.put("/scm_routing_distance_matrix/{entity_id}", response_model=ScmRoutingDistanceMatrixOut)
async def update_scm_routing_distance_matrix(
    entity_id: uuid.UUID,
    data: ScmRoutingDistanceMatrixUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingDistanceMatrixService(db).update(entity_id, data)

@router.delete("/scm_routing_distance_matrix/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_routing_distance_matrix(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmRoutingDistanceMatrixService(db).delete(entity_id)

@router.get("/scm_routing_locations", response_model=PaginatedResponse[ScmRoutingLocationsOut])
async def list_scm_routing_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmRoutingLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_routing_locations/{entity_id}", response_model=ScmRoutingLocationsOut)
async def get_scm_routing_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmRoutingLocationsService(db).get(entity_id)

@router.post("/scm_routing_locations", response_model=ScmRoutingLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_routing_locations(
    data: ScmRoutingLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingLocationsService(db).create(data)

@router.put("/scm_routing_locations/{entity_id}", response_model=ScmRoutingLocationsOut)
async def update_scm_routing_locations(
    entity_id: uuid.UUID,
    data: ScmRoutingLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingLocationsService(db).update(entity_id, data)

@router.delete("/scm_routing_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_routing_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmRoutingLocationsService(db).delete(entity_id)

@router.get("/scm_routing_problems", response_model=PaginatedResponse[ScmRoutingProblemsOut])
async def list_scm_routing_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmRoutingProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_routing_problems/{entity_id}", response_model=ScmRoutingProblemsOut)
async def get_scm_routing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmRoutingProblemsService(db).get(entity_id)

@router.post("/scm_routing_problems", response_model=ScmRoutingProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_routing_problems(
    data: ScmRoutingProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingProblemsService(db).create(data)

@router.put("/scm_routing_problems/{entity_id}", response_model=ScmRoutingProblemsOut)
async def update_scm_routing_problems(
    entity_id: uuid.UUID,
    data: ScmRoutingProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingProblemsService(db).update(entity_id, data)

@router.delete("/scm_routing_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_routing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmRoutingProblemsService(db).delete(entity_id)

@router.get("/scm_routing_solutions", response_model=PaginatedResponse[ScmRoutingSolutionsOut])
async def list_scm_routing_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmRoutingSolutionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_routing_solutions/{entity_id}", response_model=ScmRoutingSolutionsOut)
async def get_scm_routing_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmRoutingSolutionsService(db).get(entity_id)

@router.post("/scm_routing_solutions", response_model=ScmRoutingSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_routing_solutions(
    data: ScmRoutingSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingSolutionsService(db).create(data)

@router.put("/scm_routing_solutions/{entity_id}", response_model=ScmRoutingSolutionsOut)
async def update_scm_routing_solutions(
    entity_id: uuid.UUID,
    data: ScmRoutingSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingSolutionsService(db).update(entity_id, data)

@router.delete("/scm_routing_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_routing_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmRoutingSolutionsService(db).delete(entity_id)

@router.get("/scm_routing_vehicles", response_model=PaginatedResponse[ScmRoutingVehiclesOut])
async def list_scm_routing_vehicles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmRoutingVehiclesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["vehicle_code", "vehicle_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_routing_vehicles/{entity_id}", response_model=ScmRoutingVehiclesOut)
async def get_scm_routing_vehicles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmRoutingVehiclesService(db).get(entity_id)

@router.post("/scm_routing_vehicles", response_model=ScmRoutingVehiclesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_routing_vehicles(
    data: ScmRoutingVehiclesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingVehiclesService(db).create(data)

@router.put("/scm_routing_vehicles/{entity_id}", response_model=ScmRoutingVehiclesOut)
async def update_scm_routing_vehicles(
    entity_id: uuid.UUID,
    data: ScmRoutingVehiclesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmRoutingVehiclesService(db).update(entity_id, data)

@router.delete("/scm_routing_vehicles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_routing_vehicles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmRoutingVehiclesService(db).delete(entity_id)

@router.get("/scm_scenario_comparisons", response_model=PaginatedResponse[ScmScenarioComparisonsOut])
async def list_scm_scenario_comparisons(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScenarioComparisonsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scenario_comparisons/{entity_id}", response_model=ScmScenarioComparisonsOut)
async def get_scm_scenario_comparisons(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScenarioComparisonsService(db).get(entity_id)

@router.post("/scm_scenario_comparisons", response_model=ScmScenarioComparisonsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scenario_comparisons(
    data: ScmScenarioComparisonsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioComparisonsService(db).create(data)

@router.put("/scm_scenario_comparisons/{entity_id}", response_model=ScmScenarioComparisonsOut)
async def update_scm_scenario_comparisons(
    entity_id: uuid.UUID,
    data: ScmScenarioComparisonsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioComparisonsService(db).update(entity_id, data)

@router.delete("/scm_scenario_comparisons/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scenario_comparisons(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScenarioComparisonsService(db).delete(entity_id)

@router.get("/scm_scenario_results", response_model=PaginatedResponse[ScmScenarioResultsOut])
async def list_scm_scenario_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScenarioResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scenario_results/{entity_id}", response_model=ScmScenarioResultsOut)
async def get_scm_scenario_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScenarioResultsService(db).get(entity_id)

@router.post("/scm_scenario_results", response_model=ScmScenarioResultsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scenario_results(
    data: ScmScenarioResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioResultsService(db).create(data)

@router.put("/scm_scenario_results/{entity_id}", response_model=ScmScenarioResultsOut)
async def update_scm_scenario_results(
    entity_id: uuid.UUID,
    data: ScmScenarioResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioResultsService(db).update(entity_id, data)

@router.delete("/scm_scenario_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scenario_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScenarioResultsService(db).delete(entity_id)

@router.get("/scm_scenario_templates", response_model=PaginatedResponse[ScmScenarioTemplatesOut])
async def list_scm_scenario_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScenarioTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scenario_templates/{entity_id}", response_model=ScmScenarioTemplatesOut)
async def get_scm_scenario_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScenarioTemplatesService(db).get(entity_id)

@router.post("/scm_scenario_templates", response_model=ScmScenarioTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scenario_templates(
    data: ScmScenarioTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioTemplatesService(db).create(data)

@router.put("/scm_scenario_templates/{entity_id}", response_model=ScmScenarioTemplatesOut)
async def update_scm_scenario_templates(
    entity_id: uuid.UUID,
    data: ScmScenarioTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioTemplatesService(db).update(entity_id, data)

@router.delete("/scm_scenario_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scenario_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScenarioTemplatesService(db).delete(entity_id)

@router.get("/scm_scenario_types", response_model=PaginatedResponse[ScmScenarioTypesOut])
async def list_scm_scenario_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScenarioTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scenario_types/{entity_id}", response_model=ScmScenarioTypesOut)
async def get_scm_scenario_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScenarioTypesService(db).get(entity_id)

@router.post("/scm_scenario_types", response_model=ScmScenarioTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scenario_types(
    data: ScmScenarioTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioTypesService(db).create(data)

@router.put("/scm_scenario_types/{entity_id}", response_model=ScmScenarioTypesOut)
async def update_scm_scenario_types(
    entity_id: uuid.UUID,
    data: ScmScenarioTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenarioTypesService(db).update(entity_id, data)

@router.delete("/scm_scenario_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scenario_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScenarioTypesService(db).delete(entity_id)

@router.get("/scm_scenarios", response_model=PaginatedResponse[ScmScenariosOut])
async def list_scm_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scenarios/{entity_id}", response_model=ScmScenariosOut)
async def get_scm_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScenariosService(db).get(entity_id)

@router.post("/scm_scenarios", response_model=ScmScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scenarios(
    data: ScmScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenariosService(db).create(data)

@router.put("/scm_scenarios/{entity_id}", response_model=ScmScenariosOut)
async def update_scm_scenarios(
    entity_id: uuid.UUID,
    data: ScmScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScenariosService(db).update(entity_id, data)

@router.delete("/scm_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScenariosService(db).delete(entity_id)

@router.get("/scm_scipy_problems", response_model=PaginatedResponse[ScmScipyProblemsOut])
async def list_scm_scipy_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScipyProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_code", "problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scipy_problems/{entity_id}", response_model=ScmScipyProblemsOut)
async def get_scm_scipy_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScipyProblemsService(db).get(entity_id)

@router.post("/scm_scipy_problems", response_model=ScmScipyProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scipy_problems(
    data: ScmScipyProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyProblemsService(db).create(data)

@router.put("/scm_scipy_problems/{entity_id}", response_model=ScmScipyProblemsOut)
async def update_scm_scipy_problems(
    entity_id: uuid.UUID,
    data: ScmScipyProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyProblemsService(db).update(entity_id, data)

@router.delete("/scm_scipy_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scipy_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScipyProblemsService(db).delete(entity_id)

@router.get("/scm_scipy_results", response_model=PaginatedResponse[ScmScipyResultsOut])
async def list_scm_scipy_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScipyResultsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["result_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scipy_results/{entity_id}", response_model=ScmScipyResultsOut)
async def get_scm_scipy_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScipyResultsService(db).get(entity_id)

@router.post("/scm_scipy_results", response_model=ScmScipyResultsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scipy_results(
    data: ScmScipyResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyResultsService(db).create(data)

@router.put("/scm_scipy_results/{entity_id}", response_model=ScmScipyResultsOut)
async def update_scm_scipy_results(
    entity_id: uuid.UUID,
    data: ScmScipyResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyResultsService(db).update(entity_id, data)

@router.delete("/scm_scipy_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scipy_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScipyResultsService(db).delete(entity_id)

@router.get("/scm_scipy_statistical_tests", response_model=PaginatedResponse[ScmScipyStatisticalTestsOut])
async def list_scm_scipy_statistical_tests(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmScipyStatisticalTestsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["test_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_scipy_statistical_tests/{entity_id}", response_model=ScmScipyStatisticalTestsOut)
async def get_scm_scipy_statistical_tests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmScipyStatisticalTestsService(db).get(entity_id)

@router.post("/scm_scipy_statistical_tests", response_model=ScmScipyStatisticalTestsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_scipy_statistical_tests(
    data: ScmScipyStatisticalTestsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyStatisticalTestsService(db).create(data)

@router.put("/scm_scipy_statistical_tests/{entity_id}", response_model=ScmScipyStatisticalTestsOut)
async def update_scm_scipy_statistical_tests(
    entity_id: uuid.UUID,
    data: ScmScipyStatisticalTestsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmScipyStatisticalTestsService(db).update(entity_id, data)

@router.delete("/scm_scipy_statistical_tests/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_scipy_statistical_tests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmScipyStatisticalTestsService(db).delete(entity_id)

@router.get("/scm_seasonality_indices", response_model=PaginatedResponse[ScmSeasonalityIndicesOut])
async def list_scm_seasonality_indices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSeasonalityIndicesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["period_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_seasonality_indices/{entity_id}", response_model=ScmSeasonalityIndicesOut)
async def get_scm_seasonality_indices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSeasonalityIndicesService(db).get(entity_id)

@router.post("/scm_seasonality_indices", response_model=ScmSeasonalityIndicesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_seasonality_indices(
    data: ScmSeasonalityIndicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSeasonalityIndicesService(db).create(data)

@router.put("/scm_seasonality_indices/{entity_id}", response_model=ScmSeasonalityIndicesOut)
async def update_scm_seasonality_indices(
    entity_id: uuid.UUID,
    data: ScmSeasonalityIndicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSeasonalityIndicesService(db).update(entity_id, data)

@router.delete("/scm_seasonality_indices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_seasonality_indices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSeasonalityIndicesService(db).delete(entity_id)

@router.get("/scm_solver_benchmarks", response_model=PaginatedResponse[ScmSolverBenchmarksOut])
async def list_scm_solver_benchmarks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSolverBenchmarksService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_solver_benchmarks/{entity_id}", response_model=ScmSolverBenchmarksOut)
async def get_scm_solver_benchmarks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSolverBenchmarksService(db).get(entity_id)

@router.post("/scm_solver_benchmarks", response_model=ScmSolverBenchmarksOut, status_code=status.HTTP_201_CREATED)
async def create_scm_solver_benchmarks(
    data: ScmSolverBenchmarksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverBenchmarksService(db).create(data)

@router.put("/scm_solver_benchmarks/{entity_id}", response_model=ScmSolverBenchmarksOut)
async def update_scm_solver_benchmarks(
    entity_id: uuid.UUID,
    data: ScmSolverBenchmarksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverBenchmarksService(db).update(entity_id, data)

@router.delete("/scm_solver_benchmarks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_solver_benchmarks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSolverBenchmarksService(db).delete(entity_id)

@router.get("/scm_solver_instances", response_model=PaginatedResponse[ScmSolverInstancesOut])
async def list_scm_solver_instances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSolverInstancesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["instance_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_solver_instances/{entity_id}", response_model=ScmSolverInstancesOut)
async def get_scm_solver_instances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSolverInstancesService(db).get(entity_id)

@router.post("/scm_solver_instances", response_model=ScmSolverInstancesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_solver_instances(
    data: ScmSolverInstancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverInstancesService(db).create(data)

@router.put("/scm_solver_instances/{entity_id}", response_model=ScmSolverInstancesOut)
async def update_scm_solver_instances(
    entity_id: uuid.UUID,
    data: ScmSolverInstancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverInstancesService(db).update(entity_id, data)

@router.delete("/scm_solver_instances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_solver_instances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSolverInstancesService(db).delete(entity_id)

@router.get("/scm_solver_logs", response_model=PaginatedResponse[ScmSolverLogsOut])
async def list_scm_solver_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSolverLogsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_solver_logs/{entity_id}", response_model=ScmSolverLogsOut)
async def get_scm_solver_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSolverLogsService(db).get(entity_id)

@router.post("/scm_solver_logs", response_model=ScmSolverLogsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_solver_logs(
    data: ScmSolverLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverLogsService(db).create(data)

@router.put("/scm_solver_logs/{entity_id}", response_model=ScmSolverLogsOut)
async def update_scm_solver_logs(
    entity_id: uuid.UUID,
    data: ScmSolverLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverLogsService(db).update(entity_id, data)

@router.delete("/scm_solver_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_solver_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSolverLogsService(db).delete(entity_id)

@router.get("/scm_solver_parameters", response_model=PaginatedResponse[ScmSolverParametersOut])
async def list_scm_solver_parameters(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSolverParametersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["param_code", "param_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_solver_parameters/{entity_id}", response_model=ScmSolverParametersOut)
async def get_scm_solver_parameters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSolverParametersService(db).get(entity_id)

@router.post("/scm_solver_parameters", response_model=ScmSolverParametersOut, status_code=status.HTTP_201_CREATED)
async def create_scm_solver_parameters(
    data: ScmSolverParametersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverParametersService(db).create(data)

@router.put("/scm_solver_parameters/{entity_id}", response_model=ScmSolverParametersOut)
async def update_scm_solver_parameters(
    entity_id: uuid.UUID,
    data: ScmSolverParametersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverParametersService(db).update(entity_id, data)

@router.delete("/scm_solver_parameters/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_solver_parameters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSolverParametersService(db).delete(entity_id)

@router.get("/scm_solver_types", response_model=PaginatedResponse[ScmSolverTypesOut])
async def list_scm_solver_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSolverTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solver_code", "solver_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_solver_types/{entity_id}", response_model=ScmSolverTypesOut)
async def get_scm_solver_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSolverTypesService(db).get(entity_id)

@router.post("/scm_solver_types", response_model=ScmSolverTypesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_solver_types(
    data: ScmSolverTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverTypesService(db).create(data)

@router.put("/scm_solver_types/{entity_id}", response_model=ScmSolverTypesOut)
async def update_scm_solver_types(
    entity_id: uuid.UUID,
    data: ScmSolverTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSolverTypesService(db).update(entity_id, data)

@router.delete("/scm_solver_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_solver_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSolverTypesService(db).delete(entity_id)

@router.get("/scm_sop_cycles", response_model=PaginatedResponse[ScmSopCyclesOut])
async def list_scm_sop_cycles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopCyclesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["cycle_code", "cycle_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_cycles/{entity_id}", response_model=ScmSopCyclesOut)
async def get_scm_sop_cycles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopCyclesService(db).get(entity_id)

@router.post("/scm_sop_cycles", response_model=ScmSopCyclesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_cycles(
    data: ScmSopCyclesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopCyclesService(db).create(data)

@router.put("/scm_sop_cycles/{entity_id}", response_model=ScmSopCyclesOut)
async def update_scm_sop_cycles(
    entity_id: uuid.UUID,
    data: ScmSopCyclesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopCyclesService(db).update(entity_id, data)

@router.delete("/scm_sop_cycles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_cycles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopCyclesService(db).delete(entity_id)

@router.get("/scm_sop_decisions", response_model=PaginatedResponse[ScmSopDecisionsOut])
async def list_scm_sop_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopDecisionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_decisions/{entity_id}", response_model=ScmSopDecisionsOut)
async def get_scm_sop_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopDecisionsService(db).get(entity_id)

@router.post("/scm_sop_decisions", response_model=ScmSopDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_decisions(
    data: ScmSopDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopDecisionsService(db).create(data)

@router.put("/scm_sop_decisions/{entity_id}", response_model=ScmSopDecisionsOut)
async def update_scm_sop_decisions(
    entity_id: uuid.UUID,
    data: ScmSopDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopDecisionsService(db).update(entity_id, data)

@router.delete("/scm_sop_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopDecisionsService(db).delete(entity_id)

@router.get("/scm_sop_demand_plans", response_model=PaginatedResponse[ScmSopDemandPlansOut])
async def list_scm_sop_demand_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopDemandPlansService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_demand_plans/{entity_id}", response_model=ScmSopDemandPlansOut)
async def get_scm_sop_demand_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopDemandPlansService(db).get(entity_id)

@router.post("/scm_sop_demand_plans", response_model=ScmSopDemandPlansOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_demand_plans(
    data: ScmSopDemandPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopDemandPlansService(db).create(data)

@router.put("/scm_sop_demand_plans/{entity_id}", response_model=ScmSopDemandPlansOut)
async def update_scm_sop_demand_plans(
    entity_id: uuid.UUID,
    data: ScmSopDemandPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopDemandPlansService(db).update(entity_id, data)

@router.delete("/scm_sop_demand_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_demand_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopDemandPlansService(db).delete(entity_id)

@router.get("/scm_sop_kpis", response_model=PaginatedResponse[ScmSopKpisOut])
async def list_scm_sop_kpis(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopKpisService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_kpis/{entity_id}", response_model=ScmSopKpisOut)
async def get_scm_sop_kpis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopKpisService(db).get(entity_id)

@router.post("/scm_sop_kpis", response_model=ScmSopKpisOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_kpis(
    data: ScmSopKpisCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopKpisService(db).create(data)

@router.put("/scm_sop_kpis/{entity_id}", response_model=ScmSopKpisOut)
async def update_scm_sop_kpis(
    entity_id: uuid.UUID,
    data: ScmSopKpisUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopKpisService(db).update(entity_id, data)

@router.delete("/scm_sop_kpis/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_kpis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopKpisService(db).delete(entity_id)

@router.get("/scm_sop_reconciliation", response_model=PaginatedResponse[ScmSopReconciliationOut])
async def list_scm_sop_reconciliation(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopReconciliationService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_reconciliation/{entity_id}", response_model=ScmSopReconciliationOut)
async def get_scm_sop_reconciliation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopReconciliationService(db).get(entity_id)

@router.post("/scm_sop_reconciliation", response_model=ScmSopReconciliationOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_reconciliation(
    data: ScmSopReconciliationCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopReconciliationService(db).create(data)

@router.put("/scm_sop_reconciliation/{entity_id}", response_model=ScmSopReconciliationOut)
async def update_scm_sop_reconciliation(
    entity_id: uuid.UUID,
    data: ScmSopReconciliationUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopReconciliationService(db).update(entity_id, data)

@router.delete("/scm_sop_reconciliation/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_reconciliation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopReconciliationService(db).delete(entity_id)

@router.get("/scm_sop_scenarios", response_model=PaginatedResponse[ScmSopScenariosOut])
async def list_scm_sop_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_scenarios/{entity_id}", response_model=ScmSopScenariosOut)
async def get_scm_sop_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopScenariosService(db).get(entity_id)

@router.post("/scm_sop_scenarios", response_model=ScmSopScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_scenarios(
    data: ScmSopScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopScenariosService(db).create(data)

@router.put("/scm_sop_scenarios/{entity_id}", response_model=ScmSopScenariosOut)
async def update_scm_sop_scenarios(
    entity_id: uuid.UUID,
    data: ScmSopScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopScenariosService(db).update(entity_id, data)

@router.delete("/scm_sop_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopScenariosService(db).delete(entity_id)

@router.get("/scm_sop_supply_plans", response_model=PaginatedResponse[ScmSopSupplyPlansOut])
async def list_scm_sop_supply_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSopSupplyPlansService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_sop_supply_plans/{entity_id}", response_model=ScmSopSupplyPlansOut)
async def get_scm_sop_supply_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSopSupplyPlansService(db).get(entity_id)

@router.post("/scm_sop_supply_plans", response_model=ScmSopSupplyPlansOut, status_code=status.HTTP_201_CREATED)
async def create_scm_sop_supply_plans(
    data: ScmSopSupplyPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopSupplyPlansService(db).create(data)

@router.put("/scm_sop_supply_plans/{entity_id}", response_model=ScmSopSupplyPlansOut)
async def update_scm_sop_supply_plans(
    entity_id: uuid.UUID,
    data: ScmSopSupplyPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSopSupplyPlansService(db).update(entity_id, data)

@router.delete("/scm_sop_supply_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_sop_supply_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSopSupplyPlansService(db).delete(entity_id)

@router.get("/scm_supplier_forecasts", response_model=PaginatedResponse[ScmSupplierForecastsOut])
async def list_scm_supplier_forecasts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierForecastsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_forecasts/{entity_id}", response_model=ScmSupplierForecastsOut)
async def get_scm_supplier_forecasts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierForecastsService(db).get(entity_id)

@router.post("/scm_supplier_forecasts", response_model=ScmSupplierForecastsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_forecasts(
    data: ScmSupplierForecastsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierForecastsService(db).create(data)

@router.put("/scm_supplier_forecasts/{entity_id}", response_model=ScmSupplierForecastsOut)
async def update_scm_supplier_forecasts(
    entity_id: uuid.UUID,
    data: ScmSupplierForecastsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierForecastsService(db).update(entity_id, data)

@router.delete("/scm_supplier_forecasts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_forecasts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierForecastsService(db).delete(entity_id)

@router.get("/scm_supplier_performance", response_model=PaginatedResponse[ScmSupplierPerformanceOut])
async def list_scm_supplier_performance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierPerformanceService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_performance/{entity_id}", response_model=ScmSupplierPerformanceOut)
async def get_scm_supplier_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierPerformanceService(db).get(entity_id)

@router.post("/scm_supplier_performance", response_model=ScmSupplierPerformanceOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_performance(
    data: ScmSupplierPerformanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierPerformanceService(db).create(data)

@router.put("/scm_supplier_performance/{entity_id}", response_model=ScmSupplierPerformanceOut)
async def update_scm_supplier_performance(
    entity_id: uuid.UUID,
    data: ScmSupplierPerformanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierPerformanceService(db).update(entity_id, data)

@router.delete("/scm_supplier_performance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierPerformanceService(db).delete(entity_id)

@router.get("/scm_supplier_profiles", response_model=PaginatedResponse[ScmSupplierProfilesOut])
async def list_scm_supplier_profiles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierProfilesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_profiles/{entity_id}", response_model=ScmSupplierProfilesOut)
async def get_scm_supplier_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierProfilesService(db).get(entity_id)

@router.post("/scm_supplier_profiles", response_model=ScmSupplierProfilesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_profiles(
    data: ScmSupplierProfilesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierProfilesService(db).create(data)

@router.put("/scm_supplier_profiles/{entity_id}", response_model=ScmSupplierProfilesOut)
async def update_scm_supplier_profiles(
    entity_id: uuid.UUID,
    data: ScmSupplierProfilesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierProfilesService(db).update(entity_id, data)

@router.delete("/scm_supplier_profiles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierProfilesService(db).delete(entity_id)

@router.get("/scm_supplier_risk_assessments", response_model=PaginatedResponse[ScmSupplierRiskAssessmentsOut])
async def list_scm_supplier_risk_assessments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierRiskAssessmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_risk_assessments/{entity_id}", response_model=ScmSupplierRiskAssessmentsOut)
async def get_scm_supplier_risk_assessments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierRiskAssessmentsService(db).get(entity_id)

@router.post("/scm_supplier_risk_assessments", response_model=ScmSupplierRiskAssessmentsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_risk_assessments(
    data: ScmSupplierRiskAssessmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierRiskAssessmentsService(db).create(data)

@router.put("/scm_supplier_risk_assessments/{entity_id}", response_model=ScmSupplierRiskAssessmentsOut)
async def update_scm_supplier_risk_assessments(
    entity_id: uuid.UUID,
    data: ScmSupplierRiskAssessmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierRiskAssessmentsService(db).update(entity_id, data)

@router.delete("/scm_supplier_risk_assessments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_risk_assessments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierRiskAssessmentsService(db).delete(entity_id)

@router.get("/scm_supplier_scorecards", response_model=PaginatedResponse[ScmSupplierScorecardsOut])
async def list_scm_supplier_scorecards(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierScorecardsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_scorecards/{entity_id}", response_model=ScmSupplierScorecardsOut)
async def get_scm_supplier_scorecards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierScorecardsService(db).get(entity_id)

@router.post("/scm_supplier_scorecards", response_model=ScmSupplierScorecardsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_scorecards(
    data: ScmSupplierScorecardsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierScorecardsService(db).create(data)

@router.put("/scm_supplier_scorecards/{entity_id}", response_model=ScmSupplierScorecardsOut)
async def update_scm_supplier_scorecards(
    entity_id: uuid.UUID,
    data: ScmSupplierScorecardsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierScorecardsService(db).update(entity_id, data)

@router.delete("/scm_supplier_scorecards/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_scorecards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierScorecardsService(db).delete(entity_id)

@router.get("/scm_supplier_sustainability", response_model=PaginatedResponse[ScmSupplierSustainabilityOut])
async def list_scm_supplier_sustainability(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplierSustainabilityService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supplier_sustainability/{entity_id}", response_model=ScmSupplierSustainabilityOut)
async def get_scm_supplier_sustainability(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplierSustainabilityService(db).get(entity_id)

@router.post("/scm_supplier_sustainability", response_model=ScmSupplierSustainabilityOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supplier_sustainability(
    data: ScmSupplierSustainabilityCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierSustainabilityService(db).create(data)

@router.put("/scm_supplier_sustainability/{entity_id}", response_model=ScmSupplierSustainabilityOut)
async def update_scm_supplier_sustainability(
    entity_id: uuid.UUID,
    data: ScmSupplierSustainabilityUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplierSustainabilityService(db).update(entity_id, data)

@router.delete("/scm_supplier_sustainability/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supplier_sustainability(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplierSustainabilityService(db).delete(entity_id)

@router.get("/scm_supply_calendar_dates", response_model=PaginatedResponse[ScmSupplyCalendarDatesOut])
async def list_scm_supply_calendar_dates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyCalendarDatesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_calendar_dates/{entity_id}", response_model=ScmSupplyCalendarDatesOut)
async def get_scm_supply_calendar_dates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyCalendarDatesService(db).get(entity_id)

@router.post("/scm_supply_calendar_dates", response_model=ScmSupplyCalendarDatesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_calendar_dates(
    data: ScmSupplyCalendarDatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyCalendarDatesService(db).create(data)

@router.put("/scm_supply_calendar_dates/{entity_id}", response_model=ScmSupplyCalendarDatesOut)
async def update_scm_supply_calendar_dates(
    entity_id: uuid.UUID,
    data: ScmSupplyCalendarDatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyCalendarDatesService(db).update(entity_id, data)

@router.delete("/scm_supply_calendar_dates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_calendar_dates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyCalendarDatesService(db).delete(entity_id)

@router.get("/scm_supply_calendars", response_model=PaginatedResponse[ScmSupplyCalendarsOut])
async def list_scm_supply_calendars(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyCalendarsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["calendar_code", "calendar_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_calendars/{entity_id}", response_model=ScmSupplyCalendarsOut)
async def get_scm_supply_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyCalendarsService(db).get(entity_id)

@router.post("/scm_supply_calendars", response_model=ScmSupplyCalendarsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_calendars(
    data: ScmSupplyCalendarsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyCalendarsService(db).create(data)

@router.put("/scm_supply_calendars/{entity_id}", response_model=ScmSupplyCalendarsOut)
async def update_scm_supply_calendars(
    entity_id: uuid.UUID,
    data: ScmSupplyCalendarsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyCalendarsService(db).update(entity_id, data)

@router.delete("/scm_supply_calendars/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyCalendarsService(db).delete(entity_id)

@router.get("/scm_supply_constraints", response_model=PaginatedResponse[ScmSupplyConstraintsOut])
async def list_scm_supply_constraints(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyConstraintsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["constraint_code", "constraint_name", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_constraints/{entity_id}", response_model=ScmSupplyConstraintsOut)
async def get_scm_supply_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyConstraintsService(db).get(entity_id)

@router.post("/scm_supply_constraints", response_model=ScmSupplyConstraintsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_constraints(
    data: ScmSupplyConstraintsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyConstraintsService(db).create(data)

@router.put("/scm_supply_constraints/{entity_id}", response_model=ScmSupplyConstraintsOut)
async def update_scm_supply_constraints(
    entity_id: uuid.UUID,
    data: ScmSupplyConstraintsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyConstraintsService(db).update(entity_id, data)

@router.delete("/scm_supply_constraints/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyConstraintsService(db).delete(entity_id)

@router.get("/scm_supply_lead_times", response_model=PaginatedResponse[ScmSupplyLeadTimesOut])
async def list_scm_supply_lead_times(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyLeadTimesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_lead_times/{entity_id}", response_model=ScmSupplyLeadTimesOut)
async def get_scm_supply_lead_times(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyLeadTimesService(db).get(entity_id)

@router.post("/scm_supply_lead_times", response_model=ScmSupplyLeadTimesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_lead_times(
    data: ScmSupplyLeadTimesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyLeadTimesService(db).create(data)

@router.put("/scm_supply_lead_times/{entity_id}", response_model=ScmSupplyLeadTimesOut)
async def update_scm_supply_lead_times(
    entity_id: uuid.UUID,
    data: ScmSupplyLeadTimesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyLeadTimesService(db).update(entity_id, data)

@router.delete("/scm_supply_lead_times/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_lead_times(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyLeadTimesService(db).delete(entity_id)

@router.get("/scm_supply_plan_lines", response_model=PaginatedResponse[ScmSupplyPlanLinesOut])
async def list_scm_supply_plan_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyPlanLinesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_plan_lines/{entity_id}", response_model=ScmSupplyPlanLinesOut)
async def get_scm_supply_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyPlanLinesService(db).get(entity_id)

@router.post("/scm_supply_plan_lines", response_model=ScmSupplyPlanLinesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_plan_lines(
    data: ScmSupplyPlanLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyPlanLinesService(db).create(data)

@router.put("/scm_supply_plan_lines/{entity_id}", response_model=ScmSupplyPlanLinesOut)
async def update_scm_supply_plan_lines(
    entity_id: uuid.UUID,
    data: ScmSupplyPlanLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyPlanLinesService(db).update(entity_id, data)

@router.delete("/scm_supply_plan_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyPlanLinesService(db).delete(entity_id)

@router.get("/scm_supply_plans", response_model=PaginatedResponse[ScmSupplyPlansOut])
async def list_scm_supply_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyPlansService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_plans/{entity_id}", response_model=ScmSupplyPlansOut)
async def get_scm_supply_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyPlansService(db).get(entity_id)

@router.post("/scm_supply_plans", response_model=ScmSupplyPlansOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_plans(
    data: ScmSupplyPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyPlansService(db).create(data)

@router.put("/scm_supply_plans/{entity_id}", response_model=ScmSupplyPlansOut)
async def update_scm_supply_plans(
    entity_id: uuid.UUID,
    data: ScmSupplyPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyPlansService(db).update(entity_id, data)

@router.delete("/scm_supply_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyPlansService(db).delete(entity_id)

@router.get("/scm_supply_risks", response_model=PaginatedResponse[ScmSupplyRisksOut])
async def list_scm_supply_risks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplyRisksService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_risks/{entity_id}", response_model=ScmSupplyRisksOut)
async def get_scm_supply_risks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplyRisksService(db).get(entity_id)

@router.post("/scm_supply_risks", response_model=ScmSupplyRisksOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_risks(
    data: ScmSupplyRisksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyRisksService(db).create(data)

@router.put("/scm_supply_risks/{entity_id}", response_model=ScmSupplyRisksOut)
async def update_scm_supply_risks(
    entity_id: uuid.UUID,
    data: ScmSupplyRisksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplyRisksService(db).update(entity_id, data)

@router.delete("/scm_supply_risks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_risks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplyRisksService(db).delete(entity_id)

@router.get("/scm_supply_sources", response_model=PaginatedResponse[ScmSupplySourcesOut])
async def list_scm_supply_sources(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmSupplySourcesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["source_code", "source_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_supply_sources/{entity_id}", response_model=ScmSupplySourcesOut)
async def get_scm_supply_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmSupplySourcesService(db).get(entity_id)

@router.post("/scm_supply_sources", response_model=ScmSupplySourcesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_supply_sources(
    data: ScmSupplySourcesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplySourcesService(db).create(data)

@router.put("/scm_supply_sources/{entity_id}", response_model=ScmSupplySourcesOut)
async def update_scm_supply_sources(
    entity_id: uuid.UUID,
    data: ScmSupplySourcesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmSupplySourcesService(db).update(entity_id, data)

@router.delete("/scm_supply_sources/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_supply_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmSupplySourcesService(db).delete(entity_id)

@router.get("/scm_transportation_constraints", response_model=PaginatedResponse[ScmTransportationConstraintsOut])
async def list_scm_transportation_constraints(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationConstraintsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_constraints/{entity_id}", response_model=ScmTransportationConstraintsOut)
async def get_scm_transportation_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationConstraintsService(db).get(entity_id)

@router.post("/scm_transportation_constraints", response_model=ScmTransportationConstraintsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_constraints(
    data: ScmTransportationConstraintsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationConstraintsService(db).create(data)

@router.put("/scm_transportation_constraints/{entity_id}", response_model=ScmTransportationConstraintsOut)
async def update_scm_transportation_constraints(
    entity_id: uuid.UUID,
    data: ScmTransportationConstraintsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationConstraintsService(db).update(entity_id, data)

@router.delete("/scm_transportation_constraints/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationConstraintsService(db).delete(entity_id)

@router.get("/scm_transportation_costs", response_model=PaginatedResponse[ScmTransportationCostsOut])
async def list_scm_transportation_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_costs/{entity_id}", response_model=ScmTransportationCostsOut)
async def get_scm_transportation_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationCostsService(db).get(entity_id)

@router.post("/scm_transportation_costs", response_model=ScmTransportationCostsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_costs(
    data: ScmTransportationCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationCostsService(db).create(data)

@router.put("/scm_transportation_costs/{entity_id}", response_model=ScmTransportationCostsOut)
async def update_scm_transportation_costs(
    entity_id: uuid.UUID,
    data: ScmTransportationCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationCostsService(db).update(entity_id, data)

@router.delete("/scm_transportation_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationCostsService(db).delete(entity_id)

@router.get("/scm_transportation_modes", response_model=PaginatedResponse[ScmTransportationModesOut])
async def list_scm_transportation_modes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationModesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["mode_code", "mode_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_modes/{entity_id}", response_model=ScmTransportationModesOut)
async def get_scm_transportation_modes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationModesService(db).get(entity_id)

@router.post("/scm_transportation_modes", response_model=ScmTransportationModesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_modes(
    data: ScmTransportationModesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationModesService(db).create(data)

@router.put("/scm_transportation_modes/{entity_id}", response_model=ScmTransportationModesOut)
async def update_scm_transportation_modes(
    entity_id: uuid.UUID,
    data: ScmTransportationModesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationModesService(db).update(entity_id, data)

@router.delete("/scm_transportation_modes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_modes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationModesService(db).delete(entity_id)

@router.get("/scm_transportation_recommendations", response_model=PaginatedResponse[ScmTransportationRecommendationsOut])
async def list_scm_transportation_recommendations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationRecommendationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_recommendations/{entity_id}", response_model=ScmTransportationRecommendationsOut)
async def get_scm_transportation_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationRecommendationsService(db).get(entity_id)

@router.post("/scm_transportation_recommendations", response_model=ScmTransportationRecommendationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_recommendations(
    data: ScmTransportationRecommendationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationRecommendationsService(db).create(data)

@router.put("/scm_transportation_recommendations/{entity_id}", response_model=ScmTransportationRecommendationsOut)
async def update_scm_transportation_recommendations(
    entity_id: uuid.UUID,
    data: ScmTransportationRecommendationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationRecommendationsService(db).update(entity_id, data)

@router.delete("/scm_transportation_recommendations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationRecommendationsService(db).delete(entity_id)

@router.get("/scm_transportation_scenarios", response_model=PaginatedResponse[ScmTransportationScenariosOut])
async def list_scm_transportation_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_scenarios/{entity_id}", response_model=ScmTransportationScenariosOut)
async def get_scm_transportation_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationScenariosService(db).get(entity_id)

@router.post("/scm_transportation_scenarios", response_model=ScmTransportationScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_scenarios(
    data: ScmTransportationScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationScenariosService(db).create(data)

@router.put("/scm_transportation_scenarios/{entity_id}", response_model=ScmTransportationScenariosOut)
async def update_scm_transportation_scenarios(
    entity_id: uuid.UUID,
    data: ScmTransportationScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationScenariosService(db).update(entity_id, data)

@router.delete("/scm_transportation_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationScenariosService(db).delete(entity_id)

@router.get("/scm_transportation_service_levels", response_model=PaginatedResponse[ScmTransportationServiceLevelsOut])
async def list_scm_transportation_service_levels(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmTransportationServiceLevelsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_transportation_service_levels/{entity_id}", response_model=ScmTransportationServiceLevelsOut)
async def get_scm_transportation_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmTransportationServiceLevelsService(db).get(entity_id)

@router.post("/scm_transportation_service_levels", response_model=ScmTransportationServiceLevelsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_transportation_service_levels(
    data: ScmTransportationServiceLevelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationServiceLevelsService(db).create(data)

@router.put("/scm_transportation_service_levels/{entity_id}", response_model=ScmTransportationServiceLevelsOut)
async def update_scm_transportation_service_levels(
    entity_id: uuid.UUID,
    data: ScmTransportationServiceLevelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmTransportationServiceLevelsService(db).update(entity_id, data)

@router.delete("/scm_transportation_service_levels/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_transportation_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmTransportationServiceLevelsService(db).delete(entity_id)

@router.get("/scm_warehouse_aisles", response_model=PaginatedResponse[ScmWarehouseAislesOut])
async def list_scm_warehouse_aisles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehouseAislesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["aisle_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_aisles/{entity_id}", response_model=ScmWarehouseAislesOut)
async def get_scm_warehouse_aisles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehouseAislesService(db).get(entity_id)

@router.post("/scm_warehouse_aisles", response_model=ScmWarehouseAislesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_aisles(
    data: ScmWarehouseAislesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseAislesService(db).create(data)

@router.put("/scm_warehouse_aisles/{entity_id}", response_model=ScmWarehouseAislesOut)
async def update_scm_warehouse_aisles(
    entity_id: uuid.UUID,
    data: ScmWarehouseAislesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseAislesService(db).update(entity_id, data)

@router.delete("/scm_warehouse_aisles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_aisles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehouseAislesService(db).delete(entity_id)

@router.get("/scm_warehouse_locations", response_model=PaginatedResponse[ScmWarehouseLocationsOut])
async def list_scm_warehouse_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehouseLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_locations/{entity_id}", response_model=ScmWarehouseLocationsOut)
async def get_scm_warehouse_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehouseLocationsService(db).get(entity_id)

@router.post("/scm_warehouse_locations", response_model=ScmWarehouseLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_locations(
    data: ScmWarehouseLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseLocationsService(db).create(data)

@router.put("/scm_warehouse_locations/{entity_id}", response_model=ScmWarehouseLocationsOut)
async def update_scm_warehouse_locations(
    entity_id: uuid.UUID,
    data: ScmWarehouseLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseLocationsService(db).update(entity_id, data)

@router.delete("/scm_warehouse_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehouseLocationsService(db).delete(entity_id)

@router.get("/scm_warehouse_pick_batches", response_model=PaginatedResponse[ScmWarehousePickBatchesOut])
async def list_scm_warehouse_pick_batches(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehousePickBatchesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["batch_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_pick_batches/{entity_id}", response_model=ScmWarehousePickBatchesOut)
async def get_scm_warehouse_pick_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehousePickBatchesService(db).get(entity_id)

@router.post("/scm_warehouse_pick_batches", response_model=ScmWarehousePickBatchesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_pick_batches(
    data: ScmWarehousePickBatchesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickBatchesService(db).create(data)

@router.put("/scm_warehouse_pick_batches/{entity_id}", response_model=ScmWarehousePickBatchesOut)
async def update_scm_warehouse_pick_batches(
    entity_id: uuid.UUID,
    data: ScmWarehousePickBatchesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickBatchesService(db).update(entity_id, data)

@router.delete("/scm_warehouse_pick_batches/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_pick_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehousePickBatchesService(db).delete(entity_id)

@router.get("/scm_warehouse_pick_lines", response_model=PaginatedResponse[ScmWarehousePickLinesOut])
async def list_scm_warehouse_pick_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehousePickLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_pick_lines/{entity_id}", response_model=ScmWarehousePickLinesOut)
async def get_scm_warehouse_pick_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehousePickLinesService(db).get(entity_id)

@router.post("/scm_warehouse_pick_lines", response_model=ScmWarehousePickLinesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_pick_lines(
    data: ScmWarehousePickLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickLinesService(db).create(data)

@router.put("/scm_warehouse_pick_lines/{entity_id}", response_model=ScmWarehousePickLinesOut)
async def update_scm_warehouse_pick_lines(
    entity_id: uuid.UUID,
    data: ScmWarehousePickLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickLinesService(db).update(entity_id, data)

@router.delete("/scm_warehouse_pick_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_pick_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehousePickLinesService(db).delete(entity_id)

@router.get("/scm_warehouse_pick_orders", response_model=PaginatedResponse[ScmWarehousePickOrdersOut])
async def list_scm_warehouse_pick_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehousePickOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_pick_orders/{entity_id}", response_model=ScmWarehousePickOrdersOut)
async def get_scm_warehouse_pick_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehousePickOrdersService(db).get(entity_id)

@router.post("/scm_warehouse_pick_orders", response_model=ScmWarehousePickOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_pick_orders(
    data: ScmWarehousePickOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickOrdersService(db).create(data)

@router.put("/scm_warehouse_pick_orders/{entity_id}", response_model=ScmWarehousePickOrdersOut)
async def update_scm_warehouse_pick_orders(
    entity_id: uuid.UUID,
    data: ScmWarehousePickOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehousePickOrdersService(db).update(entity_id, data)

@router.delete("/scm_warehouse_pick_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_pick_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehousePickOrdersService(db).delete(entity_id)

@router.get("/scm_warehouse_waves", response_model=PaginatedResponse[ScmWarehouseWavesOut])
async def list_scm_warehouse_waves(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehouseWavesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["wave_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_waves/{entity_id}", response_model=ScmWarehouseWavesOut)
async def get_scm_warehouse_waves(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehouseWavesService(db).get(entity_id)

@router.post("/scm_warehouse_waves", response_model=ScmWarehouseWavesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_waves(
    data: ScmWarehouseWavesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseWavesService(db).create(data)

@router.put("/scm_warehouse_waves/{entity_id}", response_model=ScmWarehouseWavesOut)
async def update_scm_warehouse_waves(
    entity_id: uuid.UUID,
    data: ScmWarehouseWavesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseWavesService(db).update(entity_id, data)

@router.delete("/scm_warehouse_waves/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_waves(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehouseWavesService(db).delete(entity_id)

@router.get("/scm_warehouse_zones", response_model=PaginatedResponse[ScmWarehouseZonesOut])
async def list_scm_warehouse_zones(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    svc = ScmWarehouseZonesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["zone_code", "zone_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/scm_warehouse_zones/{entity_id}", response_model=ScmWarehouseZonesOut)
async def get_scm_warehouse_zones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "view"),
):
    return await ScmWarehouseZonesService(db).get(entity_id)

@router.post("/scm_warehouse_zones", response_model=ScmWarehouseZonesOut, status_code=status.HTTP_201_CREATED)
async def create_scm_warehouse_zones(
    data: ScmWarehouseZonesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseZonesService(db).create(data)

@router.put("/scm_warehouse_zones/{entity_id}", response_model=ScmWarehouseZonesOut)
async def update_scm_warehouse_zones(
    entity_id: uuid.UUID,
    data: ScmWarehouseZonesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    return await ScmWarehouseZonesService(db).update(entity_id, data)

@router.delete("/scm_warehouse_zones/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scm_warehouse_zones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("scm", "manage"),
):
    await ScmWarehouseZonesService(db).delete(entity_id)
