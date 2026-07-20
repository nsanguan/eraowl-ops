import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.eam.services import (
    EamAiAgentLogsService,
    EamAiDecisionsService,
    EamAiWorkflowStateService,
    EamAlertsService,
    EamAssetAttachmentsService,
    EamAssetBomService,
    EamAssetCategoriesService,
    EamAssetCriticalityService,
    EamAssetHierarchyService,
    EamAssetTypesService,
    EamAssetVendorsService,
    EamAssetsService,
    EamAuditLogService,
    EamBudgetsService,
    EamCalibrationRequirementsService,
    EamCalibrationResultsService,
    EamComplianceRecordsService,
    EamComplianceRequirementsService,
    EamComponentsService,
    EamConditionMonitoringProgramsService,
    EamConditionReadingsService,
    EamContractAssetsService,
    EamCraftsService,
    EamDecommissionPlansService,
    EamDocumentAssignmentsService,
    EamDocumentsService,
    EamFailureCodesService,
    EamFailureHistoryService,
    EamFmeaItemsService,
    EamFmeaStudiesService,
    EamFunctionalLocationsService,
    EamInspectionsService,
    EamIntegrationConnectionsService,
    EamIntegrationLogsService,
    EamJsaService,
    EamJsaStepsService,
    EamKitContentsService,
    EamKitsService,
    EamKpiDefinitionsService,
    EamKpiValuesService,
    EamLanggraphWorkflowsService,
    EamLlmConfigsService,
    EamLotoService,
    EamMaintenanceCostsService,
    EamMeterAssignmentsService,
    EamMeterReadingsService,
    EamMetersService,
    EamMlModelsService,
    EamNotificationsService,
    EamOptimizationProblemsService,
    EamOptimizationSolutionsService,
    EamOrtoolsProblemsService,
    EamPermitsService,
    EamPhysicalLocationsService,
    EamPmAssignmentsService,
    EamPmScheduleOptimizedService,
    EamPmSchedulesService,
    EamPmSchedulingProblemsService,
    EamPmTemplatesService,
    EamPredictionsService,
    EamPredictiveMaintenanceService,
    EamPromptTemplatesService,
    EamRcaActionsService,
    EamRcaCausesService,
    EamRcaStudiesService,
    EamRcmAnalysesService,
    EamRcmStudiesService,
    EamSafetyPlansService,
    EamScenariosService,
    EamScipyAnalysesService,
    EamServiceContractsService,
    EamSparePartsConsumptionService,
    EamSparePartsStorageService,
    EamStorageLocationsService,
    EamStorageOptimizationProblemsService,
    EamTechnicianCertificationsService,
    EamTechnicianRoutesService,
    EamTechnicianRoutingProblemsService,
    EamTechnicianSkillsService,
    EamTechniciansService,
    EamToolsService,
    EamVectorDocumentsService,
    EamWarrantiesService,
    EamWarrantyClaimsService,
    EamWoLaborService,
    EamWoOperationsService,
    EamWoTasksService,
    EamWoToolsService,
    EamWorkOrderStatusesService,
    EamWorkOrderTypesService,
    EamWorkOrdersService,
)
from app.modules.eam.schemas import (
    EamAiAgentLogsCreate,
    EamAiAgentLogsUpdate,
    EamAiAgentLogsOut,
    EamAiDecisionsCreate,
    EamAiDecisionsUpdate,
    EamAiDecisionsOut,
    EamAiWorkflowStateCreate,
    EamAiWorkflowStateUpdate,
    EamAiWorkflowStateOut,
    EamAlertsCreate,
    EamAlertsUpdate,
    EamAlertsOut,
    EamAssetAttachmentsCreate,
    EamAssetAttachmentsUpdate,
    EamAssetAttachmentsOut,
    EamAssetBomCreate,
    EamAssetBomUpdate,
    EamAssetBomOut,
    EamAssetCategoriesCreate,
    EamAssetCategoriesUpdate,
    EamAssetCategoriesOut,
    EamAssetCriticalityCreate,
    EamAssetCriticalityUpdate,
    EamAssetCriticalityOut,
    EamAssetHierarchyCreate,
    EamAssetHierarchyUpdate,
    EamAssetHierarchyOut,
    EamAssetTypesCreate,
    EamAssetTypesUpdate,
    EamAssetTypesOut,
    EamAssetVendorsCreate,
    EamAssetVendorsUpdate,
    EamAssetVendorsOut,
    EamAssetsCreate,
    EamAssetsUpdate,
    EamAssetsOut,
    EamAuditLogCreate,
    EamAuditLogUpdate,
    EamAuditLogOut,
    EamBudgetsCreate,
    EamBudgetsUpdate,
    EamBudgetsOut,
    EamCalibrationRequirementsCreate,
    EamCalibrationRequirementsUpdate,
    EamCalibrationRequirementsOut,
    EamCalibrationResultsCreate,
    EamCalibrationResultsUpdate,
    EamCalibrationResultsOut,
    EamComplianceRecordsCreate,
    EamComplianceRecordsUpdate,
    EamComplianceRecordsOut,
    EamComplianceRequirementsCreate,
    EamComplianceRequirementsUpdate,
    EamComplianceRequirementsOut,
    EamComponentsCreate,
    EamComponentsUpdate,
    EamComponentsOut,
    EamConditionMonitoringProgramsCreate,
    EamConditionMonitoringProgramsUpdate,
    EamConditionMonitoringProgramsOut,
    EamConditionReadingsCreate,
    EamConditionReadingsUpdate,
    EamConditionReadingsOut,
    EamContractAssetsCreate,
    EamContractAssetsUpdate,
    EamContractAssetsOut,
    EamCraftsCreate,
    EamCraftsUpdate,
    EamCraftsOut,
    EamDecommissionPlansCreate,
    EamDecommissionPlansUpdate,
    EamDecommissionPlansOut,
    EamDocumentAssignmentsCreate,
    EamDocumentAssignmentsUpdate,
    EamDocumentAssignmentsOut,
    EamDocumentsCreate,
    EamDocumentsUpdate,
    EamDocumentsOut,
    EamFailureCodesCreate,
    EamFailureCodesUpdate,
    EamFailureCodesOut,
    EamFailureHistoryCreate,
    EamFailureHistoryUpdate,
    EamFailureHistoryOut,
    EamFmeaItemsCreate,
    EamFmeaItemsUpdate,
    EamFmeaItemsOut,
    EamFmeaStudiesCreate,
    EamFmeaStudiesUpdate,
    EamFmeaStudiesOut,
    EamFunctionalLocationsCreate,
    EamFunctionalLocationsUpdate,
    EamFunctionalLocationsOut,
    EamInspectionsCreate,
    EamInspectionsUpdate,
    EamInspectionsOut,
    EamIntegrationConnectionsCreate,
    EamIntegrationConnectionsUpdate,
    EamIntegrationConnectionsOut,
    EamIntegrationLogsCreate,
    EamIntegrationLogsUpdate,
    EamIntegrationLogsOut,
    EamJsaCreate,
    EamJsaUpdate,
    EamJsaOut,
    EamJsaStepsCreate,
    EamJsaStepsUpdate,
    EamJsaStepsOut,
    EamKitContentsCreate,
    EamKitContentsUpdate,
    EamKitContentsOut,
    EamKitsCreate,
    EamKitsUpdate,
    EamKitsOut,
    EamKpiDefinitionsCreate,
    EamKpiDefinitionsUpdate,
    EamKpiDefinitionsOut,
    EamKpiValuesCreate,
    EamKpiValuesUpdate,
    EamKpiValuesOut,
    EamLanggraphWorkflowsCreate,
    EamLanggraphWorkflowsUpdate,
    EamLanggraphWorkflowsOut,
    EamLlmConfigsCreate,
    EamLlmConfigsUpdate,
    EamLlmConfigsOut,
    EamLotoCreate,
    EamLotoUpdate,
    EamLotoOut,
    EamMaintenanceCostsCreate,
    EamMaintenanceCostsUpdate,
    EamMaintenanceCostsOut,
    EamMeterAssignmentsCreate,
    EamMeterAssignmentsUpdate,
    EamMeterAssignmentsOut,
    EamMeterReadingsCreate,
    EamMeterReadingsUpdate,
    EamMeterReadingsOut,
    EamMetersCreate,
    EamMetersUpdate,
    EamMetersOut,
    EamMlModelsCreate,
    EamMlModelsUpdate,
    EamMlModelsOut,
    EamNotificationsCreate,
    EamNotificationsUpdate,
    EamNotificationsOut,
    EamOptimizationProblemsCreate,
    EamOptimizationProblemsUpdate,
    EamOptimizationProblemsOut,
    EamOptimizationSolutionsCreate,
    EamOptimizationSolutionsUpdate,
    EamOptimizationSolutionsOut,
    EamOrtoolsProblemsCreate,
    EamOrtoolsProblemsUpdate,
    EamOrtoolsProblemsOut,
    EamPermitsCreate,
    EamPermitsUpdate,
    EamPermitsOut,
    EamPhysicalLocationsCreate,
    EamPhysicalLocationsUpdate,
    EamPhysicalLocationsOut,
    EamPmAssignmentsCreate,
    EamPmAssignmentsUpdate,
    EamPmAssignmentsOut,
    EamPmScheduleOptimizedCreate,
    EamPmScheduleOptimizedUpdate,
    EamPmScheduleOptimizedOut,
    EamPmSchedulesCreate,
    EamPmSchedulesUpdate,
    EamPmSchedulesOut,
    EamPmSchedulingProblemsCreate,
    EamPmSchedulingProblemsUpdate,
    EamPmSchedulingProblemsOut,
    EamPmTemplatesCreate,
    EamPmTemplatesUpdate,
    EamPmTemplatesOut,
    EamPredictionsCreate,
    EamPredictionsUpdate,
    EamPredictionsOut,
    EamPredictiveMaintenanceCreate,
    EamPredictiveMaintenanceUpdate,
    EamPredictiveMaintenanceOut,
    EamPromptTemplatesCreate,
    EamPromptTemplatesUpdate,
    EamPromptTemplatesOut,
    EamRcaActionsCreate,
    EamRcaActionsUpdate,
    EamRcaActionsOut,
    EamRcaCausesCreate,
    EamRcaCausesUpdate,
    EamRcaCausesOut,
    EamRcaStudiesCreate,
    EamRcaStudiesUpdate,
    EamRcaStudiesOut,
    EamRcmAnalysesCreate,
    EamRcmAnalysesUpdate,
    EamRcmAnalysesOut,
    EamRcmStudiesCreate,
    EamRcmStudiesUpdate,
    EamRcmStudiesOut,
    EamSafetyPlansCreate,
    EamSafetyPlansUpdate,
    EamSafetyPlansOut,
    EamScenariosCreate,
    EamScenariosUpdate,
    EamScenariosOut,
    EamScipyAnalysesCreate,
    EamScipyAnalysesUpdate,
    EamScipyAnalysesOut,
    EamServiceContractsCreate,
    EamServiceContractsUpdate,
    EamServiceContractsOut,
    EamSparePartsConsumptionCreate,
    EamSparePartsConsumptionUpdate,
    EamSparePartsConsumptionOut,
    EamSparePartsStorageCreate,
    EamSparePartsStorageUpdate,
    EamSparePartsStorageOut,
    EamStorageLocationsCreate,
    EamStorageLocationsUpdate,
    EamStorageLocationsOut,
    EamStorageOptimizationProblemsCreate,
    EamStorageOptimizationProblemsUpdate,
    EamStorageOptimizationProblemsOut,
    EamTechnicianCertificationsCreate,
    EamTechnicianCertificationsUpdate,
    EamTechnicianCertificationsOut,
    EamTechnicianRoutesCreate,
    EamTechnicianRoutesUpdate,
    EamTechnicianRoutesOut,
    EamTechnicianRoutingProblemsCreate,
    EamTechnicianRoutingProblemsUpdate,
    EamTechnicianRoutingProblemsOut,
    EamTechnicianSkillsCreate,
    EamTechnicianSkillsUpdate,
    EamTechnicianSkillsOut,
    EamTechniciansCreate,
    EamTechniciansUpdate,
    EamTechniciansOut,
    EamToolsCreate,
    EamToolsUpdate,
    EamToolsOut,
    EamVectorDocumentsCreate,
    EamVectorDocumentsUpdate,
    EamVectorDocumentsOut,
    EamWarrantiesCreate,
    EamWarrantiesUpdate,
    EamWarrantiesOut,
    EamWarrantyClaimsCreate,
    EamWarrantyClaimsUpdate,
    EamWarrantyClaimsOut,
    EamWoLaborCreate,
    EamWoLaborUpdate,
    EamWoLaborOut,
    EamWoOperationsCreate,
    EamWoOperationsUpdate,
    EamWoOperationsOut,
    EamWoTasksCreate,
    EamWoTasksUpdate,
    EamWoTasksOut,
    EamWoToolsCreate,
    EamWoToolsUpdate,
    EamWoToolsOut,
    EamWorkOrderStatusesCreate,
    EamWorkOrderStatusesUpdate,
    EamWorkOrderStatusesOut,
    EamWorkOrderTypesCreate,
    EamWorkOrderTypesUpdate,
    EamWorkOrderTypesOut,
    EamWorkOrdersCreate,
    EamWorkOrdersUpdate,
    EamWorkOrdersOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/eam_ai_agent_logs", response_model=PaginatedResponse[EamAiAgentLogsOut])
async def list_eam_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_ai_agent_logs/{entity_id}", response_model=EamAiAgentLogsOut)
async def get_eam_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAiAgentLogsService(db).get(entity_id)

@router.post("/eam_ai_agent_logs", response_model=EamAiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_ai_agent_logs(
    data: EamAiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiAgentLogsService(db).create(data)

@router.put("/eam_ai_agent_logs/{entity_id}", response_model=EamAiAgentLogsOut)
async def update_eam_ai_agent_logs(
    entity_id: uuid.UUID,
    data: EamAiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiAgentLogsService(db).update(entity_id, data)

@router.delete("/eam_ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAiAgentLogsService(db).delete(entity_id)

@router.get("/eam_ai_decisions", response_model=PaginatedResponse[EamAiDecisionsOut])
async def list_eam_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_ai_decisions/{entity_id}", response_model=EamAiDecisionsOut)
async def get_eam_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAiDecisionsService(db).get(entity_id)

@router.post("/eam_ai_decisions", response_model=EamAiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_ai_decisions(
    data: EamAiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiDecisionsService(db).create(data)

@router.put("/eam_ai_decisions/{entity_id}", response_model=EamAiDecisionsOut)
async def update_eam_ai_decisions(
    entity_id: uuid.UUID,
    data: EamAiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiDecisionsService(db).update(entity_id, data)

@router.delete("/eam_ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAiDecisionsService(db).delete(entity_id)

@router.get("/eam_ai_workflow_state", response_model=PaginatedResponse[EamAiWorkflowStateOut])
async def list_eam_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_ai_workflow_state/{entity_id}", response_model=EamAiWorkflowStateOut)
async def get_eam_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAiWorkflowStateService(db).get(entity_id)

@router.post("/eam_ai_workflow_state", response_model=EamAiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_eam_ai_workflow_state(
    data: EamAiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiWorkflowStateService(db).create(data)

@router.put("/eam_ai_workflow_state/{entity_id}", response_model=EamAiWorkflowStateOut)
async def update_eam_ai_workflow_state(
    entity_id: uuid.UUID,
    data: EamAiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAiWorkflowStateService(db).update(entity_id, data)

@router.delete("/eam_ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAiWorkflowStateService(db).delete(entity_id)

@router.get("/eam_alerts", response_model=PaginatedResponse[EamAlertsOut])
async def list_eam_alerts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAlertsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["alert_number", "alert_type_code", "severity_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_alerts/{entity_id}", response_model=EamAlertsOut)
async def get_eam_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAlertsService(db).get(entity_id)

@router.post("/eam_alerts", response_model=EamAlertsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_alerts(
    data: EamAlertsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAlertsService(db).create(data)

@router.put("/eam_alerts/{entity_id}", response_model=EamAlertsOut)
async def update_eam_alerts(
    entity_id: uuid.UUID,
    data: EamAlertsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAlertsService(db).update(entity_id, data)

@router.delete("/eam_alerts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_alerts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAlertsService(db).delete(entity_id)

@router.get("/eam_asset_attachments", response_model=PaginatedResponse[EamAssetAttachmentsOut])
async def list_eam_asset_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["attachment_type_code", "attachment_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_attachments/{entity_id}", response_model=EamAssetAttachmentsOut)
async def get_eam_asset_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetAttachmentsService(db).get(entity_id)

@router.post("/eam_asset_attachments", response_model=EamAssetAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_attachments(
    data: EamAssetAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetAttachmentsService(db).create(data)

@router.put("/eam_asset_attachments/{entity_id}", response_model=EamAssetAttachmentsOut)
async def update_eam_asset_attachments(
    entity_id: uuid.UUID,
    data: EamAssetAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetAttachmentsService(db).update(entity_id, data)

@router.delete("/eam_asset_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetAttachmentsService(db).delete(entity_id)

@router.get("/eam_asset_bom", response_model=PaginatedResponse[EamAssetBomOut])
async def list_eam_asset_bom(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetBomService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "item_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_bom/{entity_id}", response_model=EamAssetBomOut)
async def get_eam_asset_bom(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetBomService(db).get(entity_id)

@router.post("/eam_asset_bom", response_model=EamAssetBomOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_bom(
    data: EamAssetBomCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetBomService(db).create(data)

@router.put("/eam_asset_bom/{entity_id}", response_model=EamAssetBomOut)
async def update_eam_asset_bom(
    entity_id: uuid.UUID,
    data: EamAssetBomUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetBomService(db).update(entity_id, data)

@router.delete("/eam_asset_bom/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_bom(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetBomService(db).delete(entity_id)

@router.get("/eam_asset_categories", response_model=PaginatedResponse[EamAssetCategoriesOut])
async def list_eam_asset_categories(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetCategoriesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["category_code", "category_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_categories/{entity_id}", response_model=EamAssetCategoriesOut)
async def get_eam_asset_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetCategoriesService(db).get(entity_id)

@router.post("/eam_asset_categories", response_model=EamAssetCategoriesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_categories(
    data: EamAssetCategoriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetCategoriesService(db).create(data)

@router.put("/eam_asset_categories/{entity_id}", response_model=EamAssetCategoriesOut)
async def update_eam_asset_categories(
    entity_id: uuid.UUID,
    data: EamAssetCategoriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetCategoriesService(db).update(entity_id, data)

@router.delete("/eam_asset_categories/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetCategoriesService(db).delete(entity_id)

@router.get("/eam_asset_criticality", response_model=PaginatedResponse[EamAssetCriticalityOut])
async def list_eam_asset_criticality(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetCriticalityService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["criticality_code", "criticality_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_criticality/{entity_id}", response_model=EamAssetCriticalityOut)
async def get_eam_asset_criticality(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetCriticalityService(db).get(entity_id)

@router.post("/eam_asset_criticality", response_model=EamAssetCriticalityOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_criticality(
    data: EamAssetCriticalityCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetCriticalityService(db).create(data)

@router.put("/eam_asset_criticality/{entity_id}", response_model=EamAssetCriticalityOut)
async def update_eam_asset_criticality(
    entity_id: uuid.UUID,
    data: EamAssetCriticalityUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetCriticalityService(db).update(entity_id, data)

@router.delete("/eam_asset_criticality/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_criticality(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetCriticalityService(db).delete(entity_id)

@router.get("/eam_asset_hierarchy", response_model=PaginatedResponse[EamAssetHierarchyOut])
async def list_eam_asset_hierarchy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetHierarchyService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["relationship_type_code", "position_description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_hierarchy/{entity_id}", response_model=EamAssetHierarchyOut)
async def get_eam_asset_hierarchy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetHierarchyService(db).get(entity_id)

@router.post("/eam_asset_hierarchy", response_model=EamAssetHierarchyOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_hierarchy(
    data: EamAssetHierarchyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetHierarchyService(db).create(data)

@router.put("/eam_asset_hierarchy/{entity_id}", response_model=EamAssetHierarchyOut)
async def update_eam_asset_hierarchy(
    entity_id: uuid.UUID,
    data: EamAssetHierarchyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetHierarchyService(db).update(entity_id, data)

@router.delete("/eam_asset_hierarchy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_hierarchy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetHierarchyService(db).delete(entity_id)

@router.get("/eam_asset_types", response_model=PaginatedResponse[EamAssetTypesOut])
async def list_eam_asset_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_type_code", "asset_type_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_types/{entity_id}", response_model=EamAssetTypesOut)
async def get_eam_asset_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetTypesService(db).get(entity_id)

@router.post("/eam_asset_types", response_model=EamAssetTypesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_types(
    data: EamAssetTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetTypesService(db).create(data)

@router.put("/eam_asset_types/{entity_id}", response_model=EamAssetTypesOut)
async def update_eam_asset_types(
    entity_id: uuid.UUID,
    data: EamAssetTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetTypesService(db).update(entity_id, data)

@router.delete("/eam_asset_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetTypesService(db).delete(entity_id)

@router.get("/eam_asset_vendors", response_model=PaginatedResponse[EamAssetVendorsOut])
async def list_eam_asset_vendors(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetVendorsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["vendor_code", "vendor_name", "vendor_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_asset_vendors/{entity_id}", response_model=EamAssetVendorsOut)
async def get_eam_asset_vendors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetVendorsService(db).get(entity_id)

@router.post("/eam_asset_vendors", response_model=EamAssetVendorsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_asset_vendors(
    data: EamAssetVendorsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetVendorsService(db).create(data)

@router.put("/eam_asset_vendors/{entity_id}", response_model=EamAssetVendorsOut)
async def update_eam_asset_vendors(
    entity_id: uuid.UUID,
    data: EamAssetVendorsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetVendorsService(db).update(entity_id, data)

@router.delete("/eam_asset_vendors/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_asset_vendors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetVendorsService(db).delete(entity_id)

@router.get("/eam_assets", response_model=PaginatedResponse[EamAssetsOut])
async def list_eam_assets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAssetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_number", "asset_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_assets/{entity_id}", response_model=EamAssetsOut)
async def get_eam_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAssetsService(db).get(entity_id)

@router.post("/eam_assets", response_model=EamAssetsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_assets(
    data: EamAssetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetsService(db).create(data)

@router.put("/eam_assets/{entity_id}", response_model=EamAssetsOut)
async def update_eam_assets(
    entity_id: uuid.UUID,
    data: EamAssetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAssetsService(db).update(entity_id, data)

@router.delete("/eam_assets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAssetsService(db).delete(entity_id)

@router.get("/eam_audit_log", response_model=PaginatedResponse[EamAuditLogOut])
async def list_eam_audit_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamAuditLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["table_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_audit_log/{entity_id}", response_model=EamAuditLogOut)
async def get_eam_audit_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamAuditLogService(db).get(entity_id)

@router.post("/eam_audit_log", response_model=EamAuditLogOut, status_code=status.HTTP_201_CREATED)
async def create_eam_audit_log(
    data: EamAuditLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAuditLogService(db).create(data)

@router.put("/eam_audit_log/{entity_id}", response_model=EamAuditLogOut)
async def update_eam_audit_log(
    entity_id: uuid.UUID,
    data: EamAuditLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamAuditLogService(db).update(entity_id, data)

@router.delete("/eam_audit_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_audit_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamAuditLogService(db).delete(entity_id)

@router.get("/eam_budgets", response_model=PaginatedResponse[EamBudgetsOut])
async def list_eam_budgets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamBudgetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["budget_code", "budget_name", "budget_category_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_budgets/{entity_id}", response_model=EamBudgetsOut)
async def get_eam_budgets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamBudgetsService(db).get(entity_id)

@router.post("/eam_budgets", response_model=EamBudgetsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_budgets(
    data: EamBudgetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamBudgetsService(db).create(data)

@router.put("/eam_budgets/{entity_id}", response_model=EamBudgetsOut)
async def update_eam_budgets(
    entity_id: uuid.UUID,
    data: EamBudgetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamBudgetsService(db).update(entity_id, data)

@router.delete("/eam_budgets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_budgets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamBudgetsService(db).delete(entity_id)

@router.get("/eam_calibration_requirements", response_model=PaginatedResponse[EamCalibrationRequirementsOut])
async def list_eam_calibration_requirements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamCalibrationRequirementsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["calibration_code", "calibration_name", "calibration_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_calibration_requirements/{entity_id}", response_model=EamCalibrationRequirementsOut)
async def get_eam_calibration_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamCalibrationRequirementsService(db).get(entity_id)

@router.post("/eam_calibration_requirements", response_model=EamCalibrationRequirementsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_calibration_requirements(
    data: EamCalibrationRequirementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCalibrationRequirementsService(db).create(data)

@router.put("/eam_calibration_requirements/{entity_id}", response_model=EamCalibrationRequirementsOut)
async def update_eam_calibration_requirements(
    entity_id: uuid.UUID,
    data: EamCalibrationRequirementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCalibrationRequirementsService(db).update(entity_id, data)

@router.delete("/eam_calibration_requirements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_calibration_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamCalibrationRequirementsService(db).delete(entity_id)

@router.get("/eam_calibration_results", response_model=PaginatedResponse[EamCalibrationResultsOut])
async def list_eam_calibration_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamCalibrationResultsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["certificate_number", "result_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_calibration_results/{entity_id}", response_model=EamCalibrationResultsOut)
async def get_eam_calibration_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamCalibrationResultsService(db).get(entity_id)

@router.post("/eam_calibration_results", response_model=EamCalibrationResultsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_calibration_results(
    data: EamCalibrationResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCalibrationResultsService(db).create(data)

@router.put("/eam_calibration_results/{entity_id}", response_model=EamCalibrationResultsOut)
async def update_eam_calibration_results(
    entity_id: uuid.UUID,
    data: EamCalibrationResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCalibrationResultsService(db).update(entity_id, data)

@router.delete("/eam_calibration_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_calibration_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamCalibrationResultsService(db).delete(entity_id)

@router.get("/eam_compliance_records", response_model=PaginatedResponse[EamComplianceRecordsOut])
async def list_eam_compliance_records(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamComplianceRecordsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["result_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_compliance_records/{entity_id}", response_model=EamComplianceRecordsOut)
async def get_eam_compliance_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamComplianceRecordsService(db).get(entity_id)

@router.post("/eam_compliance_records", response_model=EamComplianceRecordsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_compliance_records(
    data: EamComplianceRecordsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComplianceRecordsService(db).create(data)

@router.put("/eam_compliance_records/{entity_id}", response_model=EamComplianceRecordsOut)
async def update_eam_compliance_records(
    entity_id: uuid.UUID,
    data: EamComplianceRecordsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComplianceRecordsService(db).update(entity_id, data)

@router.delete("/eam_compliance_records/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_compliance_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamComplianceRecordsService(db).delete(entity_id)

@router.get("/eam_compliance_requirements", response_model=PaginatedResponse[EamComplianceRequirementsOut])
async def list_eam_compliance_requirements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamComplianceRequirementsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["requirement_code", "requirement_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_compliance_requirements/{entity_id}", response_model=EamComplianceRequirementsOut)
async def get_eam_compliance_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamComplianceRequirementsService(db).get(entity_id)

@router.post("/eam_compliance_requirements", response_model=EamComplianceRequirementsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_compliance_requirements(
    data: EamComplianceRequirementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComplianceRequirementsService(db).create(data)

@router.put("/eam_compliance_requirements/{entity_id}", response_model=EamComplianceRequirementsOut)
async def update_eam_compliance_requirements(
    entity_id: uuid.UUID,
    data: EamComplianceRequirementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComplianceRequirementsService(db).update(entity_id, data)

@router.delete("/eam_compliance_requirements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_compliance_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamComplianceRequirementsService(db).delete(entity_id)

@router.get("/eam_components", response_model=PaginatedResponse[EamComponentsOut])
async def list_eam_components(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamComponentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["component_code", "component_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_components/{entity_id}", response_model=EamComponentsOut)
async def get_eam_components(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamComponentsService(db).get(entity_id)

@router.post("/eam_components", response_model=EamComponentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_components(
    data: EamComponentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComponentsService(db).create(data)

@router.put("/eam_components/{entity_id}", response_model=EamComponentsOut)
async def update_eam_components(
    entity_id: uuid.UUID,
    data: EamComponentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamComponentsService(db).update(entity_id, data)

@router.delete("/eam_components/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_components(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamComponentsService(db).delete(entity_id)

@router.get("/eam_condition_monitoring_programs", response_model=PaginatedResponse[EamConditionMonitoringProgramsOut])
async def list_eam_condition_monitoring_programs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamConditionMonitoringProgramsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["program_code", "program_name", "technology_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_condition_monitoring_programs/{entity_id}", response_model=EamConditionMonitoringProgramsOut)
async def get_eam_condition_monitoring_programs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamConditionMonitoringProgramsService(db).get(entity_id)

@router.post("/eam_condition_monitoring_programs", response_model=EamConditionMonitoringProgramsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_condition_monitoring_programs(
    data: EamConditionMonitoringProgramsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamConditionMonitoringProgramsService(db).create(data)

@router.put("/eam_condition_monitoring_programs/{entity_id}", response_model=EamConditionMonitoringProgramsOut)
async def update_eam_condition_monitoring_programs(
    entity_id: uuid.UUID,
    data: EamConditionMonitoringProgramsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamConditionMonitoringProgramsService(db).update(entity_id, data)

@router.delete("/eam_condition_monitoring_programs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_condition_monitoring_programs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamConditionMonitoringProgramsService(db).delete(entity_id)

@router.get("/eam_condition_readings", response_model=PaginatedResponse[EamConditionReadingsOut])
async def list_eam_condition_readings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamConditionReadingsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["severity_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_condition_readings/{entity_id}", response_model=EamConditionReadingsOut)
async def get_eam_condition_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamConditionReadingsService(db).get(entity_id)

@router.post("/eam_condition_readings", response_model=EamConditionReadingsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_condition_readings(
    data: EamConditionReadingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamConditionReadingsService(db).create(data)

@router.put("/eam_condition_readings/{entity_id}", response_model=EamConditionReadingsOut)
async def update_eam_condition_readings(
    entity_id: uuid.UUID,
    data: EamConditionReadingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamConditionReadingsService(db).update(entity_id, data)

@router.delete("/eam_condition_readings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_condition_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamConditionReadingsService(db).delete(entity_id)

@router.get("/eam_contract_assets", response_model=PaginatedResponse[EamContractAssetsOut])
async def list_eam_contract_assets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamContractAssetsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_contract_assets/{entity_id}", response_model=EamContractAssetsOut)
async def get_eam_contract_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamContractAssetsService(db).get(entity_id)

@router.post("/eam_contract_assets", response_model=EamContractAssetsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_contract_assets(
    data: EamContractAssetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamContractAssetsService(db).create(data)

@router.put("/eam_contract_assets/{entity_id}", response_model=EamContractAssetsOut)
async def update_eam_contract_assets(
    entity_id: uuid.UUID,
    data: EamContractAssetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamContractAssetsService(db).update(entity_id, data)

@router.delete("/eam_contract_assets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_contract_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamContractAssetsService(db).delete(entity_id)

@router.get("/eam_crafts", response_model=PaginatedResponse[EamCraftsOut])
async def list_eam_crafts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamCraftsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["craft_code", "craft_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_crafts/{entity_id}", response_model=EamCraftsOut)
async def get_eam_crafts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamCraftsService(db).get(entity_id)

@router.post("/eam_crafts", response_model=EamCraftsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_crafts(
    data: EamCraftsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCraftsService(db).create(data)

@router.put("/eam_crafts/{entity_id}", response_model=EamCraftsOut)
async def update_eam_crafts(
    entity_id: uuid.UUID,
    data: EamCraftsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamCraftsService(db).update(entity_id, data)

@router.delete("/eam_crafts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_crafts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamCraftsService(db).delete(entity_id)

@router.get("/eam_decommission_plans", response_model=PaginatedResponse[EamDecommissionPlansOut])
async def list_eam_decommission_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamDecommissionPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_number", "plan_name", "plan_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_decommission_plans/{entity_id}", response_model=EamDecommissionPlansOut)
async def get_eam_decommission_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamDecommissionPlansService(db).get(entity_id)

@router.post("/eam_decommission_plans", response_model=EamDecommissionPlansOut, status_code=status.HTTP_201_CREATED)
async def create_eam_decommission_plans(
    data: EamDecommissionPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDecommissionPlansService(db).create(data)

@router.put("/eam_decommission_plans/{entity_id}", response_model=EamDecommissionPlansOut)
async def update_eam_decommission_plans(
    entity_id: uuid.UUID,
    data: EamDecommissionPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDecommissionPlansService(db).update(entity_id, data)

@router.delete("/eam_decommission_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_decommission_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamDecommissionPlansService(db).delete(entity_id)

@router.get("/eam_document_assignments", response_model=PaginatedResponse[EamDocumentAssignmentsOut])
async def list_eam_document_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamDocumentAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_document_assignments/{entity_id}", response_model=EamDocumentAssignmentsOut)
async def get_eam_document_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamDocumentAssignmentsService(db).get(entity_id)

@router.post("/eam_document_assignments", response_model=EamDocumentAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_document_assignments(
    data: EamDocumentAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDocumentAssignmentsService(db).create(data)

@router.put("/eam_document_assignments/{entity_id}", response_model=EamDocumentAssignmentsOut)
async def update_eam_document_assignments(
    entity_id: uuid.UUID,
    data: EamDocumentAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDocumentAssignmentsService(db).update(entity_id, data)

@router.delete("/eam_document_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_document_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamDocumentAssignmentsService(db).delete(entity_id)

@router.get("/eam_documents", response_model=PaginatedResponse[EamDocumentsOut])
async def list_eam_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["document_number", "document_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_documents/{entity_id}", response_model=EamDocumentsOut)
async def get_eam_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamDocumentsService(db).get(entity_id)

@router.post("/eam_documents", response_model=EamDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_documents(
    data: EamDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDocumentsService(db).create(data)

@router.put("/eam_documents/{entity_id}", response_model=EamDocumentsOut)
async def update_eam_documents(
    entity_id: uuid.UUID,
    data: EamDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamDocumentsService(db).update(entity_id, data)

@router.delete("/eam_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamDocumentsService(db).delete(entity_id)

@router.get("/eam_failure_codes", response_model=PaginatedResponse[EamFailureCodesOut])
async def list_eam_failure_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamFailureCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["failure_code", "failure_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_failure_codes/{entity_id}", response_model=EamFailureCodesOut)
async def get_eam_failure_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamFailureCodesService(db).get(entity_id)

@router.post("/eam_failure_codes", response_model=EamFailureCodesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_failure_codes(
    data: EamFailureCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFailureCodesService(db).create(data)

@router.put("/eam_failure_codes/{entity_id}", response_model=EamFailureCodesOut)
async def update_eam_failure_codes(
    entity_id: uuid.UUID,
    data: EamFailureCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFailureCodesService(db).update(entity_id, data)

@router.delete("/eam_failure_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_failure_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamFailureCodesService(db).delete(entity_id)

@router.get("/eam_failure_history", response_model=PaginatedResponse[EamFailureHistoryOut])
async def list_eam_failure_history(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamFailureHistoryService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_failure_history/{entity_id}", response_model=EamFailureHistoryOut)
async def get_eam_failure_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamFailureHistoryService(db).get(entity_id)

@router.post("/eam_failure_history", response_model=EamFailureHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_eam_failure_history(
    data: EamFailureHistoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFailureHistoryService(db).create(data)

@router.put("/eam_failure_history/{entity_id}", response_model=EamFailureHistoryOut)
async def update_eam_failure_history(
    entity_id: uuid.UUID,
    data: EamFailureHistoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFailureHistoryService(db).update(entity_id, data)

@router.delete("/eam_failure_history/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_failure_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamFailureHistoryService(db).delete(entity_id)

@router.get("/eam_fmea_items", response_model=PaginatedResponse[EamFmeaItemsOut])
async def list_eam_fmea_items(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamFmeaItemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_fmea_items/{entity_id}", response_model=EamFmeaItemsOut)
async def get_eam_fmea_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamFmeaItemsService(db).get(entity_id)

@router.post("/eam_fmea_items", response_model=EamFmeaItemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_fmea_items(
    data: EamFmeaItemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFmeaItemsService(db).create(data)

@router.put("/eam_fmea_items/{entity_id}", response_model=EamFmeaItemsOut)
async def update_eam_fmea_items(
    entity_id: uuid.UUID,
    data: EamFmeaItemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFmeaItemsService(db).update(entity_id, data)

@router.delete("/eam_fmea_items/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_fmea_items(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamFmeaItemsService(db).delete(entity_id)

@router.get("/eam_fmea_studies", response_model=PaginatedResponse[EamFmeaStudiesOut])
async def list_eam_fmea_studies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamFmeaStudiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["study_code", "study_name", "fmea_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_fmea_studies/{entity_id}", response_model=EamFmeaStudiesOut)
async def get_eam_fmea_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamFmeaStudiesService(db).get(entity_id)

@router.post("/eam_fmea_studies", response_model=EamFmeaStudiesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_fmea_studies(
    data: EamFmeaStudiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFmeaStudiesService(db).create(data)

@router.put("/eam_fmea_studies/{entity_id}", response_model=EamFmeaStudiesOut)
async def update_eam_fmea_studies(
    entity_id: uuid.UUID,
    data: EamFmeaStudiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFmeaStudiesService(db).update(entity_id, data)

@router.delete("/eam_fmea_studies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_fmea_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamFmeaStudiesService(db).delete(entity_id)

@router.get("/eam_functional_locations", response_model=PaginatedResponse[EamFunctionalLocationsOut])
async def list_eam_functional_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamFunctionalLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_functional_locations/{entity_id}", response_model=EamFunctionalLocationsOut)
async def get_eam_functional_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamFunctionalLocationsService(db).get(entity_id)

@router.post("/eam_functional_locations", response_model=EamFunctionalLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_functional_locations(
    data: EamFunctionalLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFunctionalLocationsService(db).create(data)

@router.put("/eam_functional_locations/{entity_id}", response_model=EamFunctionalLocationsOut)
async def update_eam_functional_locations(
    entity_id: uuid.UUID,
    data: EamFunctionalLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamFunctionalLocationsService(db).update(entity_id, data)

@router.delete("/eam_functional_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_functional_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamFunctionalLocationsService(db).delete(entity_id)

@router.get("/eam_inspections", response_model=PaginatedResponse[EamInspectionsOut])
async def list_eam_inspections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamInspectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["inspection_number", "inspection_name", "inspection_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_inspections/{entity_id}", response_model=EamInspectionsOut)
async def get_eam_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamInspectionsService(db).get(entity_id)

@router.post("/eam_inspections", response_model=EamInspectionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_inspections(
    data: EamInspectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamInspectionsService(db).create(data)

@router.put("/eam_inspections/{entity_id}", response_model=EamInspectionsOut)
async def update_eam_inspections(
    entity_id: uuid.UUID,
    data: EamInspectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamInspectionsService(db).update(entity_id, data)

@router.delete("/eam_inspections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamInspectionsService(db).delete(entity_id)

@router.get("/eam_integration_connections", response_model=PaginatedResponse[EamIntegrationConnectionsOut])
async def list_eam_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamIntegrationConnectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["connection_code", "connection_name", "connection_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_integration_connections/{entity_id}", response_model=EamIntegrationConnectionsOut)
async def get_eam_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamIntegrationConnectionsService(db).get(entity_id)

@router.post("/eam_integration_connections", response_model=EamIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_integration_connections(
    data: EamIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamIntegrationConnectionsService(db).create(data)

@router.put("/eam_integration_connections/{entity_id}", response_model=EamIntegrationConnectionsOut)
async def update_eam_integration_connections(
    entity_id: uuid.UUID,
    data: EamIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/eam_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamIntegrationConnectionsService(db).delete(entity_id)

@router.get("/eam_integration_logs", response_model=PaginatedResponse[EamIntegrationLogsOut])
async def list_eam_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamIntegrationLogsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["log_type_code", "status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_integration_logs/{entity_id}", response_model=EamIntegrationLogsOut)
async def get_eam_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamIntegrationLogsService(db).get(entity_id)

@router.post("/eam_integration_logs", response_model=EamIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_integration_logs(
    data: EamIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamIntegrationLogsService(db).create(data)

@router.put("/eam_integration_logs/{entity_id}", response_model=EamIntegrationLogsOut)
async def update_eam_integration_logs(
    entity_id: uuid.UUID,
    data: EamIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamIntegrationLogsService(db).update(entity_id, data)

@router.delete("/eam_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamIntegrationLogsService(db).delete(entity_id)

@router.get("/eam_jsa", response_model=PaginatedResponse[EamJsaOut])
async def list_eam_jsa(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamJsaService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["jsa_number", "title", "jsa_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_jsa/{entity_id}", response_model=EamJsaOut)
async def get_eam_jsa(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamJsaService(db).get(entity_id)

@router.post("/eam_jsa", response_model=EamJsaOut, status_code=status.HTTP_201_CREATED)
async def create_eam_jsa(
    data: EamJsaCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamJsaService(db).create(data)

@router.put("/eam_jsa/{entity_id}", response_model=EamJsaOut)
async def update_eam_jsa(
    entity_id: uuid.UUID,
    data: EamJsaUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamJsaService(db).update(entity_id, data)

@router.delete("/eam_jsa/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_jsa(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamJsaService(db).delete(entity_id)

@router.get("/eam_jsa_steps", response_model=PaginatedResponse[EamJsaStepsOut])
async def list_eam_jsa_steps(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamJsaStepsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_jsa_steps/{entity_id}", response_model=EamJsaStepsOut)
async def get_eam_jsa_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamJsaStepsService(db).get(entity_id)

@router.post("/eam_jsa_steps", response_model=EamJsaStepsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_jsa_steps(
    data: EamJsaStepsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamJsaStepsService(db).create(data)

@router.put("/eam_jsa_steps/{entity_id}", response_model=EamJsaStepsOut)
async def update_eam_jsa_steps(
    entity_id: uuid.UUID,
    data: EamJsaStepsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamJsaStepsService(db).update(entity_id, data)

@router.delete("/eam_jsa_steps/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_jsa_steps(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamJsaStepsService(db).delete(entity_id)

@router.get("/eam_kit_contents", response_model=PaginatedResponse[EamKitContentsOut])
async def list_eam_kit_contents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamKitContentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_kit_contents/{entity_id}", response_model=EamKitContentsOut)
async def get_eam_kit_contents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamKitContentsService(db).get(entity_id)

@router.post("/eam_kit_contents", response_model=EamKitContentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_kit_contents(
    data: EamKitContentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKitContentsService(db).create(data)

@router.put("/eam_kit_contents/{entity_id}", response_model=EamKitContentsOut)
async def update_eam_kit_contents(
    entity_id: uuid.UUID,
    data: EamKitContentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKitContentsService(db).update(entity_id, data)

@router.delete("/eam_kit_contents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_kit_contents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamKitContentsService(db).delete(entity_id)

@router.get("/eam_kits", response_model=PaginatedResponse[EamKitsOut])
async def list_eam_kits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamKitsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kit_code", "kit_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_kits/{entity_id}", response_model=EamKitsOut)
async def get_eam_kits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamKitsService(db).get(entity_id)

@router.post("/eam_kits", response_model=EamKitsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_kits(
    data: EamKitsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKitsService(db).create(data)

@router.put("/eam_kits/{entity_id}", response_model=EamKitsOut)
async def update_eam_kits(
    entity_id: uuid.UUID,
    data: EamKitsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKitsService(db).update(entity_id, data)

@router.delete("/eam_kits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_kits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamKitsService(db).delete(entity_id)

@router.get("/eam_kpi_definitions", response_model=PaginatedResponse[EamKpiDefinitionsOut])
async def list_eam_kpi_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamKpiDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "kpi_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_kpi_definitions/{entity_id}", response_model=EamKpiDefinitionsOut)
async def get_eam_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamKpiDefinitionsService(db).get(entity_id)

@router.post("/eam_kpi_definitions", response_model=EamKpiDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_kpi_definitions(
    data: EamKpiDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKpiDefinitionsService(db).create(data)

@router.put("/eam_kpi_definitions/{entity_id}", response_model=EamKpiDefinitionsOut)
async def update_eam_kpi_definitions(
    entity_id: uuid.UUID,
    data: EamKpiDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKpiDefinitionsService(db).update(entity_id, data)

@router.delete("/eam_kpi_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamKpiDefinitionsService(db).delete(entity_id)

@router.get("/eam_kpi_values", response_model=PaginatedResponse[EamKpiValuesOut])
async def list_eam_kpi_values(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamKpiValuesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_kpi_values/{entity_id}", response_model=EamKpiValuesOut)
async def get_eam_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamKpiValuesService(db).get(entity_id)

@router.post("/eam_kpi_values", response_model=EamKpiValuesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_kpi_values(
    data: EamKpiValuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKpiValuesService(db).create(data)

@router.put("/eam_kpi_values/{entity_id}", response_model=EamKpiValuesOut)
async def update_eam_kpi_values(
    entity_id: uuid.UUID,
    data: EamKpiValuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamKpiValuesService(db).update(entity_id, data)

@router.delete("/eam_kpi_values/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamKpiValuesService(db).delete(entity_id)

@router.get("/eam_langgraph_workflows", response_model=PaginatedResponse[EamLanggraphWorkflowsOut])
async def list_eam_langgraph_workflows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamLanggraphWorkflowsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_name", "workflow_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_langgraph_workflows/{entity_id}", response_model=EamLanggraphWorkflowsOut)
async def get_eam_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamLanggraphWorkflowsService(db).get(entity_id)

@router.post("/eam_langgraph_workflows", response_model=EamLanggraphWorkflowsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_langgraph_workflows(
    data: EamLanggraphWorkflowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLanggraphWorkflowsService(db).create(data)

@router.put("/eam_langgraph_workflows/{entity_id}", response_model=EamLanggraphWorkflowsOut)
async def update_eam_langgraph_workflows(
    entity_id: uuid.UUID,
    data: EamLanggraphWorkflowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLanggraphWorkflowsService(db).update(entity_id, data)

@router.delete("/eam_langgraph_workflows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamLanggraphWorkflowsService(db).delete(entity_id)

@router.get("/eam_llm_configs", response_model=PaginatedResponse[EamLlmConfigsOut])
async def list_eam_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_name", "model_name", "config_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_llm_configs/{entity_id}", response_model=EamLlmConfigsOut)
async def get_eam_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamLlmConfigsService(db).get(entity_id)

@router.post("/eam_llm_configs", response_model=EamLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_llm_configs(
    data: EamLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLlmConfigsService(db).create(data)

@router.put("/eam_llm_configs/{entity_id}", response_model=EamLlmConfigsOut)
async def update_eam_llm_configs(
    entity_id: uuid.UUID,
    data: EamLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLlmConfigsService(db).update(entity_id, data)

@router.delete("/eam_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamLlmConfigsService(db).delete(entity_id)

@router.get("/eam_loto", response_model=PaginatedResponse[EamLotoOut])
async def list_eam_loto(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamLotoService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["loto_number", "loto_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_loto/{entity_id}", response_model=EamLotoOut)
async def get_eam_loto(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamLotoService(db).get(entity_id)

@router.post("/eam_loto", response_model=EamLotoOut, status_code=status.HTTP_201_CREATED)
async def create_eam_loto(
    data: EamLotoCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLotoService(db).create(data)

@router.put("/eam_loto/{entity_id}", response_model=EamLotoOut)
async def update_eam_loto(
    entity_id: uuid.UUID,
    data: EamLotoUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamLotoService(db).update(entity_id, data)

@router.delete("/eam_loto/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_loto(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamLotoService(db).delete(entity_id)

@router.get("/eam_maintenance_costs", response_model=PaginatedResponse[EamMaintenanceCostsOut])
async def list_eam_maintenance_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamMaintenanceCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cost_category_code", "cost_type_code", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_maintenance_costs/{entity_id}", response_model=EamMaintenanceCostsOut)
async def get_eam_maintenance_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamMaintenanceCostsService(db).get(entity_id)

@router.post("/eam_maintenance_costs", response_model=EamMaintenanceCostsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_maintenance_costs(
    data: EamMaintenanceCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMaintenanceCostsService(db).create(data)

@router.put("/eam_maintenance_costs/{entity_id}", response_model=EamMaintenanceCostsOut)
async def update_eam_maintenance_costs(
    entity_id: uuid.UUID,
    data: EamMaintenanceCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMaintenanceCostsService(db).update(entity_id, data)

@router.delete("/eam_maintenance_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_maintenance_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamMaintenanceCostsService(db).delete(entity_id)

@router.get("/eam_meter_assignments", response_model=PaginatedResponse[EamMeterAssignmentsOut])
async def list_eam_meter_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamMeterAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["assignment_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_meter_assignments/{entity_id}", response_model=EamMeterAssignmentsOut)
async def get_eam_meter_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamMeterAssignmentsService(db).get(entity_id)

@router.post("/eam_meter_assignments", response_model=EamMeterAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_meter_assignments(
    data: EamMeterAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMeterAssignmentsService(db).create(data)

@router.put("/eam_meter_assignments/{entity_id}", response_model=EamMeterAssignmentsOut)
async def update_eam_meter_assignments(
    entity_id: uuid.UUID,
    data: EamMeterAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMeterAssignmentsService(db).update(entity_id, data)

@router.delete("/eam_meter_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_meter_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamMeterAssignmentsService(db).delete(entity_id)

@router.get("/eam_meter_readings", response_model=PaginatedResponse[EamMeterReadingsOut])
async def list_eam_meter_readings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamMeterReadingsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["unit_code", "reading_method_code", "source_system_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_meter_readings/{entity_id}", response_model=EamMeterReadingsOut)
async def get_eam_meter_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamMeterReadingsService(db).get(entity_id)

@router.post("/eam_meter_readings", response_model=EamMeterReadingsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_meter_readings(
    data: EamMeterReadingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMeterReadingsService(db).create(data)

@router.put("/eam_meter_readings/{entity_id}", response_model=EamMeterReadingsOut)
async def update_eam_meter_readings(
    entity_id: uuid.UUID,
    data: EamMeterReadingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMeterReadingsService(db).update(entity_id, data)

@router.delete("/eam_meter_readings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_meter_readings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamMeterReadingsService(db).delete(entity_id)

@router.get("/eam_meters", response_model=PaginatedResponse[EamMetersOut])
async def list_eam_meters(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamMetersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["meter_code", "meter_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_meters/{entity_id}", response_model=EamMetersOut)
async def get_eam_meters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamMetersService(db).get(entity_id)

@router.post("/eam_meters", response_model=EamMetersOut, status_code=status.HTTP_201_CREATED)
async def create_eam_meters(
    data: EamMetersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMetersService(db).create(data)

@router.put("/eam_meters/{entity_id}", response_model=EamMetersOut)
async def update_eam_meters(
    entity_id: uuid.UUID,
    data: EamMetersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMetersService(db).update(entity_id, data)

@router.delete("/eam_meters/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_meters(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamMetersService(db).delete(entity_id)

@router.get("/eam_ml_models", response_model=PaginatedResponse[EamMlModelsOut])
async def list_eam_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_code", "model_name", "model_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_ml_models/{entity_id}", response_model=EamMlModelsOut)
async def get_eam_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamMlModelsService(db).get(entity_id)

@router.post("/eam_ml_models", response_model=EamMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_ml_models(
    data: EamMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMlModelsService(db).create(data)

@router.put("/eam_ml_models/{entity_id}", response_model=EamMlModelsOut)
async def update_eam_ml_models(
    entity_id: uuid.UUID,
    data: EamMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamMlModelsService(db).update(entity_id, data)

@router.delete("/eam_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamMlModelsService(db).delete(entity_id)

@router.get("/eam_notifications", response_model=PaginatedResponse[EamNotificationsOut])
async def list_eam_notifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamNotificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["notification_type_code", "delivery_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_notifications/{entity_id}", response_model=EamNotificationsOut)
async def get_eam_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamNotificationsService(db).get(entity_id)

@router.post("/eam_notifications", response_model=EamNotificationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_notifications(
    data: EamNotificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamNotificationsService(db).create(data)

@router.put("/eam_notifications/{entity_id}", response_model=EamNotificationsOut)
async def update_eam_notifications(
    entity_id: uuid.UUID,
    data: EamNotificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamNotificationsService(db).update(entity_id, data)

@router.delete("/eam_notifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_notifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamNotificationsService(db).delete(entity_id)

@router.get("/eam_optimization_problems", response_model=PaginatedResponse[EamOptimizationProblemsOut])
async def list_eam_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamOptimizationProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_name", "problem_type_code", "objective_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_optimization_problems/{entity_id}", response_model=EamOptimizationProblemsOut)
async def get_eam_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamOptimizationProblemsService(db).get(entity_id)

@router.post("/eam_optimization_problems", response_model=EamOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_optimization_problems(
    data: EamOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOptimizationProblemsService(db).create(data)

@router.put("/eam_optimization_problems/{entity_id}", response_model=EamOptimizationProblemsOut)
async def update_eam_optimization_problems(
    entity_id: uuid.UUID,
    data: EamOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/eam_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamOptimizationProblemsService(db).delete(entity_id)

@router.get("/eam_optimization_solutions", response_model=PaginatedResponse[EamOptimizationSolutionsOut])
async def list_eam_optimization_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamOptimizationSolutionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solution_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_optimization_solutions/{entity_id}", response_model=EamOptimizationSolutionsOut)
async def get_eam_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamOptimizationSolutionsService(db).get(entity_id)

@router.post("/eam_optimization_solutions", response_model=EamOptimizationSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_optimization_solutions(
    data: EamOptimizationSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOptimizationSolutionsService(db).create(data)

@router.put("/eam_optimization_solutions/{entity_id}", response_model=EamOptimizationSolutionsOut)
async def update_eam_optimization_solutions(
    entity_id: uuid.UUID,
    data: EamOptimizationSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOptimizationSolutionsService(db).update(entity_id, data)

@router.delete("/eam_optimization_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamOptimizationSolutionsService(db).delete(entity_id)

@router.get("/eam_ortools_problems", response_model=PaginatedResponse[EamOrtoolsProblemsOut])
async def list_eam_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamOrtoolsProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_ortools_problems/{entity_id}", response_model=EamOrtoolsProblemsOut)
async def get_eam_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamOrtoolsProblemsService(db).get(entity_id)

@router.post("/eam_ortools_problems", response_model=EamOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_ortools_problems(
    data: EamOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOrtoolsProblemsService(db).create(data)

@router.put("/eam_ortools_problems/{entity_id}", response_model=EamOrtoolsProblemsOut)
async def update_eam_ortools_problems(
    entity_id: uuid.UUID,
    data: EamOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/eam_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamOrtoolsProblemsService(db).delete(entity_id)

@router.get("/eam_permits", response_model=PaginatedResponse[EamPermitsOut])
async def list_eam_permits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPermitsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["permit_number", "permit_type_code", "issuer_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_permits/{entity_id}", response_model=EamPermitsOut)
async def get_eam_permits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPermitsService(db).get(entity_id)

@router.post("/eam_permits", response_model=EamPermitsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_permits(
    data: EamPermitsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPermitsService(db).create(data)

@router.put("/eam_permits/{entity_id}", response_model=EamPermitsOut)
async def update_eam_permits(
    entity_id: uuid.UUID,
    data: EamPermitsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPermitsService(db).update(entity_id, data)

@router.delete("/eam_permits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_permits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPermitsService(db).delete(entity_id)

@router.get("/eam_physical_locations", response_model=PaginatedResponse[EamPhysicalLocationsOut])
async def list_eam_physical_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPhysicalLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_physical_locations/{entity_id}", response_model=EamPhysicalLocationsOut)
async def get_eam_physical_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPhysicalLocationsService(db).get(entity_id)

@router.post("/eam_physical_locations", response_model=EamPhysicalLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_physical_locations(
    data: EamPhysicalLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPhysicalLocationsService(db).create(data)

@router.put("/eam_physical_locations/{entity_id}", response_model=EamPhysicalLocationsOut)
async def update_eam_physical_locations(
    entity_id: uuid.UUID,
    data: EamPhysicalLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPhysicalLocationsService(db).update(entity_id, data)

@router.delete("/eam_physical_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_physical_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPhysicalLocationsService(db).delete(entity_id)

@router.get("/eam_pm_assignments", response_model=PaginatedResponse[EamPmAssignmentsOut])
async def list_eam_pm_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPmAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["assignment_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_pm_assignments/{entity_id}", response_model=EamPmAssignmentsOut)
async def get_eam_pm_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPmAssignmentsService(db).get(entity_id)

@router.post("/eam_pm_assignments", response_model=EamPmAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_pm_assignments(
    data: EamPmAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmAssignmentsService(db).create(data)

@router.put("/eam_pm_assignments/{entity_id}", response_model=EamPmAssignmentsOut)
async def update_eam_pm_assignments(
    entity_id: uuid.UUID,
    data: EamPmAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmAssignmentsService(db).update(entity_id, data)

@router.delete("/eam_pm_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_pm_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPmAssignmentsService(db).delete(entity_id)

@router.get("/eam_pm_schedule_optimized", response_model=PaginatedResponse[EamPmScheduleOptimizedOut])
async def list_eam_pm_schedule_optimized(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPmScheduleOptimizedService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_pm_schedule_optimized/{entity_id}", response_model=EamPmScheduleOptimizedOut)
async def get_eam_pm_schedule_optimized(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPmScheduleOptimizedService(db).get(entity_id)

@router.post("/eam_pm_schedule_optimized", response_model=EamPmScheduleOptimizedOut, status_code=status.HTTP_201_CREATED)
async def create_eam_pm_schedule_optimized(
    data: EamPmScheduleOptimizedCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmScheduleOptimizedService(db).create(data)

@router.put("/eam_pm_schedule_optimized/{entity_id}", response_model=EamPmScheduleOptimizedOut)
async def update_eam_pm_schedule_optimized(
    entity_id: uuid.UUID,
    data: EamPmScheduleOptimizedUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmScheduleOptimizedService(db).update(entity_id, data)

@router.delete("/eam_pm_schedule_optimized/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_pm_schedule_optimized(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPmScheduleOptimizedService(db).delete(entity_id)

@router.get("/eam_pm_schedules", response_model=PaginatedResponse[EamPmSchedulesOut])
async def list_eam_pm_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPmSchedulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["schedule_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_pm_schedules/{entity_id}", response_model=EamPmSchedulesOut)
async def get_eam_pm_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPmSchedulesService(db).get(entity_id)

@router.post("/eam_pm_schedules", response_model=EamPmSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_pm_schedules(
    data: EamPmSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmSchedulesService(db).create(data)

@router.put("/eam_pm_schedules/{entity_id}", response_model=EamPmSchedulesOut)
async def update_eam_pm_schedules(
    entity_id: uuid.UUID,
    data: EamPmSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmSchedulesService(db).update(entity_id, data)

@router.delete("/eam_pm_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_pm_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPmSchedulesService(db).delete(entity_id)

@router.get("/eam_pm_scheduling_problems", response_model=PaginatedResponse[EamPmSchedulingProblemsOut])
async def list_eam_pm_scheduling_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPmSchedulingProblemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_pm_scheduling_problems/{entity_id}", response_model=EamPmSchedulingProblemsOut)
async def get_eam_pm_scheduling_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPmSchedulingProblemsService(db).get(entity_id)

@router.post("/eam_pm_scheduling_problems", response_model=EamPmSchedulingProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_pm_scheduling_problems(
    data: EamPmSchedulingProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmSchedulingProblemsService(db).create(data)

@router.put("/eam_pm_scheduling_problems/{entity_id}", response_model=EamPmSchedulingProblemsOut)
async def update_eam_pm_scheduling_problems(
    entity_id: uuid.UUID,
    data: EamPmSchedulingProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmSchedulingProblemsService(db).update(entity_id, data)

@router.delete("/eam_pm_scheduling_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_pm_scheduling_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPmSchedulingProblemsService(db).delete(entity_id)

@router.get("/eam_pm_templates", response_model=PaginatedResponse[EamPmTemplatesOut])
async def list_eam_pm_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPmTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_code", "template_name", "work_order_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_pm_templates/{entity_id}", response_model=EamPmTemplatesOut)
async def get_eam_pm_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPmTemplatesService(db).get(entity_id)

@router.post("/eam_pm_templates", response_model=EamPmTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_pm_templates(
    data: EamPmTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmTemplatesService(db).create(data)

@router.put("/eam_pm_templates/{entity_id}", response_model=EamPmTemplatesOut)
async def update_eam_pm_templates(
    entity_id: uuid.UUID,
    data: EamPmTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPmTemplatesService(db).update(entity_id, data)

@router.delete("/eam_pm_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_pm_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPmTemplatesService(db).delete(entity_id)

@router.get("/eam_predictions", response_model=PaginatedResponse[EamPredictionsOut])
async def list_eam_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPredictionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["prediction_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_predictions/{entity_id}", response_model=EamPredictionsOut)
async def get_eam_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPredictionsService(db).get(entity_id)

@router.post("/eam_predictions", response_model=EamPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_predictions(
    data: EamPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPredictionsService(db).create(data)

@router.put("/eam_predictions/{entity_id}", response_model=EamPredictionsOut)
async def update_eam_predictions(
    entity_id: uuid.UUID,
    data: EamPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPredictionsService(db).update(entity_id, data)

@router.delete("/eam_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPredictionsService(db).delete(entity_id)

@router.get("/eam_predictive_maintenance", response_model=PaginatedResponse[EamPredictiveMaintenanceOut])
async def list_eam_predictive_maintenance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPredictiveMaintenanceService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["priority_code", "pdm_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_predictive_maintenance/{entity_id}", response_model=EamPredictiveMaintenanceOut)
async def get_eam_predictive_maintenance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPredictiveMaintenanceService(db).get(entity_id)

@router.post("/eam_predictive_maintenance", response_model=EamPredictiveMaintenanceOut, status_code=status.HTTP_201_CREATED)
async def create_eam_predictive_maintenance(
    data: EamPredictiveMaintenanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPredictiveMaintenanceService(db).create(data)

@router.put("/eam_predictive_maintenance/{entity_id}", response_model=EamPredictiveMaintenanceOut)
async def update_eam_predictive_maintenance(
    entity_id: uuid.UUID,
    data: EamPredictiveMaintenanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPredictiveMaintenanceService(db).update(entity_id, data)

@router.delete("/eam_predictive_maintenance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_predictive_maintenance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPredictiveMaintenanceService(db).delete(entity_id)

@router.get("/eam_prompt_templates", response_model=PaginatedResponse[EamPromptTemplatesOut])
async def list_eam_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_code", "template_name", "template_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_prompt_templates/{entity_id}", response_model=EamPromptTemplatesOut)
async def get_eam_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamPromptTemplatesService(db).get(entity_id)

@router.post("/eam_prompt_templates", response_model=EamPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_prompt_templates(
    data: EamPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPromptTemplatesService(db).create(data)

@router.put("/eam_prompt_templates/{entity_id}", response_model=EamPromptTemplatesOut)
async def update_eam_prompt_templates(
    entity_id: uuid.UUID,
    data: EamPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamPromptTemplatesService(db).update(entity_id, data)

@router.delete("/eam_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamPromptTemplatesService(db).delete(entity_id)

@router.get("/eam_rca_actions", response_model=PaginatedResponse[EamRcaActionsOut])
async def list_eam_rca_actions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamRcaActionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["action_type_code", "action_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_rca_actions/{entity_id}", response_model=EamRcaActionsOut)
async def get_eam_rca_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamRcaActionsService(db).get(entity_id)

@router.post("/eam_rca_actions", response_model=EamRcaActionsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_rca_actions(
    data: EamRcaActionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaActionsService(db).create(data)

@router.put("/eam_rca_actions/{entity_id}", response_model=EamRcaActionsOut)
async def update_eam_rca_actions(
    entity_id: uuid.UUID,
    data: EamRcaActionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaActionsService(db).update(entity_id, data)

@router.delete("/eam_rca_actions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_rca_actions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamRcaActionsService(db).delete(entity_id)

@router.get("/eam_rca_causes", response_model=PaginatedResponse[EamRcaCausesOut])
async def list_eam_rca_causes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamRcaCausesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cause_type_code", "category_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_rca_causes/{entity_id}", response_model=EamRcaCausesOut)
async def get_eam_rca_causes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamRcaCausesService(db).get(entity_id)

@router.post("/eam_rca_causes", response_model=EamRcaCausesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_rca_causes(
    data: EamRcaCausesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaCausesService(db).create(data)

@router.put("/eam_rca_causes/{entity_id}", response_model=EamRcaCausesOut)
async def update_eam_rca_causes(
    entity_id: uuid.UUID,
    data: EamRcaCausesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaCausesService(db).update(entity_id, data)

@router.delete("/eam_rca_causes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_rca_causes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamRcaCausesService(db).delete(entity_id)

@router.get("/eam_rca_studies", response_model=PaginatedResponse[EamRcaStudiesOut])
async def list_eam_rca_studies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamRcaStudiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["study_code", "study_name", "rca_method_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_rca_studies/{entity_id}", response_model=EamRcaStudiesOut)
async def get_eam_rca_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamRcaStudiesService(db).get(entity_id)

@router.post("/eam_rca_studies", response_model=EamRcaStudiesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_rca_studies(
    data: EamRcaStudiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaStudiesService(db).create(data)

@router.put("/eam_rca_studies/{entity_id}", response_model=EamRcaStudiesOut)
async def update_eam_rca_studies(
    entity_id: uuid.UUID,
    data: EamRcaStudiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcaStudiesService(db).update(entity_id, data)

@router.delete("/eam_rca_studies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_rca_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamRcaStudiesService(db).delete(entity_id)

@router.get("/eam_rcm_analyses", response_model=PaginatedResponse[EamRcmAnalysesOut])
async def list_eam_rcm_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamRcmAnalysesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["task_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_rcm_analyses/{entity_id}", response_model=EamRcmAnalysesOut)
async def get_eam_rcm_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamRcmAnalysesService(db).get(entity_id)

@router.post("/eam_rcm_analyses", response_model=EamRcmAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_rcm_analyses(
    data: EamRcmAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcmAnalysesService(db).create(data)

@router.put("/eam_rcm_analyses/{entity_id}", response_model=EamRcmAnalysesOut)
async def update_eam_rcm_analyses(
    entity_id: uuid.UUID,
    data: EamRcmAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcmAnalysesService(db).update(entity_id, data)

@router.delete("/eam_rcm_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_rcm_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamRcmAnalysesService(db).delete(entity_id)

@router.get("/eam_rcm_studies", response_model=PaginatedResponse[EamRcmStudiesOut])
async def list_eam_rcm_studies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamRcmStudiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["study_code", "study_name", "study_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_rcm_studies/{entity_id}", response_model=EamRcmStudiesOut)
async def get_eam_rcm_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamRcmStudiesService(db).get(entity_id)

@router.post("/eam_rcm_studies", response_model=EamRcmStudiesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_rcm_studies(
    data: EamRcmStudiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcmStudiesService(db).create(data)

@router.put("/eam_rcm_studies/{entity_id}", response_model=EamRcmStudiesOut)
async def update_eam_rcm_studies(
    entity_id: uuid.UUID,
    data: EamRcmStudiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamRcmStudiesService(db).update(entity_id, data)

@router.delete("/eam_rcm_studies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_rcm_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamRcmStudiesService(db).delete(entity_id)

@router.get("/eam_safety_plans", response_model=PaginatedResponse[EamSafetyPlansOut])
async def list_eam_safety_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamSafetyPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_code", "plan_name", "plan_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_safety_plans/{entity_id}", response_model=EamSafetyPlansOut)
async def get_eam_safety_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamSafetyPlansService(db).get(entity_id)

@router.post("/eam_safety_plans", response_model=EamSafetyPlansOut, status_code=status.HTTP_201_CREATED)
async def create_eam_safety_plans(
    data: EamSafetyPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSafetyPlansService(db).create(data)

@router.put("/eam_safety_plans/{entity_id}", response_model=EamSafetyPlansOut)
async def update_eam_safety_plans(
    entity_id: uuid.UUID,
    data: EamSafetyPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSafetyPlansService(db).update(entity_id, data)

@router.delete("/eam_safety_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_safety_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamSafetyPlansService(db).delete(entity_id)

@router.get("/eam_scenarios", response_model=PaginatedResponse[EamScenariosOut])
async def list_eam_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_code", "scenario_name", "scenario_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_scenarios/{entity_id}", response_model=EamScenariosOut)
async def get_eam_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamScenariosService(db).get(entity_id)

@router.post("/eam_scenarios", response_model=EamScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_eam_scenarios(
    data: EamScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamScenariosService(db).create(data)

@router.put("/eam_scenarios/{entity_id}", response_model=EamScenariosOut)
async def update_eam_scenarios(
    entity_id: uuid.UUID,
    data: EamScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamScenariosService(db).update(entity_id, data)

@router.delete("/eam_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamScenariosService(db).delete(entity_id)

@router.get("/eam_scipy_analyses", response_model=PaginatedResponse[EamScipyAnalysesOut])
async def list_eam_scipy_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamScipyAnalysesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["analysis_name", "analysis_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_scipy_analyses/{entity_id}", response_model=EamScipyAnalysesOut)
async def get_eam_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamScipyAnalysesService(db).get(entity_id)

@router.post("/eam_scipy_analyses", response_model=EamScipyAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_scipy_analyses(
    data: EamScipyAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamScipyAnalysesService(db).create(data)

@router.put("/eam_scipy_analyses/{entity_id}", response_model=EamScipyAnalysesOut)
async def update_eam_scipy_analyses(
    entity_id: uuid.UUID,
    data: EamScipyAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamScipyAnalysesService(db).update(entity_id, data)

@router.delete("/eam_scipy_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamScipyAnalysesService(db).delete(entity_id)

@router.get("/eam_service_contracts", response_model=PaginatedResponse[EamServiceContractsOut])
async def list_eam_service_contracts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamServiceContractsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["contract_number", "contract_name", "contract_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_service_contracts/{entity_id}", response_model=EamServiceContractsOut)
async def get_eam_service_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamServiceContractsService(db).get(entity_id)

@router.post("/eam_service_contracts", response_model=EamServiceContractsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_service_contracts(
    data: EamServiceContractsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamServiceContractsService(db).create(data)

@router.put("/eam_service_contracts/{entity_id}", response_model=EamServiceContractsOut)
async def update_eam_service_contracts(
    entity_id: uuid.UUID,
    data: EamServiceContractsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamServiceContractsService(db).update(entity_id, data)

@router.delete("/eam_service_contracts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_service_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamServiceContractsService(db).delete(entity_id)

@router.get("/eam_spare_parts_consumption", response_model=PaginatedResponse[EamSparePartsConsumptionOut])
async def list_eam_spare_parts_consumption(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamSparePartsConsumptionService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_spare_parts_consumption/{entity_id}", response_model=EamSparePartsConsumptionOut)
async def get_eam_spare_parts_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamSparePartsConsumptionService(db).get(entity_id)

@router.post("/eam_spare_parts_consumption", response_model=EamSparePartsConsumptionOut, status_code=status.HTTP_201_CREATED)
async def create_eam_spare_parts_consumption(
    data: EamSparePartsConsumptionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSparePartsConsumptionService(db).create(data)

@router.put("/eam_spare_parts_consumption/{entity_id}", response_model=EamSparePartsConsumptionOut)
async def update_eam_spare_parts_consumption(
    entity_id: uuid.UUID,
    data: EamSparePartsConsumptionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSparePartsConsumptionService(db).update(entity_id, data)

@router.delete("/eam_spare_parts_consumption/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_spare_parts_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamSparePartsConsumptionService(db).delete(entity_id)

@router.get("/eam_spare_parts_storage", response_model=PaginatedResponse[EamSparePartsStorageOut])
async def list_eam_spare_parts_storage(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamSparePartsStorageService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["container_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_spare_parts_storage/{entity_id}", response_model=EamSparePartsStorageOut)
async def get_eam_spare_parts_storage(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamSparePartsStorageService(db).get(entity_id)

@router.post("/eam_spare_parts_storage", response_model=EamSparePartsStorageOut, status_code=status.HTTP_201_CREATED)
async def create_eam_spare_parts_storage(
    data: EamSparePartsStorageCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSparePartsStorageService(db).create(data)

@router.put("/eam_spare_parts_storage/{entity_id}", response_model=EamSparePartsStorageOut)
async def update_eam_spare_parts_storage(
    entity_id: uuid.UUID,
    data: EamSparePartsStorageUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamSparePartsStorageService(db).update(entity_id, data)

@router.delete("/eam_spare_parts_storage/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_spare_parts_storage(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamSparePartsStorageService(db).delete(entity_id)

@router.get("/eam_storage_locations", response_model=PaginatedResponse[EamStorageLocationsOut])
async def list_eam_storage_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamStorageLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name", "location_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_storage_locations/{entity_id}", response_model=EamStorageLocationsOut)
async def get_eam_storage_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamStorageLocationsService(db).get(entity_id)

@router.post("/eam_storage_locations", response_model=EamStorageLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_storage_locations(
    data: EamStorageLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamStorageLocationsService(db).create(data)

@router.put("/eam_storage_locations/{entity_id}", response_model=EamStorageLocationsOut)
async def update_eam_storage_locations(
    entity_id: uuid.UUID,
    data: EamStorageLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamStorageLocationsService(db).update(entity_id, data)

@router.delete("/eam_storage_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_storage_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamStorageLocationsService(db).delete(entity_id)

@router.get("/eam_storage_optimization_problems", response_model=PaginatedResponse[EamStorageOptimizationProblemsOut])
async def list_eam_storage_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamStorageOptimizationProblemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_storage_optimization_problems/{entity_id}", response_model=EamStorageOptimizationProblemsOut)
async def get_eam_storage_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamStorageOptimizationProblemsService(db).get(entity_id)

@router.post("/eam_storage_optimization_problems", response_model=EamStorageOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_storage_optimization_problems(
    data: EamStorageOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamStorageOptimizationProblemsService(db).create(data)

@router.put("/eam_storage_optimization_problems/{entity_id}", response_model=EamStorageOptimizationProblemsOut)
async def update_eam_storage_optimization_problems(
    entity_id: uuid.UUID,
    data: EamStorageOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamStorageOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/eam_storage_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_storage_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamStorageOptimizationProblemsService(db).delete(entity_id)

@router.get("/eam_technician_certifications", response_model=PaginatedResponse[EamTechnicianCertificationsOut])
async def list_eam_technician_certifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamTechnicianCertificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["certification_code", "certification_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_technician_certifications/{entity_id}", response_model=EamTechnicianCertificationsOut)
async def get_eam_technician_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamTechnicianCertificationsService(db).get(entity_id)

@router.post("/eam_technician_certifications", response_model=EamTechnicianCertificationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_technician_certifications(
    data: EamTechnicianCertificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianCertificationsService(db).create(data)

@router.put("/eam_technician_certifications/{entity_id}", response_model=EamTechnicianCertificationsOut)
async def update_eam_technician_certifications(
    entity_id: uuid.UUID,
    data: EamTechnicianCertificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianCertificationsService(db).update(entity_id, data)

@router.delete("/eam_technician_certifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_technician_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamTechnicianCertificationsService(db).delete(entity_id)

@router.get("/eam_technician_routes", response_model=PaginatedResponse[EamTechnicianRoutesOut])
async def list_eam_technician_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamTechnicianRoutesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["technician_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_technician_routes/{entity_id}", response_model=EamTechnicianRoutesOut)
async def get_eam_technician_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamTechnicianRoutesService(db).get(entity_id)

@router.post("/eam_technician_routes", response_model=EamTechnicianRoutesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_technician_routes(
    data: EamTechnicianRoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianRoutesService(db).create(data)

@router.put("/eam_technician_routes/{entity_id}", response_model=EamTechnicianRoutesOut)
async def update_eam_technician_routes(
    entity_id: uuid.UUID,
    data: EamTechnicianRoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianRoutesService(db).update(entity_id, data)

@router.delete("/eam_technician_routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_technician_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamTechnicianRoutesService(db).delete(entity_id)

@router.get("/eam_technician_routing_problems", response_model=PaginatedResponse[EamTechnicianRoutingProblemsOut])
async def list_eam_technician_routing_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamTechnicianRoutingProblemsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_technician_routing_problems/{entity_id}", response_model=EamTechnicianRoutingProblemsOut)
async def get_eam_technician_routing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamTechnicianRoutingProblemsService(db).get(entity_id)

@router.post("/eam_technician_routing_problems", response_model=EamTechnicianRoutingProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_technician_routing_problems(
    data: EamTechnicianRoutingProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianRoutingProblemsService(db).create(data)

@router.put("/eam_technician_routing_problems/{entity_id}", response_model=EamTechnicianRoutingProblemsOut)
async def update_eam_technician_routing_problems(
    entity_id: uuid.UUID,
    data: EamTechnicianRoutingProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianRoutingProblemsService(db).update(entity_id, data)

@router.delete("/eam_technician_routing_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_technician_routing_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamTechnicianRoutingProblemsService(db).delete(entity_id)

@router.get("/eam_technician_skills", response_model=PaginatedResponse[EamTechnicianSkillsOut])
async def list_eam_technician_skills(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamTechnicianSkillsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["skill_code", "skill_name", "certification_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_technician_skills/{entity_id}", response_model=EamTechnicianSkillsOut)
async def get_eam_technician_skills(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamTechnicianSkillsService(db).get(entity_id)

@router.post("/eam_technician_skills", response_model=EamTechnicianSkillsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_technician_skills(
    data: EamTechnicianSkillsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianSkillsService(db).create(data)

@router.put("/eam_technician_skills/{entity_id}", response_model=EamTechnicianSkillsOut)
async def update_eam_technician_skills(
    entity_id: uuid.UUID,
    data: EamTechnicianSkillsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechnicianSkillsService(db).update(entity_id, data)

@router.delete("/eam_technician_skills/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_technician_skills(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamTechnicianSkillsService(db).delete(entity_id)

@router.get("/eam_technicians", response_model=PaginatedResponse[EamTechniciansOut])
async def list_eam_technicians(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamTechniciansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["technician_code", "first_name", "last_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_technicians/{entity_id}", response_model=EamTechniciansOut)
async def get_eam_technicians(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamTechniciansService(db).get(entity_id)

@router.post("/eam_technicians", response_model=EamTechniciansOut, status_code=status.HTTP_201_CREATED)
async def create_eam_technicians(
    data: EamTechniciansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechniciansService(db).create(data)

@router.put("/eam_technicians/{entity_id}", response_model=EamTechniciansOut)
async def update_eam_technicians(
    entity_id: uuid.UUID,
    data: EamTechniciansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamTechniciansService(db).update(entity_id, data)

@router.delete("/eam_technicians/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_technicians(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamTechniciansService(db).delete(entity_id)

@router.get("/eam_tools", response_model=PaginatedResponse[EamToolsOut])
async def list_eam_tools(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamToolsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tool_code", "tool_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_tools/{entity_id}", response_model=EamToolsOut)
async def get_eam_tools(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamToolsService(db).get(entity_id)

@router.post("/eam_tools", response_model=EamToolsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_tools(
    data: EamToolsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamToolsService(db).create(data)

@router.put("/eam_tools/{entity_id}", response_model=EamToolsOut)
async def update_eam_tools(
    entity_id: uuid.UUID,
    data: EamToolsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamToolsService(db).update(entity_id, data)

@router.delete("/eam_tools/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_tools(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamToolsService(db).delete(entity_id)

@router.get("/eam_vector_documents", response_model=PaginatedResponse[EamVectorDocumentsOut])
async def list_eam_vector_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamVectorDocumentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_vector_documents/{entity_id}", response_model=EamVectorDocumentsOut)
async def get_eam_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamVectorDocumentsService(db).get(entity_id)

@router.post("/eam_vector_documents", response_model=EamVectorDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_vector_documents(
    data: EamVectorDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamVectorDocumentsService(db).create(data)

@router.put("/eam_vector_documents/{entity_id}", response_model=EamVectorDocumentsOut)
async def update_eam_vector_documents(
    entity_id: uuid.UUID,
    data: EamVectorDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamVectorDocumentsService(db).update(entity_id, data)

@router.delete("/eam_vector_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamVectorDocumentsService(db).delete(entity_id)

@router.get("/eam_warranties", response_model=PaginatedResponse[EamWarrantiesOut])
async def list_eam_warranties(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWarrantiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["warranty_number", "warranty_name", "warranty_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_warranties/{entity_id}", response_model=EamWarrantiesOut)
async def get_eam_warranties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWarrantiesService(db).get(entity_id)

@router.post("/eam_warranties", response_model=EamWarrantiesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_warranties(
    data: EamWarrantiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWarrantiesService(db).create(data)

@router.put("/eam_warranties/{entity_id}", response_model=EamWarrantiesOut)
async def update_eam_warranties(
    entity_id: uuid.UUID,
    data: EamWarrantiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWarrantiesService(db).update(entity_id, data)

@router.delete("/eam_warranties/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_warranties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWarrantiesService(db).delete(entity_id)

@router.get("/eam_warranty_claims", response_model=PaginatedResponse[EamWarrantyClaimsOut])
async def list_eam_warranty_claims(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWarrantyClaimsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["claim_number", "currency_code", "claim_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_warranty_claims/{entity_id}", response_model=EamWarrantyClaimsOut)
async def get_eam_warranty_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWarrantyClaimsService(db).get(entity_id)

@router.post("/eam_warranty_claims", response_model=EamWarrantyClaimsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_warranty_claims(
    data: EamWarrantyClaimsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWarrantyClaimsService(db).create(data)

@router.put("/eam_warranty_claims/{entity_id}", response_model=EamWarrantyClaimsOut)
async def update_eam_warranty_claims(
    entity_id: uuid.UUID,
    data: EamWarrantyClaimsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWarrantyClaimsService(db).update(entity_id, data)

@router.delete("/eam_warranty_claims/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_warranty_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWarrantyClaimsService(db).delete(entity_id)

@router.get("/eam_wo_labor", response_model=PaginatedResponse[EamWoLaborOut])
async def list_eam_wo_labor(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWoLaborService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["craft_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_wo_labor/{entity_id}", response_model=EamWoLaborOut)
async def get_eam_wo_labor(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWoLaborService(db).get(entity_id)

@router.post("/eam_wo_labor", response_model=EamWoLaborOut, status_code=status.HTTP_201_CREATED)
async def create_eam_wo_labor(
    data: EamWoLaborCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoLaborService(db).create(data)

@router.put("/eam_wo_labor/{entity_id}", response_model=EamWoLaborOut)
async def update_eam_wo_labor(
    entity_id: uuid.UUID,
    data: EamWoLaborUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoLaborService(db).update(entity_id, data)

@router.delete("/eam_wo_labor/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_wo_labor(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWoLaborService(db).delete(entity_id)

@router.get("/eam_wo_operations", response_model=PaginatedResponse[EamWoOperationsOut])
async def list_eam_wo_operations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWoOperationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["operation_code", "operation_name", "operation_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_wo_operations/{entity_id}", response_model=EamWoOperationsOut)
async def get_eam_wo_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWoOperationsService(db).get(entity_id)

@router.post("/eam_wo_operations", response_model=EamWoOperationsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_wo_operations(
    data: EamWoOperationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoOperationsService(db).create(data)

@router.put("/eam_wo_operations/{entity_id}", response_model=EamWoOperationsOut)
async def update_eam_wo_operations(
    entity_id: uuid.UUID,
    data: EamWoOperationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoOperationsService(db).update(entity_id, data)

@router.delete("/eam_wo_operations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_wo_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWoOperationsService(db).delete(entity_id)

@router.get("/eam_wo_tasks", response_model=PaginatedResponse[EamWoTasksOut])
async def list_eam_wo_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWoTasksService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["task_code", "task_name", "craft_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_wo_tasks/{entity_id}", response_model=EamWoTasksOut)
async def get_eam_wo_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWoTasksService(db).get(entity_id)

@router.post("/eam_wo_tasks", response_model=EamWoTasksOut, status_code=status.HTTP_201_CREATED)
async def create_eam_wo_tasks(
    data: EamWoTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoTasksService(db).create(data)

@router.put("/eam_wo_tasks/{entity_id}", response_model=EamWoTasksOut)
async def update_eam_wo_tasks(
    entity_id: uuid.UUID,
    data: EamWoTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoTasksService(db).update(entity_id, data)

@router.delete("/eam_wo_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_wo_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWoTasksService(db).delete(entity_id)

@router.get("/eam_wo_tools", response_model=PaginatedResponse[EamWoToolsOut])
async def list_eam_wo_tools(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWoToolsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_wo_tools/{entity_id}", response_model=EamWoToolsOut)
async def get_eam_wo_tools(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWoToolsService(db).get(entity_id)

@router.post("/eam_wo_tools", response_model=EamWoToolsOut, status_code=status.HTTP_201_CREATED)
async def create_eam_wo_tools(
    data: EamWoToolsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoToolsService(db).create(data)

@router.put("/eam_wo_tools/{entity_id}", response_model=EamWoToolsOut)
async def update_eam_wo_tools(
    entity_id: uuid.UUID,
    data: EamWoToolsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWoToolsService(db).update(entity_id, data)

@router.delete("/eam_wo_tools/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_wo_tools(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWoToolsService(db).delete(entity_id)

@router.get("/eam_work_order_statuses", response_model=PaginatedResponse[EamWorkOrderStatusesOut])
async def list_eam_work_order_statuses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWorkOrderStatusesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["work_order_status_code", "work_order_status_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_work_order_statuses/{entity_id}", response_model=EamWorkOrderStatusesOut)
async def get_eam_work_order_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWorkOrderStatusesService(db).get(entity_id)

@router.post("/eam_work_order_statuses", response_model=EamWorkOrderStatusesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_work_order_statuses(
    data: EamWorkOrderStatusesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrderStatusesService(db).create(data)

@router.put("/eam_work_order_statuses/{entity_id}", response_model=EamWorkOrderStatusesOut)
async def update_eam_work_order_statuses(
    entity_id: uuid.UUID,
    data: EamWorkOrderStatusesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrderStatusesService(db).update(entity_id, data)

@router.delete("/eam_work_order_statuses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_work_order_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWorkOrderStatusesService(db).delete(entity_id)

@router.get("/eam_work_order_types", response_model=PaginatedResponse[EamWorkOrderTypesOut])
async def list_eam_work_order_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWorkOrderTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["work_order_type_code", "work_order_type_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_work_order_types/{entity_id}", response_model=EamWorkOrderTypesOut)
async def get_eam_work_order_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWorkOrderTypesService(db).get(entity_id)

@router.post("/eam_work_order_types", response_model=EamWorkOrderTypesOut, status_code=status.HTTP_201_CREATED)
async def create_eam_work_order_types(
    data: EamWorkOrderTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrderTypesService(db).create(data)

@router.put("/eam_work_order_types/{entity_id}", response_model=EamWorkOrderTypesOut)
async def update_eam_work_order_types(
    entity_id: uuid.UUID,
    data: EamWorkOrderTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrderTypesService(db).update(entity_id, data)

@router.delete("/eam_work_order_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_work_order_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWorkOrderTypesService(db).delete(entity_id)

@router.get("/eam_work_orders", response_model=PaginatedResponse[EamWorkOrdersOut])
async def list_eam_work_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    svc = EamWorkOrdersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["work_order_number", "work_order_type_code", "work_order_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/eam_work_orders/{entity_id}", response_model=EamWorkOrdersOut)
async def get_eam_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "view"),
):
    return await EamWorkOrdersService(db).get(entity_id)

@router.post("/eam_work_orders", response_model=EamWorkOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_eam_work_orders(
    data: EamWorkOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrdersService(db).create(data)

@router.put("/eam_work_orders/{entity_id}", response_model=EamWorkOrdersOut)
async def update_eam_work_orders(
    entity_id: uuid.UUID,
    data: EamWorkOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    return await EamWorkOrdersService(db).update(entity_id, data)

@router.delete("/eam_work_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_eam_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("eam", "manage"),
):
    await EamWorkOrdersService(db).delete(entity_id)
