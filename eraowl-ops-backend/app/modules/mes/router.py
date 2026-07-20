import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.mes.services import (
    JobOrdersService,
    MachineTelemetryService,
    MesAiAgentLogsService,
    MesAiFeatureStoreService,
    MesAiModelRegistryService,
    MesAiWorkflowStatesService,
    MesAlertsService,
    MesAlgorithmsService,
    MesAndonBoardsService,
    MesAndonTriggersService,
    MesBatchRecordMaterialsService,
    MesBatchRecordStepsService,
    MesBatchRecordsService,
    MesCrewAssignmentsService,
    MesCrewsService,
    MesCribCompartmentsService,
    MesCribPackingResultsService,
    MesDeliveryRequestsService,
    MesDeliveryRoutesService,
    MesDigitalTwinModelsService,
    MesDocumentInstancesService,
    MesDocumentsService,
    MesDowntimeEventsService,
    MesDowntimeReasonsService,
    MesEnergyMetersService,
    MesEnergyReadingsService,
    MesEquipmentService,
    MesEquipmentAssignmentsService,
    MesEquipmentCapabilitiesService,
    MesEquipmentCertificationsService,
    MesEquipmentClassesService,
    MesEquipmentConnectionsService,
    MesEquipmentDataPointsService,
    MesEquipmentLocationsService,
    MesEquipmentStatusesService,
    MesEquipmentTypesService,
    MesGenealogyService,
    MesGenealogySnapshotsService,
    MesInstructionAcknowledgmentsService,
    MesInstructionVersionsService,
    MesInstructionsService,
    MesIntegrationConnectionsService,
    MesIntegrationLogsService,
    MesKpiActualsService,
    MesKpiDefinitionsService,
    MesLaborAssignmentsService,
    MesLaborTimeCollectionService,
    MesLineBalancingService,
    MesLlmConfigsService,
    MesMachineAlarmsService,
    MesMachineDataValuesService,
    MesMachineEventsService,
    MesMachineProgramsService,
    MesMaintenanceHistoryService,
    MesMaintenancePartsService,
    MesMaintenanceSchedulesService,
    MesMaintenanceWorkOrdersService,
    MesMaterialConsumptionService,
    MesMaterialIssuesService,
    MesMaterialReturnsService,
    MesMlModelVersionsService,
    MesMlModelsService,
    MesNotificationsService,
    MesOeeCalculationsService,
    MesOeeLossesService,
    MesOeeTargetsService,
    MesOperationExecutionService,
    MesOperationStepsService,
    MesOperatorAssignmentsService,
    MesOperatorCertificationsService,
    MesOperatorPerformanceService,
    MesOperatorSchedulesService,
    MesOperatorSkillsService,
    MesOperatorTrainingService,
    MesOperatorsService,
    MesOptimizationProblemsService,
    MesOptimizationResultsService,
    MesOrtoolsProblemsService,
    MesPerformanceActualsService,
    MesPerformanceMetricsService,
    MesPredictionsService,
    MesProductionCellsService,
    MesProductionLinesService,
    MesPromptTemplatesService,
    MesQualityHoldsService,
    MesQualityInspectionsService,
    MesQualitySpcDataService,
    MesResourceAvailabilityService,
    MesResourceCostsService,
    MesResourceTypesService,
    MesResourcesService,
    MesScenariosService,
    MesScheduleResultsService,
    MesSchedulingProblemsService,
    MesScipyAnalysesService,
    MesSensorCalibrationsService,
    MesSensorsService,
    MesShiftHandoversService,
    MesShiftSchedulesService,
    MesShiftsService,
    MesSolverConfigsService,
    MesStationAssignmentsService,
    MesStationTypesService,
    MesStationsService,
    MesToolCribsService,
    MesToolingAssignmentsService,
    MesToolingLifeTrackingService,
    MesToolingMasterService,
    MesToolingTypesService,
    MesVectorStoreConfigsService,
    MesVectorStoreDocumentsService,
    MesWorkCenterCalendarsService,
    MesWorkCenterCapacitiesService,
    MesWorkCenterConstraintsService,
    MesWorkCenterTypesService,
    MesWorkCentersService,
    MesWorkOrderExecutionService,
    MesWorkOrderHoldsService,
    MesWorkOrderSignaturesService,
    MesWorkflowDefinitionsService,
    MesWorkflowExecutionsService,
    WorkCentersService,
)
from app.modules.mes.schemas import (
    JobOrdersCreate,
    JobOrdersUpdate,
    JobOrdersOut,
    MachineTelemetryCreate,
    MachineTelemetryUpdate,
    MachineTelemetryOut,
    MesAiAgentLogsCreate,
    MesAiAgentLogsUpdate,
    MesAiAgentLogsOut,
    MesAiFeatureStoreCreate,
    MesAiFeatureStoreUpdate,
    MesAiFeatureStoreOut,
    MesAiModelRegistryCreate,
    MesAiModelRegistryUpdate,
    MesAiModelRegistryOut,
    MesAiWorkflowStatesCreate,
    MesAiWorkflowStatesUpdate,
    MesAiWorkflowStatesOut,
    MesAlertsCreate,
    MesAlertsUpdate,
    MesAlertsOut,
    MesAlgorithmsCreate,
    MesAlgorithmsUpdate,
    MesAlgorithmsOut,
    MesAndonBoardsCreate,
    MesAndonBoardsUpdate,
    MesAndonBoardsOut,
    MesAndonTriggersCreate,
    MesAndonTriggersUpdate,
    MesAndonTriggersOut,
    MesBatchRecordMaterialsCreate,
    MesBatchRecordMaterialsUpdate,
    MesBatchRecordMaterialsOut,
    MesBatchRecordStepsCreate,
    MesBatchRecordStepsUpdate,
    MesBatchRecordStepsOut,
    MesBatchRecordsCreate,
    MesBatchRecordsUpdate,
    MesBatchRecordsOut,
    MesCrewAssignmentsCreate,
    MesCrewAssignmentsUpdate,
    MesCrewAssignmentsOut,
    MesCrewsCreate,
    MesCrewsUpdate,
    MesCrewsOut,
    MesCribCompartmentsCreate,
    MesCribCompartmentsUpdate,
    MesCribCompartmentsOut,
    MesCribPackingResultsCreate,
    MesCribPackingResultsUpdate,
    MesCribPackingResultsOut,
    MesDeliveryRequestsCreate,
    MesDeliveryRequestsUpdate,
    MesDeliveryRequestsOut,
    MesDeliveryRoutesCreate,
    MesDeliveryRoutesUpdate,
    MesDeliveryRoutesOut,
    MesDigitalTwinModelsCreate,
    MesDigitalTwinModelsUpdate,
    MesDigitalTwinModelsOut,
    MesDocumentInstancesCreate,
    MesDocumentInstancesUpdate,
    MesDocumentInstancesOut,
    MesDocumentsCreate,
    MesDocumentsUpdate,
    MesDocumentsOut,
    MesDowntimeEventsCreate,
    MesDowntimeEventsUpdate,
    MesDowntimeEventsOut,
    MesDowntimeReasonsCreate,
    MesDowntimeReasonsUpdate,
    MesDowntimeReasonsOut,
    MesEnergyMetersCreate,
    MesEnergyMetersUpdate,
    MesEnergyMetersOut,
    MesEnergyReadingsCreate,
    MesEnergyReadingsUpdate,
    MesEnergyReadingsOut,
    MesEquipmentCreate,
    MesEquipmentUpdate,
    MesEquipmentOut,
    MesEquipmentAssignmentsCreate,
    MesEquipmentAssignmentsUpdate,
    MesEquipmentAssignmentsOut,
    MesEquipmentCapabilitiesCreate,
    MesEquipmentCapabilitiesUpdate,
    MesEquipmentCapabilitiesOut,
    MesEquipmentCertificationsCreate,
    MesEquipmentCertificationsUpdate,
    MesEquipmentCertificationsOut,
    MesEquipmentClassesCreate,
    MesEquipmentClassesUpdate,
    MesEquipmentClassesOut,
    MesEquipmentConnectionsCreate,
    MesEquipmentConnectionsUpdate,
    MesEquipmentConnectionsOut,
    MesEquipmentDataPointsCreate,
    MesEquipmentDataPointsUpdate,
    MesEquipmentDataPointsOut,
    MesEquipmentLocationsCreate,
    MesEquipmentLocationsUpdate,
    MesEquipmentLocationsOut,
    MesEquipmentStatusesCreate,
    MesEquipmentStatusesUpdate,
    MesEquipmentStatusesOut,
    MesEquipmentTypesCreate,
    MesEquipmentTypesUpdate,
    MesEquipmentTypesOut,
    MesGenealogyCreate,
    MesGenealogyUpdate,
    MesGenealogyOut,
    MesGenealogySnapshotsCreate,
    MesGenealogySnapshotsUpdate,
    MesGenealogySnapshotsOut,
    MesInstructionAcknowledgmentsCreate,
    MesInstructionAcknowledgmentsUpdate,
    MesInstructionAcknowledgmentsOut,
    MesInstructionVersionsCreate,
    MesInstructionVersionsUpdate,
    MesInstructionVersionsOut,
    MesInstructionsCreate,
    MesInstructionsUpdate,
    MesInstructionsOut,
    MesIntegrationConnectionsCreate,
    MesIntegrationConnectionsUpdate,
    MesIntegrationConnectionsOut,
    MesIntegrationLogsCreate,
    MesIntegrationLogsUpdate,
    MesIntegrationLogsOut,
    MesKpiActualsCreate,
    MesKpiActualsUpdate,
    MesKpiActualsOut,
    MesKpiDefinitionsCreate,
    MesKpiDefinitionsUpdate,
    MesKpiDefinitionsOut,
    MesLaborAssignmentsCreate,
    MesLaborAssignmentsUpdate,
    MesLaborAssignmentsOut,
    MesLaborTimeCollectionCreate,
    MesLaborTimeCollectionUpdate,
    MesLaborTimeCollectionOut,
    MesLineBalancingCreate,
    MesLineBalancingUpdate,
    MesLineBalancingOut,
    MesLlmConfigsCreate,
    MesLlmConfigsUpdate,
    MesLlmConfigsOut,
    MesMachineAlarmsCreate,
    MesMachineAlarmsUpdate,
    MesMachineAlarmsOut,
    MesMachineDataValuesCreate,
    MesMachineDataValuesUpdate,
    MesMachineDataValuesOut,
    MesMachineEventsCreate,
    MesMachineEventsUpdate,
    MesMachineEventsOut,
    MesMachineProgramsCreate,
    MesMachineProgramsUpdate,
    MesMachineProgramsOut,
    MesMaintenanceHistoryCreate,
    MesMaintenanceHistoryUpdate,
    MesMaintenanceHistoryOut,
    MesMaintenancePartsCreate,
    MesMaintenancePartsUpdate,
    MesMaintenancePartsOut,
    MesMaintenanceSchedulesCreate,
    MesMaintenanceSchedulesUpdate,
    MesMaintenanceSchedulesOut,
    MesMaintenanceWorkOrdersCreate,
    MesMaintenanceWorkOrdersUpdate,
    MesMaintenanceWorkOrdersOut,
    MesMaterialConsumptionCreate,
    MesMaterialConsumptionUpdate,
    MesMaterialConsumptionOut,
    MesMaterialIssuesCreate,
    MesMaterialIssuesUpdate,
    MesMaterialIssuesOut,
    MesMaterialReturnsCreate,
    MesMaterialReturnsUpdate,
    MesMaterialReturnsOut,
    MesMlModelVersionsCreate,
    MesMlModelVersionsUpdate,
    MesMlModelVersionsOut,
    MesMlModelsCreate,
    MesMlModelsUpdate,
    MesMlModelsOut,
    MesNotificationsCreate,
    MesNotificationsUpdate,
    MesNotificationsOut,
    MesOeeCalculationsCreate,
    MesOeeCalculationsUpdate,
    MesOeeCalculationsOut,
    MesOeeLossesCreate,
    MesOeeLossesUpdate,
    MesOeeLossesOut,
    MesOeeTargetsCreate,
    MesOeeTargetsUpdate,
    MesOeeTargetsOut,
    MesOperationExecutionCreate,
    MesOperationExecutionUpdate,
    MesOperationExecutionOut,
    MesOperationStepsCreate,
    MesOperationStepsUpdate,
    MesOperationStepsOut,
    MesOperatorAssignmentsCreate,
    MesOperatorAssignmentsUpdate,
    MesOperatorAssignmentsOut,
    MesOperatorCertificationsCreate,
    MesOperatorCertificationsUpdate,
    MesOperatorCertificationsOut,
    MesOperatorPerformanceCreate,
    MesOperatorPerformanceUpdate,
    MesOperatorPerformanceOut,
    MesOperatorSchedulesCreate,
    MesOperatorSchedulesUpdate,
    MesOperatorSchedulesOut,
    MesOperatorSkillsCreate,
    MesOperatorSkillsUpdate,
    MesOperatorSkillsOut,
    MesOperatorTrainingCreate,
    MesOperatorTrainingUpdate,
    MesOperatorTrainingOut,
    MesOperatorsCreate,
    MesOperatorsUpdate,
    MesOperatorsOut,
    MesOptimizationProblemsCreate,
    MesOptimizationProblemsUpdate,
    MesOptimizationProblemsOut,
    MesOptimizationResultsCreate,
    MesOptimizationResultsUpdate,
    MesOptimizationResultsOut,
    MesOrtoolsProblemsCreate,
    MesOrtoolsProblemsUpdate,
    MesOrtoolsProblemsOut,
    MesPerformanceActualsCreate,
    MesPerformanceActualsUpdate,
    MesPerformanceActualsOut,
    MesPerformanceMetricsCreate,
    MesPerformanceMetricsUpdate,
    MesPerformanceMetricsOut,
    MesPredictionsCreate,
    MesPredictionsUpdate,
    MesPredictionsOut,
    MesProductionCellsCreate,
    MesProductionCellsUpdate,
    MesProductionCellsOut,
    MesProductionLinesCreate,
    MesProductionLinesUpdate,
    MesProductionLinesOut,
    MesPromptTemplatesCreate,
    MesPromptTemplatesUpdate,
    MesPromptTemplatesOut,
    MesQualityHoldsCreate,
    MesQualityHoldsUpdate,
    MesQualityHoldsOut,
    MesQualityInspectionsCreate,
    MesQualityInspectionsUpdate,
    MesQualityInspectionsOut,
    MesQualitySpcDataCreate,
    MesQualitySpcDataUpdate,
    MesQualitySpcDataOut,
    MesResourceAvailabilityCreate,
    MesResourceAvailabilityUpdate,
    MesResourceAvailabilityOut,
    MesResourceCostsCreate,
    MesResourceCostsUpdate,
    MesResourceCostsOut,
    MesResourceTypesCreate,
    MesResourceTypesUpdate,
    MesResourceTypesOut,
    MesResourcesCreate,
    MesResourcesUpdate,
    MesResourcesOut,
    MesScenariosCreate,
    MesScenariosUpdate,
    MesScenariosOut,
    MesScheduleResultsCreate,
    MesScheduleResultsUpdate,
    MesScheduleResultsOut,
    MesSchedulingProblemsCreate,
    MesSchedulingProblemsUpdate,
    MesSchedulingProblemsOut,
    MesScipyAnalysesCreate,
    MesScipyAnalysesUpdate,
    MesScipyAnalysesOut,
    MesSensorCalibrationsCreate,
    MesSensorCalibrationsUpdate,
    MesSensorCalibrationsOut,
    MesSensorsCreate,
    MesSensorsUpdate,
    MesSensorsOut,
    MesShiftHandoversCreate,
    MesShiftHandoversUpdate,
    MesShiftHandoversOut,
    MesShiftSchedulesCreate,
    MesShiftSchedulesUpdate,
    MesShiftSchedulesOut,
    MesShiftsCreate,
    MesShiftsUpdate,
    MesShiftsOut,
    MesSolverConfigsCreate,
    MesSolverConfigsUpdate,
    MesSolverConfigsOut,
    MesStationAssignmentsCreate,
    MesStationAssignmentsUpdate,
    MesStationAssignmentsOut,
    MesStationTypesCreate,
    MesStationTypesUpdate,
    MesStationTypesOut,
    MesStationsCreate,
    MesStationsUpdate,
    MesStationsOut,
    MesToolCribsCreate,
    MesToolCribsUpdate,
    MesToolCribsOut,
    MesToolingAssignmentsCreate,
    MesToolingAssignmentsUpdate,
    MesToolingAssignmentsOut,
    MesToolingLifeTrackingCreate,
    MesToolingLifeTrackingUpdate,
    MesToolingLifeTrackingOut,
    MesToolingMasterCreate,
    MesToolingMasterUpdate,
    MesToolingMasterOut,
    MesToolingTypesCreate,
    MesToolingTypesUpdate,
    MesToolingTypesOut,
    MesVectorStoreConfigsCreate,
    MesVectorStoreConfigsUpdate,
    MesVectorStoreConfigsOut,
    MesVectorStoreDocumentsCreate,
    MesVectorStoreDocumentsUpdate,
    MesVectorStoreDocumentsOut,
    MesWorkCenterCalendarsCreate,
    MesWorkCenterCalendarsUpdate,
    MesWorkCenterCalendarsOut,
    MesWorkCenterCapacitiesCreate,
    MesWorkCenterCapacitiesUpdate,
    MesWorkCenterCapacitiesOut,
    MesWorkCenterConstraintsCreate,
    MesWorkCenterConstraintsUpdate,
    MesWorkCenterConstraintsOut,
    MesWorkCenterTypesCreate,
    MesWorkCenterTypesUpdate,
    MesWorkCenterTypesOut,
    MesWorkCentersCreate,
    MesWorkCentersUpdate,
    MesWorkCentersOut,
    MesWorkOrderExecutionCreate,
    MesWorkOrderExecutionUpdate,
    MesWorkOrderExecutionOut,
    MesWorkOrderHoldsCreate,
    MesWorkOrderHoldsUpdate,
    MesWorkOrderHoldsOut,
    MesWorkOrderSignaturesCreate,
    MesWorkOrderSignaturesUpdate,
    MesWorkOrderSignaturesOut,
    MesWorkflowDefinitionsCreate,
    MesWorkflowDefinitionsUpdate,
    MesWorkflowDefinitionsOut,
    MesWorkflowExecutionsCreate,
    MesWorkflowExecutionsUpdate,
    MesWorkflowExecutionsOut,
    WorkCentersCreate,
    WorkCentersUpdate,
    WorkCentersOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/job_orders", response_model=PaginatedResponse[JobOrdersOut])
async def list_job_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = JobOrdersService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/job_orders/{entity_id}", response_model=JobOrdersOut)
async def get_job_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await JobOrdersService(db).get(entity_id)

@router.post("/job_orders", response_model=JobOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_job_orders(
    data: JobOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await JobOrdersService(db).create(data)

@router.put("/job_orders/{entity_id}", response_model=JobOrdersOut)
async def update_job_orders(
    entity_id: uuid.UUID,
    data: JobOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await JobOrdersService(db).update(entity_id, data)

@router.delete("/job_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await JobOrdersService(db).delete(entity_id)

@router.get("/machine_telemetry", response_model=PaginatedResponse[MachineTelemetryOut])
async def list_machine_telemetry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MachineTelemetryService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["metric_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/machine_telemetry/{entity_id}", response_model=MachineTelemetryOut)
async def get_machine_telemetry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MachineTelemetryService(db).get(entity_id)

@router.post("/machine_telemetry", response_model=MachineTelemetryOut, status_code=status.HTTP_201_CREATED)
async def create_machine_telemetry(
    data: MachineTelemetryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MachineTelemetryService(db).create(data)

@router.put("/machine_telemetry/{entity_id}", response_model=MachineTelemetryOut)
async def update_machine_telemetry(
    entity_id: uuid.UUID,
    data: MachineTelemetryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MachineTelemetryService(db).update(entity_id, data)

@router.delete("/machine_telemetry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_machine_telemetry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MachineTelemetryService(db).delete(entity_id)

@router.get("/mes_ai_agent_logs", response_model=PaginatedResponse[MesAiAgentLogsOut])
async def list_mes_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ai_agent_logs/{entity_id}", response_model=MesAiAgentLogsOut)
async def get_mes_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAiAgentLogsService(db).get(entity_id)

@router.post("/mes_ai_agent_logs", response_model=MesAiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ai_agent_logs(
    data: MesAiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiAgentLogsService(db).create(data)

@router.put("/mes_ai_agent_logs/{entity_id}", response_model=MesAiAgentLogsOut)
async def update_mes_ai_agent_logs(
    entity_id: uuid.UUID,
    data: MesAiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiAgentLogsService(db).update(entity_id, data)

@router.delete("/mes_ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAiAgentLogsService(db).delete(entity_id)

@router.get("/mes_ai_feature_store", response_model=PaginatedResponse[MesAiFeatureStoreOut])
async def list_mes_ai_feature_store(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAiFeatureStoreService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["feature_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ai_feature_store/{entity_id}", response_model=MesAiFeatureStoreOut)
async def get_mes_ai_feature_store(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAiFeatureStoreService(db).get(entity_id)

@router.post("/mes_ai_feature_store", response_model=MesAiFeatureStoreOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ai_feature_store(
    data: MesAiFeatureStoreCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiFeatureStoreService(db).create(data)

@router.put("/mes_ai_feature_store/{entity_id}", response_model=MesAiFeatureStoreOut)
async def update_mes_ai_feature_store(
    entity_id: uuid.UUID,
    data: MesAiFeatureStoreUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiFeatureStoreService(db).update(entity_id, data)

@router.delete("/mes_ai_feature_store/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ai_feature_store(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAiFeatureStoreService(db).delete(entity_id)

@router.get("/mes_ai_model_registry", response_model=PaginatedResponse[MesAiModelRegistryOut])
async def list_mes_ai_model_registry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAiModelRegistryService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ai_model_registry/{entity_id}", response_model=MesAiModelRegistryOut)
async def get_mes_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAiModelRegistryService(db).get(entity_id)

@router.post("/mes_ai_model_registry", response_model=MesAiModelRegistryOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ai_model_registry(
    data: MesAiModelRegistryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiModelRegistryService(db).create(data)

@router.put("/mes_ai_model_registry/{entity_id}", response_model=MesAiModelRegistryOut)
async def update_mes_ai_model_registry(
    entity_id: uuid.UUID,
    data: MesAiModelRegistryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiModelRegistryService(db).update(entity_id, data)

@router.delete("/mes_ai_model_registry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAiModelRegistryService(db).delete(entity_id)

@router.get("/mes_ai_workflow_states", response_model=PaginatedResponse[MesAiWorkflowStatesOut])
async def list_mes_ai_workflow_states(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAiWorkflowStatesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ai_workflow_states/{entity_id}", response_model=MesAiWorkflowStatesOut)
async def get_mes_ai_workflow_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAiWorkflowStatesService(db).get(entity_id)

@router.post("/mes_ai_workflow_states", response_model=MesAiWorkflowStatesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ai_workflow_states(
    data: MesAiWorkflowStatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiWorkflowStatesService(db).create(data)

@router.put("/mes_ai_workflow_states/{entity_id}", response_model=MesAiWorkflowStatesOut)
async def update_mes_ai_workflow_states(
    entity_id: uuid.UUID,
    data: MesAiWorkflowStatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAiWorkflowStatesService(db).update(entity_id, data)

@router.delete("/mes_ai_workflow_states/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ai_workflow_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAiWorkflowStatesService(db).delete(entity_id)

@router.get("/mes_alerts", response_model=PaginatedResponse[MesAlertsOut])
async def list_mes_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAlertsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_alerts/{entity_id}", response_model=MesAlertsOut)
async def get_mes_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAlertsService(db).get(entity_id)

@router.post("/mes_alerts", response_model=MesAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_alerts(
    data: MesAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAlertsService(db).create(data)

@router.put("/mes_alerts/{entity_id}", response_model=MesAlertsOut)
async def update_mes_alerts(
    entity_id: uuid.UUID,
    data: MesAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAlertsService(db).update(entity_id, data)

@router.delete("/mes_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAlertsService(db).delete(entity_id)

@router.get("/mes_algorithms", response_model=PaginatedResponse[MesAlgorithmsOut])
async def list_mes_algorithms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAlgorithmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["algorithm_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_algorithms/{entity_id}", response_model=MesAlgorithmsOut)
async def get_mes_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAlgorithmsService(db).get(entity_id)

@router.post("/mes_algorithms", response_model=MesAlgorithmsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_algorithms(
    data: MesAlgorithmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAlgorithmsService(db).create(data)

@router.put("/mes_algorithms/{entity_id}", response_model=MesAlgorithmsOut)
async def update_mes_algorithms(
    entity_id: uuid.UUID,
    data: MesAlgorithmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAlgorithmsService(db).update(entity_id, data)

@router.delete("/mes_algorithms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAlgorithmsService(db).delete(entity_id)

@router.get("/mes_andon_boards", response_model=PaginatedResponse[MesAndonBoardsOut])
async def list_mes_andon_boards(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAndonBoardsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["board_code", "board_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_andon_boards/{entity_id}", response_model=MesAndonBoardsOut)
async def get_mes_andon_boards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAndonBoardsService(db).get(entity_id)

@router.post("/mes_andon_boards", response_model=MesAndonBoardsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_andon_boards(
    data: MesAndonBoardsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAndonBoardsService(db).create(data)

@router.put("/mes_andon_boards/{entity_id}", response_model=MesAndonBoardsOut)
async def update_mes_andon_boards(
    entity_id: uuid.UUID,
    data: MesAndonBoardsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAndonBoardsService(db).update(entity_id, data)

@router.delete("/mes_andon_boards/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_andon_boards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAndonBoardsService(db).delete(entity_id)

@router.get("/mes_andon_triggers", response_model=PaginatedResponse[MesAndonTriggersOut])
async def list_mes_andon_triggers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesAndonTriggersService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_andon_triggers/{entity_id}", response_model=MesAndonTriggersOut)
async def get_mes_andon_triggers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesAndonTriggersService(db).get(entity_id)

@router.post("/mes_andon_triggers", response_model=MesAndonTriggersOut, status_code=status.HTTP_201_CREATED)
async def create_mes_andon_triggers(
    data: MesAndonTriggersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAndonTriggersService(db).create(data)

@router.put("/mes_andon_triggers/{entity_id}", response_model=MesAndonTriggersOut)
async def update_mes_andon_triggers(
    entity_id: uuid.UUID,
    data: MesAndonTriggersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesAndonTriggersService(db).update(entity_id, data)

@router.delete("/mes_andon_triggers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_andon_triggers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesAndonTriggersService(db).delete(entity_id)

@router.get("/mes_batch_record_materials", response_model=PaginatedResponse[MesBatchRecordMaterialsOut])
async def list_mes_batch_record_materials(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesBatchRecordMaterialsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "item_name", "lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_batch_record_materials/{entity_id}", response_model=MesBatchRecordMaterialsOut)
async def get_mes_batch_record_materials(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesBatchRecordMaterialsService(db).get(entity_id)

@router.post("/mes_batch_record_materials", response_model=MesBatchRecordMaterialsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_batch_record_materials(
    data: MesBatchRecordMaterialsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordMaterialsService(db).create(data)

@router.put("/mes_batch_record_materials/{entity_id}", response_model=MesBatchRecordMaterialsOut)
async def update_mes_batch_record_materials(
    entity_id: uuid.UUID,
    data: MesBatchRecordMaterialsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordMaterialsService(db).update(entity_id, data)

@router.delete("/mes_batch_record_materials/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_batch_record_materials(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesBatchRecordMaterialsService(db).delete(entity_id)

@router.get("/mes_batch_record_steps", response_model=PaginatedResponse[MesBatchRecordStepsOut])
async def list_mes_batch_record_steps(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesBatchRecordStepsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_batch_record_steps/{entity_id}", response_model=MesBatchRecordStepsOut)
async def get_mes_batch_record_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesBatchRecordStepsService(db).get(entity_id)

@router.post("/mes_batch_record_steps", response_model=MesBatchRecordStepsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_batch_record_steps(
    data: MesBatchRecordStepsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordStepsService(db).create(data)

@router.put("/mes_batch_record_steps/{entity_id}", response_model=MesBatchRecordStepsOut)
async def update_mes_batch_record_steps(
    entity_id: uuid.UUID,
    data: MesBatchRecordStepsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordStepsService(db).update(entity_id, data)

@router.delete("/mes_batch_record_steps/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_batch_record_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesBatchRecordStepsService(db).delete(entity_id)

@router.get("/mes_batch_records", response_model=PaginatedResponse[MesBatchRecordsOut])
async def list_mes_batch_records(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesBatchRecordsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["batch_number", "product_code", "product_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_batch_records/{entity_id}", response_model=MesBatchRecordsOut)
async def get_mes_batch_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesBatchRecordsService(db).get(entity_id)

@router.post("/mes_batch_records", response_model=MesBatchRecordsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_batch_records(
    data: MesBatchRecordsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordsService(db).create(data)

@router.put("/mes_batch_records/{entity_id}", response_model=MesBatchRecordsOut)
async def update_mes_batch_records(
    entity_id: uuid.UUID,
    data: MesBatchRecordsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesBatchRecordsService(db).update(entity_id, data)

@router.delete("/mes_batch_records/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_batch_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesBatchRecordsService(db).delete(entity_id)

@router.get("/mes_crew_assignments", response_model=PaginatedResponse[MesCrewAssignmentsOut])
async def list_mes_crew_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesCrewAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_crew_assignments/{entity_id}", response_model=MesCrewAssignmentsOut)
async def get_mes_crew_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesCrewAssignmentsService(db).get(entity_id)

@router.post("/mes_crew_assignments", response_model=MesCrewAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_crew_assignments(
    data: MesCrewAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCrewAssignmentsService(db).create(data)

@router.put("/mes_crew_assignments/{entity_id}", response_model=MesCrewAssignmentsOut)
async def update_mes_crew_assignments(
    entity_id: uuid.UUID,
    data: MesCrewAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCrewAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_crew_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_crew_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesCrewAssignmentsService(db).delete(entity_id)

@router.get("/mes_crews", response_model=PaginatedResponse[MesCrewsOut])
async def list_mes_crews(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesCrewsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["crew_code", "crew_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_crews/{entity_id}", response_model=MesCrewsOut)
async def get_mes_crews(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesCrewsService(db).get(entity_id)

@router.post("/mes_crews", response_model=MesCrewsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_crews(
    data: MesCrewsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCrewsService(db).create(data)

@router.put("/mes_crews/{entity_id}", response_model=MesCrewsOut)
async def update_mes_crews(
    entity_id: uuid.UUID,
    data: MesCrewsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCrewsService(db).update(entity_id, data)

@router.delete("/mes_crews/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_crews(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesCrewsService(db).delete(entity_id)

@router.get("/mes_crib_compartments", response_model=PaginatedResponse[MesCribCompartmentsOut])
async def list_mes_crib_compartments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesCribCompartmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["compartment_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_crib_compartments/{entity_id}", response_model=MesCribCompartmentsOut)
async def get_mes_crib_compartments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesCribCompartmentsService(db).get(entity_id)

@router.post("/mes_crib_compartments", response_model=MesCribCompartmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_crib_compartments(
    data: MesCribCompartmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCribCompartmentsService(db).create(data)

@router.put("/mes_crib_compartments/{entity_id}", response_model=MesCribCompartmentsOut)
async def update_mes_crib_compartments(
    entity_id: uuid.UUID,
    data: MesCribCompartmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCribCompartmentsService(db).update(entity_id, data)

@router.delete("/mes_crib_compartments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_crib_compartments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesCribCompartmentsService(db).delete(entity_id)

@router.get("/mes_crib_packing_results", response_model=PaginatedResponse[MesCribPackingResultsOut])
async def list_mes_crib_packing_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesCribPackingResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_crib_packing_results/{entity_id}", response_model=MesCribPackingResultsOut)
async def get_mes_crib_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesCribPackingResultsService(db).get(entity_id)

@router.post("/mes_crib_packing_results", response_model=MesCribPackingResultsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_crib_packing_results(
    data: MesCribPackingResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCribPackingResultsService(db).create(data)

@router.put("/mes_crib_packing_results/{entity_id}", response_model=MesCribPackingResultsOut)
async def update_mes_crib_packing_results(
    entity_id: uuid.UUID,
    data: MesCribPackingResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesCribPackingResultsService(db).update(entity_id, data)

@router.delete("/mes_crib_packing_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_crib_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesCribPackingResultsService(db).delete(entity_id)

@router.get("/mes_delivery_requests", response_model=PaginatedResponse[MesDeliveryRequestsOut])
async def list_mes_delivery_requests(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDeliveryRequestsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["request_number", "item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_delivery_requests/{entity_id}", response_model=MesDeliveryRequestsOut)
async def get_mes_delivery_requests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDeliveryRequestsService(db).get(entity_id)

@router.post("/mes_delivery_requests", response_model=MesDeliveryRequestsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_delivery_requests(
    data: MesDeliveryRequestsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDeliveryRequestsService(db).create(data)

@router.put("/mes_delivery_requests/{entity_id}", response_model=MesDeliveryRequestsOut)
async def update_mes_delivery_requests(
    entity_id: uuid.UUID,
    data: MesDeliveryRequestsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDeliveryRequestsService(db).update(entity_id, data)

@router.delete("/mes_delivery_requests/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_delivery_requests(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDeliveryRequestsService(db).delete(entity_id)

@router.get("/mes_delivery_routes", response_model=PaginatedResponse[MesDeliveryRoutesOut])
async def list_mes_delivery_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDeliveryRoutesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["route_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_delivery_routes/{entity_id}", response_model=MesDeliveryRoutesOut)
async def get_mes_delivery_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDeliveryRoutesService(db).get(entity_id)

@router.post("/mes_delivery_routes", response_model=MesDeliveryRoutesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_delivery_routes(
    data: MesDeliveryRoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDeliveryRoutesService(db).create(data)

@router.put("/mes_delivery_routes/{entity_id}", response_model=MesDeliveryRoutesOut)
async def update_mes_delivery_routes(
    entity_id: uuid.UUID,
    data: MesDeliveryRoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDeliveryRoutesService(db).update(entity_id, data)

@router.delete("/mes_delivery_routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_delivery_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDeliveryRoutesService(db).delete(entity_id)

@router.get("/mes_digital_twin_models", response_model=PaginatedResponse[MesDigitalTwinModelsOut])
async def list_mes_digital_twin_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDigitalTwinModelsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["twin_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_digital_twin_models/{entity_id}", response_model=MesDigitalTwinModelsOut)
async def get_mes_digital_twin_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDigitalTwinModelsService(db).get(entity_id)

@router.post("/mes_digital_twin_models", response_model=MesDigitalTwinModelsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_digital_twin_models(
    data: MesDigitalTwinModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDigitalTwinModelsService(db).create(data)

@router.put("/mes_digital_twin_models/{entity_id}", response_model=MesDigitalTwinModelsOut)
async def update_mes_digital_twin_models(
    entity_id: uuid.UUID,
    data: MesDigitalTwinModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDigitalTwinModelsService(db).update(entity_id, data)

@router.delete("/mes_digital_twin_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_digital_twin_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDigitalTwinModelsService(db).delete(entity_id)

@router.get("/mes_document_instances", response_model=PaginatedResponse[MesDocumentInstancesOut])
async def list_mes_document_instances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDocumentInstancesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_document_instances/{entity_id}", response_model=MesDocumentInstancesOut)
async def get_mes_document_instances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDocumentInstancesService(db).get(entity_id)

@router.post("/mes_document_instances", response_model=MesDocumentInstancesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_document_instances(
    data: MesDocumentInstancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDocumentInstancesService(db).create(data)

@router.put("/mes_document_instances/{entity_id}", response_model=MesDocumentInstancesOut)
async def update_mes_document_instances(
    entity_id: uuid.UUID,
    data: MesDocumentInstancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDocumentInstancesService(db).update(entity_id, data)

@router.delete("/mes_document_instances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_document_instances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDocumentInstancesService(db).delete(entity_id)

@router.get("/mes_documents", response_model=PaginatedResponse[MesDocumentsOut])
async def list_mes_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["document_code", "document_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_documents/{entity_id}", response_model=MesDocumentsOut)
async def get_mes_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDocumentsService(db).get(entity_id)

@router.post("/mes_documents", response_model=MesDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_documents(
    data: MesDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDocumentsService(db).create(data)

@router.put("/mes_documents/{entity_id}", response_model=MesDocumentsOut)
async def update_mes_documents(
    entity_id: uuid.UUID,
    data: MesDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDocumentsService(db).update(entity_id, data)

@router.delete("/mes_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDocumentsService(db).delete(entity_id)

@router.get("/mes_downtime_events", response_model=PaginatedResponse[MesDowntimeEventsOut])
async def list_mes_downtime_events(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDowntimeEventsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_downtime_events/{entity_id}", response_model=MesDowntimeEventsOut)
async def get_mes_downtime_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDowntimeEventsService(db).get(entity_id)

@router.post("/mes_downtime_events", response_model=MesDowntimeEventsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_downtime_events(
    data: MesDowntimeEventsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDowntimeEventsService(db).create(data)

@router.put("/mes_downtime_events/{entity_id}", response_model=MesDowntimeEventsOut)
async def update_mes_downtime_events(
    entity_id: uuid.UUID,
    data: MesDowntimeEventsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDowntimeEventsService(db).update(entity_id, data)

@router.delete("/mes_downtime_events/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_downtime_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDowntimeEventsService(db).delete(entity_id)

@router.get("/mes_downtime_reasons", response_model=PaginatedResponse[MesDowntimeReasonsOut])
async def list_mes_downtime_reasons(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesDowntimeReasonsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["reason_code", "reason_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_downtime_reasons/{entity_id}", response_model=MesDowntimeReasonsOut)
async def get_mes_downtime_reasons(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesDowntimeReasonsService(db).get(entity_id)

@router.post("/mes_downtime_reasons", response_model=MesDowntimeReasonsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_downtime_reasons(
    data: MesDowntimeReasonsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDowntimeReasonsService(db).create(data)

@router.put("/mes_downtime_reasons/{entity_id}", response_model=MesDowntimeReasonsOut)
async def update_mes_downtime_reasons(
    entity_id: uuid.UUID,
    data: MesDowntimeReasonsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesDowntimeReasonsService(db).update(entity_id, data)

@router.delete("/mes_downtime_reasons/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_downtime_reasons(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesDowntimeReasonsService(db).delete(entity_id)

@router.get("/mes_energy_meters", response_model=PaginatedResponse[MesEnergyMetersOut])
async def list_mes_energy_meters(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEnergyMetersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["meter_code", "meter_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_energy_meters/{entity_id}", response_model=MesEnergyMetersOut)
async def get_mes_energy_meters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEnergyMetersService(db).get(entity_id)

@router.post("/mes_energy_meters", response_model=MesEnergyMetersOut, status_code=status.HTTP_201_CREATED)
async def create_mes_energy_meters(
    data: MesEnergyMetersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEnergyMetersService(db).create(data)

@router.put("/mes_energy_meters/{entity_id}", response_model=MesEnergyMetersOut)
async def update_mes_energy_meters(
    entity_id: uuid.UUID,
    data: MesEnergyMetersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEnergyMetersService(db).update(entity_id, data)

@router.delete("/mes_energy_meters/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_energy_meters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEnergyMetersService(db).delete(entity_id)

@router.get("/mes_energy_readings", response_model=PaginatedResponse[MesEnergyReadingsOut])
async def list_mes_energy_readings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEnergyReadingsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_energy_readings/{entity_id}", response_model=MesEnergyReadingsOut)
async def get_mes_energy_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEnergyReadingsService(db).get(entity_id)

@router.post("/mes_energy_readings", response_model=MesEnergyReadingsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_energy_readings(
    data: MesEnergyReadingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEnergyReadingsService(db).create(data)

@router.put("/mes_energy_readings/{entity_id}", response_model=MesEnergyReadingsOut)
async def update_mes_energy_readings(
    entity_id: uuid.UUID,
    data: MesEnergyReadingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEnergyReadingsService(db).update(entity_id, data)

@router.delete("/mes_energy_readings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_energy_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEnergyReadingsService(db).delete(entity_id)

@router.get("/mes_equipment", response_model=PaginatedResponse[MesEquipmentOut])
async def list_mes_equipment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["equipment_code", "equipment_name", "serial_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment/{entity_id}", response_model=MesEquipmentOut)
async def get_mes_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentService(db).get(entity_id)

@router.post("/mes_equipment", response_model=MesEquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment(
    data: MesEquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentService(db).create(data)

@router.put("/mes_equipment/{entity_id}", response_model=MesEquipmentOut)
async def update_mes_equipment(
    entity_id: uuid.UUID,
    data: MesEquipmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentService(db).update(entity_id, data)

@router.delete("/mes_equipment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentService(db).delete(entity_id)

@router.get("/mes_equipment_assignments", response_model=PaginatedResponse[MesEquipmentAssignmentsOut])
async def list_mes_equipment_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_assignments/{entity_id}", response_model=MesEquipmentAssignmentsOut)
async def get_mes_equipment_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentAssignmentsService(db).get(entity_id)

@router.post("/mes_equipment_assignments", response_model=MesEquipmentAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_assignments(
    data: MesEquipmentAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentAssignmentsService(db).create(data)

@router.put("/mes_equipment_assignments/{entity_id}", response_model=MesEquipmentAssignmentsOut)
async def update_mes_equipment_assignments(
    entity_id: uuid.UUID,
    data: MesEquipmentAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_equipment_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentAssignmentsService(db).delete(entity_id)

@router.get("/mes_equipment_capabilities", response_model=PaginatedResponse[MesEquipmentCapabilitiesOut])
async def list_mes_equipment_capabilities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentCapabilitiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_capabilities/{entity_id}", response_model=MesEquipmentCapabilitiesOut)
async def get_mes_equipment_capabilities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentCapabilitiesService(db).get(entity_id)

@router.post("/mes_equipment_capabilities", response_model=MesEquipmentCapabilitiesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_capabilities(
    data: MesEquipmentCapabilitiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentCapabilitiesService(db).create(data)

@router.put("/mes_equipment_capabilities/{entity_id}", response_model=MesEquipmentCapabilitiesOut)
async def update_mes_equipment_capabilities(
    entity_id: uuid.UUID,
    data: MesEquipmentCapabilitiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentCapabilitiesService(db).update(entity_id, data)

@router.delete("/mes_equipment_capabilities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_capabilities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentCapabilitiesService(db).delete(entity_id)

@router.get("/mes_equipment_certifications", response_model=PaginatedResponse[MesEquipmentCertificationsOut])
async def list_mes_equipment_certifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentCertificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cert_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_certifications/{entity_id}", response_model=MesEquipmentCertificationsOut)
async def get_mes_equipment_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentCertificationsService(db).get(entity_id)

@router.post("/mes_equipment_certifications", response_model=MesEquipmentCertificationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_certifications(
    data: MesEquipmentCertificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentCertificationsService(db).create(data)

@router.put("/mes_equipment_certifications/{entity_id}", response_model=MesEquipmentCertificationsOut)
async def update_mes_equipment_certifications(
    entity_id: uuid.UUID,
    data: MesEquipmentCertificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentCertificationsService(db).update(entity_id, data)

@router.delete("/mes_equipment_certifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentCertificationsService(db).delete(entity_id)

@router.get("/mes_equipment_classes", response_model=PaginatedResponse[MesEquipmentClassesOut])
async def list_mes_equipment_classes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentClassesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["class_code", "class_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_classes/{entity_id}", response_model=MesEquipmentClassesOut)
async def get_mes_equipment_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentClassesService(db).get(entity_id)

@router.post("/mes_equipment_classes", response_model=MesEquipmentClassesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_classes(
    data: MesEquipmentClassesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentClassesService(db).create(data)

@router.put("/mes_equipment_classes/{entity_id}", response_model=MesEquipmentClassesOut)
async def update_mes_equipment_classes(
    entity_id: uuid.UUID,
    data: MesEquipmentClassesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentClassesService(db).update(entity_id, data)

@router.delete("/mes_equipment_classes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentClassesService(db).delete(entity_id)

@router.get("/mes_equipment_connections", response_model=PaginatedResponse[MesEquipmentConnectionsOut])
async def list_mes_equipment_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentConnectionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_connections/{entity_id}", response_model=MesEquipmentConnectionsOut)
async def get_mes_equipment_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentConnectionsService(db).get(entity_id)

@router.post("/mes_equipment_connections", response_model=MesEquipmentConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_connections(
    data: MesEquipmentConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentConnectionsService(db).create(data)

@router.put("/mes_equipment_connections/{entity_id}", response_model=MesEquipmentConnectionsOut)
async def update_mes_equipment_connections(
    entity_id: uuid.UUID,
    data: MesEquipmentConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentConnectionsService(db).update(entity_id, data)

@router.delete("/mes_equipment_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentConnectionsService(db).delete(entity_id)

@router.get("/mes_equipment_data_points", response_model=PaginatedResponse[MesEquipmentDataPointsOut])
async def list_mes_equipment_data_points(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentDataPointsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["point_code", "point_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_data_points/{entity_id}", response_model=MesEquipmentDataPointsOut)
async def get_mes_equipment_data_points(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentDataPointsService(db).get(entity_id)

@router.post("/mes_equipment_data_points", response_model=MesEquipmentDataPointsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_data_points(
    data: MesEquipmentDataPointsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentDataPointsService(db).create(data)

@router.put("/mes_equipment_data_points/{entity_id}", response_model=MesEquipmentDataPointsOut)
async def update_mes_equipment_data_points(
    entity_id: uuid.UUID,
    data: MesEquipmentDataPointsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentDataPointsService(db).update(entity_id, data)

@router.delete("/mes_equipment_data_points/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_data_points(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentDataPointsService(db).delete(entity_id)

@router.get("/mes_equipment_locations", response_model=PaginatedResponse[MesEquipmentLocationsOut])
async def list_mes_equipment_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_locations/{entity_id}", response_model=MesEquipmentLocationsOut)
async def get_mes_equipment_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentLocationsService(db).get(entity_id)

@router.post("/mes_equipment_locations", response_model=MesEquipmentLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_locations(
    data: MesEquipmentLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentLocationsService(db).create(data)

@router.put("/mes_equipment_locations/{entity_id}", response_model=MesEquipmentLocationsOut)
async def update_mes_equipment_locations(
    entity_id: uuid.UUID,
    data: MesEquipmentLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentLocationsService(db).update(entity_id, data)

@router.delete("/mes_equipment_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentLocationsService(db).delete(entity_id)

@router.get("/mes_equipment_statuses", response_model=PaginatedResponse[MesEquipmentStatusesOut])
async def list_mes_equipment_statuses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentStatusesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["status_code", "status_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_statuses/{entity_id}", response_model=MesEquipmentStatusesOut)
async def get_mes_equipment_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentStatusesService(db).get(entity_id)

@router.post("/mes_equipment_statuses", response_model=MesEquipmentStatusesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_statuses(
    data: MesEquipmentStatusesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentStatusesService(db).create(data)

@router.put("/mes_equipment_statuses/{entity_id}", response_model=MesEquipmentStatusesOut)
async def update_mes_equipment_statuses(
    entity_id: uuid.UUID,
    data: MesEquipmentStatusesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentStatusesService(db).update(entity_id, data)

@router.delete("/mes_equipment_statuses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentStatusesService(db).delete(entity_id)

@router.get("/mes_equipment_types", response_model=PaginatedResponse[MesEquipmentTypesOut])
async def list_mes_equipment_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesEquipmentTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_equipment_types/{entity_id}", response_model=MesEquipmentTypesOut)
async def get_mes_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesEquipmentTypesService(db).get(entity_id)

@router.post("/mes_equipment_types", response_model=MesEquipmentTypesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_equipment_types(
    data: MesEquipmentTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentTypesService(db).create(data)

@router.put("/mes_equipment_types/{entity_id}", response_model=MesEquipmentTypesOut)
async def update_mes_equipment_types(
    entity_id: uuid.UUID,
    data: MesEquipmentTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesEquipmentTypesService(db).update(entity_id, data)

@router.delete("/mes_equipment_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesEquipmentTypesService(db).delete(entity_id)

@router.get("/mes_genealogy", response_model=PaginatedResponse[MesGenealogyOut])
async def list_mes_genealogy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesGenealogyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_genealogy/{entity_id}", response_model=MesGenealogyOut)
async def get_mes_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesGenealogyService(db).get(entity_id)

@router.post("/mes_genealogy", response_model=MesGenealogyOut, status_code=status.HTTP_201_CREATED)
async def create_mes_genealogy(
    data: MesGenealogyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesGenealogyService(db).create(data)

@router.put("/mes_genealogy/{entity_id}", response_model=MesGenealogyOut)
async def update_mes_genealogy(
    entity_id: uuid.UUID,
    data: MesGenealogyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesGenealogyService(db).update(entity_id, data)

@router.delete("/mes_genealogy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesGenealogyService(db).delete(entity_id)

@router.get("/mes_genealogy_snapshots", response_model=PaginatedResponse[MesGenealogySnapshotsOut])
async def list_mes_genealogy_snapshots(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesGenealogySnapshotsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_genealogy_snapshots/{entity_id}", response_model=MesGenealogySnapshotsOut)
async def get_mes_genealogy_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesGenealogySnapshotsService(db).get(entity_id)

@router.post("/mes_genealogy_snapshots", response_model=MesGenealogySnapshotsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_genealogy_snapshots(
    data: MesGenealogySnapshotsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesGenealogySnapshotsService(db).create(data)

@router.put("/mes_genealogy_snapshots/{entity_id}", response_model=MesGenealogySnapshotsOut)
async def update_mes_genealogy_snapshots(
    entity_id: uuid.UUID,
    data: MesGenealogySnapshotsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesGenealogySnapshotsService(db).update(entity_id, data)

@router.delete("/mes_genealogy_snapshots/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_genealogy_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesGenealogySnapshotsService(db).delete(entity_id)

@router.get("/mes_instruction_acknowledgments", response_model=PaginatedResponse[MesInstructionAcknowledgmentsOut])
async def list_mes_instruction_acknowledgments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesInstructionAcknowledgmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_instruction_acknowledgments/{entity_id}", response_model=MesInstructionAcknowledgmentsOut)
async def get_mes_instruction_acknowledgments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesInstructionAcknowledgmentsService(db).get(entity_id)

@router.post("/mes_instruction_acknowledgments", response_model=MesInstructionAcknowledgmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_instruction_acknowledgments(
    data: MesInstructionAcknowledgmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionAcknowledgmentsService(db).create(data)

@router.put("/mes_instruction_acknowledgments/{entity_id}", response_model=MesInstructionAcknowledgmentsOut)
async def update_mes_instruction_acknowledgments(
    entity_id: uuid.UUID,
    data: MesInstructionAcknowledgmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionAcknowledgmentsService(db).update(entity_id, data)

@router.delete("/mes_instruction_acknowledgments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_instruction_acknowledgments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesInstructionAcknowledgmentsService(db).delete(entity_id)

@router.get("/mes_instruction_versions", response_model=PaginatedResponse[MesInstructionVersionsOut])
async def list_mes_instruction_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesInstructionVersionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_instruction_versions/{entity_id}", response_model=MesInstructionVersionsOut)
async def get_mes_instruction_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesInstructionVersionsService(db).get(entity_id)

@router.post("/mes_instruction_versions", response_model=MesInstructionVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_instruction_versions(
    data: MesInstructionVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionVersionsService(db).create(data)

@router.put("/mes_instruction_versions/{entity_id}", response_model=MesInstructionVersionsOut)
async def update_mes_instruction_versions(
    entity_id: uuid.UUID,
    data: MesInstructionVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionVersionsService(db).update(entity_id, data)

@router.delete("/mes_instruction_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_instruction_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesInstructionVersionsService(db).delete(entity_id)

@router.get("/mes_instructions", response_model=PaginatedResponse[MesInstructionsOut])
async def list_mes_instructions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesInstructionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["instruction_code", "instruction_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_instructions/{entity_id}", response_model=MesInstructionsOut)
async def get_mes_instructions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesInstructionsService(db).get(entity_id)

@router.post("/mes_instructions", response_model=MesInstructionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_instructions(
    data: MesInstructionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionsService(db).create(data)

@router.put("/mes_instructions/{entity_id}", response_model=MesInstructionsOut)
async def update_mes_instructions(
    entity_id: uuid.UUID,
    data: MesInstructionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesInstructionsService(db).update(entity_id, data)

@router.delete("/mes_instructions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_instructions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesInstructionsService(db).delete(entity_id)

@router.get("/mes_integration_connections", response_model=PaginatedResponse[MesIntegrationConnectionsOut])
async def list_mes_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesIntegrationConnectionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["connection_code", "connection_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_integration_connections/{entity_id}", response_model=MesIntegrationConnectionsOut)
async def get_mes_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesIntegrationConnectionsService(db).get(entity_id)

@router.post("/mes_integration_connections", response_model=MesIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_integration_connections(
    data: MesIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesIntegrationConnectionsService(db).create(data)

@router.put("/mes_integration_connections/{entity_id}", response_model=MesIntegrationConnectionsOut)
async def update_mes_integration_connections(
    entity_id: uuid.UUID,
    data: MesIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/mes_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesIntegrationConnectionsService(db).delete(entity_id)

@router.get("/mes_integration_logs", response_model=PaginatedResponse[MesIntegrationLogsOut])
async def list_mes_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesIntegrationLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_integration_logs/{entity_id}", response_model=MesIntegrationLogsOut)
async def get_mes_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesIntegrationLogsService(db).get(entity_id)

@router.post("/mes_integration_logs", response_model=MesIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_integration_logs(
    data: MesIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesIntegrationLogsService(db).create(data)

@router.put("/mes_integration_logs/{entity_id}", response_model=MesIntegrationLogsOut)
async def update_mes_integration_logs(
    entity_id: uuid.UUID,
    data: MesIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesIntegrationLogsService(db).update(entity_id, data)

@router.delete("/mes_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesIntegrationLogsService(db).delete(entity_id)

@router.get("/mes_kpi_actuals", response_model=PaginatedResponse[MesKpiActualsOut])
async def list_mes_kpi_actuals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesKpiActualsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_kpi_actuals/{entity_id}", response_model=MesKpiActualsOut)
async def get_mes_kpi_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesKpiActualsService(db).get(entity_id)

@router.post("/mes_kpi_actuals", response_model=MesKpiActualsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_kpi_actuals(
    data: MesKpiActualsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesKpiActualsService(db).create(data)

@router.put("/mes_kpi_actuals/{entity_id}", response_model=MesKpiActualsOut)
async def update_mes_kpi_actuals(
    entity_id: uuid.UUID,
    data: MesKpiActualsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesKpiActualsService(db).update(entity_id, data)

@router.delete("/mes_kpi_actuals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_kpi_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesKpiActualsService(db).delete(entity_id)

@router.get("/mes_kpi_definitions", response_model=PaginatedResponse[MesKpiDefinitionsOut])
async def list_mes_kpi_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesKpiDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "kpi_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_kpi_definitions/{entity_id}", response_model=MesKpiDefinitionsOut)
async def get_mes_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesKpiDefinitionsService(db).get(entity_id)

@router.post("/mes_kpi_definitions", response_model=MesKpiDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_kpi_definitions(
    data: MesKpiDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesKpiDefinitionsService(db).create(data)

@router.put("/mes_kpi_definitions/{entity_id}", response_model=MesKpiDefinitionsOut)
async def update_mes_kpi_definitions(
    entity_id: uuid.UUID,
    data: MesKpiDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesKpiDefinitionsService(db).update(entity_id, data)

@router.delete("/mes_kpi_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesKpiDefinitionsService(db).delete(entity_id)

@router.get("/mes_labor_assignments", response_model=PaginatedResponse[MesLaborAssignmentsOut])
async def list_mes_labor_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesLaborAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_labor_assignments/{entity_id}", response_model=MesLaborAssignmentsOut)
async def get_mes_labor_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesLaborAssignmentsService(db).get(entity_id)

@router.post("/mes_labor_assignments", response_model=MesLaborAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_labor_assignments(
    data: MesLaborAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLaborAssignmentsService(db).create(data)

@router.put("/mes_labor_assignments/{entity_id}", response_model=MesLaborAssignmentsOut)
async def update_mes_labor_assignments(
    entity_id: uuid.UUID,
    data: MesLaborAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLaborAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_labor_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_labor_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesLaborAssignmentsService(db).delete(entity_id)

@router.get("/mes_labor_time_collection", response_model=PaginatedResponse[MesLaborTimeCollectionOut])
async def list_mes_labor_time_collection(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesLaborTimeCollectionService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_labor_time_collection/{entity_id}", response_model=MesLaborTimeCollectionOut)
async def get_mes_labor_time_collection(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesLaborTimeCollectionService(db).get(entity_id)

@router.post("/mes_labor_time_collection", response_model=MesLaborTimeCollectionOut, status_code=status.HTTP_201_CREATED)
async def create_mes_labor_time_collection(
    data: MesLaborTimeCollectionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLaborTimeCollectionService(db).create(data)

@router.put("/mes_labor_time_collection/{entity_id}", response_model=MesLaborTimeCollectionOut)
async def update_mes_labor_time_collection(
    entity_id: uuid.UUID,
    data: MesLaborTimeCollectionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLaborTimeCollectionService(db).update(entity_id, data)

@router.delete("/mes_labor_time_collection/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_labor_time_collection(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesLaborTimeCollectionService(db).delete(entity_id)

@router.get("/mes_line_balancing", response_model=PaginatedResponse[MesLineBalancingOut])
async def list_mes_line_balancing(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesLineBalancingService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_line_balancing/{entity_id}", response_model=MesLineBalancingOut)
async def get_mes_line_balancing(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesLineBalancingService(db).get(entity_id)

@router.post("/mes_line_balancing", response_model=MesLineBalancingOut, status_code=status.HTTP_201_CREATED)
async def create_mes_line_balancing(
    data: MesLineBalancingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLineBalancingService(db).create(data)

@router.put("/mes_line_balancing/{entity_id}", response_model=MesLineBalancingOut)
async def update_mes_line_balancing(
    entity_id: uuid.UUID,
    data: MesLineBalancingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLineBalancingService(db).update(entity_id, data)

@router.delete("/mes_line_balancing/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_line_balancing(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesLineBalancingService(db).delete(entity_id)

@router.get("/mes_llm_configs", response_model=PaginatedResponse[MesLlmConfigsOut])
async def list_mes_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_name", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_llm_configs/{entity_id}", response_model=MesLlmConfigsOut)
async def get_mes_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesLlmConfigsService(db).get(entity_id)

@router.post("/mes_llm_configs", response_model=MesLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_llm_configs(
    data: MesLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLlmConfigsService(db).create(data)

@router.put("/mes_llm_configs/{entity_id}", response_model=MesLlmConfigsOut)
async def update_mes_llm_configs(
    entity_id: uuid.UUID,
    data: MesLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesLlmConfigsService(db).update(entity_id, data)

@router.delete("/mes_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesLlmConfigsService(db).delete(entity_id)

@router.get("/mes_machine_alarms", response_model=PaginatedResponse[MesMachineAlarmsOut])
async def list_mes_machine_alarms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMachineAlarmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["alarm_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_machine_alarms/{entity_id}", response_model=MesMachineAlarmsOut)
async def get_mes_machine_alarms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMachineAlarmsService(db).get(entity_id)

@router.post("/mes_machine_alarms", response_model=MesMachineAlarmsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_machine_alarms(
    data: MesMachineAlarmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineAlarmsService(db).create(data)

@router.put("/mes_machine_alarms/{entity_id}", response_model=MesMachineAlarmsOut)
async def update_mes_machine_alarms(
    entity_id: uuid.UUID,
    data: MesMachineAlarmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineAlarmsService(db).update(entity_id, data)

@router.delete("/mes_machine_alarms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_machine_alarms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMachineAlarmsService(db).delete(entity_id)

@router.get("/mes_machine_data_values", response_model=PaginatedResponse[MesMachineDataValuesOut])
async def list_mes_machine_data_values(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMachineDataValuesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_machine_data_values/{entity_id}", response_model=MesMachineDataValuesOut)
async def get_mes_machine_data_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMachineDataValuesService(db).get(entity_id)

@router.post("/mes_machine_data_values", response_model=MesMachineDataValuesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_machine_data_values(
    data: MesMachineDataValuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineDataValuesService(db).create(data)

@router.put("/mes_machine_data_values/{entity_id}", response_model=MesMachineDataValuesOut)
async def update_mes_machine_data_values(
    entity_id: uuid.UUID,
    data: MesMachineDataValuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineDataValuesService(db).update(entity_id, data)

@router.delete("/mes_machine_data_values/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_machine_data_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMachineDataValuesService(db).delete(entity_id)

@router.get("/mes_machine_events", response_model=PaginatedResponse[MesMachineEventsOut])
async def list_mes_machine_events(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMachineEventsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["event_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_machine_events/{entity_id}", response_model=MesMachineEventsOut)
async def get_mes_machine_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMachineEventsService(db).get(entity_id)

@router.post("/mes_machine_events", response_model=MesMachineEventsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_machine_events(
    data: MesMachineEventsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineEventsService(db).create(data)

@router.put("/mes_machine_events/{entity_id}", response_model=MesMachineEventsOut)
async def update_mes_machine_events(
    entity_id: uuid.UUID,
    data: MesMachineEventsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineEventsService(db).update(entity_id, data)

@router.delete("/mes_machine_events/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_machine_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMachineEventsService(db).delete(entity_id)

@router.get("/mes_machine_programs", response_model=PaginatedResponse[MesMachineProgramsOut])
async def list_mes_machine_programs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMachineProgramsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["program_code", "program_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_machine_programs/{entity_id}", response_model=MesMachineProgramsOut)
async def get_mes_machine_programs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMachineProgramsService(db).get(entity_id)

@router.post("/mes_machine_programs", response_model=MesMachineProgramsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_machine_programs(
    data: MesMachineProgramsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineProgramsService(db).create(data)

@router.put("/mes_machine_programs/{entity_id}", response_model=MesMachineProgramsOut)
async def update_mes_machine_programs(
    entity_id: uuid.UUID,
    data: MesMachineProgramsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMachineProgramsService(db).update(entity_id, data)

@router.delete("/mes_machine_programs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_machine_programs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMachineProgramsService(db).delete(entity_id)

@router.get("/mes_maintenance_history", response_model=PaginatedResponse[MesMaintenanceHistoryOut])
async def list_mes_maintenance_history(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaintenanceHistoryService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_maintenance_history/{entity_id}", response_model=MesMaintenanceHistoryOut)
async def get_mes_maintenance_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaintenanceHistoryService(db).get(entity_id)

@router.post("/mes_maintenance_history", response_model=MesMaintenanceHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_mes_maintenance_history(
    data: MesMaintenanceHistoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceHistoryService(db).create(data)

@router.put("/mes_maintenance_history/{entity_id}", response_model=MesMaintenanceHistoryOut)
async def update_mes_maintenance_history(
    entity_id: uuid.UUID,
    data: MesMaintenanceHistoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceHistoryService(db).update(entity_id, data)

@router.delete("/mes_maintenance_history/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_maintenance_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaintenanceHistoryService(db).delete(entity_id)

@router.get("/mes_maintenance_parts", response_model=PaginatedResponse[MesMaintenancePartsOut])
async def list_mes_maintenance_parts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaintenancePartsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "item_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_maintenance_parts/{entity_id}", response_model=MesMaintenancePartsOut)
async def get_mes_maintenance_parts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaintenancePartsService(db).get(entity_id)

@router.post("/mes_maintenance_parts", response_model=MesMaintenancePartsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_maintenance_parts(
    data: MesMaintenancePartsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenancePartsService(db).create(data)

@router.put("/mes_maintenance_parts/{entity_id}", response_model=MesMaintenancePartsOut)
async def update_mes_maintenance_parts(
    entity_id: uuid.UUID,
    data: MesMaintenancePartsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenancePartsService(db).update(entity_id, data)

@router.delete("/mes_maintenance_parts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_maintenance_parts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaintenancePartsService(db).delete(entity_id)

@router.get("/mes_maintenance_schedules", response_model=PaginatedResponse[MesMaintenanceSchedulesOut])
async def list_mes_maintenance_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaintenanceSchedulesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_maintenance_schedules/{entity_id}", response_model=MesMaintenanceSchedulesOut)
async def get_mes_maintenance_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaintenanceSchedulesService(db).get(entity_id)

@router.post("/mes_maintenance_schedules", response_model=MesMaintenanceSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_maintenance_schedules(
    data: MesMaintenanceSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceSchedulesService(db).create(data)

@router.put("/mes_maintenance_schedules/{entity_id}", response_model=MesMaintenanceSchedulesOut)
async def update_mes_maintenance_schedules(
    entity_id: uuid.UUID,
    data: MesMaintenanceSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceSchedulesService(db).update(entity_id, data)

@router.delete("/mes_maintenance_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_maintenance_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaintenanceSchedulesService(db).delete(entity_id)

@router.get("/mes_maintenance_work_orders", response_model=PaginatedResponse[MesMaintenanceWorkOrdersOut])
async def list_mes_maintenance_work_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaintenanceWorkOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_maintenance_work_orders/{entity_id}", response_model=MesMaintenanceWorkOrdersOut)
async def get_mes_maintenance_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaintenanceWorkOrdersService(db).get(entity_id)

@router.post("/mes_maintenance_work_orders", response_model=MesMaintenanceWorkOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_mes_maintenance_work_orders(
    data: MesMaintenanceWorkOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceWorkOrdersService(db).create(data)

@router.put("/mes_maintenance_work_orders/{entity_id}", response_model=MesMaintenanceWorkOrdersOut)
async def update_mes_maintenance_work_orders(
    entity_id: uuid.UUID,
    data: MesMaintenanceWorkOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaintenanceWorkOrdersService(db).update(entity_id, data)

@router.delete("/mes_maintenance_work_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_maintenance_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaintenanceWorkOrdersService(db).delete(entity_id)

@router.get("/mes_material_consumption", response_model=PaginatedResponse[MesMaterialConsumptionOut])
async def list_mes_material_consumption(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaterialConsumptionService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "item_name", "lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_material_consumption/{entity_id}", response_model=MesMaterialConsumptionOut)
async def get_mes_material_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaterialConsumptionService(db).get(entity_id)

@router.post("/mes_material_consumption", response_model=MesMaterialConsumptionOut, status_code=status.HTTP_201_CREATED)
async def create_mes_material_consumption(
    data: MesMaterialConsumptionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialConsumptionService(db).create(data)

@router.put("/mes_material_consumption/{entity_id}", response_model=MesMaterialConsumptionOut)
async def update_mes_material_consumption(
    entity_id: uuid.UUID,
    data: MesMaterialConsumptionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialConsumptionService(db).update(entity_id, data)

@router.delete("/mes_material_consumption/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_material_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaterialConsumptionService(db).delete(entity_id)

@router.get("/mes_material_issues", response_model=PaginatedResponse[MesMaterialIssuesOut])
async def list_mes_material_issues(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaterialIssuesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_material_issues/{entity_id}", response_model=MesMaterialIssuesOut)
async def get_mes_material_issues(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaterialIssuesService(db).get(entity_id)

@router.post("/mes_material_issues", response_model=MesMaterialIssuesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_material_issues(
    data: MesMaterialIssuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialIssuesService(db).create(data)

@router.put("/mes_material_issues/{entity_id}", response_model=MesMaterialIssuesOut)
async def update_mes_material_issues(
    entity_id: uuid.UUID,
    data: MesMaterialIssuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialIssuesService(db).update(entity_id, data)

@router.delete("/mes_material_issues/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_material_issues(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaterialIssuesService(db).delete(entity_id)

@router.get("/mes_material_returns", response_model=PaginatedResponse[MesMaterialReturnsOut])
async def list_mes_material_returns(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMaterialReturnsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_material_returns/{entity_id}", response_model=MesMaterialReturnsOut)
async def get_mes_material_returns(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMaterialReturnsService(db).get(entity_id)

@router.post("/mes_material_returns", response_model=MesMaterialReturnsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_material_returns(
    data: MesMaterialReturnsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialReturnsService(db).create(data)

@router.put("/mes_material_returns/{entity_id}", response_model=MesMaterialReturnsOut)
async def update_mes_material_returns(
    entity_id: uuid.UUID,
    data: MesMaterialReturnsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMaterialReturnsService(db).update(entity_id, data)

@router.delete("/mes_material_returns/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_material_returns(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMaterialReturnsService(db).delete(entity_id)

@router.get("/mes_ml_model_versions", response_model=PaginatedResponse[MesMlModelVersionsOut])
async def list_mes_ml_model_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMlModelVersionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ml_model_versions/{entity_id}", response_model=MesMlModelVersionsOut)
async def get_mes_ml_model_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMlModelVersionsService(db).get(entity_id)

@router.post("/mes_ml_model_versions", response_model=MesMlModelVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ml_model_versions(
    data: MesMlModelVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMlModelVersionsService(db).create(data)

@router.put("/mes_ml_model_versions/{entity_id}", response_model=MesMlModelVersionsOut)
async def update_mes_ml_model_versions(
    entity_id: uuid.UUID,
    data: MesMlModelVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMlModelVersionsService(db).update(entity_id, data)

@router.delete("/mes_ml_model_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ml_model_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMlModelVersionsService(db).delete(entity_id)

@router.get("/mes_ml_models", response_model=PaginatedResponse[MesMlModelsOut])
async def list_mes_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ml_models/{entity_id}", response_model=MesMlModelsOut)
async def get_mes_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesMlModelsService(db).get(entity_id)

@router.post("/mes_ml_models", response_model=MesMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ml_models(
    data: MesMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMlModelsService(db).create(data)

@router.put("/mes_ml_models/{entity_id}", response_model=MesMlModelsOut)
async def update_mes_ml_models(
    entity_id: uuid.UUID,
    data: MesMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesMlModelsService(db).update(entity_id, data)

@router.delete("/mes_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesMlModelsService(db).delete(entity_id)

@router.get("/mes_notifications", response_model=PaginatedResponse[MesNotificationsOut])
async def list_mes_notifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesNotificationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["recipient_email"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_notifications/{entity_id}", response_model=MesNotificationsOut)
async def get_mes_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesNotificationsService(db).get(entity_id)

@router.post("/mes_notifications", response_model=MesNotificationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_notifications(
    data: MesNotificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesNotificationsService(db).create(data)

@router.put("/mes_notifications/{entity_id}", response_model=MesNotificationsOut)
async def update_mes_notifications(
    entity_id: uuid.UUID,
    data: MesNotificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesNotificationsService(db).update(entity_id, data)

@router.delete("/mes_notifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesNotificationsService(db).delete(entity_id)

@router.get("/mes_oee_calculations", response_model=PaginatedResponse[MesOeeCalculationsOut])
async def list_mes_oee_calculations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOeeCalculationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_oee_calculations/{entity_id}", response_model=MesOeeCalculationsOut)
async def get_mes_oee_calculations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOeeCalculationsService(db).get(entity_id)

@router.post("/mes_oee_calculations", response_model=MesOeeCalculationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_oee_calculations(
    data: MesOeeCalculationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeCalculationsService(db).create(data)

@router.put("/mes_oee_calculations/{entity_id}", response_model=MesOeeCalculationsOut)
async def update_mes_oee_calculations(
    entity_id: uuid.UUID,
    data: MesOeeCalculationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeCalculationsService(db).update(entity_id, data)

@router.delete("/mes_oee_calculations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_oee_calculations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOeeCalculationsService(db).delete(entity_id)

@router.get("/mes_oee_losses", response_model=PaginatedResponse[MesOeeLossesOut])
async def list_mes_oee_losses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOeeLossesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_oee_losses/{entity_id}", response_model=MesOeeLossesOut)
async def get_mes_oee_losses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOeeLossesService(db).get(entity_id)

@router.post("/mes_oee_losses", response_model=MesOeeLossesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_oee_losses(
    data: MesOeeLossesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeLossesService(db).create(data)

@router.put("/mes_oee_losses/{entity_id}", response_model=MesOeeLossesOut)
async def update_mes_oee_losses(
    entity_id: uuid.UUID,
    data: MesOeeLossesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeLossesService(db).update(entity_id, data)

@router.delete("/mes_oee_losses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_oee_losses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOeeLossesService(db).delete(entity_id)

@router.get("/mes_oee_targets", response_model=PaginatedResponse[MesOeeTargetsOut])
async def list_mes_oee_targets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOeeTargetsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_oee_targets/{entity_id}", response_model=MesOeeTargetsOut)
async def get_mes_oee_targets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOeeTargetsService(db).get(entity_id)

@router.post("/mes_oee_targets", response_model=MesOeeTargetsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_oee_targets(
    data: MesOeeTargetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeTargetsService(db).create(data)

@router.put("/mes_oee_targets/{entity_id}", response_model=MesOeeTargetsOut)
async def update_mes_oee_targets(
    entity_id: uuid.UUID,
    data: MesOeeTargetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOeeTargetsService(db).update(entity_id, data)

@router.delete("/mes_oee_targets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_oee_targets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOeeTargetsService(db).delete(entity_id)

@router.get("/mes_operation_execution", response_model=PaginatedResponse[MesOperationExecutionOut])
async def list_mes_operation_execution(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperationExecutionService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["operation_code", "operation_name", "scrap_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operation_execution/{entity_id}", response_model=MesOperationExecutionOut)
async def get_mes_operation_execution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperationExecutionService(db).get(entity_id)

@router.post("/mes_operation_execution", response_model=MesOperationExecutionOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operation_execution(
    data: MesOperationExecutionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperationExecutionService(db).create(data)

@router.put("/mes_operation_execution/{entity_id}", response_model=MesOperationExecutionOut)
async def update_mes_operation_execution(
    entity_id: uuid.UUID,
    data: MesOperationExecutionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperationExecutionService(db).update(entity_id, data)

@router.delete("/mes_operation_execution/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operation_execution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperationExecutionService(db).delete(entity_id)

@router.get("/mes_operation_steps", response_model=PaginatedResponse[MesOperationStepsOut])
async def list_mes_operation_steps(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperationStepsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operation_steps/{entity_id}", response_model=MesOperationStepsOut)
async def get_mes_operation_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperationStepsService(db).get(entity_id)

@router.post("/mes_operation_steps", response_model=MesOperationStepsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operation_steps(
    data: MesOperationStepsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperationStepsService(db).create(data)

@router.put("/mes_operation_steps/{entity_id}", response_model=MesOperationStepsOut)
async def update_mes_operation_steps(
    entity_id: uuid.UUID,
    data: MesOperationStepsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperationStepsService(db).update(entity_id, data)

@router.delete("/mes_operation_steps/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operation_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperationStepsService(db).delete(entity_id)

@router.get("/mes_operator_assignments", response_model=PaginatedResponse[MesOperatorAssignmentsOut])
async def list_mes_operator_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_assignments/{entity_id}", response_model=MesOperatorAssignmentsOut)
async def get_mes_operator_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorAssignmentsService(db).get(entity_id)

@router.post("/mes_operator_assignments", response_model=MesOperatorAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_assignments(
    data: MesOperatorAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorAssignmentsService(db).create(data)

@router.put("/mes_operator_assignments/{entity_id}", response_model=MesOperatorAssignmentsOut)
async def update_mes_operator_assignments(
    entity_id: uuid.UUID,
    data: MesOperatorAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_operator_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorAssignmentsService(db).delete(entity_id)

@router.get("/mes_operator_certifications", response_model=PaginatedResponse[MesOperatorCertificationsOut])
async def list_mes_operator_certifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorCertificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cert_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_certifications/{entity_id}", response_model=MesOperatorCertificationsOut)
async def get_mes_operator_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorCertificationsService(db).get(entity_id)

@router.post("/mes_operator_certifications", response_model=MesOperatorCertificationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_certifications(
    data: MesOperatorCertificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorCertificationsService(db).create(data)

@router.put("/mes_operator_certifications/{entity_id}", response_model=MesOperatorCertificationsOut)
async def update_mes_operator_certifications(
    entity_id: uuid.UUID,
    data: MesOperatorCertificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorCertificationsService(db).update(entity_id, data)

@router.delete("/mes_operator_certifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorCertificationsService(db).delete(entity_id)

@router.get("/mes_operator_performance", response_model=PaginatedResponse[MesOperatorPerformanceOut])
async def list_mes_operator_performance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorPerformanceService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_performance/{entity_id}", response_model=MesOperatorPerformanceOut)
async def get_mes_operator_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorPerformanceService(db).get(entity_id)

@router.post("/mes_operator_performance", response_model=MesOperatorPerformanceOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_performance(
    data: MesOperatorPerformanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorPerformanceService(db).create(data)

@router.put("/mes_operator_performance/{entity_id}", response_model=MesOperatorPerformanceOut)
async def update_mes_operator_performance(
    entity_id: uuid.UUID,
    data: MesOperatorPerformanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorPerformanceService(db).update(entity_id, data)

@router.delete("/mes_operator_performance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorPerformanceService(db).delete(entity_id)

@router.get("/mes_operator_schedules", response_model=PaginatedResponse[MesOperatorSchedulesOut])
async def list_mes_operator_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorSchedulesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_schedules/{entity_id}", response_model=MesOperatorSchedulesOut)
async def get_mes_operator_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorSchedulesService(db).get(entity_id)

@router.post("/mes_operator_schedules", response_model=MesOperatorSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_schedules(
    data: MesOperatorSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorSchedulesService(db).create(data)

@router.put("/mes_operator_schedules/{entity_id}", response_model=MesOperatorSchedulesOut)
async def update_mes_operator_schedules(
    entity_id: uuid.UUID,
    data: MesOperatorSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorSchedulesService(db).update(entity_id, data)

@router.delete("/mes_operator_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorSchedulesService(db).delete(entity_id)

@router.get("/mes_operator_skills", response_model=PaginatedResponse[MesOperatorSkillsOut])
async def list_mes_operator_skills(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorSkillsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["skill_code", "skill_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_skills/{entity_id}", response_model=MesOperatorSkillsOut)
async def get_mes_operator_skills(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorSkillsService(db).get(entity_id)

@router.post("/mes_operator_skills", response_model=MesOperatorSkillsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_skills(
    data: MesOperatorSkillsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorSkillsService(db).create(data)

@router.put("/mes_operator_skills/{entity_id}", response_model=MesOperatorSkillsOut)
async def update_mes_operator_skills(
    entity_id: uuid.UUID,
    data: MesOperatorSkillsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorSkillsService(db).update(entity_id, data)

@router.delete("/mes_operator_skills/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_skills(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorSkillsService(db).delete(entity_id)

@router.get("/mes_operator_training", response_model=PaginatedResponse[MesOperatorTrainingOut])
async def list_mes_operator_training(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorTrainingService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operator_training/{entity_id}", response_model=MesOperatorTrainingOut)
async def get_mes_operator_training(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorTrainingService(db).get(entity_id)

@router.post("/mes_operator_training", response_model=MesOperatorTrainingOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operator_training(
    data: MesOperatorTrainingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorTrainingService(db).create(data)

@router.put("/mes_operator_training/{entity_id}", response_model=MesOperatorTrainingOut)
async def update_mes_operator_training(
    entity_id: uuid.UUID,
    data: MesOperatorTrainingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorTrainingService(db).update(entity_id, data)

@router.delete("/mes_operator_training/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operator_training(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorTrainingService(db).delete(entity_id)

@router.get("/mes_operators", response_model=PaginatedResponse[MesOperatorsOut])
async def list_mes_operators(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOperatorsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["employee_code", "first_name", "last_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_operators/{entity_id}", response_model=MesOperatorsOut)
async def get_mes_operators(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOperatorsService(db).get(entity_id)

@router.post("/mes_operators", response_model=MesOperatorsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_operators(
    data: MesOperatorsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorsService(db).create(data)

@router.put("/mes_operators/{entity_id}", response_model=MesOperatorsOut)
async def update_mes_operators(
    entity_id: uuid.UUID,
    data: MesOperatorsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOperatorsService(db).update(entity_id, data)

@router.delete("/mes_operators/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_operators(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOperatorsService(db).delete(entity_id)

@router.get("/mes_optimization_problems", response_model=PaginatedResponse[MesOptimizationProblemsOut])
async def list_mes_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOptimizationProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_optimization_problems/{entity_id}", response_model=MesOptimizationProblemsOut)
async def get_mes_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOptimizationProblemsService(db).get(entity_id)

@router.post("/mes_optimization_problems", response_model=MesOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_optimization_problems(
    data: MesOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOptimizationProblemsService(db).create(data)

@router.put("/mes_optimization_problems/{entity_id}", response_model=MesOptimizationProblemsOut)
async def update_mes_optimization_problems(
    entity_id: uuid.UUID,
    data: MesOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/mes_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOptimizationProblemsService(db).delete(entity_id)

@router.get("/mes_optimization_results", response_model=PaginatedResponse[MesOptimizationResultsOut])
async def list_mes_optimization_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOptimizationResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_optimization_results/{entity_id}", response_model=MesOptimizationResultsOut)
async def get_mes_optimization_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOptimizationResultsService(db).get(entity_id)

@router.post("/mes_optimization_results", response_model=MesOptimizationResultsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_optimization_results(
    data: MesOptimizationResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOptimizationResultsService(db).create(data)

@router.put("/mes_optimization_results/{entity_id}", response_model=MesOptimizationResultsOut)
async def update_mes_optimization_results(
    entity_id: uuid.UUID,
    data: MesOptimizationResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOptimizationResultsService(db).update(entity_id, data)

@router.delete("/mes_optimization_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_optimization_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOptimizationResultsService(db).delete(entity_id)

@router.get("/mes_ortools_problems", response_model=PaginatedResponse[MesOrtoolsProblemsOut])
async def list_mes_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesOrtoolsProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_ortools_problems/{entity_id}", response_model=MesOrtoolsProblemsOut)
async def get_mes_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesOrtoolsProblemsService(db).get(entity_id)

@router.post("/mes_ortools_problems", response_model=MesOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_ortools_problems(
    data: MesOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOrtoolsProblemsService(db).create(data)

@router.put("/mes_ortools_problems/{entity_id}", response_model=MesOrtoolsProblemsOut)
async def update_mes_ortools_problems(
    entity_id: uuid.UUID,
    data: MesOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/mes_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesOrtoolsProblemsService(db).delete(entity_id)

@router.get("/mes_performance_actuals", response_model=PaginatedResponse[MesPerformanceActualsOut])
async def list_mes_performance_actuals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesPerformanceActualsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_performance_actuals/{entity_id}", response_model=MesPerformanceActualsOut)
async def get_mes_performance_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesPerformanceActualsService(db).get(entity_id)

@router.post("/mes_performance_actuals", response_model=MesPerformanceActualsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_performance_actuals(
    data: MesPerformanceActualsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPerformanceActualsService(db).create(data)

@router.put("/mes_performance_actuals/{entity_id}", response_model=MesPerformanceActualsOut)
async def update_mes_performance_actuals(
    entity_id: uuid.UUID,
    data: MesPerformanceActualsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPerformanceActualsService(db).update(entity_id, data)

@router.delete("/mes_performance_actuals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_performance_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesPerformanceActualsService(db).delete(entity_id)

@router.get("/mes_performance_metrics", response_model=PaginatedResponse[MesPerformanceMetricsOut])
async def list_mes_performance_metrics(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesPerformanceMetricsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["metric_code", "metric_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_performance_metrics/{entity_id}", response_model=MesPerformanceMetricsOut)
async def get_mes_performance_metrics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesPerformanceMetricsService(db).get(entity_id)

@router.post("/mes_performance_metrics", response_model=MesPerformanceMetricsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_performance_metrics(
    data: MesPerformanceMetricsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPerformanceMetricsService(db).create(data)

@router.put("/mes_performance_metrics/{entity_id}", response_model=MesPerformanceMetricsOut)
async def update_mes_performance_metrics(
    entity_id: uuid.UUID,
    data: MesPerformanceMetricsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPerformanceMetricsService(db).update(entity_id, data)

@router.delete("/mes_performance_metrics/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_performance_metrics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesPerformanceMetricsService(db).delete(entity_id)

@router.get("/mes_predictions", response_model=PaginatedResponse[MesPredictionsOut])
async def list_mes_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesPredictionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_predictions/{entity_id}", response_model=MesPredictionsOut)
async def get_mes_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesPredictionsService(db).get(entity_id)

@router.post("/mes_predictions", response_model=MesPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_predictions(
    data: MesPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPredictionsService(db).create(data)

@router.put("/mes_predictions/{entity_id}", response_model=MesPredictionsOut)
async def update_mes_predictions(
    entity_id: uuid.UUID,
    data: MesPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPredictionsService(db).update(entity_id, data)

@router.delete("/mes_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesPredictionsService(db).delete(entity_id)

@router.get("/mes_production_cells", response_model=PaginatedResponse[MesProductionCellsOut])
async def list_mes_production_cells(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesProductionCellsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cell_code", "cell_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_production_cells/{entity_id}", response_model=MesProductionCellsOut)
async def get_mes_production_cells(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesProductionCellsService(db).get(entity_id)

@router.post("/mes_production_cells", response_model=MesProductionCellsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_production_cells(
    data: MesProductionCellsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesProductionCellsService(db).create(data)

@router.put("/mes_production_cells/{entity_id}", response_model=MesProductionCellsOut)
async def update_mes_production_cells(
    entity_id: uuid.UUID,
    data: MesProductionCellsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesProductionCellsService(db).update(entity_id, data)

@router.delete("/mes_production_cells/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_production_cells(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesProductionCellsService(db).delete(entity_id)

@router.get("/mes_production_lines", response_model=PaginatedResponse[MesProductionLinesOut])
async def list_mes_production_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesProductionLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["line_code", "line_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_production_lines/{entity_id}", response_model=MesProductionLinesOut)
async def get_mes_production_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesProductionLinesService(db).get(entity_id)

@router.post("/mes_production_lines", response_model=MesProductionLinesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_production_lines(
    data: MesProductionLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesProductionLinesService(db).create(data)

@router.put("/mes_production_lines/{entity_id}", response_model=MesProductionLinesOut)
async def update_mes_production_lines(
    entity_id: uuid.UUID,
    data: MesProductionLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesProductionLinesService(db).update(entity_id, data)

@router.delete("/mes_production_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_production_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesProductionLinesService(db).delete(entity_id)

@router.get("/mes_prompt_templates", response_model=PaginatedResponse[MesPromptTemplatesOut])
async def list_mes_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_prompt_templates/{entity_id}", response_model=MesPromptTemplatesOut)
async def get_mes_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesPromptTemplatesService(db).get(entity_id)

@router.post("/mes_prompt_templates", response_model=MesPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_prompt_templates(
    data: MesPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPromptTemplatesService(db).create(data)

@router.put("/mes_prompt_templates/{entity_id}", response_model=MesPromptTemplatesOut)
async def update_mes_prompt_templates(
    entity_id: uuid.UUID,
    data: MesPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesPromptTemplatesService(db).update(entity_id, data)

@router.delete("/mes_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesPromptTemplatesService(db).delete(entity_id)

@router.get("/mes_quality_holds", response_model=PaginatedResponse[MesQualityHoldsOut])
async def list_mes_quality_holds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesQualityHoldsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_quality_holds/{entity_id}", response_model=MesQualityHoldsOut)
async def get_mes_quality_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesQualityHoldsService(db).get(entity_id)

@router.post("/mes_quality_holds", response_model=MesQualityHoldsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_quality_holds(
    data: MesQualityHoldsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualityHoldsService(db).create(data)

@router.put("/mes_quality_holds/{entity_id}", response_model=MesQualityHoldsOut)
async def update_mes_quality_holds(
    entity_id: uuid.UUID,
    data: MesQualityHoldsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualityHoldsService(db).update(entity_id, data)

@router.delete("/mes_quality_holds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_quality_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesQualityHoldsService(db).delete(entity_id)

@router.get("/mes_quality_inspections", response_model=PaginatedResponse[MesQualityInspectionsOut])
async def list_mes_quality_inspections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesQualityInspectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["defect_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_quality_inspections/{entity_id}", response_model=MesQualityInspectionsOut)
async def get_mes_quality_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesQualityInspectionsService(db).get(entity_id)

@router.post("/mes_quality_inspections", response_model=MesQualityInspectionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_quality_inspections(
    data: MesQualityInspectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualityInspectionsService(db).create(data)

@router.put("/mes_quality_inspections/{entity_id}", response_model=MesQualityInspectionsOut)
async def update_mes_quality_inspections(
    entity_id: uuid.UUID,
    data: MesQualityInspectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualityInspectionsService(db).update(entity_id, data)

@router.delete("/mes_quality_inspections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_quality_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesQualityInspectionsService(db).delete(entity_id)

@router.get("/mes_quality_spc_data", response_model=PaginatedResponse[MesQualitySpcDataOut])
async def list_mes_quality_spc_data(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesQualitySpcDataService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_quality_spc_data/{entity_id}", response_model=MesQualitySpcDataOut)
async def get_mes_quality_spc_data(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesQualitySpcDataService(db).get(entity_id)

@router.post("/mes_quality_spc_data", response_model=MesQualitySpcDataOut, status_code=status.HTTP_201_CREATED)
async def create_mes_quality_spc_data(
    data: MesQualitySpcDataCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualitySpcDataService(db).create(data)

@router.put("/mes_quality_spc_data/{entity_id}", response_model=MesQualitySpcDataOut)
async def update_mes_quality_spc_data(
    entity_id: uuid.UUID,
    data: MesQualitySpcDataUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesQualitySpcDataService(db).update(entity_id, data)

@router.delete("/mes_quality_spc_data/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_quality_spc_data(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesQualitySpcDataService(db).delete(entity_id)

@router.get("/mes_resource_availability", response_model=PaginatedResponse[MesResourceAvailabilityOut])
async def list_mes_resource_availability(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesResourceAvailabilityService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_resource_availability/{entity_id}", response_model=MesResourceAvailabilityOut)
async def get_mes_resource_availability(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesResourceAvailabilityService(db).get(entity_id)

@router.post("/mes_resource_availability", response_model=MesResourceAvailabilityOut, status_code=status.HTTP_201_CREATED)
async def create_mes_resource_availability(
    data: MesResourceAvailabilityCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceAvailabilityService(db).create(data)

@router.put("/mes_resource_availability/{entity_id}", response_model=MesResourceAvailabilityOut)
async def update_mes_resource_availability(
    entity_id: uuid.UUID,
    data: MesResourceAvailabilityUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceAvailabilityService(db).update(entity_id, data)

@router.delete("/mes_resource_availability/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_resource_availability(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesResourceAvailabilityService(db).delete(entity_id)

@router.get("/mes_resource_costs", response_model=PaginatedResponse[MesResourceCostsOut])
async def list_mes_resource_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesResourceCostsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_resource_costs/{entity_id}", response_model=MesResourceCostsOut)
async def get_mes_resource_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesResourceCostsService(db).get(entity_id)

@router.post("/mes_resource_costs", response_model=MesResourceCostsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_resource_costs(
    data: MesResourceCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceCostsService(db).create(data)

@router.put("/mes_resource_costs/{entity_id}", response_model=MesResourceCostsOut)
async def update_mes_resource_costs(
    entity_id: uuid.UUID,
    data: MesResourceCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceCostsService(db).update(entity_id, data)

@router.delete("/mes_resource_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_resource_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesResourceCostsService(db).delete(entity_id)

@router.get("/mes_resource_types", response_model=PaginatedResponse[MesResourceTypesOut])
async def list_mes_resource_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesResourceTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_resource_types/{entity_id}", response_model=MesResourceTypesOut)
async def get_mes_resource_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesResourceTypesService(db).get(entity_id)

@router.post("/mes_resource_types", response_model=MesResourceTypesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_resource_types(
    data: MesResourceTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceTypesService(db).create(data)

@router.put("/mes_resource_types/{entity_id}", response_model=MesResourceTypesOut)
async def update_mes_resource_types(
    entity_id: uuid.UUID,
    data: MesResourceTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourceTypesService(db).update(entity_id, data)

@router.delete("/mes_resource_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_resource_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesResourceTypesService(db).delete(entity_id)

@router.get("/mes_resources", response_model=PaginatedResponse[MesResourcesOut])
async def list_mes_resources(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesResourcesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["resource_code", "resource_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_resources/{entity_id}", response_model=MesResourcesOut)
async def get_mes_resources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesResourcesService(db).get(entity_id)

@router.post("/mes_resources", response_model=MesResourcesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_resources(
    data: MesResourcesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourcesService(db).create(data)

@router.put("/mes_resources/{entity_id}", response_model=MesResourcesOut)
async def update_mes_resources(
    entity_id: uuid.UUID,
    data: MesResourcesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesResourcesService(db).update(entity_id, data)

@router.delete("/mes_resources/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_resources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesResourcesService(db).delete(entity_id)

@router.get("/mes_scenarios", response_model=PaginatedResponse[MesScenariosOut])
async def list_mes_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_scenarios/{entity_id}", response_model=MesScenariosOut)
async def get_mes_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesScenariosService(db).get(entity_id)

@router.post("/mes_scenarios", response_model=MesScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_mes_scenarios(
    data: MesScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScenariosService(db).create(data)

@router.put("/mes_scenarios/{entity_id}", response_model=MesScenariosOut)
async def update_mes_scenarios(
    entity_id: uuid.UUID,
    data: MesScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScenariosService(db).update(entity_id, data)

@router.delete("/mes_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesScenariosService(db).delete(entity_id)

@router.get("/mes_schedule_results", response_model=PaginatedResponse[MesScheduleResultsOut])
async def list_mes_schedule_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesScheduleResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_schedule_results/{entity_id}", response_model=MesScheduleResultsOut)
async def get_mes_schedule_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesScheduleResultsService(db).get(entity_id)

@router.post("/mes_schedule_results", response_model=MesScheduleResultsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_schedule_results(
    data: MesScheduleResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScheduleResultsService(db).create(data)

@router.put("/mes_schedule_results/{entity_id}", response_model=MesScheduleResultsOut)
async def update_mes_schedule_results(
    entity_id: uuid.UUID,
    data: MesScheduleResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScheduleResultsService(db).update(entity_id, data)

@router.delete("/mes_schedule_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_schedule_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesScheduleResultsService(db).delete(entity_id)

@router.get("/mes_scheduling_problems", response_model=PaginatedResponse[MesSchedulingProblemsOut])
async def list_mes_scheduling_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesSchedulingProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_scheduling_problems/{entity_id}", response_model=MesSchedulingProblemsOut)
async def get_mes_scheduling_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesSchedulingProblemsService(db).get(entity_id)

@router.post("/mes_scheduling_problems", response_model=MesSchedulingProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_scheduling_problems(
    data: MesSchedulingProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSchedulingProblemsService(db).create(data)

@router.put("/mes_scheduling_problems/{entity_id}", response_model=MesSchedulingProblemsOut)
async def update_mes_scheduling_problems(
    entity_id: uuid.UUID,
    data: MesSchedulingProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSchedulingProblemsService(db).update(entity_id, data)

@router.delete("/mes_scheduling_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_scheduling_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesSchedulingProblemsService(db).delete(entity_id)

@router.get("/mes_scipy_analyses", response_model=PaginatedResponse[MesScipyAnalysesOut])
async def list_mes_scipy_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesScipyAnalysesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["analysis_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_scipy_analyses/{entity_id}", response_model=MesScipyAnalysesOut)
async def get_mes_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesScipyAnalysesService(db).get(entity_id)

@router.post("/mes_scipy_analyses", response_model=MesScipyAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_scipy_analyses(
    data: MesScipyAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScipyAnalysesService(db).create(data)

@router.put("/mes_scipy_analyses/{entity_id}", response_model=MesScipyAnalysesOut)
async def update_mes_scipy_analyses(
    entity_id: uuid.UUID,
    data: MesScipyAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesScipyAnalysesService(db).update(entity_id, data)

@router.delete("/mes_scipy_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesScipyAnalysesService(db).delete(entity_id)

@router.get("/mes_sensor_calibrations", response_model=PaginatedResponse[MesSensorCalibrationsOut])
async def list_mes_sensor_calibrations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesSensorCalibrationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["certificate_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_sensor_calibrations/{entity_id}", response_model=MesSensorCalibrationsOut)
async def get_mes_sensor_calibrations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesSensorCalibrationsService(db).get(entity_id)

@router.post("/mes_sensor_calibrations", response_model=MesSensorCalibrationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_sensor_calibrations(
    data: MesSensorCalibrationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSensorCalibrationsService(db).create(data)

@router.put("/mes_sensor_calibrations/{entity_id}", response_model=MesSensorCalibrationsOut)
async def update_mes_sensor_calibrations(
    entity_id: uuid.UUID,
    data: MesSensorCalibrationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSensorCalibrationsService(db).update(entity_id, data)

@router.delete("/mes_sensor_calibrations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_sensor_calibrations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesSensorCalibrationsService(db).delete(entity_id)

@router.get("/mes_sensors", response_model=PaginatedResponse[MesSensorsOut])
async def list_mes_sensors(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesSensorsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["sensor_code", "sensor_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_sensors/{entity_id}", response_model=MesSensorsOut)
async def get_mes_sensors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesSensorsService(db).get(entity_id)

@router.post("/mes_sensors", response_model=MesSensorsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_sensors(
    data: MesSensorsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSensorsService(db).create(data)

@router.put("/mes_sensors/{entity_id}", response_model=MesSensorsOut)
async def update_mes_sensors(
    entity_id: uuid.UUID,
    data: MesSensorsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSensorsService(db).update(entity_id, data)

@router.delete("/mes_sensors/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_sensors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesSensorsService(db).delete(entity_id)

@router.get("/mes_shift_handovers", response_model=PaginatedResponse[MesShiftHandoversOut])
async def list_mes_shift_handovers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesShiftHandoversService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_shift_handovers/{entity_id}", response_model=MesShiftHandoversOut)
async def get_mes_shift_handovers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesShiftHandoversService(db).get(entity_id)

@router.post("/mes_shift_handovers", response_model=MesShiftHandoversOut, status_code=status.HTTP_201_CREATED)
async def create_mes_shift_handovers(
    data: MesShiftHandoversCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftHandoversService(db).create(data)

@router.put("/mes_shift_handovers/{entity_id}", response_model=MesShiftHandoversOut)
async def update_mes_shift_handovers(
    entity_id: uuid.UUID,
    data: MesShiftHandoversUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftHandoversService(db).update(entity_id, data)

@router.delete("/mes_shift_handovers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_shift_handovers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesShiftHandoversService(db).delete(entity_id)

@router.get("/mes_shift_schedules", response_model=PaginatedResponse[MesShiftSchedulesOut])
async def list_mes_shift_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesShiftSchedulesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_shift_schedules/{entity_id}", response_model=MesShiftSchedulesOut)
async def get_mes_shift_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesShiftSchedulesService(db).get(entity_id)

@router.post("/mes_shift_schedules", response_model=MesShiftSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_shift_schedules(
    data: MesShiftSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftSchedulesService(db).create(data)

@router.put("/mes_shift_schedules/{entity_id}", response_model=MesShiftSchedulesOut)
async def update_mes_shift_schedules(
    entity_id: uuid.UUID,
    data: MesShiftSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftSchedulesService(db).update(entity_id, data)

@router.delete("/mes_shift_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_shift_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesShiftSchedulesService(db).delete(entity_id)

@router.get("/mes_shifts", response_model=PaginatedResponse[MesShiftsOut])
async def list_mes_shifts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesShiftsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["shift_code", "shift_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_shifts/{entity_id}", response_model=MesShiftsOut)
async def get_mes_shifts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesShiftsService(db).get(entity_id)

@router.post("/mes_shifts", response_model=MesShiftsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_shifts(
    data: MesShiftsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftsService(db).create(data)

@router.put("/mes_shifts/{entity_id}", response_model=MesShiftsOut)
async def update_mes_shifts(
    entity_id: uuid.UUID,
    data: MesShiftsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesShiftsService(db).update(entity_id, data)

@router.delete("/mes_shifts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_shifts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesShiftsService(db).delete(entity_id)

@router.get("/mes_solver_configs", response_model=PaginatedResponse[MesSolverConfigsOut])
async def list_mes_solver_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesSolverConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solver_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_solver_configs/{entity_id}", response_model=MesSolverConfigsOut)
async def get_mes_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesSolverConfigsService(db).get(entity_id)

@router.post("/mes_solver_configs", response_model=MesSolverConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_solver_configs(
    data: MesSolverConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSolverConfigsService(db).create(data)

@router.put("/mes_solver_configs/{entity_id}", response_model=MesSolverConfigsOut)
async def update_mes_solver_configs(
    entity_id: uuid.UUID,
    data: MesSolverConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesSolverConfigsService(db).update(entity_id, data)

@router.delete("/mes_solver_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesSolverConfigsService(db).delete(entity_id)

@router.get("/mes_station_assignments", response_model=PaginatedResponse[MesStationAssignmentsOut])
async def list_mes_station_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesStationAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_station_assignments/{entity_id}", response_model=MesStationAssignmentsOut)
async def get_mes_station_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesStationAssignmentsService(db).get(entity_id)

@router.post("/mes_station_assignments", response_model=MesStationAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_station_assignments(
    data: MesStationAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationAssignmentsService(db).create(data)

@router.put("/mes_station_assignments/{entity_id}", response_model=MesStationAssignmentsOut)
async def update_mes_station_assignments(
    entity_id: uuid.UUID,
    data: MesStationAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_station_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_station_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesStationAssignmentsService(db).delete(entity_id)

@router.get("/mes_station_types", response_model=PaginatedResponse[MesStationTypesOut])
async def list_mes_station_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesStationTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_station_types/{entity_id}", response_model=MesStationTypesOut)
async def get_mes_station_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesStationTypesService(db).get(entity_id)

@router.post("/mes_station_types", response_model=MesStationTypesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_station_types(
    data: MesStationTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationTypesService(db).create(data)

@router.put("/mes_station_types/{entity_id}", response_model=MesStationTypesOut)
async def update_mes_station_types(
    entity_id: uuid.UUID,
    data: MesStationTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationTypesService(db).update(entity_id, data)

@router.delete("/mes_station_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_station_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesStationTypesService(db).delete(entity_id)

@router.get("/mes_stations", response_model=PaginatedResponse[MesStationsOut])
async def list_mes_stations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesStationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["station_code", "station_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_stations/{entity_id}", response_model=MesStationsOut)
async def get_mes_stations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesStationsService(db).get(entity_id)

@router.post("/mes_stations", response_model=MesStationsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_stations(
    data: MesStationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationsService(db).create(data)

@router.put("/mes_stations/{entity_id}", response_model=MesStationsOut)
async def update_mes_stations(
    entity_id: uuid.UUID,
    data: MesStationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesStationsService(db).update(entity_id, data)

@router.delete("/mes_stations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_stations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesStationsService(db).delete(entity_id)

@router.get("/mes_tool_cribs", response_model=PaginatedResponse[MesToolCribsOut])
async def list_mes_tool_cribs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesToolCribsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["crib_code", "crib_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_tool_cribs/{entity_id}", response_model=MesToolCribsOut)
async def get_mes_tool_cribs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesToolCribsService(db).get(entity_id)

@router.post("/mes_tool_cribs", response_model=MesToolCribsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_tool_cribs(
    data: MesToolCribsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolCribsService(db).create(data)

@router.put("/mes_tool_cribs/{entity_id}", response_model=MesToolCribsOut)
async def update_mes_tool_cribs(
    entity_id: uuid.UUID,
    data: MesToolCribsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolCribsService(db).update(entity_id, data)

@router.delete("/mes_tool_cribs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_tool_cribs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesToolCribsService(db).delete(entity_id)

@router.get("/mes_tooling_assignments", response_model=PaginatedResponse[MesToolingAssignmentsOut])
async def list_mes_tooling_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesToolingAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_tooling_assignments/{entity_id}", response_model=MesToolingAssignmentsOut)
async def get_mes_tooling_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesToolingAssignmentsService(db).get(entity_id)

@router.post("/mes_tooling_assignments", response_model=MesToolingAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_tooling_assignments(
    data: MesToolingAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingAssignmentsService(db).create(data)

@router.put("/mes_tooling_assignments/{entity_id}", response_model=MesToolingAssignmentsOut)
async def update_mes_tooling_assignments(
    entity_id: uuid.UUID,
    data: MesToolingAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingAssignmentsService(db).update(entity_id, data)

@router.delete("/mes_tooling_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_tooling_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesToolingAssignmentsService(db).delete(entity_id)

@router.get("/mes_tooling_life_tracking", response_model=PaginatedResponse[MesToolingLifeTrackingOut])
async def list_mes_tooling_life_tracking(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesToolingLifeTrackingService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_tooling_life_tracking/{entity_id}", response_model=MesToolingLifeTrackingOut)
async def get_mes_tooling_life_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesToolingLifeTrackingService(db).get(entity_id)

@router.post("/mes_tooling_life_tracking", response_model=MesToolingLifeTrackingOut, status_code=status.HTTP_201_CREATED)
async def create_mes_tooling_life_tracking(
    data: MesToolingLifeTrackingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingLifeTrackingService(db).create(data)

@router.put("/mes_tooling_life_tracking/{entity_id}", response_model=MesToolingLifeTrackingOut)
async def update_mes_tooling_life_tracking(
    entity_id: uuid.UUID,
    data: MesToolingLifeTrackingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingLifeTrackingService(db).update(entity_id, data)

@router.delete("/mes_tooling_life_tracking/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_tooling_life_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesToolingLifeTrackingService(db).delete(entity_id)

@router.get("/mes_tooling_master", response_model=PaginatedResponse[MesToolingMasterOut])
async def list_mes_tooling_master(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesToolingMasterService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["tool_code", "tool_name", "serial_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_tooling_master/{entity_id}", response_model=MesToolingMasterOut)
async def get_mes_tooling_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesToolingMasterService(db).get(entity_id)

@router.post("/mes_tooling_master", response_model=MesToolingMasterOut, status_code=status.HTTP_201_CREATED)
async def create_mes_tooling_master(
    data: MesToolingMasterCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingMasterService(db).create(data)

@router.put("/mes_tooling_master/{entity_id}", response_model=MesToolingMasterOut)
async def update_mes_tooling_master(
    entity_id: uuid.UUID,
    data: MesToolingMasterUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingMasterService(db).update(entity_id, data)

@router.delete("/mes_tooling_master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_tooling_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesToolingMasterService(db).delete(entity_id)

@router.get("/mes_tooling_types", response_model=PaginatedResponse[MesToolingTypesOut])
async def list_mes_tooling_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesToolingTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_tooling_types/{entity_id}", response_model=MesToolingTypesOut)
async def get_mes_tooling_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesToolingTypesService(db).get(entity_id)

@router.post("/mes_tooling_types", response_model=MesToolingTypesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_tooling_types(
    data: MesToolingTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingTypesService(db).create(data)

@router.put("/mes_tooling_types/{entity_id}", response_model=MesToolingTypesOut)
async def update_mes_tooling_types(
    entity_id: uuid.UUID,
    data: MesToolingTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesToolingTypesService(db).update(entity_id, data)

@router.delete("/mes_tooling_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_tooling_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesToolingTypesService(db).delete(entity_id)

@router.get("/mes_vector_store_configs", response_model=PaginatedResponse[MesVectorStoreConfigsOut])
async def list_mes_vector_store_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesVectorStoreConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_name", "collection_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_vector_store_configs/{entity_id}", response_model=MesVectorStoreConfigsOut)
async def get_mes_vector_store_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesVectorStoreConfigsService(db).get(entity_id)

@router.post("/mes_vector_store_configs", response_model=MesVectorStoreConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_vector_store_configs(
    data: MesVectorStoreConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesVectorStoreConfigsService(db).create(data)

@router.put("/mes_vector_store_configs/{entity_id}", response_model=MesVectorStoreConfigsOut)
async def update_mes_vector_store_configs(
    entity_id: uuid.UUID,
    data: MesVectorStoreConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesVectorStoreConfigsService(db).update(entity_id, data)

@router.delete("/mes_vector_store_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_vector_store_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesVectorStoreConfigsService(db).delete(entity_id)

@router.get("/mes_vector_store_documents", response_model=PaginatedResponse[MesVectorStoreDocumentsOut])
async def list_mes_vector_store_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesVectorStoreDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_vector_store_documents/{entity_id}", response_model=MesVectorStoreDocumentsOut)
async def get_mes_vector_store_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesVectorStoreDocumentsService(db).get(entity_id)

@router.post("/mes_vector_store_documents", response_model=MesVectorStoreDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_vector_store_documents(
    data: MesVectorStoreDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesVectorStoreDocumentsService(db).create(data)

@router.put("/mes_vector_store_documents/{entity_id}", response_model=MesVectorStoreDocumentsOut)
async def update_mes_vector_store_documents(
    entity_id: uuid.UUID,
    data: MesVectorStoreDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesVectorStoreDocumentsService(db).update(entity_id, data)

@router.delete("/mes_vector_store_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_vector_store_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesVectorStoreDocumentsService(db).delete(entity_id)

@router.get("/mes_work_center_calendars", response_model=PaginatedResponse[MesWorkCenterCalendarsOut])
async def list_mes_work_center_calendars(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkCenterCalendarsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_center_calendars/{entity_id}", response_model=MesWorkCenterCalendarsOut)
async def get_mes_work_center_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkCenterCalendarsService(db).get(entity_id)

@router.post("/mes_work_center_calendars", response_model=MesWorkCenterCalendarsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_center_calendars(
    data: MesWorkCenterCalendarsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterCalendarsService(db).create(data)

@router.put("/mes_work_center_calendars/{entity_id}", response_model=MesWorkCenterCalendarsOut)
async def update_mes_work_center_calendars(
    entity_id: uuid.UUID,
    data: MesWorkCenterCalendarsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterCalendarsService(db).update(entity_id, data)

@router.delete("/mes_work_center_calendars/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_center_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkCenterCalendarsService(db).delete(entity_id)

@router.get("/mes_work_center_capacities", response_model=PaginatedResponse[MesWorkCenterCapacitiesOut])
async def list_mes_work_center_capacities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkCenterCapacitiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_center_capacities/{entity_id}", response_model=MesWorkCenterCapacitiesOut)
async def get_mes_work_center_capacities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkCenterCapacitiesService(db).get(entity_id)

@router.post("/mes_work_center_capacities", response_model=MesWorkCenterCapacitiesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_center_capacities(
    data: MesWorkCenterCapacitiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterCapacitiesService(db).create(data)

@router.put("/mes_work_center_capacities/{entity_id}", response_model=MesWorkCenterCapacitiesOut)
async def update_mes_work_center_capacities(
    entity_id: uuid.UUID,
    data: MesWorkCenterCapacitiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterCapacitiesService(db).update(entity_id, data)

@router.delete("/mes_work_center_capacities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_center_capacities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkCenterCapacitiesService(db).delete(entity_id)

@router.get("/mes_work_center_constraints", response_model=PaginatedResponse[MesWorkCenterConstraintsOut])
async def list_mes_work_center_constraints(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkCenterConstraintsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["constraint_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_center_constraints/{entity_id}", response_model=MesWorkCenterConstraintsOut)
async def get_mes_work_center_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkCenterConstraintsService(db).get(entity_id)

@router.post("/mes_work_center_constraints", response_model=MesWorkCenterConstraintsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_center_constraints(
    data: MesWorkCenterConstraintsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterConstraintsService(db).create(data)

@router.put("/mes_work_center_constraints/{entity_id}", response_model=MesWorkCenterConstraintsOut)
async def update_mes_work_center_constraints(
    entity_id: uuid.UUID,
    data: MesWorkCenterConstraintsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterConstraintsService(db).update(entity_id, data)

@router.delete("/mes_work_center_constraints/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_center_constraints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkCenterConstraintsService(db).delete(entity_id)

@router.get("/mes_work_center_types", response_model=PaginatedResponse[MesWorkCenterTypesOut])
async def list_mes_work_center_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkCenterTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_center_types/{entity_id}", response_model=MesWorkCenterTypesOut)
async def get_mes_work_center_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkCenterTypesService(db).get(entity_id)

@router.post("/mes_work_center_types", response_model=MesWorkCenterTypesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_center_types(
    data: MesWorkCenterTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterTypesService(db).create(data)

@router.put("/mes_work_center_types/{entity_id}", response_model=MesWorkCenterTypesOut)
async def update_mes_work_center_types(
    entity_id: uuid.UUID,
    data: MesWorkCenterTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCenterTypesService(db).update(entity_id, data)

@router.delete("/mes_work_center_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_center_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkCenterTypesService(db).delete(entity_id)

@router.get("/mes_work_centers", response_model=PaginatedResponse[MesWorkCentersOut])
async def list_mes_work_centers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkCentersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["center_code", "center_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_centers/{entity_id}", response_model=MesWorkCentersOut)
async def get_mes_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkCentersService(db).get(entity_id)

@router.post("/mes_work_centers", response_model=MesWorkCentersOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_centers(
    data: MesWorkCentersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCentersService(db).create(data)

@router.put("/mes_work_centers/{entity_id}", response_model=MesWorkCentersOut)
async def update_mes_work_centers(
    entity_id: uuid.UUID,
    data: MesWorkCentersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkCentersService(db).update(entity_id, data)

@router.delete("/mes_work_centers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkCentersService(db).delete(entity_id)

@router.get("/mes_work_order_execution", response_model=PaginatedResponse[MesWorkOrderExecutionOut])
async def list_mes_work_order_execution(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkOrderExecutionService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["work_order_number", "product_code", "product_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_order_execution/{entity_id}", response_model=MesWorkOrderExecutionOut)
async def get_mes_work_order_execution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkOrderExecutionService(db).get(entity_id)

@router.post("/mes_work_order_execution", response_model=MesWorkOrderExecutionOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_order_execution(
    data: MesWorkOrderExecutionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderExecutionService(db).create(data)

@router.put("/mes_work_order_execution/{entity_id}", response_model=MesWorkOrderExecutionOut)
async def update_mes_work_order_execution(
    entity_id: uuid.UUID,
    data: MesWorkOrderExecutionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderExecutionService(db).update(entity_id, data)

@router.delete("/mes_work_order_execution/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_order_execution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkOrderExecutionService(db).delete(entity_id)

@router.get("/mes_work_order_holds", response_model=PaginatedResponse[MesWorkOrderHoldsOut])
async def list_mes_work_order_holds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkOrderHoldsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_order_holds/{entity_id}", response_model=MesWorkOrderHoldsOut)
async def get_mes_work_order_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkOrderHoldsService(db).get(entity_id)

@router.post("/mes_work_order_holds", response_model=MesWorkOrderHoldsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_order_holds(
    data: MesWorkOrderHoldsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderHoldsService(db).create(data)

@router.put("/mes_work_order_holds/{entity_id}", response_model=MesWorkOrderHoldsOut)
async def update_mes_work_order_holds(
    entity_id: uuid.UUID,
    data: MesWorkOrderHoldsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderHoldsService(db).update(entity_id, data)

@router.delete("/mes_work_order_holds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_order_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkOrderHoldsService(db).delete(entity_id)

@router.get("/mes_work_order_signatures", response_model=PaginatedResponse[MesWorkOrderSignaturesOut])
async def list_mes_work_order_signatures(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkOrderSignaturesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_work_order_signatures/{entity_id}", response_model=MesWorkOrderSignaturesOut)
async def get_mes_work_order_signatures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkOrderSignaturesService(db).get(entity_id)

@router.post("/mes_work_order_signatures", response_model=MesWorkOrderSignaturesOut, status_code=status.HTTP_201_CREATED)
async def create_mes_work_order_signatures(
    data: MesWorkOrderSignaturesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderSignaturesService(db).create(data)

@router.put("/mes_work_order_signatures/{entity_id}", response_model=MesWorkOrderSignaturesOut)
async def update_mes_work_order_signatures(
    entity_id: uuid.UUID,
    data: MesWorkOrderSignaturesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkOrderSignaturesService(db).update(entity_id, data)

@router.delete("/mes_work_order_signatures/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_work_order_signatures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkOrderSignaturesService(db).delete(entity_id)

@router.get("/mes_workflow_definitions", response_model=PaginatedResponse[MesWorkflowDefinitionsOut])
async def list_mes_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_workflow_definitions/{entity_id}", response_model=MesWorkflowDefinitionsOut)
async def get_mes_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkflowDefinitionsService(db).get(entity_id)

@router.post("/mes_workflow_definitions", response_model=MesWorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_workflow_definitions(
    data: MesWorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkflowDefinitionsService(db).create(data)

@router.put("/mes_workflow_definitions/{entity_id}", response_model=MesWorkflowDefinitionsOut)
async def update_mes_workflow_definitions(
    entity_id: uuid.UUID,
    data: MesWorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/mes_workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkflowDefinitionsService(db).delete(entity_id)

@router.get("/mes_workflow_executions", response_model=PaginatedResponse[MesWorkflowExecutionsOut])
async def list_mes_workflow_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = MesWorkflowExecutionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mes_workflow_executions/{entity_id}", response_model=MesWorkflowExecutionsOut)
async def get_mes_workflow_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await MesWorkflowExecutionsService(db).get(entity_id)

@router.post("/mes_workflow_executions", response_model=MesWorkflowExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_mes_workflow_executions(
    data: MesWorkflowExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkflowExecutionsService(db).create(data)

@router.put("/mes_workflow_executions/{entity_id}", response_model=MesWorkflowExecutionsOut)
async def update_mes_workflow_executions(
    entity_id: uuid.UUID,
    data: MesWorkflowExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await MesWorkflowExecutionsService(db).update(entity_id, data)

@router.delete("/mes_workflow_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mes_workflow_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await MesWorkflowExecutionsService(db).delete(entity_id)

@router.get("/work_centers", response_model=PaginatedResponse[WorkCentersOut])
async def list_work_centers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    svc = WorkCentersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["center_code", "center_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/work_centers/{entity_id}", response_model=WorkCentersOut)
async def get_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "view"),
):
    return await WorkCentersService(db).get(entity_id)

@router.post("/work_centers", response_model=WorkCentersOut, status_code=status.HTTP_201_CREATED)
async def create_work_centers(
    data: WorkCentersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await WorkCentersService(db).create(data)

@router.put("/work_centers/{entity_id}", response_model=WorkCentersOut)
async def update_work_centers(
    entity_id: uuid.UUID,
    data: WorkCentersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    return await WorkCentersService(db).update(entity_id, data)

@router.delete("/work_centers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("mes", "manage"),
):
    await WorkCentersService(db).delete(entity_id)
