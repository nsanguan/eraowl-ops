import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.qc.services import (
    AiAgentLogsService,
    AiDecisionsService,
    AiModelRegistryService,
    AiWorkflowStateService,
    InspectionChecklistService,
    InspectionOrdersService,
    InspectionPlansService,
    InspectionResultsService,
    QcAgentDefinitionsService,
    QcAlgorithmsService,
    QcAuditFindingsService,
    QcAuditsService,
    QcCapaActionsService,
    QcCapaHeadersService,
    QcCharacteristicValueSetsService,
    QcCharacteristicsService,
    QcComplaintInvestigationsService,
    QcControlPlanCharacteristicsService,
    QcControlPlansService,
    QcCostOfQualityService,
    QcCustomerComplaintsService,
    QcDefectMasterService,
    QcDefectOccurrencesService,
    QcDocumentsService,
    QcEquipmentCalibrationService,
    QcFailureAnalysisService,
    QcFmeaActionsService,
    QcFmeaHeadersService,
    QcFmeaItemsService,
    QcHoldsService,
    QcInspectionEquipmentService,
    QcInspectionLotsService,
    QcInspectionRoutesService,
    QcInspectionsService,
    QcIntegrationConnectionsService,
    QcIntegrationLogsService,
    QcKpiActualsService,
    QcKpiDefinitionsService,
    QcLanggraphExecutionsService,
    QcLanggraphStatesService,
    QcLanggraphWorkflowsService,
    QcLlmConfigsService,
    QcLotDispositionsService,
    QcMlModelsService,
    QcMsaMeasurementsService,
    QcMsaStudiesService,
    QcNcrAttachmentsService,
    QcNcrContainmentService,
    QcNcrHeadersService,
    QcNotificationsService,
    QcOptimizationProblemsService,
    QcOrtoolsProblemsService,
    QcPlanAttachmentsService,
    QcPlanElementsService,
    QcPlanTriggersService,
    QcPlansService,
    QcPpapSubmissionsService,
    QcPredictionsService,
    QcPromptTemplatesService,
    QcRootCauseAnalysisService,
    QcRootCauseCausesService,
    QcSampleContainersService,
    QcSamplePackingResultsService,
    QcSamplingPlanLinesService,
    QcSamplingPlansService,
    QcScenariosService,
    QcScipyAnalysesService,
    QcSolverConfigsService,
    QcSpcAlertsService,
    QcSpcChartsService,
    QcSpcDataPointsService,
    QcSpecLimitsService,
    QcSpecsService,
    QcSupplierProfilesService,
    QcSupplierScorecardsService,
    QcTestEquipmentService,
    QcTestMethodsService,
    QcTestResultLinesService,
    QcTestResultsService,
    QcTrainingAttendeesService,
    QcTrainingCoursesService,
    QcVectorDocumentsService,
)
from app.modules.qc.schemas import (
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiModelRegistryCreate,
    AiModelRegistryUpdate,
    AiModelRegistryOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    InspectionChecklistCreate,
    InspectionChecklistUpdate,
    InspectionChecklistOut,
    InspectionOrdersCreate,
    InspectionOrdersUpdate,
    InspectionOrdersOut,
    InspectionPlansCreate,
    InspectionPlansUpdate,
    InspectionPlansOut,
    InspectionResultsCreate,
    InspectionResultsUpdate,
    InspectionResultsOut,
    QcAgentDefinitionsCreate,
    QcAgentDefinitionsUpdate,
    QcAgentDefinitionsOut,
    QcAlgorithmsCreate,
    QcAlgorithmsUpdate,
    QcAlgorithmsOut,
    QcAuditFindingsCreate,
    QcAuditFindingsUpdate,
    QcAuditFindingsOut,
    QcAuditsCreate,
    QcAuditsUpdate,
    QcAuditsOut,
    QcCapaActionsCreate,
    QcCapaActionsUpdate,
    QcCapaActionsOut,
    QcCapaHeadersCreate,
    QcCapaHeadersUpdate,
    QcCapaHeadersOut,
    QcCharacteristicValueSetsCreate,
    QcCharacteristicValueSetsUpdate,
    QcCharacteristicValueSetsOut,
    QcCharacteristicsCreate,
    QcCharacteristicsUpdate,
    QcCharacteristicsOut,
    QcComplaintInvestigationsCreate,
    QcComplaintInvestigationsUpdate,
    QcComplaintInvestigationsOut,
    QcControlPlanCharacteristicsCreate,
    QcControlPlanCharacteristicsUpdate,
    QcControlPlanCharacteristicsOut,
    QcControlPlansCreate,
    QcControlPlansUpdate,
    QcControlPlansOut,
    QcCostOfQualityCreate,
    QcCostOfQualityUpdate,
    QcCostOfQualityOut,
    QcCustomerComplaintsCreate,
    QcCustomerComplaintsUpdate,
    QcCustomerComplaintsOut,
    QcDefectMasterCreate,
    QcDefectMasterUpdate,
    QcDefectMasterOut,
    QcDefectOccurrencesCreate,
    QcDefectOccurrencesUpdate,
    QcDefectOccurrencesOut,
    QcDocumentsCreate,
    QcDocumentsUpdate,
    QcDocumentsOut,
    QcEquipmentCalibrationCreate,
    QcEquipmentCalibrationUpdate,
    QcEquipmentCalibrationOut,
    QcFailureAnalysisCreate,
    QcFailureAnalysisUpdate,
    QcFailureAnalysisOut,
    QcFmeaActionsCreate,
    QcFmeaActionsUpdate,
    QcFmeaActionsOut,
    QcFmeaHeadersCreate,
    QcFmeaHeadersUpdate,
    QcFmeaHeadersOut,
    QcFmeaItemsCreate,
    QcFmeaItemsUpdate,
    QcFmeaItemsOut,
    QcHoldsCreate,
    QcHoldsUpdate,
    QcHoldsOut,
    QcInspectionEquipmentCreate,
    QcInspectionEquipmentUpdate,
    QcInspectionEquipmentOut,
    QcInspectionLotsCreate,
    QcInspectionLotsUpdate,
    QcInspectionLotsOut,
    QcInspectionRoutesCreate,
    QcInspectionRoutesUpdate,
    QcInspectionRoutesOut,
    QcInspectionsCreate,
    QcInspectionsUpdate,
    QcInspectionsOut,
    QcIntegrationConnectionsCreate,
    QcIntegrationConnectionsUpdate,
    QcIntegrationConnectionsOut,
    QcIntegrationLogsCreate,
    QcIntegrationLogsUpdate,
    QcIntegrationLogsOut,
    QcKpiActualsCreate,
    QcKpiActualsUpdate,
    QcKpiActualsOut,
    QcKpiDefinitionsCreate,
    QcKpiDefinitionsUpdate,
    QcKpiDefinitionsOut,
    QcLanggraphExecutionsCreate,
    QcLanggraphExecutionsUpdate,
    QcLanggraphExecutionsOut,
    QcLanggraphStatesCreate,
    QcLanggraphStatesUpdate,
    QcLanggraphStatesOut,
    QcLanggraphWorkflowsCreate,
    QcLanggraphWorkflowsUpdate,
    QcLanggraphWorkflowsOut,
    QcLlmConfigsCreate,
    QcLlmConfigsUpdate,
    QcLlmConfigsOut,
    QcLotDispositionsCreate,
    QcLotDispositionsUpdate,
    QcLotDispositionsOut,
    QcMlModelsCreate,
    QcMlModelsUpdate,
    QcMlModelsOut,
    QcMsaMeasurementsCreate,
    QcMsaMeasurementsUpdate,
    QcMsaMeasurementsOut,
    QcMsaStudiesCreate,
    QcMsaStudiesUpdate,
    QcMsaStudiesOut,
    QcNcrAttachmentsCreate,
    QcNcrAttachmentsUpdate,
    QcNcrAttachmentsOut,
    QcNcrContainmentCreate,
    QcNcrContainmentUpdate,
    QcNcrContainmentOut,
    QcNcrHeadersCreate,
    QcNcrHeadersUpdate,
    QcNcrHeadersOut,
    QcNotificationsCreate,
    QcNotificationsUpdate,
    QcNotificationsOut,
    QcOptimizationProblemsCreate,
    QcOptimizationProblemsUpdate,
    QcOptimizationProblemsOut,
    QcOrtoolsProblemsCreate,
    QcOrtoolsProblemsUpdate,
    QcOrtoolsProblemsOut,
    QcPlanAttachmentsCreate,
    QcPlanAttachmentsUpdate,
    QcPlanAttachmentsOut,
    QcPlanElementsCreate,
    QcPlanElementsUpdate,
    QcPlanElementsOut,
    QcPlanTriggersCreate,
    QcPlanTriggersUpdate,
    QcPlanTriggersOut,
    QcPlansCreate,
    QcPlansUpdate,
    QcPlansOut,
    QcPpapSubmissionsCreate,
    QcPpapSubmissionsUpdate,
    QcPpapSubmissionsOut,
    QcPredictionsCreate,
    QcPredictionsUpdate,
    QcPredictionsOut,
    QcPromptTemplatesCreate,
    QcPromptTemplatesUpdate,
    QcPromptTemplatesOut,
    QcRootCauseAnalysisCreate,
    QcRootCauseAnalysisUpdate,
    QcRootCauseAnalysisOut,
    QcRootCauseCausesCreate,
    QcRootCauseCausesUpdate,
    QcRootCauseCausesOut,
    QcSampleContainersCreate,
    QcSampleContainersUpdate,
    QcSampleContainersOut,
    QcSamplePackingResultsCreate,
    QcSamplePackingResultsUpdate,
    QcSamplePackingResultsOut,
    QcSamplingPlanLinesCreate,
    QcSamplingPlanLinesUpdate,
    QcSamplingPlanLinesOut,
    QcSamplingPlansCreate,
    QcSamplingPlansUpdate,
    QcSamplingPlansOut,
    QcScenariosCreate,
    QcScenariosUpdate,
    QcScenariosOut,
    QcScipyAnalysesCreate,
    QcScipyAnalysesUpdate,
    QcScipyAnalysesOut,
    QcSolverConfigsCreate,
    QcSolverConfigsUpdate,
    QcSolverConfigsOut,
    QcSpcAlertsCreate,
    QcSpcAlertsUpdate,
    QcSpcAlertsOut,
    QcSpcChartsCreate,
    QcSpcChartsUpdate,
    QcSpcChartsOut,
    QcSpcDataPointsCreate,
    QcSpcDataPointsUpdate,
    QcSpcDataPointsOut,
    QcSpecLimitsCreate,
    QcSpecLimitsUpdate,
    QcSpecLimitsOut,
    QcSpecsCreate,
    QcSpecsUpdate,
    QcSpecsOut,
    QcSupplierProfilesCreate,
    QcSupplierProfilesUpdate,
    QcSupplierProfilesOut,
    QcSupplierScorecardsCreate,
    QcSupplierScorecardsUpdate,
    QcSupplierScorecardsOut,
    QcTestEquipmentCreate,
    QcTestEquipmentUpdate,
    QcTestEquipmentOut,
    QcTestMethodsCreate,
    QcTestMethodsUpdate,
    QcTestMethodsOut,
    QcTestResultLinesCreate,
    QcTestResultLinesUpdate,
    QcTestResultLinesOut,
    QcTestResultsCreate,
    QcTestResultsUpdate,
    QcTestResultsOut,
    QcTrainingAttendeesCreate,
    QcTrainingAttendeesUpdate,
    QcTrainingAttendeesOut,
    QcTrainingCoursesCreate,
    QcTrainingCoursesUpdate,
    QcTrainingCoursesOut,
    QcVectorDocumentsCreate,
    QcVectorDocumentsUpdate,
    QcVectorDocumentsOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = AiAgentLogsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["agent_name", "log_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["decision_code", "decision_type_code", "decision_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_model_registry", response_model=PaginatedResponse[AiModelRegistryOut])
async def list_ai_model_registry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = AiModelRegistryService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name", "model_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_model_registry/{entity_id}", response_model=AiModelRegistryOut)
async def get_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await AiModelRegistryService(db).get(entity_id)

@router.post("/ai_model_registry", response_model=AiModelRegistryOut, status_code=status.HTTP_201_CREATED)
async def create_ai_model_registry(
    data: AiModelRegistryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiModelRegistryService(db).create(data)

@router.put("/ai_model_registry/{entity_id}", response_model=AiModelRegistryOut)
async def update_ai_model_registry(
    entity_id: uuid.UUID,
    data: AiModelRegistryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiModelRegistryService(db).update(entity_id, data)

@router.delete("/ai_model_registry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await AiModelRegistryService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = AiWorkflowStateService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_name", "workflow_type_code", "workflow_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/inspection_checklist", response_model=PaginatedResponse[InspectionChecklistOut])
async def list_inspection_checklist(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = InspectionChecklistService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["parameter_name", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_checklist/{entity_id}", response_model=InspectionChecklistOut)
async def get_inspection_checklist(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await InspectionChecklistService(db).get(entity_id)

@router.post("/inspection_checklist", response_model=InspectionChecklistOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_checklist(
    data: InspectionChecklistCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionChecklistService(db).create(data)

@router.put("/inspection_checklist/{entity_id}", response_model=InspectionChecklistOut)
async def update_inspection_checklist(
    entity_id: uuid.UUID,
    data: InspectionChecklistUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionChecklistService(db).update(entity_id, data)

@router.delete("/inspection_checklist/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_checklist(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await InspectionChecklistService(db).delete(entity_id)

@router.get("/inspection_orders", response_model=PaginatedResponse[InspectionOrdersOut])
async def list_inspection_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = InspectionOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_orders/{entity_id}", response_model=InspectionOrdersOut)
async def get_inspection_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await InspectionOrdersService(db).get(entity_id)

@router.post("/inspection_orders", response_model=InspectionOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_orders(
    data: InspectionOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionOrdersService(db).create(data)

@router.put("/inspection_orders/{entity_id}", response_model=InspectionOrdersOut)
async def update_inspection_orders(
    entity_id: uuid.UUID,
    data: InspectionOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionOrdersService(db).update(entity_id, data)

@router.delete("/inspection_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await InspectionOrdersService(db).delete(entity_id)

@router.get("/inspection_plans", response_model=PaginatedResponse[InspectionPlansOut])
async def list_inspection_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = InspectionPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_plans/{entity_id}", response_model=InspectionPlansOut)
async def get_inspection_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await InspectionPlansService(db).get(entity_id)

@router.post("/inspection_plans", response_model=InspectionPlansOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_plans(
    data: InspectionPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionPlansService(db).create(data)

@router.put("/inspection_plans/{entity_id}", response_model=InspectionPlansOut)
async def update_inspection_plans(
    entity_id: uuid.UUID,
    data: InspectionPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionPlansService(db).update(entity_id, data)

@router.delete("/inspection_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await InspectionPlansService(db).delete(entity_id)

@router.get("/inspection_results", response_model=PaginatedResponse[InspectionResultsOut])
async def list_inspection_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = InspectionResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_results/{entity_id}", response_model=InspectionResultsOut)
async def get_inspection_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await InspectionResultsService(db).get(entity_id)

@router.post("/inspection_results", response_model=InspectionResultsOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_results(
    data: InspectionResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionResultsService(db).create(data)

@router.put("/inspection_results/{entity_id}", response_model=InspectionResultsOut)
async def update_inspection_results(
    entity_id: uuid.UUID,
    data: InspectionResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await InspectionResultsService(db).update(entity_id, data)

@router.delete("/inspection_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await InspectionResultsService(db).delete(entity_id)

@router.get("/qc_agent_definitions", response_model=PaginatedResponse[QcAgentDefinitionsOut])
async def list_qc_agent_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcAgentDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["agent_code", "agent_name", "agent_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_agent_definitions/{entity_id}", response_model=QcAgentDefinitionsOut)
async def get_qc_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcAgentDefinitionsService(db).get(entity_id)

@router.post("/qc_agent_definitions", response_model=QcAgentDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_agent_definitions(
    data: QcAgentDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAgentDefinitionsService(db).create(data)

@router.put("/qc_agent_definitions/{entity_id}", response_model=QcAgentDefinitionsOut)
async def update_qc_agent_definitions(
    entity_id: uuid.UUID,
    data: QcAgentDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAgentDefinitionsService(db).update(entity_id, data)

@router.delete("/qc_agent_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcAgentDefinitionsService(db).delete(entity_id)

@router.get("/qc_algorithms", response_model=PaginatedResponse[QcAlgorithmsOut])
async def list_qc_algorithms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcAlgorithmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["algorithm_code", "algorithm_name", "algorithm_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_algorithms/{entity_id}", response_model=QcAlgorithmsOut)
async def get_qc_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcAlgorithmsService(db).get(entity_id)

@router.post("/qc_algorithms", response_model=QcAlgorithmsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_algorithms(
    data: QcAlgorithmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAlgorithmsService(db).create(data)

@router.put("/qc_algorithms/{entity_id}", response_model=QcAlgorithmsOut)
async def update_qc_algorithms(
    entity_id: uuid.UUID,
    data: QcAlgorithmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAlgorithmsService(db).update(entity_id, data)

@router.delete("/qc_algorithms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcAlgorithmsService(db).delete(entity_id)

@router.get("/qc_audit_findings", response_model=PaginatedResponse[QcAuditFindingsOut])
async def list_qc_audit_findings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcAuditFindingsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["finding_number", "finding_type_code", "finding_severity_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_audit_findings/{entity_id}", response_model=QcAuditFindingsOut)
async def get_qc_audit_findings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcAuditFindingsService(db).get(entity_id)

@router.post("/qc_audit_findings", response_model=QcAuditFindingsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_audit_findings(
    data: QcAuditFindingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAuditFindingsService(db).create(data)

@router.put("/qc_audit_findings/{entity_id}", response_model=QcAuditFindingsOut)
async def update_qc_audit_findings(
    entity_id: uuid.UUID,
    data: QcAuditFindingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAuditFindingsService(db).update(entity_id, data)

@router.delete("/qc_audit_findings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_audit_findings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcAuditFindingsService(db).delete(entity_id)

@router.get("/qc_audits", response_model=PaginatedResponse[QcAuditsOut])
async def list_qc_audits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcAuditsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["audit_number", "audit_title", "audit_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_audits/{entity_id}", response_model=QcAuditsOut)
async def get_qc_audits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcAuditsService(db).get(entity_id)

@router.post("/qc_audits", response_model=QcAuditsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_audits(
    data: QcAuditsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAuditsService(db).create(data)

@router.put("/qc_audits/{entity_id}", response_model=QcAuditsOut)
async def update_qc_audits(
    entity_id: uuid.UUID,
    data: QcAuditsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcAuditsService(db).update(entity_id, data)

@router.delete("/qc_audits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_audits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcAuditsService(db).delete(entity_id)

@router.get("/qc_capa_actions", response_model=PaginatedResponse[QcCapaActionsOut])
async def list_qc_capa_actions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCapaActionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["action_type_code", "action_description", "action_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_capa_actions/{entity_id}", response_model=QcCapaActionsOut)
async def get_qc_capa_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCapaActionsService(db).get(entity_id)

@router.post("/qc_capa_actions", response_model=QcCapaActionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_capa_actions(
    data: QcCapaActionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCapaActionsService(db).create(data)

@router.put("/qc_capa_actions/{entity_id}", response_model=QcCapaActionsOut)
async def update_qc_capa_actions(
    entity_id: uuid.UUID,
    data: QcCapaActionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCapaActionsService(db).update(entity_id, data)

@router.delete("/qc_capa_actions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_capa_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCapaActionsService(db).delete(entity_id)

@router.get("/qc_capa_headers", response_model=PaginatedResponse[QcCapaHeadersOut])
async def list_qc_capa_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCapaHeadersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["capa_number", "capa_title", "capa_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_capa_headers/{entity_id}", response_model=QcCapaHeadersOut)
async def get_qc_capa_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCapaHeadersService(db).get(entity_id)

@router.post("/qc_capa_headers", response_model=QcCapaHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_qc_capa_headers(
    data: QcCapaHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCapaHeadersService(db).create(data)

@router.put("/qc_capa_headers/{entity_id}", response_model=QcCapaHeadersOut)
async def update_qc_capa_headers(
    entity_id: uuid.UUID,
    data: QcCapaHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCapaHeadersService(db).update(entity_id, data)

@router.delete("/qc_capa_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_capa_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCapaHeadersService(db).delete(entity_id)

@router.get("/qc_characteristic_value_sets", response_model=PaginatedResponse[QcCharacteristicValueSetsOut])
async def list_qc_characteristic_value_sets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCharacteristicValueSetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["value_code", "value_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_characteristic_value_sets/{entity_id}", response_model=QcCharacteristicValueSetsOut)
async def get_qc_characteristic_value_sets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCharacteristicValueSetsService(db).get(entity_id)

@router.post("/qc_characteristic_value_sets", response_model=QcCharacteristicValueSetsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_characteristic_value_sets(
    data: QcCharacteristicValueSetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCharacteristicValueSetsService(db).create(data)

@router.put("/qc_characteristic_value_sets/{entity_id}", response_model=QcCharacteristicValueSetsOut)
async def update_qc_characteristic_value_sets(
    entity_id: uuid.UUID,
    data: QcCharacteristicValueSetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCharacteristicValueSetsService(db).update(entity_id, data)

@router.delete("/qc_characteristic_value_sets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_characteristic_value_sets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCharacteristicValueSetsService(db).delete(entity_id)

@router.get("/qc_characteristics", response_model=PaginatedResponse[QcCharacteristicsOut])
async def list_qc_characteristics(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCharacteristicsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["characteristic_code", "characteristic_name", "characteristic_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_characteristics/{entity_id}", response_model=QcCharacteristicsOut)
async def get_qc_characteristics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCharacteristicsService(db).get(entity_id)

@router.post("/qc_characteristics", response_model=QcCharacteristicsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_characteristics(
    data: QcCharacteristicsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCharacteristicsService(db).create(data)

@router.put("/qc_characteristics/{entity_id}", response_model=QcCharacteristicsOut)
async def update_qc_characteristics(
    entity_id: uuid.UUID,
    data: QcCharacteristicsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCharacteristicsService(db).update(entity_id, data)

@router.delete("/qc_characteristics/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_characteristics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCharacteristicsService(db).delete(entity_id)

@router.get("/qc_complaint_investigations", response_model=PaginatedResponse[QcComplaintInvestigationsOut])
async def list_qc_complaint_investigations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcComplaintInvestigationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["investigation_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_complaint_investigations/{entity_id}", response_model=QcComplaintInvestigationsOut)
async def get_qc_complaint_investigations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcComplaintInvestigationsService(db).get(entity_id)

@router.post("/qc_complaint_investigations", response_model=QcComplaintInvestigationsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_complaint_investigations(
    data: QcComplaintInvestigationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcComplaintInvestigationsService(db).create(data)

@router.put("/qc_complaint_investigations/{entity_id}", response_model=QcComplaintInvestigationsOut)
async def update_qc_complaint_investigations(
    entity_id: uuid.UUID,
    data: QcComplaintInvestigationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcComplaintInvestigationsService(db).update(entity_id, data)

@router.delete("/qc_complaint_investigations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_complaint_investigations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcComplaintInvestigationsService(db).delete(entity_id)

@router.get("/qc_control_plan_characteristics", response_model=PaginatedResponse[QcControlPlanCharacteristicsOut])
async def list_qc_control_plan_characteristics(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcControlPlanCharacteristicsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["operation_code", "process_step_code", "characteristic_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_control_plan_characteristics/{entity_id}", response_model=QcControlPlanCharacteristicsOut)
async def get_qc_control_plan_characteristics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcControlPlanCharacteristicsService(db).get(entity_id)

@router.post("/qc_control_plan_characteristics", response_model=QcControlPlanCharacteristicsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_control_plan_characteristics(
    data: QcControlPlanCharacteristicsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcControlPlanCharacteristicsService(db).create(data)

@router.put("/qc_control_plan_characteristics/{entity_id}", response_model=QcControlPlanCharacteristicsOut)
async def update_qc_control_plan_characteristics(
    entity_id: uuid.UUID,
    data: QcControlPlanCharacteristicsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcControlPlanCharacteristicsService(db).update(entity_id, data)

@router.delete("/qc_control_plan_characteristics/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_control_plan_characteristics(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcControlPlanCharacteristicsService(db).delete(entity_id)

@router.get("/qc_control_plans", response_model=PaginatedResponse[QcControlPlansOut])
async def list_qc_control_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcControlPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["control_plan_number", "control_plan_title", "control_plan_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_control_plans/{entity_id}", response_model=QcControlPlansOut)
async def get_qc_control_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcControlPlansService(db).get(entity_id)

@router.post("/qc_control_plans", response_model=QcControlPlansOut, status_code=status.HTTP_201_CREATED)
async def create_qc_control_plans(
    data: QcControlPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcControlPlansService(db).create(data)

@router.put("/qc_control_plans/{entity_id}", response_model=QcControlPlansOut)
async def update_qc_control_plans(
    entity_id: uuid.UUID,
    data: QcControlPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcControlPlansService(db).update(entity_id, data)

@router.delete("/qc_control_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_control_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcControlPlansService(db).delete(entity_id)

@router.get("/qc_cost_of_quality", response_model=PaginatedResponse[QcCostOfQualityOut])
async def list_qc_cost_of_quality(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCostOfQualityService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["coq_number", "coq_category_code", "coq_item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_cost_of_quality/{entity_id}", response_model=QcCostOfQualityOut)
async def get_qc_cost_of_quality(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCostOfQualityService(db).get(entity_id)

@router.post("/qc_cost_of_quality", response_model=QcCostOfQualityOut, status_code=status.HTTP_201_CREATED)
async def create_qc_cost_of_quality(
    data: QcCostOfQualityCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCostOfQualityService(db).create(data)

@router.put("/qc_cost_of_quality/{entity_id}", response_model=QcCostOfQualityOut)
async def update_qc_cost_of_quality(
    entity_id: uuid.UUID,
    data: QcCostOfQualityUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCostOfQualityService(db).update(entity_id, data)

@router.delete("/qc_cost_of_quality/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_cost_of_quality(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCostOfQualityService(db).delete(entity_id)

@router.get("/qc_customer_complaints", response_model=PaginatedResponse[QcCustomerComplaintsOut])
async def list_qc_customer_complaints(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcCustomerComplaintsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["complaint_number", "complaint_title", "complaint_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_customer_complaints/{entity_id}", response_model=QcCustomerComplaintsOut)
async def get_qc_customer_complaints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcCustomerComplaintsService(db).get(entity_id)

@router.post("/qc_customer_complaints", response_model=QcCustomerComplaintsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_customer_complaints(
    data: QcCustomerComplaintsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCustomerComplaintsService(db).create(data)

@router.put("/qc_customer_complaints/{entity_id}", response_model=QcCustomerComplaintsOut)
async def update_qc_customer_complaints(
    entity_id: uuid.UUID,
    data: QcCustomerComplaintsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcCustomerComplaintsService(db).update(entity_id, data)

@router.delete("/qc_customer_complaints/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_customer_complaints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcCustomerComplaintsService(db).delete(entity_id)

@router.get("/qc_defect_master", response_model=PaginatedResponse[QcDefectMasterOut])
async def list_qc_defect_master(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcDefectMasterService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["defect_code", "defect_name", "defect_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_defect_master/{entity_id}", response_model=QcDefectMasterOut)
async def get_qc_defect_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcDefectMasterService(db).get(entity_id)

@router.post("/qc_defect_master", response_model=QcDefectMasterOut, status_code=status.HTTP_201_CREATED)
async def create_qc_defect_master(
    data: QcDefectMasterCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDefectMasterService(db).create(data)

@router.put("/qc_defect_master/{entity_id}", response_model=QcDefectMasterOut)
async def update_qc_defect_master(
    entity_id: uuid.UUID,
    data: QcDefectMasterUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDefectMasterService(db).update(entity_id, data)

@router.delete("/qc_defect_master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_defect_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcDefectMasterService(db).delete(entity_id)

@router.get("/qc_defect_occurrences", response_model=PaginatedResponse[QcDefectOccurrencesOut])
async def list_qc_defect_occurrences(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcDefectOccurrencesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lot_number", "shift_code", "process_step_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_defect_occurrences/{entity_id}", response_model=QcDefectOccurrencesOut)
async def get_qc_defect_occurrences(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcDefectOccurrencesService(db).get(entity_id)

@router.post("/qc_defect_occurrences", response_model=QcDefectOccurrencesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_defect_occurrences(
    data: QcDefectOccurrencesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDefectOccurrencesService(db).create(data)

@router.put("/qc_defect_occurrences/{entity_id}", response_model=QcDefectOccurrencesOut)
async def update_qc_defect_occurrences(
    entity_id: uuid.UUID,
    data: QcDefectOccurrencesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDefectOccurrencesService(db).update(entity_id, data)

@router.delete("/qc_defect_occurrences/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_defect_occurrences(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcDefectOccurrencesService(db).delete(entity_id)

@router.get("/qc_documents", response_model=PaginatedResponse[QcDocumentsOut])
async def list_qc_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["document_number", "document_title", "document_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_documents/{entity_id}", response_model=QcDocumentsOut)
async def get_qc_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcDocumentsService(db).get(entity_id)

@router.post("/qc_documents", response_model=QcDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_documents(
    data: QcDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDocumentsService(db).create(data)

@router.put("/qc_documents/{entity_id}", response_model=QcDocumentsOut)
async def update_qc_documents(
    entity_id: uuid.UUID,
    data: QcDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcDocumentsService(db).update(entity_id, data)

@router.delete("/qc_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcDocumentsService(db).delete(entity_id)

@router.get("/qc_equipment_calibration", response_model=PaginatedResponse[QcEquipmentCalibrationOut])
async def list_qc_equipment_calibration(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcEquipmentCalibrationService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["calibration_number", "calibration_type_code", "calibration_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_equipment_calibration/{entity_id}", response_model=QcEquipmentCalibrationOut)
async def get_qc_equipment_calibration(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcEquipmentCalibrationService(db).get(entity_id)

@router.post("/qc_equipment_calibration", response_model=QcEquipmentCalibrationOut, status_code=status.HTTP_201_CREATED)
async def create_qc_equipment_calibration(
    data: QcEquipmentCalibrationCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcEquipmentCalibrationService(db).create(data)

@router.put("/qc_equipment_calibration/{entity_id}", response_model=QcEquipmentCalibrationOut)
async def update_qc_equipment_calibration(
    entity_id: uuid.UUID,
    data: QcEquipmentCalibrationUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcEquipmentCalibrationService(db).update(entity_id, data)

@router.delete("/qc_equipment_calibration/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_equipment_calibration(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcEquipmentCalibrationService(db).delete(entity_id)

@router.get("/qc_failure_analysis", response_model=PaginatedResponse[QcFailureAnalysisOut])
async def list_qc_failure_analysis(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcFailureAnalysisService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["fa_number", "fa_type_code", "fa_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_failure_analysis/{entity_id}", response_model=QcFailureAnalysisOut)
async def get_qc_failure_analysis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcFailureAnalysisService(db).get(entity_id)

@router.post("/qc_failure_analysis", response_model=QcFailureAnalysisOut, status_code=status.HTTP_201_CREATED)
async def create_qc_failure_analysis(
    data: QcFailureAnalysisCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFailureAnalysisService(db).create(data)

@router.put("/qc_failure_analysis/{entity_id}", response_model=QcFailureAnalysisOut)
async def update_qc_failure_analysis(
    entity_id: uuid.UUID,
    data: QcFailureAnalysisUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFailureAnalysisService(db).update(entity_id, data)

@router.delete("/qc_failure_analysis/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_failure_analysis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcFailureAnalysisService(db).delete(entity_id)

@router.get("/qc_fmea_actions", response_model=PaginatedResponse[QcFmeaActionsOut])
async def list_qc_fmea_actions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcFmeaActionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["action_description", "action_type_code", "action_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_fmea_actions/{entity_id}", response_model=QcFmeaActionsOut)
async def get_qc_fmea_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcFmeaActionsService(db).get(entity_id)

@router.post("/qc_fmea_actions", response_model=QcFmeaActionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_fmea_actions(
    data: QcFmeaActionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaActionsService(db).create(data)

@router.put("/qc_fmea_actions/{entity_id}", response_model=QcFmeaActionsOut)
async def update_qc_fmea_actions(
    entity_id: uuid.UUID,
    data: QcFmeaActionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaActionsService(db).update(entity_id, data)

@router.delete("/qc_fmea_actions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_fmea_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcFmeaActionsService(db).delete(entity_id)

@router.get("/qc_fmea_headers", response_model=PaginatedResponse[QcFmeaHeadersOut])
async def list_qc_fmea_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcFmeaHeadersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["fmea_number", "fmea_title", "fmea_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_fmea_headers/{entity_id}", response_model=QcFmeaHeadersOut)
async def get_qc_fmea_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcFmeaHeadersService(db).get(entity_id)

@router.post("/qc_fmea_headers", response_model=QcFmeaHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_qc_fmea_headers(
    data: QcFmeaHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaHeadersService(db).create(data)

@router.put("/qc_fmea_headers/{entity_id}", response_model=QcFmeaHeadersOut)
async def update_qc_fmea_headers(
    entity_id: uuid.UUID,
    data: QcFmeaHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaHeadersService(db).update(entity_id, data)

@router.delete("/qc_fmea_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_fmea_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcFmeaHeadersService(db).delete(entity_id)

@router.get("/qc_fmea_items", response_model=PaginatedResponse[QcFmeaItemsOut])
async def list_qc_fmea_items(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcFmeaItemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_fmea_items/{entity_id}", response_model=QcFmeaItemsOut)
async def get_qc_fmea_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcFmeaItemsService(db).get(entity_id)

@router.post("/qc_fmea_items", response_model=QcFmeaItemsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_fmea_items(
    data: QcFmeaItemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaItemsService(db).create(data)

@router.put("/qc_fmea_items/{entity_id}", response_model=QcFmeaItemsOut)
async def update_qc_fmea_items(
    entity_id: uuid.UUID,
    data: QcFmeaItemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcFmeaItemsService(db).update(entity_id, data)

@router.delete("/qc_fmea_items/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_fmea_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcFmeaItemsService(db).delete(entity_id)

@router.get("/qc_holds", response_model=PaginatedResponse[QcHoldsOut])
async def list_qc_holds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcHoldsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["hold_number", "hold_type_code", "hold_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_holds/{entity_id}", response_model=QcHoldsOut)
async def get_qc_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcHoldsService(db).get(entity_id)

@router.post("/qc_holds", response_model=QcHoldsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_holds(
    data: QcHoldsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcHoldsService(db).create(data)

@router.put("/qc_holds/{entity_id}", response_model=QcHoldsOut)
async def update_qc_holds(
    entity_id: uuid.UUID,
    data: QcHoldsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcHoldsService(db).update(entity_id, data)

@router.delete("/qc_holds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcHoldsService(db).delete(entity_id)

@router.get("/qc_inspection_equipment", response_model=PaginatedResponse[QcInspectionEquipmentOut])
async def list_qc_inspection_equipment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcInspectionEquipmentService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_inspection_equipment/{entity_id}", response_model=QcInspectionEquipmentOut)
async def get_qc_inspection_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcInspectionEquipmentService(db).get(entity_id)

@router.post("/qc_inspection_equipment", response_model=QcInspectionEquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_qc_inspection_equipment(
    data: QcInspectionEquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionEquipmentService(db).create(data)

@router.put("/qc_inspection_equipment/{entity_id}", response_model=QcInspectionEquipmentOut)
async def update_qc_inspection_equipment(
    entity_id: uuid.UUID,
    data: QcInspectionEquipmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionEquipmentService(db).update(entity_id, data)

@router.delete("/qc_inspection_equipment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_inspection_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcInspectionEquipmentService(db).delete(entity_id)

@router.get("/qc_inspection_lots", response_model=PaginatedResponse[QcInspectionLotsOut])
async def list_qc_inspection_lots(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcInspectionLotsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lot_number", "serial_number", "lot_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_inspection_lots/{entity_id}", response_model=QcInspectionLotsOut)
async def get_qc_inspection_lots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcInspectionLotsService(db).get(entity_id)

@router.post("/qc_inspection_lots", response_model=QcInspectionLotsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_inspection_lots(
    data: QcInspectionLotsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionLotsService(db).create(data)

@router.put("/qc_inspection_lots/{entity_id}", response_model=QcInspectionLotsOut)
async def update_qc_inspection_lots(
    entity_id: uuid.UUID,
    data: QcInspectionLotsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionLotsService(db).update(entity_id, data)

@router.delete("/qc_inspection_lots/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_inspection_lots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcInspectionLotsService(db).delete(entity_id)

@router.get("/qc_inspection_routes", response_model=PaginatedResponse[QcInspectionRoutesOut])
async def list_qc_inspection_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcInspectionRoutesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["route_name", "inspector_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_inspection_routes/{entity_id}", response_model=QcInspectionRoutesOut)
async def get_qc_inspection_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcInspectionRoutesService(db).get(entity_id)

@router.post("/qc_inspection_routes", response_model=QcInspectionRoutesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_inspection_routes(
    data: QcInspectionRoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionRoutesService(db).create(data)

@router.put("/qc_inspection_routes/{entity_id}", response_model=QcInspectionRoutesOut)
async def update_qc_inspection_routes(
    entity_id: uuid.UUID,
    data: QcInspectionRoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionRoutesService(db).update(entity_id, data)

@router.delete("/qc_inspection_routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_inspection_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcInspectionRoutesService(db).delete(entity_id)

@router.get("/qc_inspections", response_model=PaginatedResponse[QcInspectionsOut])
async def list_qc_inspections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcInspectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["inspection_number", "inspection_type_code", "source_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_inspections/{entity_id}", response_model=QcInspectionsOut)
async def get_qc_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcInspectionsService(db).get(entity_id)

@router.post("/qc_inspections", response_model=QcInspectionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_inspections(
    data: QcInspectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionsService(db).create(data)

@router.put("/qc_inspections/{entity_id}", response_model=QcInspectionsOut)
async def update_qc_inspections(
    entity_id: uuid.UUID,
    data: QcInspectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcInspectionsService(db).update(entity_id, data)

@router.delete("/qc_inspections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcInspectionsService(db).delete(entity_id)

@router.get("/qc_integration_connections", response_model=PaginatedResponse[QcIntegrationConnectionsOut])
async def list_qc_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcIntegrationConnectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["connection_code", "connection_name", "integration_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_integration_connections/{entity_id}", response_model=QcIntegrationConnectionsOut)
async def get_qc_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcIntegrationConnectionsService(db).get(entity_id)

@router.post("/qc_integration_connections", response_model=QcIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_integration_connections(
    data: QcIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcIntegrationConnectionsService(db).create(data)

@router.put("/qc_integration_connections/{entity_id}", response_model=QcIntegrationConnectionsOut)
async def update_qc_integration_connections(
    entity_id: uuid.UUID,
    data: QcIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/qc_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcIntegrationConnectionsService(db).delete(entity_id)

@router.get("/qc_integration_logs", response_model=PaginatedResponse[QcIntegrationLogsOut])
async def list_qc_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcIntegrationLogsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["log_type_code", "log_status_code", "direction_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_integration_logs/{entity_id}", response_model=QcIntegrationLogsOut)
async def get_qc_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcIntegrationLogsService(db).get(entity_id)

@router.post("/qc_integration_logs", response_model=QcIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_integration_logs(
    data: QcIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcIntegrationLogsService(db).create(data)

@router.put("/qc_integration_logs/{entity_id}", response_model=QcIntegrationLogsOut)
async def update_qc_integration_logs(
    entity_id: uuid.UUID,
    data: QcIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcIntegrationLogsService(db).update(entity_id, data)

@router.delete("/qc_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcIntegrationLogsService(db).delete(entity_id)

@router.get("/qc_kpi_actuals", response_model=PaginatedResponse[QcKpiActualsOut])
async def list_qc_kpi_actuals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcKpiActualsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["period_type_code", "entity_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_kpi_actuals/{entity_id}", response_model=QcKpiActualsOut)
async def get_qc_kpi_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcKpiActualsService(db).get(entity_id)

@router.post("/qc_kpi_actuals", response_model=QcKpiActualsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_kpi_actuals(
    data: QcKpiActualsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcKpiActualsService(db).create(data)

@router.put("/qc_kpi_actuals/{entity_id}", response_model=QcKpiActualsOut)
async def update_qc_kpi_actuals(
    entity_id: uuid.UUID,
    data: QcKpiActualsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcKpiActualsService(db).update(entity_id, data)

@router.delete("/qc_kpi_actuals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_kpi_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcKpiActualsService(db).delete(entity_id)

@router.get("/qc_kpi_definitions", response_model=PaginatedResponse[QcKpiDefinitionsOut])
async def list_qc_kpi_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcKpiDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "kpi_name", "kpi_category_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_kpi_definitions/{entity_id}", response_model=QcKpiDefinitionsOut)
async def get_qc_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcKpiDefinitionsService(db).get(entity_id)

@router.post("/qc_kpi_definitions", response_model=QcKpiDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_kpi_definitions(
    data: QcKpiDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcKpiDefinitionsService(db).create(data)

@router.put("/qc_kpi_definitions/{entity_id}", response_model=QcKpiDefinitionsOut)
async def update_qc_kpi_definitions(
    entity_id: uuid.UUID,
    data: QcKpiDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcKpiDefinitionsService(db).update(entity_id, data)

@router.delete("/qc_kpi_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcKpiDefinitionsService(db).delete(entity_id)

@router.get("/qc_langgraph_executions", response_model=PaginatedResponse[QcLanggraphExecutionsOut])
async def list_qc_langgraph_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcLanggraphExecutionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["execution_name", "execution_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_langgraph_executions/{entity_id}", response_model=QcLanggraphExecutionsOut)
async def get_qc_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcLanggraphExecutionsService(db).get(entity_id)

@router.post("/qc_langgraph_executions", response_model=QcLanggraphExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_langgraph_executions(
    data: QcLanggraphExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphExecutionsService(db).create(data)

@router.put("/qc_langgraph_executions/{entity_id}", response_model=QcLanggraphExecutionsOut)
async def update_qc_langgraph_executions(
    entity_id: uuid.UUID,
    data: QcLanggraphExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphExecutionsService(db).update(entity_id, data)

@router.delete("/qc_langgraph_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcLanggraphExecutionsService(db).delete(entity_id)

@router.get("/qc_langgraph_states", response_model=PaginatedResponse[QcLanggraphStatesOut])
async def list_qc_langgraph_states(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcLanggraphStatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["node_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_langgraph_states/{entity_id}", response_model=QcLanggraphStatesOut)
async def get_qc_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcLanggraphStatesService(db).get(entity_id)

@router.post("/qc_langgraph_states", response_model=QcLanggraphStatesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_langgraph_states(
    data: QcLanggraphStatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphStatesService(db).create(data)

@router.put("/qc_langgraph_states/{entity_id}", response_model=QcLanggraphStatesOut)
async def update_qc_langgraph_states(
    entity_id: uuid.UUID,
    data: QcLanggraphStatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphStatesService(db).update(entity_id, data)

@router.delete("/qc_langgraph_states/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcLanggraphStatesService(db).delete(entity_id)

@router.get("/qc_langgraph_workflows", response_model=PaginatedResponse[QcLanggraphWorkflowsOut])
async def list_qc_langgraph_workflows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcLanggraphWorkflowsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name", "workflow_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_langgraph_workflows/{entity_id}", response_model=QcLanggraphWorkflowsOut)
async def get_qc_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcLanggraphWorkflowsService(db).get(entity_id)

@router.post("/qc_langgraph_workflows", response_model=QcLanggraphWorkflowsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_langgraph_workflows(
    data: QcLanggraphWorkflowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphWorkflowsService(db).create(data)

@router.put("/qc_langgraph_workflows/{entity_id}", response_model=QcLanggraphWorkflowsOut)
async def update_qc_langgraph_workflows(
    entity_id: uuid.UUID,
    data: QcLanggraphWorkflowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLanggraphWorkflowsService(db).update(entity_id, data)

@router.delete("/qc_langgraph_workflows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcLanggraphWorkflowsService(db).delete(entity_id)

@router.get("/qc_llm_configs", response_model=PaginatedResponse[QcLlmConfigsOut])
async def list_qc_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_code", "config_name", "provider_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_llm_configs/{entity_id}", response_model=QcLlmConfigsOut)
async def get_qc_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcLlmConfigsService(db).get(entity_id)

@router.post("/qc_llm_configs", response_model=QcLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_llm_configs(
    data: QcLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLlmConfigsService(db).create(data)

@router.put("/qc_llm_configs/{entity_id}", response_model=QcLlmConfigsOut)
async def update_qc_llm_configs(
    entity_id: uuid.UUID,
    data: QcLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLlmConfigsService(db).update(entity_id, data)

@router.delete("/qc_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcLlmConfigsService(db).delete(entity_id)

@router.get("/qc_lot_dispositions", response_model=PaginatedResponse[QcLotDispositionsOut])
async def list_qc_lot_dispositions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcLotDispositionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["disposition_number", "lot_number", "serial_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_lot_dispositions/{entity_id}", response_model=QcLotDispositionsOut)
async def get_qc_lot_dispositions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcLotDispositionsService(db).get(entity_id)

@router.post("/qc_lot_dispositions", response_model=QcLotDispositionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_lot_dispositions(
    data: QcLotDispositionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLotDispositionsService(db).create(data)

@router.put("/qc_lot_dispositions/{entity_id}", response_model=QcLotDispositionsOut)
async def update_qc_lot_dispositions(
    entity_id: uuid.UUID,
    data: QcLotDispositionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcLotDispositionsService(db).update(entity_id, data)

@router.delete("/qc_lot_dispositions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_lot_dispositions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcLotDispositionsService(db).delete(entity_id)

@router.get("/qc_ml_models", response_model=PaginatedResponse[QcMlModelsOut])
async def list_qc_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name", "model_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ml_models/{entity_id}", response_model=QcMlModelsOut)
async def get_qc_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcMlModelsService(db).get(entity_id)

@router.post("/qc_ml_models", response_model=QcMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ml_models(
    data: QcMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMlModelsService(db).create(data)

@router.put("/qc_ml_models/{entity_id}", response_model=QcMlModelsOut)
async def update_qc_ml_models(
    entity_id: uuid.UUID,
    data: QcMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMlModelsService(db).update(entity_id, data)

@router.delete("/qc_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcMlModelsService(db).delete(entity_id)

@router.get("/qc_msa_measurements", response_model=PaginatedResponse[QcMsaMeasurementsOut])
async def list_qc_msa_measurements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcMsaMeasurementsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["operator_name", "part_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_msa_measurements/{entity_id}", response_model=QcMsaMeasurementsOut)
async def get_qc_msa_measurements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcMsaMeasurementsService(db).get(entity_id)

@router.post("/qc_msa_measurements", response_model=QcMsaMeasurementsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_msa_measurements(
    data: QcMsaMeasurementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMsaMeasurementsService(db).create(data)

@router.put("/qc_msa_measurements/{entity_id}", response_model=QcMsaMeasurementsOut)
async def update_qc_msa_measurements(
    entity_id: uuid.UUID,
    data: QcMsaMeasurementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMsaMeasurementsService(db).update(entity_id, data)

@router.delete("/qc_msa_measurements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_msa_measurements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcMsaMeasurementsService(db).delete(entity_id)

@router.get("/qc_msa_studies", response_model=PaginatedResponse[QcMsaStudiesOut])
async def list_qc_msa_studies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcMsaStudiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["msa_study_number", "msa_study_name", "msa_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_msa_studies/{entity_id}", response_model=QcMsaStudiesOut)
async def get_qc_msa_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcMsaStudiesService(db).get(entity_id)

@router.post("/qc_msa_studies", response_model=QcMsaStudiesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_msa_studies(
    data: QcMsaStudiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMsaStudiesService(db).create(data)

@router.put("/qc_msa_studies/{entity_id}", response_model=QcMsaStudiesOut)
async def update_qc_msa_studies(
    entity_id: uuid.UUID,
    data: QcMsaStudiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcMsaStudiesService(db).update(entity_id, data)

@router.delete("/qc_msa_studies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_msa_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcMsaStudiesService(db).delete(entity_id)

@router.get("/qc_ncr_attachments", response_model=PaginatedResponse[QcNcrAttachmentsOut])
async def list_qc_ncr_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcNcrAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["attachment_type_code", "file_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ncr_attachments/{entity_id}", response_model=QcNcrAttachmentsOut)
async def get_qc_ncr_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcNcrAttachmentsService(db).get(entity_id)

@router.post("/qc_ncr_attachments", response_model=QcNcrAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ncr_attachments(
    data: QcNcrAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrAttachmentsService(db).create(data)

@router.put("/qc_ncr_attachments/{entity_id}", response_model=QcNcrAttachmentsOut)
async def update_qc_ncr_attachments(
    entity_id: uuid.UUID,
    data: QcNcrAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrAttachmentsService(db).update(entity_id, data)

@router.delete("/qc_ncr_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ncr_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcNcrAttachmentsService(db).delete(entity_id)

@router.get("/qc_ncr_containment", response_model=PaginatedResponse[QcNcrContainmentOut])
async def list_qc_ncr_containment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcNcrContainmentService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["containment_type_code", "description", "containment_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ncr_containment/{entity_id}", response_model=QcNcrContainmentOut)
async def get_qc_ncr_containment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcNcrContainmentService(db).get(entity_id)

@router.post("/qc_ncr_containment", response_model=QcNcrContainmentOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ncr_containment(
    data: QcNcrContainmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrContainmentService(db).create(data)

@router.put("/qc_ncr_containment/{entity_id}", response_model=QcNcrContainmentOut)
async def update_qc_ncr_containment(
    entity_id: uuid.UUID,
    data: QcNcrContainmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrContainmentService(db).update(entity_id, data)

@router.delete("/qc_ncr_containment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ncr_containment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcNcrContainmentService(db).delete(entity_id)

@router.get("/qc_ncr_headers", response_model=PaginatedResponse[QcNcrHeadersOut])
async def list_qc_ncr_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcNcrHeadersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["ncr_number", "ncr_title", "ncr_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ncr_headers/{entity_id}", response_model=QcNcrHeadersOut)
async def get_qc_ncr_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcNcrHeadersService(db).get(entity_id)

@router.post("/qc_ncr_headers", response_model=QcNcrHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ncr_headers(
    data: QcNcrHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrHeadersService(db).create(data)

@router.put("/qc_ncr_headers/{entity_id}", response_model=QcNcrHeadersOut)
async def update_qc_ncr_headers(
    entity_id: uuid.UUID,
    data: QcNcrHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNcrHeadersService(db).update(entity_id, data)

@router.delete("/qc_ncr_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ncr_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcNcrHeadersService(db).delete(entity_id)

@router.get("/qc_notifications", response_model=PaginatedResponse[QcNotificationsOut])
async def list_qc_notifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcNotificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["notification_number", "notification_type_code", "notification_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_notifications/{entity_id}", response_model=QcNotificationsOut)
async def get_qc_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcNotificationsService(db).get(entity_id)

@router.post("/qc_notifications", response_model=QcNotificationsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_notifications(
    data: QcNotificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNotificationsService(db).create(data)

@router.put("/qc_notifications/{entity_id}", response_model=QcNotificationsOut)
async def update_qc_notifications(
    entity_id: uuid.UUID,
    data: QcNotificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcNotificationsService(db).update(entity_id, data)

@router.delete("/qc_notifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcNotificationsService(db).delete(entity_id)

@router.get("/qc_optimization_problems", response_model=PaginatedResponse[QcOptimizationProblemsOut])
async def list_qc_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcOptimizationProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_name", "problem_type_code", "problem_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_optimization_problems/{entity_id}", response_model=QcOptimizationProblemsOut)
async def get_qc_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcOptimizationProblemsService(db).get(entity_id)

@router.post("/qc_optimization_problems", response_model=QcOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_optimization_problems(
    data: QcOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcOptimizationProblemsService(db).create(data)

@router.put("/qc_optimization_problems/{entity_id}", response_model=QcOptimizationProblemsOut)
async def update_qc_optimization_problems(
    entity_id: uuid.UUID,
    data: QcOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/qc_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcOptimizationProblemsService(db).delete(entity_id)

@router.get("/qc_ortools_problems", response_model=PaginatedResponse[QcOrtoolsProblemsOut])
async def list_qc_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcOrtoolsProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_code", "problem_name", "problem_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ortools_problems/{entity_id}", response_model=QcOrtoolsProblemsOut)
async def get_qc_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcOrtoolsProblemsService(db).get(entity_id)

@router.post("/qc_ortools_problems", response_model=QcOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ortools_problems(
    data: QcOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcOrtoolsProblemsService(db).create(data)

@router.put("/qc_ortools_problems/{entity_id}", response_model=QcOrtoolsProblemsOut)
async def update_qc_ortools_problems(
    entity_id: uuid.UUID,
    data: QcOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/qc_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcOrtoolsProblemsService(db).delete(entity_id)

@router.get("/qc_plan_attachments", response_model=PaginatedResponse[QcPlanAttachmentsOut])
async def list_qc_plan_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPlanAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["attachment_type_code", "file_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_plan_attachments/{entity_id}", response_model=QcPlanAttachmentsOut)
async def get_qc_plan_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPlanAttachmentsService(db).get(entity_id)

@router.post("/qc_plan_attachments", response_model=QcPlanAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_plan_attachments(
    data: QcPlanAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanAttachmentsService(db).create(data)

@router.put("/qc_plan_attachments/{entity_id}", response_model=QcPlanAttachmentsOut)
async def update_qc_plan_attachments(
    entity_id: uuid.UUID,
    data: QcPlanAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanAttachmentsService(db).update(entity_id, data)

@router.delete("/qc_plan_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_plan_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPlanAttachmentsService(db).delete(entity_id)

@router.get("/qc_plan_elements", response_model=PaginatedResponse[QcPlanElementsOut])
async def list_qc_plan_elements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPlanElementsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["element_type_code", "frequency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_plan_elements/{entity_id}", response_model=QcPlanElementsOut)
async def get_qc_plan_elements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPlanElementsService(db).get(entity_id)

@router.post("/qc_plan_elements", response_model=QcPlanElementsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_plan_elements(
    data: QcPlanElementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanElementsService(db).create(data)

@router.put("/qc_plan_elements/{entity_id}", response_model=QcPlanElementsOut)
async def update_qc_plan_elements(
    entity_id: uuid.UUID,
    data: QcPlanElementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanElementsService(db).update(entity_id, data)

@router.delete("/qc_plan_elements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_plan_elements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPlanElementsService(db).delete(entity_id)

@router.get("/qc_plan_triggers", response_model=PaginatedResponse[QcPlanTriggersOut])
async def list_qc_plan_triggers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPlanTriggersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["trigger_type_code", "trigger_event_code", "trigger_source_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_plan_triggers/{entity_id}", response_model=QcPlanTriggersOut)
async def get_qc_plan_triggers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPlanTriggersService(db).get(entity_id)

@router.post("/qc_plan_triggers", response_model=QcPlanTriggersOut, status_code=status.HTTP_201_CREATED)
async def create_qc_plan_triggers(
    data: QcPlanTriggersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanTriggersService(db).create(data)

@router.put("/qc_plan_triggers/{entity_id}", response_model=QcPlanTriggersOut)
async def update_qc_plan_triggers(
    entity_id: uuid.UUID,
    data: QcPlanTriggersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlanTriggersService(db).update(entity_id, data)

@router.delete("/qc_plan_triggers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_plan_triggers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPlanTriggersService(db).delete(entity_id)

@router.get("/qc_plans", response_model=PaginatedResponse[QcPlansOut])
async def list_qc_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_number", "plan_name", "plan_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_plans/{entity_id}", response_model=QcPlansOut)
async def get_qc_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPlansService(db).get(entity_id)

@router.post("/qc_plans", response_model=QcPlansOut, status_code=status.HTTP_201_CREATED)
async def create_qc_plans(
    data: QcPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlansService(db).create(data)

@router.put("/qc_plans/{entity_id}", response_model=QcPlansOut)
async def update_qc_plans(
    entity_id: uuid.UUID,
    data: QcPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPlansService(db).update(entity_id, data)

@router.delete("/qc_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPlansService(db).delete(entity_id)

@router.get("/qc_ppap_submissions", response_model=PaginatedResponse[QcPpapSubmissionsOut])
async def list_qc_ppap_submissions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPpapSubmissionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["ppap_number", "ppap_status_code", "customer_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_ppap_submissions/{entity_id}", response_model=QcPpapSubmissionsOut)
async def get_qc_ppap_submissions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPpapSubmissionsService(db).get(entity_id)

@router.post("/qc_ppap_submissions", response_model=QcPpapSubmissionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_ppap_submissions(
    data: QcPpapSubmissionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPpapSubmissionsService(db).create(data)

@router.put("/qc_ppap_submissions/{entity_id}", response_model=QcPpapSubmissionsOut)
async def update_qc_ppap_submissions(
    entity_id: uuid.UUID,
    data: QcPpapSubmissionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPpapSubmissionsService(db).update(entity_id, data)

@router.delete("/qc_ppap_submissions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_ppap_submissions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPpapSubmissionsService(db).delete(entity_id)

@router.get("/qc_predictions", response_model=PaginatedResponse[QcPredictionsOut])
async def list_qc_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPredictionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["prediction_code", "prediction_type_code", "entity_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_predictions/{entity_id}", response_model=QcPredictionsOut)
async def get_qc_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPredictionsService(db).get(entity_id)

@router.post("/qc_predictions", response_model=QcPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_predictions(
    data: QcPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPredictionsService(db).create(data)

@router.put("/qc_predictions/{entity_id}", response_model=QcPredictionsOut)
async def update_qc_predictions(
    entity_id: uuid.UUID,
    data: QcPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPredictionsService(db).update(entity_id, data)

@router.delete("/qc_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPredictionsService(db).delete(entity_id)

@router.get("/qc_prompt_templates", response_model=PaginatedResponse[QcPromptTemplatesOut])
async def list_qc_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_code", "template_name", "template_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_prompt_templates/{entity_id}", response_model=QcPromptTemplatesOut)
async def get_qc_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcPromptTemplatesService(db).get(entity_id)

@router.post("/qc_prompt_templates", response_model=QcPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_prompt_templates(
    data: QcPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPromptTemplatesService(db).create(data)

@router.put("/qc_prompt_templates/{entity_id}", response_model=QcPromptTemplatesOut)
async def update_qc_prompt_templates(
    entity_id: uuid.UUID,
    data: QcPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcPromptTemplatesService(db).update(entity_id, data)

@router.delete("/qc_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcPromptTemplatesService(db).delete(entity_id)

@router.get("/qc_root_cause_analysis", response_model=PaginatedResponse[QcRootCauseAnalysisOut])
async def list_qc_root_cause_analysis(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcRootCauseAnalysisService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rca_number", "rca_method_code", "rca_title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_root_cause_analysis/{entity_id}", response_model=QcRootCauseAnalysisOut)
async def get_qc_root_cause_analysis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcRootCauseAnalysisService(db).get(entity_id)

@router.post("/qc_root_cause_analysis", response_model=QcRootCauseAnalysisOut, status_code=status.HTTP_201_CREATED)
async def create_qc_root_cause_analysis(
    data: QcRootCauseAnalysisCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcRootCauseAnalysisService(db).create(data)

@router.put("/qc_root_cause_analysis/{entity_id}", response_model=QcRootCauseAnalysisOut)
async def update_qc_root_cause_analysis(
    entity_id: uuid.UUID,
    data: QcRootCauseAnalysisUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcRootCauseAnalysisService(db).update(entity_id, data)

@router.delete("/qc_root_cause_analysis/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_root_cause_analysis(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcRootCauseAnalysisService(db).delete(entity_id)

@router.get("/qc_root_cause_causes", response_model=PaginatedResponse[QcRootCauseCausesOut])
async def list_qc_root_cause_causes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcRootCauseCausesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cause_type_code", "cause_description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_root_cause_causes/{entity_id}", response_model=QcRootCauseCausesOut)
async def get_qc_root_cause_causes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcRootCauseCausesService(db).get(entity_id)

@router.post("/qc_root_cause_causes", response_model=QcRootCauseCausesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_root_cause_causes(
    data: QcRootCauseCausesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcRootCauseCausesService(db).create(data)

@router.put("/qc_root_cause_causes/{entity_id}", response_model=QcRootCauseCausesOut)
async def update_qc_root_cause_causes(
    entity_id: uuid.UUID,
    data: QcRootCauseCausesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcRootCauseCausesService(db).update(entity_id, data)

@router.delete("/qc_root_cause_causes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_root_cause_causes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcRootCauseCausesService(db).delete(entity_id)

@router.get("/qc_sample_containers", response_model=PaginatedResponse[QcSampleContainersOut])
async def list_qc_sample_containers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSampleContainersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["container_code", "container_name", "container_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_sample_containers/{entity_id}", response_model=QcSampleContainersOut)
async def get_qc_sample_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSampleContainersService(db).get(entity_id)

@router.post("/qc_sample_containers", response_model=QcSampleContainersOut, status_code=status.HTTP_201_CREATED)
async def create_qc_sample_containers(
    data: QcSampleContainersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSampleContainersService(db).create(data)

@router.put("/qc_sample_containers/{entity_id}", response_model=QcSampleContainersOut)
async def update_qc_sample_containers(
    entity_id: uuid.UUID,
    data: QcSampleContainersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSampleContainersService(db).update(entity_id, data)

@router.delete("/qc_sample_containers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_sample_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSampleContainersService(db).delete(entity_id)

@router.get("/qc_sample_packing_results", response_model=PaginatedResponse[QcSamplePackingResultsOut])
async def list_qc_sample_packing_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSamplePackingResultsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["container_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_sample_packing_results/{entity_id}", response_model=QcSamplePackingResultsOut)
async def get_qc_sample_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSamplePackingResultsService(db).get(entity_id)

@router.post("/qc_sample_packing_results", response_model=QcSamplePackingResultsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_sample_packing_results(
    data: QcSamplePackingResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplePackingResultsService(db).create(data)

@router.put("/qc_sample_packing_results/{entity_id}", response_model=QcSamplePackingResultsOut)
async def update_qc_sample_packing_results(
    entity_id: uuid.UUID,
    data: QcSamplePackingResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplePackingResultsService(db).update(entity_id, data)

@router.delete("/qc_sample_packing_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_sample_packing_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSamplePackingResultsService(db).delete(entity_id)

@router.get("/qc_sampling_plan_lines", response_model=PaginatedResponse[QcSamplingPlanLinesOut])
async def list_qc_sampling_plan_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSamplingPlanLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_sampling_plan_lines/{entity_id}", response_model=QcSamplingPlanLinesOut)
async def get_qc_sampling_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSamplingPlanLinesService(db).get(entity_id)

@router.post("/qc_sampling_plan_lines", response_model=QcSamplingPlanLinesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_sampling_plan_lines(
    data: QcSamplingPlanLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplingPlanLinesService(db).create(data)

@router.put("/qc_sampling_plan_lines/{entity_id}", response_model=QcSamplingPlanLinesOut)
async def update_qc_sampling_plan_lines(
    entity_id: uuid.UUID,
    data: QcSamplingPlanLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplingPlanLinesService(db).update(entity_id, data)

@router.delete("/qc_sampling_plan_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_sampling_plan_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSamplingPlanLinesService(db).delete(entity_id)

@router.get("/qc_sampling_plans", response_model=PaginatedResponse[QcSamplingPlansOut])
async def list_qc_sampling_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSamplingPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_code", "plan_name", "sampling_standard_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_sampling_plans/{entity_id}", response_model=QcSamplingPlansOut)
async def get_qc_sampling_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSamplingPlansService(db).get(entity_id)

@router.post("/qc_sampling_plans", response_model=QcSamplingPlansOut, status_code=status.HTTP_201_CREATED)
async def create_qc_sampling_plans(
    data: QcSamplingPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplingPlansService(db).create(data)

@router.put("/qc_sampling_plans/{entity_id}", response_model=QcSamplingPlansOut)
async def update_qc_sampling_plans(
    entity_id: uuid.UUID,
    data: QcSamplingPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSamplingPlansService(db).update(entity_id, data)

@router.delete("/qc_sampling_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_sampling_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSamplingPlansService(db).delete(entity_id)

@router.get("/qc_scenarios", response_model=PaginatedResponse[QcScenariosOut])
async def list_qc_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_code", "scenario_name", "scenario_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_scenarios/{entity_id}", response_model=QcScenariosOut)
async def get_qc_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcScenariosService(db).get(entity_id)

@router.post("/qc_scenarios", response_model=QcScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_qc_scenarios(
    data: QcScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcScenariosService(db).create(data)

@router.put("/qc_scenarios/{entity_id}", response_model=QcScenariosOut)
async def update_qc_scenarios(
    entity_id: uuid.UUID,
    data: QcScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcScenariosService(db).update(entity_id, data)

@router.delete("/qc_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcScenariosService(db).delete(entity_id)

@router.get("/qc_scipy_analyses", response_model=PaginatedResponse[QcScipyAnalysesOut])
async def list_qc_scipy_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcScipyAnalysesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["analysis_code", "analysis_name", "analysis_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_scipy_analyses/{entity_id}", response_model=QcScipyAnalysesOut)
async def get_qc_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcScipyAnalysesService(db).get(entity_id)

@router.post("/qc_scipy_analyses", response_model=QcScipyAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_scipy_analyses(
    data: QcScipyAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcScipyAnalysesService(db).create(data)

@router.put("/qc_scipy_analyses/{entity_id}", response_model=QcScipyAnalysesOut)
async def update_qc_scipy_analyses(
    entity_id: uuid.UUID,
    data: QcScipyAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcScipyAnalysesService(db).update(entity_id, data)

@router.delete("/qc_scipy_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcScipyAnalysesService(db).delete(entity_id)

@router.get("/qc_solver_configs", response_model=PaginatedResponse[QcSolverConfigsOut])
async def list_qc_solver_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSolverConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solver_name", "solver_type_code", "algorithm_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_solver_configs/{entity_id}", response_model=QcSolverConfigsOut)
async def get_qc_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSolverConfigsService(db).get(entity_id)

@router.post("/qc_solver_configs", response_model=QcSolverConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_solver_configs(
    data: QcSolverConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSolverConfigsService(db).create(data)

@router.put("/qc_solver_configs/{entity_id}", response_model=QcSolverConfigsOut)
async def update_qc_solver_configs(
    entity_id: uuid.UUID,
    data: QcSolverConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSolverConfigsService(db).update(entity_id, data)

@router.delete("/qc_solver_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSolverConfigsService(db).delete(entity_id)

@router.get("/qc_spc_alerts", response_model=PaginatedResponse[QcSpcAlertsOut])
async def list_qc_spc_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSpcAlertsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["alert_type_code", "alert_severity_code", "alert_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_spc_alerts/{entity_id}", response_model=QcSpcAlertsOut)
async def get_qc_spc_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSpcAlertsService(db).get(entity_id)

@router.post("/qc_spc_alerts", response_model=QcSpcAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_spc_alerts(
    data: QcSpcAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcAlertsService(db).create(data)

@router.put("/qc_spc_alerts/{entity_id}", response_model=QcSpcAlertsOut)
async def update_qc_spc_alerts(
    entity_id: uuid.UUID,
    data: QcSpcAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcAlertsService(db).update(entity_id, data)

@router.delete("/qc_spc_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_spc_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSpcAlertsService(db).delete(entity_id)

@router.get("/qc_spc_charts", response_model=PaginatedResponse[QcSpcChartsOut])
async def list_qc_spc_charts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSpcChartsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["chart_code", "chart_name", "chart_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_spc_charts/{entity_id}", response_model=QcSpcChartsOut)
async def get_qc_spc_charts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSpcChartsService(db).get(entity_id)

@router.post("/qc_spc_charts", response_model=QcSpcChartsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_spc_charts(
    data: QcSpcChartsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcChartsService(db).create(data)

@router.put("/qc_spc_charts/{entity_id}", response_model=QcSpcChartsOut)
async def update_qc_spc_charts(
    entity_id: uuid.UUID,
    data: QcSpcChartsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcChartsService(db).update(entity_id, data)

@router.delete("/qc_spc_charts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_spc_charts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSpcChartsService(db).delete(entity_id)

@router.get("/qc_spc_data_points", response_model=PaginatedResponse[QcSpcDataPointsOut])
async def list_qc_spc_data_points(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSpcDataPointsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["operator_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_spc_data_points/{entity_id}", response_model=QcSpcDataPointsOut)
async def get_qc_spc_data_points(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSpcDataPointsService(db).get(entity_id)

@router.post("/qc_spc_data_points", response_model=QcSpcDataPointsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_spc_data_points(
    data: QcSpcDataPointsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcDataPointsService(db).create(data)

@router.put("/qc_spc_data_points/{entity_id}", response_model=QcSpcDataPointsOut)
async def update_qc_spc_data_points(
    entity_id: uuid.UUID,
    data: QcSpcDataPointsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpcDataPointsService(db).update(entity_id, data)

@router.delete("/qc_spc_data_points/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_spc_data_points(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSpcDataPointsService(db).delete(entity_id)

@router.get("/qc_spec_limits", response_model=PaginatedResponse[QcSpecLimitsOut])
async def list_qc_spec_limits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSpecLimitsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["limit_type_code", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_spec_limits/{entity_id}", response_model=QcSpecLimitsOut)
async def get_qc_spec_limits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSpecLimitsService(db).get(entity_id)

@router.post("/qc_spec_limits", response_model=QcSpecLimitsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_spec_limits(
    data: QcSpecLimitsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpecLimitsService(db).create(data)

@router.put("/qc_spec_limits/{entity_id}", response_model=QcSpecLimitsOut)
async def update_qc_spec_limits(
    entity_id: uuid.UUID,
    data: QcSpecLimitsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpecLimitsService(db).update(entity_id, data)

@router.delete("/qc_spec_limits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_spec_limits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSpecLimitsService(db).delete(entity_id)

@router.get("/qc_specs", response_model=PaginatedResponse[QcSpecsOut])
async def list_qc_specs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSpecsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["spec_number", "spec_name", "spec_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_specs/{entity_id}", response_model=QcSpecsOut)
async def get_qc_specs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSpecsService(db).get(entity_id)

@router.post("/qc_specs", response_model=QcSpecsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_specs(
    data: QcSpecsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpecsService(db).create(data)

@router.put("/qc_specs/{entity_id}", response_model=QcSpecsOut)
async def update_qc_specs(
    entity_id: uuid.UUID,
    data: QcSpecsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSpecsService(db).update(entity_id, data)

@router.delete("/qc_specs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_specs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSpecsService(db).delete(entity_id)

@router.get("/qc_supplier_profiles", response_model=PaginatedResponse[QcSupplierProfilesOut])
async def list_qc_supplier_profiles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSupplierProfilesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["supplier_code", "supplier_name", "risk_level_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_supplier_profiles/{entity_id}", response_model=QcSupplierProfilesOut)
async def get_qc_supplier_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSupplierProfilesService(db).get(entity_id)

@router.post("/qc_supplier_profiles", response_model=QcSupplierProfilesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_supplier_profiles(
    data: QcSupplierProfilesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSupplierProfilesService(db).create(data)

@router.put("/qc_supplier_profiles/{entity_id}", response_model=QcSupplierProfilesOut)
async def update_qc_supplier_profiles(
    entity_id: uuid.UUID,
    data: QcSupplierProfilesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSupplierProfilesService(db).update(entity_id, data)

@router.delete("/qc_supplier_profiles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_supplier_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSupplierProfilesService(db).delete(entity_id)

@router.get("/qc_supplier_scorecards", response_model=PaginatedResponse[QcSupplierScorecardsOut])
async def list_qc_supplier_scorecards(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcSupplierScorecardsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_supplier_scorecards/{entity_id}", response_model=QcSupplierScorecardsOut)
async def get_qc_supplier_scorecards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcSupplierScorecardsService(db).get(entity_id)

@router.post("/qc_supplier_scorecards", response_model=QcSupplierScorecardsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_supplier_scorecards(
    data: QcSupplierScorecardsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSupplierScorecardsService(db).create(data)

@router.put("/qc_supplier_scorecards/{entity_id}", response_model=QcSupplierScorecardsOut)
async def update_qc_supplier_scorecards(
    entity_id: uuid.UUID,
    data: QcSupplierScorecardsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcSupplierScorecardsService(db).update(entity_id, data)

@router.delete("/qc_supplier_scorecards/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_supplier_scorecards(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcSupplierScorecardsService(db).delete(entity_id)

@router.get("/qc_test_equipment", response_model=PaginatedResponse[QcTestEquipmentOut])
async def list_qc_test_equipment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTestEquipmentService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["equipment_code", "equipment_name", "equipment_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_test_equipment/{entity_id}", response_model=QcTestEquipmentOut)
async def get_qc_test_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTestEquipmentService(db).get(entity_id)

@router.post("/qc_test_equipment", response_model=QcTestEquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_qc_test_equipment(
    data: QcTestEquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestEquipmentService(db).create(data)

@router.put("/qc_test_equipment/{entity_id}", response_model=QcTestEquipmentOut)
async def update_qc_test_equipment(
    entity_id: uuid.UUID,
    data: QcTestEquipmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestEquipmentService(db).update(entity_id, data)

@router.delete("/qc_test_equipment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_test_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTestEquipmentService(db).delete(entity_id)

@router.get("/qc_test_methods", response_model=PaginatedResponse[QcTestMethodsOut])
async def list_qc_test_methods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTestMethodsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["method_code", "method_name", "method_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_test_methods/{entity_id}", response_model=QcTestMethodsOut)
async def get_qc_test_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTestMethodsService(db).get(entity_id)

@router.post("/qc_test_methods", response_model=QcTestMethodsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_test_methods(
    data: QcTestMethodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestMethodsService(db).create(data)

@router.put("/qc_test_methods/{entity_id}", response_model=QcTestMethodsOut)
async def update_qc_test_methods(
    entity_id: uuid.UUID,
    data: QcTestMethodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestMethodsService(db).update(entity_id, data)

@router.delete("/qc_test_methods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_test_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTestMethodsService(db).delete(entity_id)

@router.get("/qc_test_result_lines", response_model=PaginatedResponse[QcTestResultLinesOut])
async def list_qc_test_result_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTestResultLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code", "result_status_code", "defect_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_test_result_lines/{entity_id}", response_model=QcTestResultLinesOut)
async def get_qc_test_result_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTestResultLinesService(db).get(entity_id)

@router.post("/qc_test_result_lines", response_model=QcTestResultLinesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_test_result_lines(
    data: QcTestResultLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestResultLinesService(db).create(data)

@router.put("/qc_test_result_lines/{entity_id}", response_model=QcTestResultLinesOut)
async def update_qc_test_result_lines(
    entity_id: uuid.UUID,
    data: QcTestResultLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestResultLinesService(db).update(entity_id, data)

@router.delete("/qc_test_result_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_test_result_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTestResultLinesService(db).delete(entity_id)

@router.get("/qc_test_results", response_model=PaginatedResponse[QcTestResultsOut])
async def list_qc_test_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTestResultsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["test_result_number", "test_result_status_code", "overall_result_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_test_results/{entity_id}", response_model=QcTestResultsOut)
async def get_qc_test_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTestResultsService(db).get(entity_id)

@router.post("/qc_test_results", response_model=QcTestResultsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_test_results(
    data: QcTestResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestResultsService(db).create(data)

@router.put("/qc_test_results/{entity_id}", response_model=QcTestResultsOut)
async def update_qc_test_results(
    entity_id: uuid.UUID,
    data: QcTestResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTestResultsService(db).update(entity_id, data)

@router.delete("/qc_test_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_test_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTestResultsService(db).delete(entity_id)

@router.get("/qc_training_attendees", response_model=PaginatedResponse[QcTrainingAttendeesOut])
async def list_qc_training_attendees(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTrainingAttendeesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["employee_name", "trainer_name", "attendance_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_training_attendees/{entity_id}", response_model=QcTrainingAttendeesOut)
async def get_qc_training_attendees(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTrainingAttendeesService(db).get(entity_id)

@router.post("/qc_training_attendees", response_model=QcTrainingAttendeesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_training_attendees(
    data: QcTrainingAttendeesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTrainingAttendeesService(db).create(data)

@router.put("/qc_training_attendees/{entity_id}", response_model=QcTrainingAttendeesOut)
async def update_qc_training_attendees(
    entity_id: uuid.UUID,
    data: QcTrainingAttendeesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTrainingAttendeesService(db).update(entity_id, data)

@router.delete("/qc_training_attendees/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_training_attendees(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTrainingAttendeesService(db).delete(entity_id)

@router.get("/qc_training_courses", response_model=PaginatedResponse[QcTrainingCoursesOut])
async def list_qc_training_courses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcTrainingCoursesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["course_code", "course_name", "course_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_training_courses/{entity_id}", response_model=QcTrainingCoursesOut)
async def get_qc_training_courses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcTrainingCoursesService(db).get(entity_id)

@router.post("/qc_training_courses", response_model=QcTrainingCoursesOut, status_code=status.HTTP_201_CREATED)
async def create_qc_training_courses(
    data: QcTrainingCoursesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTrainingCoursesService(db).create(data)

@router.put("/qc_training_courses/{entity_id}", response_model=QcTrainingCoursesOut)
async def update_qc_training_courses(
    entity_id: uuid.UUID,
    data: QcTrainingCoursesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcTrainingCoursesService(db).update(entity_id, data)

@router.delete("/qc_training_courses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_training_courses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcTrainingCoursesService(db).delete(entity_id)

@router.get("/qc_vector_documents", response_model=PaginatedResponse[QcVectorDocumentsOut])
async def list_qc_vector_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    svc = QcVectorDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["collection_name", "source_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/qc_vector_documents/{entity_id}", response_model=QcVectorDocumentsOut)
async def get_qc_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "view"),
):
    return await QcVectorDocumentsService(db).get(entity_id)

@router.post("/qc_vector_documents", response_model=QcVectorDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_qc_vector_documents(
    data: QcVectorDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcVectorDocumentsService(db).create(data)

@router.put("/qc_vector_documents/{entity_id}", response_model=QcVectorDocumentsOut)
async def update_qc_vector_documents(
    entity_id: uuid.UUID,
    data: QcVectorDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    return await QcVectorDocumentsService(db).update(entity_id, data)

@router.delete("/qc_vector_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qc_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("qc", "manage"),
):
    await QcVectorDocumentsService(db).delete(entity_id)
