import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.fa.services import (
    AiAgentLogsService,
    AiDecisionsService,
    AiModelRegistryService,
    AiWorkflowStateService,
    FaAdditionsService,
    FaAdjustmentsService,
    FaAgentDefinitionsService,
    FaAlgorithmsService,
    FaAssetAttachmentsService,
    FaAssetBookAssignmentsService,
    FaAssetCategoriesService,
    FaAssetCategoryHierarchyService,
    FaAssetComponentsService,
    FaAssetCustomAttributesService,
    FaAssetPhotosService,
    FaAssetStorageService,
    FaAssetTagsService,
    FaAssetTypesService,
    FaAssetsService,
    FaBonusDepreciationService,
    FaBookTypesService,
    FaCipCostsService,
    FaCipProjectsService,
    FaCountLinesService,
    FaCountRoutesService,
    FaCountSheetsService,
    FaCountVariancesService,
    FaCustodiansService,
    FaDeprnBookPeriodsService,
    FaDeprnBooksService,
    FaDeprnCalculationService,
    FaDeprnConventionsService,
    FaDeprnMethodsService,
    FaGroupAssetMembersService,
    FaGroupAssetsService,
    FaImpairmentsService,
    FaInsuranceClaimsService,
    FaInsurancePoliciesService,
    FaIntegrationConnectionsService,
    FaIntegrationLogsService,
    FaLanggraphExecutionsService,
    FaLanggraphStatesService,
    FaLanggraphWorkflowsService,
    FaLeaseAssetsService,
    FaLeaseSchedulesService,
    FaLeasesService,
    FaLlmConfigsService,
    FaLocationsService,
    FaMlModelsService,
    FaMobileDevicesService,
    FaMobileScansService,
    FaMobileSyncBatchesService,
    FaMobileUsersService,
    FaOptimizationProblemsService,
    FaOrtoolsProblemsService,
    FaPhotosService,
    FaPhysicalCountsService,
    FaPredictionActualsService,
    FaPredictionsService,
    FaPromptTemplatesService,
    FaReinstatementsService,
    FaReportSchedulesService,
    FaReportsService,
    FaRetirementsService,
    FaRevaluationsService,
    FaScenariosService,
    FaScipyAnalysesService,
    FaSignaturesService,
    FaSolverConfigsService,
    FaTaxPaymentsService,
    FaTaxRecordsService,
    FaTransactionsService,
    FaTransfersService,
    FaVectorDocumentsService,
    FaWarrantiesService,
    FaWarrantyClaimsService,
)
from app.modules.fa.schemas import (
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
    FaAdditionsCreate,
    FaAdditionsUpdate,
    FaAdditionsOut,
    FaAdjustmentsCreate,
    FaAdjustmentsUpdate,
    FaAdjustmentsOut,
    FaAgentDefinitionsCreate,
    FaAgentDefinitionsUpdate,
    FaAgentDefinitionsOut,
    FaAlgorithmsCreate,
    FaAlgorithmsUpdate,
    FaAlgorithmsOut,
    FaAssetAttachmentsCreate,
    FaAssetAttachmentsUpdate,
    FaAssetAttachmentsOut,
    FaAssetBookAssignmentsCreate,
    FaAssetBookAssignmentsUpdate,
    FaAssetBookAssignmentsOut,
    FaAssetCategoriesCreate,
    FaAssetCategoriesUpdate,
    FaAssetCategoriesOut,
    FaAssetCategoryHierarchyCreate,
    FaAssetCategoryHierarchyUpdate,
    FaAssetCategoryHierarchyOut,
    FaAssetComponentsCreate,
    FaAssetComponentsUpdate,
    FaAssetComponentsOut,
    FaAssetCustomAttributesCreate,
    FaAssetCustomAttributesUpdate,
    FaAssetCustomAttributesOut,
    FaAssetPhotosCreate,
    FaAssetPhotosUpdate,
    FaAssetPhotosOut,
    FaAssetStorageCreate,
    FaAssetStorageUpdate,
    FaAssetStorageOut,
    FaAssetTagsCreate,
    FaAssetTagsUpdate,
    FaAssetTagsOut,
    FaAssetTypesCreate,
    FaAssetTypesUpdate,
    FaAssetTypesOut,
    FaAssetsCreate,
    FaAssetsUpdate,
    FaAssetsOut,
    FaBonusDepreciationCreate,
    FaBonusDepreciationUpdate,
    FaBonusDepreciationOut,
    FaBookTypesCreate,
    FaBookTypesUpdate,
    FaBookTypesOut,
    FaCipCostsCreate,
    FaCipCostsUpdate,
    FaCipCostsOut,
    FaCipProjectsCreate,
    FaCipProjectsUpdate,
    FaCipProjectsOut,
    FaCountLinesCreate,
    FaCountLinesUpdate,
    FaCountLinesOut,
    FaCountRoutesCreate,
    FaCountRoutesUpdate,
    FaCountRoutesOut,
    FaCountSheetsCreate,
    FaCountSheetsUpdate,
    FaCountSheetsOut,
    FaCountVariancesCreate,
    FaCountVariancesUpdate,
    FaCountVariancesOut,
    FaCustodiansCreate,
    FaCustodiansUpdate,
    FaCustodiansOut,
    FaDeprnBookPeriodsCreate,
    FaDeprnBookPeriodsUpdate,
    FaDeprnBookPeriodsOut,
    FaDeprnBooksCreate,
    FaDeprnBooksUpdate,
    FaDeprnBooksOut,
    FaDeprnCalculationCreate,
    FaDeprnCalculationUpdate,
    FaDeprnCalculationOut,
    FaDeprnConventionsCreate,
    FaDeprnConventionsUpdate,
    FaDeprnConventionsOut,
    FaDeprnMethodsCreate,
    FaDeprnMethodsUpdate,
    FaDeprnMethodsOut,
    FaGroupAssetMembersCreate,
    FaGroupAssetMembersUpdate,
    FaGroupAssetMembersOut,
    FaGroupAssetsCreate,
    FaGroupAssetsUpdate,
    FaGroupAssetsOut,
    FaImpairmentsCreate,
    FaImpairmentsUpdate,
    FaImpairmentsOut,
    FaInsuranceClaimsCreate,
    FaInsuranceClaimsUpdate,
    FaInsuranceClaimsOut,
    FaInsurancePoliciesCreate,
    FaInsurancePoliciesUpdate,
    FaInsurancePoliciesOut,
    FaIntegrationConnectionsCreate,
    FaIntegrationConnectionsUpdate,
    FaIntegrationConnectionsOut,
    FaIntegrationLogsCreate,
    FaIntegrationLogsUpdate,
    FaIntegrationLogsOut,
    FaLanggraphExecutionsCreate,
    FaLanggraphExecutionsUpdate,
    FaLanggraphExecutionsOut,
    FaLanggraphStatesCreate,
    FaLanggraphStatesUpdate,
    FaLanggraphStatesOut,
    FaLanggraphWorkflowsCreate,
    FaLanggraphWorkflowsUpdate,
    FaLanggraphWorkflowsOut,
    FaLeaseAssetsCreate,
    FaLeaseAssetsUpdate,
    FaLeaseAssetsOut,
    FaLeaseSchedulesCreate,
    FaLeaseSchedulesUpdate,
    FaLeaseSchedulesOut,
    FaLeasesCreate,
    FaLeasesUpdate,
    FaLeasesOut,
    FaLlmConfigsCreate,
    FaLlmConfigsUpdate,
    FaLlmConfigsOut,
    FaLocationsCreate,
    FaLocationsUpdate,
    FaLocationsOut,
    FaMlModelsCreate,
    FaMlModelsUpdate,
    FaMlModelsOut,
    FaMobileDevicesCreate,
    FaMobileDevicesUpdate,
    FaMobileDevicesOut,
    FaMobileScansCreate,
    FaMobileScansUpdate,
    FaMobileScansOut,
    FaMobileSyncBatchesCreate,
    FaMobileSyncBatchesUpdate,
    FaMobileSyncBatchesOut,
    FaMobileUsersCreate,
    FaMobileUsersUpdate,
    FaMobileUsersOut,
    FaOptimizationProblemsCreate,
    FaOptimizationProblemsUpdate,
    FaOptimizationProblemsOut,
    FaOrtoolsProblemsCreate,
    FaOrtoolsProblemsUpdate,
    FaOrtoolsProblemsOut,
    FaPhotosCreate,
    FaPhotosUpdate,
    FaPhotosOut,
    FaPhysicalCountsCreate,
    FaPhysicalCountsUpdate,
    FaPhysicalCountsOut,
    FaPredictionActualsCreate,
    FaPredictionActualsUpdate,
    FaPredictionActualsOut,
    FaPredictionsCreate,
    FaPredictionsUpdate,
    FaPredictionsOut,
    FaPromptTemplatesCreate,
    FaPromptTemplatesUpdate,
    FaPromptTemplatesOut,
    FaReinstatementsCreate,
    FaReinstatementsUpdate,
    FaReinstatementsOut,
    FaReportSchedulesCreate,
    FaReportSchedulesUpdate,
    FaReportSchedulesOut,
    FaReportsCreate,
    FaReportsUpdate,
    FaReportsOut,
    FaRetirementsCreate,
    FaRetirementsUpdate,
    FaRetirementsOut,
    FaRevaluationsCreate,
    FaRevaluationsUpdate,
    FaRevaluationsOut,
    FaScenariosCreate,
    FaScenariosUpdate,
    FaScenariosOut,
    FaScipyAnalysesCreate,
    FaScipyAnalysesUpdate,
    FaScipyAnalysesOut,
    FaSignaturesCreate,
    FaSignaturesUpdate,
    FaSignaturesOut,
    FaSolverConfigsCreate,
    FaSolverConfigsUpdate,
    FaSolverConfigsOut,
    FaTaxPaymentsCreate,
    FaTaxPaymentsUpdate,
    FaTaxPaymentsOut,
    FaTaxRecordsCreate,
    FaTaxRecordsUpdate,
    FaTaxRecordsOut,
    FaTransactionsCreate,
    FaTransactionsUpdate,
    FaTransactionsOut,
    FaTransfersCreate,
    FaTransfersUpdate,
    FaTransfersOut,
    FaVectorDocumentsCreate,
    FaVectorDocumentsUpdate,
    FaVectorDocumentsOut,
    FaWarrantiesCreate,
    FaWarrantiesUpdate,
    FaWarrantiesOut,
    FaWarrantyClaimsCreate,
    FaWarrantyClaimsUpdate,
    FaWarrantyClaimsOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = AiAgentLogsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["decision_type_code", "entity_type_code", "decision_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_model_registry", response_model=PaginatedResponse[AiModelRegistryOut])
async def list_ai_model_registry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = AiModelRegistryService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name", "model_type_code", "model_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_model_registry/{entity_id}", response_model=AiModelRegistryOut)
async def get_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await AiModelRegistryService(db).get(entity_id)

@router.post("/ai_model_registry", response_model=AiModelRegistryOut, status_code=status.HTTP_201_CREATED)
async def create_ai_model_registry(
    data: AiModelRegistryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiModelRegistryService(db).create(data)

@router.put("/ai_model_registry/{entity_id}", response_model=AiModelRegistryOut)
async def update_ai_model_registry(
    entity_id: uuid.UUID,
    data: AiModelRegistryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiModelRegistryService(db).update(entity_id, data)

@router.delete("/ai_model_registry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await AiModelRegistryService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = AiWorkflowStateService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_type_code", "state_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/fa_additions", response_model=PaginatedResponse[FaAdditionsOut])
async def list_fa_additions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAdditionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["addition_source_code", "supplier_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_additions/{entity_id}", response_model=FaAdditionsOut)
async def get_fa_additions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAdditionsService(db).get(entity_id)

@router.post("/fa_additions", response_model=FaAdditionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_additions(
    data: FaAdditionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAdditionsService(db).create(data)

@router.put("/fa_additions/{entity_id}", response_model=FaAdditionsOut)
async def update_fa_additions(
    entity_id: uuid.UUID,
    data: FaAdditionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAdditionsService(db).update(entity_id, data)

@router.delete("/fa_additions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_additions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAdditionsService(db).delete(entity_id)

@router.get("/fa_adjustments", response_model=PaginatedResponse[FaAdjustmentsOut])
async def list_fa_adjustments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAdjustmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["adjustment_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_adjustments/{entity_id}", response_model=FaAdjustmentsOut)
async def get_fa_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAdjustmentsService(db).get(entity_id)

@router.post("/fa_adjustments", response_model=FaAdjustmentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_adjustments(
    data: FaAdjustmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAdjustmentsService(db).create(data)

@router.put("/fa_adjustments/{entity_id}", response_model=FaAdjustmentsOut)
async def update_fa_adjustments(
    entity_id: uuid.UUID,
    data: FaAdjustmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAdjustmentsService(db).update(entity_id, data)

@router.delete("/fa_adjustments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAdjustmentsService(db).delete(entity_id)

@router.get("/fa_agent_definitions", response_model=PaginatedResponse[FaAgentDefinitionsOut])
async def list_fa_agent_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAgentDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["agent_name", "agent_type_code", "agent_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_agent_definitions/{entity_id}", response_model=FaAgentDefinitionsOut)
async def get_fa_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAgentDefinitionsService(db).get(entity_id)

@router.post("/fa_agent_definitions", response_model=FaAgentDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_agent_definitions(
    data: FaAgentDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAgentDefinitionsService(db).create(data)

@router.put("/fa_agent_definitions/{entity_id}", response_model=FaAgentDefinitionsOut)
async def update_fa_agent_definitions(
    entity_id: uuid.UUID,
    data: FaAgentDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAgentDefinitionsService(db).update(entity_id, data)

@router.delete("/fa_agent_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAgentDefinitionsService(db).delete(entity_id)

@router.get("/fa_algorithms", response_model=PaginatedResponse[FaAlgorithmsOut])
async def list_fa_algorithms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAlgorithmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["algorithm_name", "algorithm_type_code", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_algorithms/{entity_id}", response_model=FaAlgorithmsOut)
async def get_fa_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAlgorithmsService(db).get(entity_id)

@router.post("/fa_algorithms", response_model=FaAlgorithmsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_algorithms(
    data: FaAlgorithmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAlgorithmsService(db).create(data)

@router.put("/fa_algorithms/{entity_id}", response_model=FaAlgorithmsOut)
async def update_fa_algorithms(
    entity_id: uuid.UUID,
    data: FaAlgorithmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAlgorithmsService(db).update(entity_id, data)

@router.delete("/fa_algorithms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAlgorithmsService(db).delete(entity_id)

@router.get("/fa_asset_attachments", response_model=PaginatedResponse[FaAssetAttachmentsOut])
async def list_fa_asset_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["attachment_type_code", "file_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_attachments/{entity_id}", response_model=FaAssetAttachmentsOut)
async def get_fa_asset_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetAttachmentsService(db).get(entity_id)

@router.post("/fa_asset_attachments", response_model=FaAssetAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_attachments(
    data: FaAssetAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetAttachmentsService(db).create(data)

@router.put("/fa_asset_attachments/{entity_id}", response_model=FaAssetAttachmentsOut)
async def update_fa_asset_attachments(
    entity_id: uuid.UUID,
    data: FaAssetAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetAttachmentsService(db).update(entity_id, data)

@router.delete("/fa_asset_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetAttachmentsService(db).delete(entity_id)

@router.get("/fa_asset_book_assignments", response_model=PaginatedResponse[FaAssetBookAssignmentsOut])
async def list_fa_asset_book_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetBookAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["deprn_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_book_assignments/{entity_id}", response_model=FaAssetBookAssignmentsOut)
async def get_fa_asset_book_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetBookAssignmentsService(db).get(entity_id)

@router.post("/fa_asset_book_assignments", response_model=FaAssetBookAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_book_assignments(
    data: FaAssetBookAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetBookAssignmentsService(db).create(data)

@router.put("/fa_asset_book_assignments/{entity_id}", response_model=FaAssetBookAssignmentsOut)
async def update_fa_asset_book_assignments(
    entity_id: uuid.UUID,
    data: FaAssetBookAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetBookAssignmentsService(db).update(entity_id, data)

@router.delete("/fa_asset_book_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_book_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetBookAssignmentsService(db).delete(entity_id)

@router.get("/fa_asset_categories", response_model=PaginatedResponse[FaAssetCategoriesOut])
async def list_fa_asset_categories(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetCategoriesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["category_code", "category_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_categories/{entity_id}", response_model=FaAssetCategoriesOut)
async def get_fa_asset_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetCategoriesService(db).get(entity_id)

@router.post("/fa_asset_categories", response_model=FaAssetCategoriesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_categories(
    data: FaAssetCategoriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCategoriesService(db).create(data)

@router.put("/fa_asset_categories/{entity_id}", response_model=FaAssetCategoriesOut)
async def update_fa_asset_categories(
    entity_id: uuid.UUID,
    data: FaAssetCategoriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCategoriesService(db).update(entity_id, data)

@router.delete("/fa_asset_categories/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetCategoriesService(db).delete(entity_id)

@router.get("/fa_asset_category_hierarchy", response_model=PaginatedResponse[FaAssetCategoryHierarchyOut])
async def list_fa_asset_category_hierarchy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetCategoryHierarchyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_category_hierarchy/{entity_id}", response_model=FaAssetCategoryHierarchyOut)
async def get_fa_asset_category_hierarchy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetCategoryHierarchyService(db).get(entity_id)

@router.post("/fa_asset_category_hierarchy", response_model=FaAssetCategoryHierarchyOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_category_hierarchy(
    data: FaAssetCategoryHierarchyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCategoryHierarchyService(db).create(data)

@router.put("/fa_asset_category_hierarchy/{entity_id}", response_model=FaAssetCategoryHierarchyOut)
async def update_fa_asset_category_hierarchy(
    entity_id: uuid.UUID,
    data: FaAssetCategoryHierarchyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCategoryHierarchyService(db).update(entity_id, data)

@router.delete("/fa_asset_category_hierarchy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_category_hierarchy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetCategoryHierarchyService(db).delete(entity_id)

@router.get("/fa_asset_components", response_model=PaginatedResponse[FaAssetComponentsOut])
async def list_fa_asset_components(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetComponentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["component_name", "component_description", "component_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_components/{entity_id}", response_model=FaAssetComponentsOut)
async def get_fa_asset_components(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetComponentsService(db).get(entity_id)

@router.post("/fa_asset_components", response_model=FaAssetComponentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_components(
    data: FaAssetComponentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetComponentsService(db).create(data)

@router.put("/fa_asset_components/{entity_id}", response_model=FaAssetComponentsOut)
async def update_fa_asset_components(
    entity_id: uuid.UUID,
    data: FaAssetComponentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetComponentsService(db).update(entity_id, data)

@router.delete("/fa_asset_components/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_components(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetComponentsService(db).delete(entity_id)

@router.get("/fa_asset_custom_attributes", response_model=PaginatedResponse[FaAssetCustomAttributesOut])
async def list_fa_asset_custom_attributes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetCustomAttributesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["attribute_name", "attribute_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_custom_attributes/{entity_id}", response_model=FaAssetCustomAttributesOut)
async def get_fa_asset_custom_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetCustomAttributesService(db).get(entity_id)

@router.post("/fa_asset_custom_attributes", response_model=FaAssetCustomAttributesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_custom_attributes(
    data: FaAssetCustomAttributesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCustomAttributesService(db).create(data)

@router.put("/fa_asset_custom_attributes/{entity_id}", response_model=FaAssetCustomAttributesOut)
async def update_fa_asset_custom_attributes(
    entity_id: uuid.UUID,
    data: FaAssetCustomAttributesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetCustomAttributesService(db).update(entity_id, data)

@router.delete("/fa_asset_custom_attributes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_custom_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetCustomAttributesService(db).delete(entity_id)

@router.get("/fa_asset_photos", response_model=PaginatedResponse[FaAssetPhotosOut])
async def list_fa_asset_photos(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetPhotosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["photo_type_code", "file_name", "photographer_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_photos/{entity_id}", response_model=FaAssetPhotosOut)
async def get_fa_asset_photos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetPhotosService(db).get(entity_id)

@router.post("/fa_asset_photos", response_model=FaAssetPhotosOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_photos(
    data: FaAssetPhotosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetPhotosService(db).create(data)

@router.put("/fa_asset_photos/{entity_id}", response_model=FaAssetPhotosOut)
async def update_fa_asset_photos(
    entity_id: uuid.UUID,
    data: FaAssetPhotosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetPhotosService(db).update(entity_id, data)

@router.delete("/fa_asset_photos/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_photos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetPhotosService(db).delete(entity_id)

@router.get("/fa_asset_storage", response_model=PaginatedResponse[FaAssetStorageOut])
async def list_fa_asset_storage(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetStorageService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["container_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_storage/{entity_id}", response_model=FaAssetStorageOut)
async def get_fa_asset_storage(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetStorageService(db).get(entity_id)

@router.post("/fa_asset_storage", response_model=FaAssetStorageOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_storage(
    data: FaAssetStorageCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetStorageService(db).create(data)

@router.put("/fa_asset_storage/{entity_id}", response_model=FaAssetStorageOut)
async def update_fa_asset_storage(
    entity_id: uuid.UUID,
    data: FaAssetStorageUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetStorageService(db).update(entity_id, data)

@router.delete("/fa_asset_storage/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_storage(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetStorageService(db).delete(entity_id)

@router.get("/fa_asset_tags", response_model=PaginatedResponse[FaAssetTagsOut])
async def list_fa_asset_tags(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetTagsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tag_type_code", "tag_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_tags/{entity_id}", response_model=FaAssetTagsOut)
async def get_fa_asset_tags(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetTagsService(db).get(entity_id)

@router.post("/fa_asset_tags", response_model=FaAssetTagsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_tags(
    data: FaAssetTagsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetTagsService(db).create(data)

@router.put("/fa_asset_tags/{entity_id}", response_model=FaAssetTagsOut)
async def update_fa_asset_tags(
    entity_id: uuid.UUID,
    data: FaAssetTagsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetTagsService(db).update(entity_id, data)

@router.delete("/fa_asset_tags/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_tags(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetTagsService(db).delete(entity_id)

@router.get("/fa_asset_types", response_model=PaginatedResponse[FaAssetTypesOut])
async def list_fa_asset_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_type_code", "asset_type_name", "asset_class_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_asset_types/{entity_id}", response_model=FaAssetTypesOut)
async def get_fa_asset_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetTypesService(db).get(entity_id)

@router.post("/fa_asset_types", response_model=FaAssetTypesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_asset_types(
    data: FaAssetTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetTypesService(db).create(data)

@router.put("/fa_asset_types/{entity_id}", response_model=FaAssetTypesOut)
async def update_fa_asset_types(
    entity_id: uuid.UUID,
    data: FaAssetTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetTypesService(db).update(entity_id, data)

@router.delete("/fa_asset_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_asset_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetTypesService(db).delete(entity_id)

@router.get("/fa_assets", response_model=PaginatedResponse[FaAssetsOut])
async def list_fa_assets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaAssetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_number", "asset_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_assets/{entity_id}", response_model=FaAssetsOut)
async def get_fa_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaAssetsService(db).get(entity_id)

@router.post("/fa_assets", response_model=FaAssetsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_assets(
    data: FaAssetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetsService(db).create(data)

@router.put("/fa_assets/{entity_id}", response_model=FaAssetsOut)
async def update_fa_assets(
    entity_id: uuid.UUID,
    data: FaAssetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaAssetsService(db).update(entity_id, data)

@router.delete("/fa_assets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaAssetsService(db).delete(entity_id)

@router.get("/fa_bonus_depreciation", response_model=PaginatedResponse[FaBonusDepreciationOut])
async def list_fa_bonus_depreciation(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaBonusDepreciationService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["bonus_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_bonus_depreciation/{entity_id}", response_model=FaBonusDepreciationOut)
async def get_fa_bonus_depreciation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaBonusDepreciationService(db).get(entity_id)

@router.post("/fa_bonus_depreciation", response_model=FaBonusDepreciationOut, status_code=status.HTTP_201_CREATED)
async def create_fa_bonus_depreciation(
    data: FaBonusDepreciationCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaBonusDepreciationService(db).create(data)

@router.put("/fa_bonus_depreciation/{entity_id}", response_model=FaBonusDepreciationOut)
async def update_fa_bonus_depreciation(
    entity_id: uuid.UUID,
    data: FaBonusDepreciationUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaBonusDepreciationService(db).update(entity_id, data)

@router.delete("/fa_bonus_depreciation/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_bonus_depreciation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaBonusDepreciationService(db).delete(entity_id)

@router.get("/fa_book_types", response_model=PaginatedResponse[FaBookTypesOut])
async def list_fa_book_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaBookTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["book_type_code", "book_type_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_book_types/{entity_id}", response_model=FaBookTypesOut)
async def get_fa_book_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaBookTypesService(db).get(entity_id)

@router.post("/fa_book_types", response_model=FaBookTypesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_book_types(
    data: FaBookTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaBookTypesService(db).create(data)

@router.put("/fa_book_types/{entity_id}", response_model=FaBookTypesOut)
async def update_fa_book_types(
    entity_id: uuid.UUID,
    data: FaBookTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaBookTypesService(db).update(entity_id, data)

@router.delete("/fa_book_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_book_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaBookTypesService(db).delete(entity_id)

@router.get("/fa_cip_costs", response_model=PaginatedResponse[FaCipCostsOut])
async def list_fa_cip_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCipCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cost_type_code", "description", "reference_doc_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_cip_costs/{entity_id}", response_model=FaCipCostsOut)
async def get_fa_cip_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCipCostsService(db).get(entity_id)

@router.post("/fa_cip_costs", response_model=FaCipCostsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_cip_costs(
    data: FaCipCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCipCostsService(db).create(data)

@router.put("/fa_cip_costs/{entity_id}", response_model=FaCipCostsOut)
async def update_fa_cip_costs(
    entity_id: uuid.UUID,
    data: FaCipCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCipCostsService(db).update(entity_id, data)

@router.delete("/fa_cip_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_cip_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCipCostsService(db).delete(entity_id)

@router.get("/fa_cip_projects", response_model=PaginatedResponse[FaCipProjectsOut])
async def list_fa_cip_projects(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCipProjectsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["project_code", "project_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_cip_projects/{entity_id}", response_model=FaCipProjectsOut)
async def get_fa_cip_projects(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCipProjectsService(db).get(entity_id)

@router.post("/fa_cip_projects", response_model=FaCipProjectsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_cip_projects(
    data: FaCipProjectsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCipProjectsService(db).create(data)

@router.put("/fa_cip_projects/{entity_id}", response_model=FaCipProjectsOut)
async def update_fa_cip_projects(
    entity_id: uuid.UUID,
    data: FaCipProjectsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCipProjectsService(db).update(entity_id, data)

@router.delete("/fa_cip_projects/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_cip_projects(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCipProjectsService(db).delete(entity_id)

@router.get("/fa_count_lines", response_model=PaginatedResponse[FaCountLinesOut])
async def list_fa_count_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCountLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_number", "asset_description", "barcode_expected"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_count_lines/{entity_id}", response_model=FaCountLinesOut)
async def get_fa_count_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCountLinesService(db).get(entity_id)

@router.post("/fa_count_lines", response_model=FaCountLinesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_count_lines(
    data: FaCountLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountLinesService(db).create(data)

@router.put("/fa_count_lines/{entity_id}", response_model=FaCountLinesOut)
async def update_fa_count_lines(
    entity_id: uuid.UUID,
    data: FaCountLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountLinesService(db).update(entity_id, data)

@router.delete("/fa_count_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_count_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCountLinesService(db).delete(entity_id)

@router.get("/fa_count_routes", response_model=PaginatedResponse[FaCountRoutesOut])
async def list_fa_count_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCountRoutesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["counter_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_count_routes/{entity_id}", response_model=FaCountRoutesOut)
async def get_fa_count_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCountRoutesService(db).get(entity_id)

@router.post("/fa_count_routes", response_model=FaCountRoutesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_count_routes(
    data: FaCountRoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountRoutesService(db).create(data)

@router.put("/fa_count_routes/{entity_id}", response_model=FaCountRoutesOut)
async def update_fa_count_routes(
    entity_id: uuid.UUID,
    data: FaCountRoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountRoutesService(db).update(entity_id, data)

@router.delete("/fa_count_routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_count_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCountRoutesService(db).delete(entity_id)

@router.get("/fa_count_sheets", response_model=PaginatedResponse[FaCountSheetsOut])
async def list_fa_count_sheets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCountSheetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["sheet_number", "counter_name", "sheet_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_count_sheets/{entity_id}", response_model=FaCountSheetsOut)
async def get_fa_count_sheets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCountSheetsService(db).get(entity_id)

@router.post("/fa_count_sheets", response_model=FaCountSheetsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_count_sheets(
    data: FaCountSheetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountSheetsService(db).create(data)

@router.put("/fa_count_sheets/{entity_id}", response_model=FaCountSheetsOut)
async def update_fa_count_sheets(
    entity_id: uuid.UUID,
    data: FaCountSheetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountSheetsService(db).update(entity_id, data)

@router.delete("/fa_count_sheets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_count_sheets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCountSheetsService(db).delete(entity_id)

@router.get("/fa_count_variances", response_model=PaginatedResponse[FaCountVariancesOut])
async def list_fa_count_variances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCountVariancesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["variance_type_code", "variance_severity_code", "variance_reason_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_count_variances/{entity_id}", response_model=FaCountVariancesOut)
async def get_fa_count_variances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCountVariancesService(db).get(entity_id)

@router.post("/fa_count_variances", response_model=FaCountVariancesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_count_variances(
    data: FaCountVariancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountVariancesService(db).create(data)

@router.put("/fa_count_variances/{entity_id}", response_model=FaCountVariancesOut)
async def update_fa_count_variances(
    entity_id: uuid.UUID,
    data: FaCountVariancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCountVariancesService(db).update(entity_id, data)

@router.delete("/fa_count_variances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_count_variances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCountVariancesService(db).delete(entity_id)

@router.get("/fa_custodians", response_model=PaginatedResponse[FaCustodiansOut])
async def list_fa_custodians(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaCustodiansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["custodian_code", "custodian_name", "custodian_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_custodians/{entity_id}", response_model=FaCustodiansOut)
async def get_fa_custodians(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaCustodiansService(db).get(entity_id)

@router.post("/fa_custodians", response_model=FaCustodiansOut, status_code=status.HTTP_201_CREATED)
async def create_fa_custodians(
    data: FaCustodiansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCustodiansService(db).create(data)

@router.put("/fa_custodians/{entity_id}", response_model=FaCustodiansOut)
async def update_fa_custodians(
    entity_id: uuid.UUID,
    data: FaCustodiansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaCustodiansService(db).update(entity_id, data)

@router.delete("/fa_custodians/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_custodians(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaCustodiansService(db).delete(entity_id)

@router.get("/fa_deprn_book_periods", response_model=PaginatedResponse[FaDeprnBookPeriodsOut])
async def list_fa_deprn_book_periods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaDeprnBookPeriodsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["period_name", "period_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_deprn_book_periods/{entity_id}", response_model=FaDeprnBookPeriodsOut)
async def get_fa_deprn_book_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaDeprnBookPeriodsService(db).get(entity_id)

@router.post("/fa_deprn_book_periods", response_model=FaDeprnBookPeriodsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_deprn_book_periods(
    data: FaDeprnBookPeriodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnBookPeriodsService(db).create(data)

@router.put("/fa_deprn_book_periods/{entity_id}", response_model=FaDeprnBookPeriodsOut)
async def update_fa_deprn_book_periods(
    entity_id: uuid.UUID,
    data: FaDeprnBookPeriodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnBookPeriodsService(db).update(entity_id, data)

@router.delete("/fa_deprn_book_periods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_deprn_book_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaDeprnBookPeriodsService(db).delete(entity_id)

@router.get("/fa_deprn_books", response_model=PaginatedResponse[FaDeprnBooksOut])
async def list_fa_deprn_books(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaDeprnBooksService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["book_code", "book_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_deprn_books/{entity_id}", response_model=FaDeprnBooksOut)
async def get_fa_deprn_books(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaDeprnBooksService(db).get(entity_id)

@router.post("/fa_deprn_books", response_model=FaDeprnBooksOut, status_code=status.HTTP_201_CREATED)
async def create_fa_deprn_books(
    data: FaDeprnBooksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnBooksService(db).create(data)

@router.put("/fa_deprn_books/{entity_id}", response_model=FaDeprnBooksOut)
async def update_fa_deprn_books(
    entity_id: uuid.UUID,
    data: FaDeprnBooksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnBooksService(db).update(entity_id, data)

@router.delete("/fa_deprn_books/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_deprn_books(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaDeprnBooksService(db).delete(entity_id)

@router.get("/fa_deprn_calculation", response_model=PaginatedResponse[FaDeprnCalculationOut])
async def list_fa_deprn_calculation(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaDeprnCalculationService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["deprn_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_deprn_calculation/{entity_id}", response_model=FaDeprnCalculationOut)
async def get_fa_deprn_calculation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaDeprnCalculationService(db).get(entity_id)

@router.post("/fa_deprn_calculation", response_model=FaDeprnCalculationOut, status_code=status.HTTP_201_CREATED)
async def create_fa_deprn_calculation(
    data: FaDeprnCalculationCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnCalculationService(db).create(data)

@router.put("/fa_deprn_calculation/{entity_id}", response_model=FaDeprnCalculationOut)
async def update_fa_deprn_calculation(
    entity_id: uuid.UUID,
    data: FaDeprnCalculationUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnCalculationService(db).update(entity_id, data)

@router.delete("/fa_deprn_calculation/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_deprn_calculation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaDeprnCalculationService(db).delete(entity_id)

@router.get("/fa_deprn_conventions", response_model=PaginatedResponse[FaDeprnConventionsOut])
async def list_fa_deprn_conventions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaDeprnConventionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["convention_code", "convention_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_deprn_conventions/{entity_id}", response_model=FaDeprnConventionsOut)
async def get_fa_deprn_conventions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaDeprnConventionsService(db).get(entity_id)

@router.post("/fa_deprn_conventions", response_model=FaDeprnConventionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_deprn_conventions(
    data: FaDeprnConventionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnConventionsService(db).create(data)

@router.put("/fa_deprn_conventions/{entity_id}", response_model=FaDeprnConventionsOut)
async def update_fa_deprn_conventions(
    entity_id: uuid.UUID,
    data: FaDeprnConventionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnConventionsService(db).update(entity_id, data)

@router.delete("/fa_deprn_conventions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_deprn_conventions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaDeprnConventionsService(db).delete(entity_id)

@router.get("/fa_deprn_methods", response_model=PaginatedResponse[FaDeprnMethodsOut])
async def list_fa_deprn_methods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaDeprnMethodsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["method_code", "method_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_deprn_methods/{entity_id}", response_model=FaDeprnMethodsOut)
async def get_fa_deprn_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaDeprnMethodsService(db).get(entity_id)

@router.post("/fa_deprn_methods", response_model=FaDeprnMethodsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_deprn_methods(
    data: FaDeprnMethodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnMethodsService(db).create(data)

@router.put("/fa_deprn_methods/{entity_id}", response_model=FaDeprnMethodsOut)
async def update_fa_deprn_methods(
    entity_id: uuid.UUID,
    data: FaDeprnMethodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaDeprnMethodsService(db).update(entity_id, data)

@router.delete("/fa_deprn_methods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_deprn_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaDeprnMethodsService(db).delete(entity_id)

@router.get("/fa_group_asset_members", response_model=PaginatedResponse[FaGroupAssetMembersOut])
async def list_fa_group_asset_members(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaGroupAssetMembersService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_group_asset_members/{entity_id}", response_model=FaGroupAssetMembersOut)
async def get_fa_group_asset_members(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaGroupAssetMembersService(db).get(entity_id)

@router.post("/fa_group_asset_members", response_model=FaGroupAssetMembersOut, status_code=status.HTTP_201_CREATED)
async def create_fa_group_asset_members(
    data: FaGroupAssetMembersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaGroupAssetMembersService(db).create(data)

@router.put("/fa_group_asset_members/{entity_id}", response_model=FaGroupAssetMembersOut)
async def update_fa_group_asset_members(
    entity_id: uuid.UUID,
    data: FaGroupAssetMembersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaGroupAssetMembersService(db).update(entity_id, data)

@router.delete("/fa_group_asset_members/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_group_asset_members(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaGroupAssetMembersService(db).delete(entity_id)

@router.get("/fa_group_assets", response_model=PaginatedResponse[FaGroupAssetsOut])
async def list_fa_group_assets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaGroupAssetsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["group_code", "group_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_group_assets/{entity_id}", response_model=FaGroupAssetsOut)
async def get_fa_group_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaGroupAssetsService(db).get(entity_id)

@router.post("/fa_group_assets", response_model=FaGroupAssetsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_group_assets(
    data: FaGroupAssetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaGroupAssetsService(db).create(data)

@router.put("/fa_group_assets/{entity_id}", response_model=FaGroupAssetsOut)
async def update_fa_group_assets(
    entity_id: uuid.UUID,
    data: FaGroupAssetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaGroupAssetsService(db).update(entity_id, data)

@router.delete("/fa_group_assets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_group_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaGroupAssetsService(db).delete(entity_id)

@router.get("/fa_impairments", response_model=PaginatedResponse[FaImpairmentsOut])
async def list_fa_impairments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaImpairmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["impairment_indicator_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_impairments/{entity_id}", response_model=FaImpairmentsOut)
async def get_fa_impairments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaImpairmentsService(db).get(entity_id)

@router.post("/fa_impairments", response_model=FaImpairmentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_impairments(
    data: FaImpairmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaImpairmentsService(db).create(data)

@router.put("/fa_impairments/{entity_id}", response_model=FaImpairmentsOut)
async def update_fa_impairments(
    entity_id: uuid.UUID,
    data: FaImpairmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaImpairmentsService(db).update(entity_id, data)

@router.delete("/fa_impairments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_impairments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaImpairmentsService(db).delete(entity_id)

@router.get("/fa_insurance_claims", response_model=PaginatedResponse[FaInsuranceClaimsOut])
async def list_fa_insurance_claims(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaInsuranceClaimsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["claim_number", "claim_type_code", "claim_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_insurance_claims/{entity_id}", response_model=FaInsuranceClaimsOut)
async def get_fa_insurance_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaInsuranceClaimsService(db).get(entity_id)

@router.post("/fa_insurance_claims", response_model=FaInsuranceClaimsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_insurance_claims(
    data: FaInsuranceClaimsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaInsuranceClaimsService(db).create(data)

@router.put("/fa_insurance_claims/{entity_id}", response_model=FaInsuranceClaimsOut)
async def update_fa_insurance_claims(
    entity_id: uuid.UUID,
    data: FaInsuranceClaimsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaInsuranceClaimsService(db).update(entity_id, data)

@router.delete("/fa_insurance_claims/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_insurance_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaInsuranceClaimsService(db).delete(entity_id)

@router.get("/fa_insurance_policies", response_model=PaginatedResponse[FaInsurancePoliciesOut])
async def list_fa_insurance_policies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaInsurancePoliciesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["policy_number", "policy_name", "coverage_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_insurance_policies/{entity_id}", response_model=FaInsurancePoliciesOut)
async def get_fa_insurance_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaInsurancePoliciesService(db).get(entity_id)

@router.post("/fa_insurance_policies", response_model=FaInsurancePoliciesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_insurance_policies(
    data: FaInsurancePoliciesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaInsurancePoliciesService(db).create(data)

@router.put("/fa_insurance_policies/{entity_id}", response_model=FaInsurancePoliciesOut)
async def update_fa_insurance_policies(
    entity_id: uuid.UUID,
    data: FaInsurancePoliciesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaInsurancePoliciesService(db).update(entity_id, data)

@router.delete("/fa_insurance_policies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_insurance_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaInsurancePoliciesService(db).delete(entity_id)

@router.get("/fa_integration_connections", response_model=PaginatedResponse[FaIntegrationConnectionsOut])
async def list_fa_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaIntegrationConnectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["connection_name", "system_code", "integration_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_integration_connections/{entity_id}", response_model=FaIntegrationConnectionsOut)
async def get_fa_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaIntegrationConnectionsService(db).get(entity_id)

@router.post("/fa_integration_connections", response_model=FaIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_integration_connections(
    data: FaIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaIntegrationConnectionsService(db).create(data)

@router.put("/fa_integration_connections/{entity_id}", response_model=FaIntegrationConnectionsOut)
async def update_fa_integration_connections(
    entity_id: uuid.UUID,
    data: FaIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/fa_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaIntegrationConnectionsService(db).delete(entity_id)

@router.get("/fa_integration_logs", response_model=PaginatedResponse[FaIntegrationLogsOut])
async def list_fa_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaIntegrationLogsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_integration_logs/{entity_id}", response_model=FaIntegrationLogsOut)
async def get_fa_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaIntegrationLogsService(db).get(entity_id)

@router.post("/fa_integration_logs", response_model=FaIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_integration_logs(
    data: FaIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaIntegrationLogsService(db).create(data)

@router.put("/fa_integration_logs/{entity_id}", response_model=FaIntegrationLogsOut)
async def update_fa_integration_logs(
    entity_id: uuid.UUID,
    data: FaIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaIntegrationLogsService(db).update(entity_id, data)

@router.delete("/fa_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaIntegrationLogsService(db).delete(entity_id)

@router.get("/fa_langgraph_executions", response_model=PaginatedResponse[FaLanggraphExecutionsOut])
async def list_fa_langgraph_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLanggraphExecutionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["execution_name", "execution_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_langgraph_executions/{entity_id}", response_model=FaLanggraphExecutionsOut)
async def get_fa_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLanggraphExecutionsService(db).get(entity_id)

@router.post("/fa_langgraph_executions", response_model=FaLanggraphExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_langgraph_executions(
    data: FaLanggraphExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphExecutionsService(db).create(data)

@router.put("/fa_langgraph_executions/{entity_id}", response_model=FaLanggraphExecutionsOut)
async def update_fa_langgraph_executions(
    entity_id: uuid.UUID,
    data: FaLanggraphExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphExecutionsService(db).update(entity_id, data)

@router.delete("/fa_langgraph_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLanggraphExecutionsService(db).delete(entity_id)

@router.get("/fa_langgraph_states", response_model=PaginatedResponse[FaLanggraphStatesOut])
async def list_fa_langgraph_states(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLanggraphStatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["node_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_langgraph_states/{entity_id}", response_model=FaLanggraphStatesOut)
async def get_fa_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLanggraphStatesService(db).get(entity_id)

@router.post("/fa_langgraph_states", response_model=FaLanggraphStatesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_langgraph_states(
    data: FaLanggraphStatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphStatesService(db).create(data)

@router.put("/fa_langgraph_states/{entity_id}", response_model=FaLanggraphStatesOut)
async def update_fa_langgraph_states(
    entity_id: uuid.UUID,
    data: FaLanggraphStatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphStatesService(db).update(entity_id, data)

@router.delete("/fa_langgraph_states/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLanggraphStatesService(db).delete(entity_id)

@router.get("/fa_langgraph_workflows", response_model=PaginatedResponse[FaLanggraphWorkflowsOut])
async def list_fa_langgraph_workflows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLanggraphWorkflowsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_name", "workflow_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_langgraph_workflows/{entity_id}", response_model=FaLanggraphWorkflowsOut)
async def get_fa_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLanggraphWorkflowsService(db).get(entity_id)

@router.post("/fa_langgraph_workflows", response_model=FaLanggraphWorkflowsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_langgraph_workflows(
    data: FaLanggraphWorkflowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphWorkflowsService(db).create(data)

@router.put("/fa_langgraph_workflows/{entity_id}", response_model=FaLanggraphWorkflowsOut)
async def update_fa_langgraph_workflows(
    entity_id: uuid.UUID,
    data: FaLanggraphWorkflowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLanggraphWorkflowsService(db).update(entity_id, data)

@router.delete("/fa_langgraph_workflows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLanggraphWorkflowsService(db).delete(entity_id)

@router.get("/fa_lease_assets", response_model=PaginatedResponse[FaLeaseAssetsOut])
async def list_fa_lease_assets(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLeaseAssetsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_lease_assets/{entity_id}", response_model=FaLeaseAssetsOut)
async def get_fa_lease_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLeaseAssetsService(db).get(entity_id)

@router.post("/fa_lease_assets", response_model=FaLeaseAssetsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_lease_assets(
    data: FaLeaseAssetsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeaseAssetsService(db).create(data)

@router.put("/fa_lease_assets/{entity_id}", response_model=FaLeaseAssetsOut)
async def update_fa_lease_assets(
    entity_id: uuid.UUID,
    data: FaLeaseAssetsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeaseAssetsService(db).update(entity_id, data)

@router.delete("/fa_lease_assets/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_lease_assets(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLeaseAssetsService(db).delete(entity_id)

@router.get("/fa_lease_schedules", response_model=PaginatedResponse[FaLeaseSchedulesOut])
async def list_fa_lease_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLeaseSchedulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["payment_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_lease_schedules/{entity_id}", response_model=FaLeaseSchedulesOut)
async def get_fa_lease_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLeaseSchedulesService(db).get(entity_id)

@router.post("/fa_lease_schedules", response_model=FaLeaseSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_lease_schedules(
    data: FaLeaseSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeaseSchedulesService(db).create(data)

@router.put("/fa_lease_schedules/{entity_id}", response_model=FaLeaseSchedulesOut)
async def update_fa_lease_schedules(
    entity_id: uuid.UUID,
    data: FaLeaseSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeaseSchedulesService(db).update(entity_id, data)

@router.delete("/fa_lease_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_lease_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLeaseSchedulesService(db).delete(entity_id)

@router.get("/fa_leases", response_model=PaginatedResponse[FaLeasesOut])
async def list_fa_leases(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLeasesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lease_number", "lease_name", "lease_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_leases/{entity_id}", response_model=FaLeasesOut)
async def get_fa_leases(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLeasesService(db).get(entity_id)

@router.post("/fa_leases", response_model=FaLeasesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_leases(
    data: FaLeasesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeasesService(db).create(data)

@router.put("/fa_leases/{entity_id}", response_model=FaLeasesOut)
async def update_fa_leases(
    entity_id: uuid.UUID,
    data: FaLeasesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLeasesService(db).update(entity_id, data)

@router.delete("/fa_leases/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_leases(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLeasesService(db).delete(entity_id)

@router.get("/fa_llm_configs", response_model=PaginatedResponse[FaLlmConfigsOut])
async def list_fa_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["config_name", "provider_name", "model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_llm_configs/{entity_id}", response_model=FaLlmConfigsOut)
async def get_fa_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLlmConfigsService(db).get(entity_id)

@router.post("/fa_llm_configs", response_model=FaLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_llm_configs(
    data: FaLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLlmConfigsService(db).create(data)

@router.put("/fa_llm_configs/{entity_id}", response_model=FaLlmConfigsOut)
async def update_fa_llm_configs(
    entity_id: uuid.UUID,
    data: FaLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLlmConfigsService(db).update(entity_id, data)

@router.delete("/fa_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLlmConfigsService(db).delete(entity_id)

@router.get("/fa_locations", response_model=PaginatedResponse[FaLocationsOut])
async def list_fa_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_locations/{entity_id}", response_model=FaLocationsOut)
async def get_fa_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaLocationsService(db).get(entity_id)

@router.post("/fa_locations", response_model=FaLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_locations(
    data: FaLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLocationsService(db).create(data)

@router.put("/fa_locations/{entity_id}", response_model=FaLocationsOut)
async def update_fa_locations(
    entity_id: uuid.UUID,
    data: FaLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaLocationsService(db).update(entity_id, data)

@router.delete("/fa_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaLocationsService(db).delete(entity_id)

@router.get("/fa_ml_models", response_model=PaginatedResponse[FaMlModelsOut])
async def list_fa_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name", "model_type_code", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_ml_models/{entity_id}", response_model=FaMlModelsOut)
async def get_fa_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaMlModelsService(db).get(entity_id)

@router.post("/fa_ml_models", response_model=FaMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_ml_models(
    data: FaMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMlModelsService(db).create(data)

@router.put("/fa_ml_models/{entity_id}", response_model=FaMlModelsOut)
async def update_fa_ml_models(
    entity_id: uuid.UUID,
    data: FaMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMlModelsService(db).update(entity_id, data)

@router.delete("/fa_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaMlModelsService(db).delete(entity_id)

@router.get("/fa_mobile_devices", response_model=PaginatedResponse[FaMobileDevicesOut])
async def list_fa_mobile_devices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaMobileDevicesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["device_name", "device_type_code", "imei_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_mobile_devices/{entity_id}", response_model=FaMobileDevicesOut)
async def get_fa_mobile_devices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaMobileDevicesService(db).get(entity_id)

@router.post("/fa_mobile_devices", response_model=FaMobileDevicesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_mobile_devices(
    data: FaMobileDevicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileDevicesService(db).create(data)

@router.put("/fa_mobile_devices/{entity_id}", response_model=FaMobileDevicesOut)
async def update_fa_mobile_devices(
    entity_id: uuid.UUID,
    data: FaMobileDevicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileDevicesService(db).update(entity_id, data)

@router.delete("/fa_mobile_devices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_mobile_devices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaMobileDevicesService(db).delete(entity_id)

@router.get("/fa_mobile_scans", response_model=PaginatedResponse[FaMobileScansOut])
async def list_fa_mobile_scans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaMobileScansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["asset_number", "barcode_scanned", "scan_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_mobile_scans/{entity_id}", response_model=FaMobileScansOut)
async def get_fa_mobile_scans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaMobileScansService(db).get(entity_id)

@router.post("/fa_mobile_scans", response_model=FaMobileScansOut, status_code=status.HTTP_201_CREATED)
async def create_fa_mobile_scans(
    data: FaMobileScansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileScansService(db).create(data)

@router.put("/fa_mobile_scans/{entity_id}", response_model=FaMobileScansOut)
async def update_fa_mobile_scans(
    entity_id: uuid.UUID,
    data: FaMobileScansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileScansService(db).update(entity_id, data)

@router.delete("/fa_mobile_scans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_mobile_scans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaMobileScansService(db).delete(entity_id)

@router.get("/fa_mobile_sync_batches", response_model=PaginatedResponse[FaMobileSyncBatchesOut])
async def list_fa_mobile_sync_batches(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaMobileSyncBatchesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["batch_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_mobile_sync_batches/{entity_id}", response_model=FaMobileSyncBatchesOut)
async def get_fa_mobile_sync_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaMobileSyncBatchesService(db).get(entity_id)

@router.post("/fa_mobile_sync_batches", response_model=FaMobileSyncBatchesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_mobile_sync_batches(
    data: FaMobileSyncBatchesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileSyncBatchesService(db).create(data)

@router.put("/fa_mobile_sync_batches/{entity_id}", response_model=FaMobileSyncBatchesOut)
async def update_fa_mobile_sync_batches(
    entity_id: uuid.UUID,
    data: FaMobileSyncBatchesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileSyncBatchesService(db).update(entity_id, data)

@router.delete("/fa_mobile_sync_batches/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_mobile_sync_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaMobileSyncBatchesService(db).delete(entity_id)

@router.get("/fa_mobile_users", response_model=PaginatedResponse[FaMobileUsersOut])
async def list_fa_mobile_users(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaMobileUsersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["username", "role_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_mobile_users/{entity_id}", response_model=FaMobileUsersOut)
async def get_fa_mobile_users(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaMobileUsersService(db).get(entity_id)

@router.post("/fa_mobile_users", response_model=FaMobileUsersOut, status_code=status.HTTP_201_CREATED)
async def create_fa_mobile_users(
    data: FaMobileUsersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileUsersService(db).create(data)

@router.put("/fa_mobile_users/{entity_id}", response_model=FaMobileUsersOut)
async def update_fa_mobile_users(
    entity_id: uuid.UUID,
    data: FaMobileUsersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaMobileUsersService(db).update(entity_id, data)

@router.delete("/fa_mobile_users/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_mobile_users(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaMobileUsersService(db).delete(entity_id)

@router.get("/fa_optimization_problems", response_model=PaginatedResponse[FaOptimizationProblemsOut])
async def list_fa_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaOptimizationProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_name", "problem_type_code", "objective_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_optimization_problems/{entity_id}", response_model=FaOptimizationProblemsOut)
async def get_fa_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaOptimizationProblemsService(db).get(entity_id)

@router.post("/fa_optimization_problems", response_model=FaOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_optimization_problems(
    data: FaOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaOptimizationProblemsService(db).create(data)

@router.put("/fa_optimization_problems/{entity_id}", response_model=FaOptimizationProblemsOut)
async def update_fa_optimization_problems(
    entity_id: uuid.UUID,
    data: FaOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/fa_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaOptimizationProblemsService(db).delete(entity_id)

@router.get("/fa_ortools_problems", response_model=PaginatedResponse[FaOrtoolsProblemsOut])
async def list_fa_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaOrtoolsProblemsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["problem_name", "solution_quality_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_ortools_problems/{entity_id}", response_model=FaOrtoolsProblemsOut)
async def get_fa_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaOrtoolsProblemsService(db).get(entity_id)

@router.post("/fa_ortools_problems", response_model=FaOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_ortools_problems(
    data: FaOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaOrtoolsProblemsService(db).create(data)

@router.put("/fa_ortools_problems/{entity_id}", response_model=FaOrtoolsProblemsOut)
async def update_fa_ortools_problems(
    entity_id: uuid.UUID,
    data: FaOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/fa_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaOrtoolsProblemsService(db).delete(entity_id)

@router.get("/fa_photos", response_model=PaginatedResponse[FaPhotosOut])
async def list_fa_photos(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaPhotosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["entity_type_code", "photo_type_code", "file_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_photos/{entity_id}", response_model=FaPhotosOut)
async def get_fa_photos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaPhotosService(db).get(entity_id)

@router.post("/fa_photos", response_model=FaPhotosOut, status_code=status.HTTP_201_CREATED)
async def create_fa_photos(
    data: FaPhotosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPhotosService(db).create(data)

@router.put("/fa_photos/{entity_id}", response_model=FaPhotosOut)
async def update_fa_photos(
    entity_id: uuid.UUID,
    data: FaPhotosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPhotosService(db).update(entity_id, data)

@router.delete("/fa_photos/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_photos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaPhotosService(db).delete(entity_id)

@router.get("/fa_physical_counts", response_model=PaginatedResponse[FaPhysicalCountsOut])
async def list_fa_physical_counts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaPhysicalCountsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["count_name", "description", "count_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_physical_counts/{entity_id}", response_model=FaPhysicalCountsOut)
async def get_fa_physical_counts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaPhysicalCountsService(db).get(entity_id)

@router.post("/fa_physical_counts", response_model=FaPhysicalCountsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_physical_counts(
    data: FaPhysicalCountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPhysicalCountsService(db).create(data)

@router.put("/fa_physical_counts/{entity_id}", response_model=FaPhysicalCountsOut)
async def update_fa_physical_counts(
    entity_id: uuid.UUID,
    data: FaPhysicalCountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPhysicalCountsService(db).update(entity_id, data)

@router.delete("/fa_physical_counts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_physical_counts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaPhysicalCountsService(db).delete(entity_id)

@router.get("/fa_prediction_actuals", response_model=PaginatedResponse[FaPredictionActualsOut])
async def list_fa_prediction_actuals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaPredictionActualsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["entity_type_code", "actual_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_prediction_actuals/{entity_id}", response_model=FaPredictionActualsOut)
async def get_fa_prediction_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaPredictionActualsService(db).get(entity_id)

@router.post("/fa_prediction_actuals", response_model=FaPredictionActualsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_prediction_actuals(
    data: FaPredictionActualsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPredictionActualsService(db).create(data)

@router.put("/fa_prediction_actuals/{entity_id}", response_model=FaPredictionActualsOut)
async def update_fa_prediction_actuals(
    entity_id: uuid.UUID,
    data: FaPredictionActualsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPredictionActualsService(db).update(entity_id, data)

@router.delete("/fa_prediction_actuals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_prediction_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaPredictionActualsService(db).delete(entity_id)

@router.get("/fa_predictions", response_model=PaginatedResponse[FaPredictionsOut])
async def list_fa_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaPredictionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["prediction_type_code", "entity_type_code", "prediction_label"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_predictions/{entity_id}", response_model=FaPredictionsOut)
async def get_fa_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaPredictionsService(db).get(entity_id)

@router.post("/fa_predictions", response_model=FaPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_predictions(
    data: FaPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPredictionsService(db).create(data)

@router.put("/fa_predictions/{entity_id}", response_model=FaPredictionsOut)
async def update_fa_predictions(
    entity_id: uuid.UUID,
    data: FaPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPredictionsService(db).update(entity_id, data)

@router.delete("/fa_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaPredictionsService(db).delete(entity_id)

@router.get("/fa_prompt_templates", response_model=PaginatedResponse[FaPromptTemplatesOut])
async def list_fa_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["template_name", "template_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_prompt_templates/{entity_id}", response_model=FaPromptTemplatesOut)
async def get_fa_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaPromptTemplatesService(db).get(entity_id)

@router.post("/fa_prompt_templates", response_model=FaPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_prompt_templates(
    data: FaPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPromptTemplatesService(db).create(data)

@router.put("/fa_prompt_templates/{entity_id}", response_model=FaPromptTemplatesOut)
async def update_fa_prompt_templates(
    entity_id: uuid.UUID,
    data: FaPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaPromptTemplatesService(db).update(entity_id, data)

@router.delete("/fa_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaPromptTemplatesService(db).delete(entity_id)

@router.get("/fa_reinstatements", response_model=PaginatedResponse[FaReinstatementsOut])
async def list_fa_reinstatements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaReinstatementsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_reinstatements/{entity_id}", response_model=FaReinstatementsOut)
async def get_fa_reinstatements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaReinstatementsService(db).get(entity_id)

@router.post("/fa_reinstatements", response_model=FaReinstatementsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_reinstatements(
    data: FaReinstatementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReinstatementsService(db).create(data)

@router.put("/fa_reinstatements/{entity_id}", response_model=FaReinstatementsOut)
async def update_fa_reinstatements(
    entity_id: uuid.UUID,
    data: FaReinstatementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReinstatementsService(db).update(entity_id, data)

@router.delete("/fa_reinstatements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_reinstatements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaReinstatementsService(db).delete(entity_id)

@router.get("/fa_report_schedules", response_model=PaginatedResponse[FaReportSchedulesOut])
async def list_fa_report_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaReportSchedulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["schedule_name", "frequency_code", "schedule_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_report_schedules/{entity_id}", response_model=FaReportSchedulesOut)
async def get_fa_report_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaReportSchedulesService(db).get(entity_id)

@router.post("/fa_report_schedules", response_model=FaReportSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_report_schedules(
    data: FaReportSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReportSchedulesService(db).create(data)

@router.put("/fa_report_schedules/{entity_id}", response_model=FaReportSchedulesOut)
async def update_fa_report_schedules(
    entity_id: uuid.UUID,
    data: FaReportSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReportSchedulesService(db).update(entity_id, data)

@router.delete("/fa_report_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_report_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaReportSchedulesService(db).delete(entity_id)

@router.get("/fa_reports", response_model=PaginatedResponse[FaReportsOut])
async def list_fa_reports(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaReportsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["report_code", "report_name", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_reports/{entity_id}", response_model=FaReportsOut)
async def get_fa_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaReportsService(db).get(entity_id)

@router.post("/fa_reports", response_model=FaReportsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_reports(
    data: FaReportsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReportsService(db).create(data)

@router.put("/fa_reports/{entity_id}", response_model=FaReportsOut)
async def update_fa_reports(
    entity_id: uuid.UUID,
    data: FaReportsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaReportsService(db).update(entity_id, data)

@router.delete("/fa_reports/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaReportsService(db).delete(entity_id)

@router.get("/fa_retirements", response_model=PaginatedResponse[FaRetirementsOut])
async def list_fa_retirements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaRetirementsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["retirement_type_code", "buyer_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_retirements/{entity_id}", response_model=FaRetirementsOut)
async def get_fa_retirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaRetirementsService(db).get(entity_id)

@router.post("/fa_retirements", response_model=FaRetirementsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_retirements(
    data: FaRetirementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaRetirementsService(db).create(data)

@router.put("/fa_retirements/{entity_id}", response_model=FaRetirementsOut)
async def update_fa_retirements(
    entity_id: uuid.UUID,
    data: FaRetirementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaRetirementsService(db).update(entity_id, data)

@router.delete("/fa_retirements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_retirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaRetirementsService(db).delete(entity_id)

@router.get("/fa_revaluations", response_model=PaginatedResponse[FaRevaluationsOut])
async def list_fa_revaluations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaRevaluationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["revaluation_reason_code", "appraiser_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_revaluations/{entity_id}", response_model=FaRevaluationsOut)
async def get_fa_revaluations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaRevaluationsService(db).get(entity_id)

@router.post("/fa_revaluations", response_model=FaRevaluationsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_revaluations(
    data: FaRevaluationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaRevaluationsService(db).create(data)

@router.put("/fa_revaluations/{entity_id}", response_model=FaRevaluationsOut)
async def update_fa_revaluations(
    entity_id: uuid.UUID,
    data: FaRevaluationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaRevaluationsService(db).update(entity_id, data)

@router.delete("/fa_revaluations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_revaluations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaRevaluationsService(db).delete(entity_id)

@router.get("/fa_scenarios", response_model=PaginatedResponse[FaScenariosOut])
async def list_fa_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_name", "scenario_type_code", "description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_scenarios/{entity_id}", response_model=FaScenariosOut)
async def get_fa_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaScenariosService(db).get(entity_id)

@router.post("/fa_scenarios", response_model=FaScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_fa_scenarios(
    data: FaScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaScenariosService(db).create(data)

@router.put("/fa_scenarios/{entity_id}", response_model=FaScenariosOut)
async def update_fa_scenarios(
    entity_id: uuid.UUID,
    data: FaScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaScenariosService(db).update(entity_id, data)

@router.delete("/fa_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaScenariosService(db).delete(entity_id)

@router.get("/fa_scipy_analyses", response_model=PaginatedResponse[FaScipyAnalysesOut])
async def list_fa_scipy_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaScipyAnalysesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["analysis_name", "analysis_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_scipy_analyses/{entity_id}", response_model=FaScipyAnalysesOut)
async def get_fa_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaScipyAnalysesService(db).get(entity_id)

@router.post("/fa_scipy_analyses", response_model=FaScipyAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_scipy_analyses(
    data: FaScipyAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaScipyAnalysesService(db).create(data)

@router.put("/fa_scipy_analyses/{entity_id}", response_model=FaScipyAnalysesOut)
async def update_fa_scipy_analyses(
    entity_id: uuid.UUID,
    data: FaScipyAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaScipyAnalysesService(db).update(entity_id, data)

@router.delete("/fa_scipy_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaScipyAnalysesService(db).delete(entity_id)

@router.get("/fa_signatures", response_model=PaginatedResponse[FaSignaturesOut])
async def list_fa_signatures(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaSignaturesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["entity_type_code", "signature_type_code", "signer_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_signatures/{entity_id}", response_model=FaSignaturesOut)
async def get_fa_signatures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaSignaturesService(db).get(entity_id)

@router.post("/fa_signatures", response_model=FaSignaturesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_signatures(
    data: FaSignaturesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaSignaturesService(db).create(data)

@router.put("/fa_signatures/{entity_id}", response_model=FaSignaturesOut)
async def update_fa_signatures(
    entity_id: uuid.UUID,
    data: FaSignaturesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaSignaturesService(db).update(entity_id, data)

@router.delete("/fa_signatures/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_signatures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaSignaturesService(db).delete(entity_id)

@router.get("/fa_solver_configs", response_model=PaginatedResponse[FaSolverConfigsOut])
async def list_fa_solver_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaSolverConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solver_name", "solver_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_solver_configs/{entity_id}", response_model=FaSolverConfigsOut)
async def get_fa_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaSolverConfigsService(db).get(entity_id)

@router.post("/fa_solver_configs", response_model=FaSolverConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_solver_configs(
    data: FaSolverConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaSolverConfigsService(db).create(data)

@router.put("/fa_solver_configs/{entity_id}", response_model=FaSolverConfigsOut)
async def update_fa_solver_configs(
    entity_id: uuid.UUID,
    data: FaSolverConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaSolverConfigsService(db).update(entity_id, data)

@router.delete("/fa_solver_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaSolverConfigsService(db).delete(entity_id)

@router.get("/fa_tax_payments", response_model=PaginatedResponse[FaTaxPaymentsOut])
async def list_fa_tax_payments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaTaxPaymentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_tax_payments/{entity_id}", response_model=FaTaxPaymentsOut)
async def get_fa_tax_payments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaTaxPaymentsService(db).get(entity_id)

@router.post("/fa_tax_payments", response_model=FaTaxPaymentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_tax_payments(
    data: FaTaxPaymentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTaxPaymentsService(db).create(data)

@router.put("/fa_tax_payments/{entity_id}", response_model=FaTaxPaymentsOut)
async def update_fa_tax_payments(
    entity_id: uuid.UUID,
    data: FaTaxPaymentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTaxPaymentsService(db).update(entity_id, data)

@router.delete("/fa_tax_payments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_tax_payments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaTaxPaymentsService(db).delete(entity_id)

@router.get("/fa_tax_records", response_model=PaginatedResponse[FaTaxRecordsOut])
async def list_fa_tax_records(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaTaxRecordsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_type_code", "tax_status_code", "exemption_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_tax_records/{entity_id}", response_model=FaTaxRecordsOut)
async def get_fa_tax_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaTaxRecordsService(db).get(entity_id)

@router.post("/fa_tax_records", response_model=FaTaxRecordsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_tax_records(
    data: FaTaxRecordsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTaxRecordsService(db).create(data)

@router.put("/fa_tax_records/{entity_id}", response_model=FaTaxRecordsOut)
async def update_fa_tax_records(
    entity_id: uuid.UUID,
    data: FaTaxRecordsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTaxRecordsService(db).update(entity_id, data)

@router.delete("/fa_tax_records/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_tax_records(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaTaxRecordsService(db).delete(entity_id)

@router.get("/fa_transactions", response_model=PaginatedResponse[FaTransactionsOut])
async def list_fa_transactions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaTransactionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["transaction_type_code", "transaction_number", "asset_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_transactions/{entity_id}", response_model=FaTransactionsOut)
async def get_fa_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaTransactionsService(db).get(entity_id)

@router.post("/fa_transactions", response_model=FaTransactionsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_transactions(
    data: FaTransactionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTransactionsService(db).create(data)

@router.put("/fa_transactions/{entity_id}", response_model=FaTransactionsOut)
async def update_fa_transactions(
    entity_id: uuid.UUID,
    data: FaTransactionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTransactionsService(db).update(entity_id, data)

@router.delete("/fa_transactions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaTransactionsService(db).delete(entity_id)

@router.get("/fa_transfers", response_model=PaginatedResponse[FaTransfersOut])
async def list_fa_transfers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaTransfersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["transfer_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_transfers/{entity_id}", response_model=FaTransfersOut)
async def get_fa_transfers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaTransfersService(db).get(entity_id)

@router.post("/fa_transfers", response_model=FaTransfersOut, status_code=status.HTTP_201_CREATED)
async def create_fa_transfers(
    data: FaTransfersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTransfersService(db).create(data)

@router.put("/fa_transfers/{entity_id}", response_model=FaTransfersOut)
async def update_fa_transfers(
    entity_id: uuid.UUID,
    data: FaTransfersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaTransfersService(db).update(entity_id, data)

@router.delete("/fa_transfers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_transfers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaTransfersService(db).delete(entity_id)

@router.get("/fa_vector_documents", response_model=PaginatedResponse[FaVectorDocumentsOut])
async def list_fa_vector_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaVectorDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["document_name", "document_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_vector_documents/{entity_id}", response_model=FaVectorDocumentsOut)
async def get_fa_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaVectorDocumentsService(db).get(entity_id)

@router.post("/fa_vector_documents", response_model=FaVectorDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_vector_documents(
    data: FaVectorDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaVectorDocumentsService(db).create(data)

@router.put("/fa_vector_documents/{entity_id}", response_model=FaVectorDocumentsOut)
async def update_fa_vector_documents(
    entity_id: uuid.UUID,
    data: FaVectorDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaVectorDocumentsService(db).update(entity_id, data)

@router.delete("/fa_vector_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaVectorDocumentsService(db).delete(entity_id)

@router.get("/fa_warranties", response_model=PaginatedResponse[FaWarrantiesOut])
async def list_fa_warranties(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaWarrantiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["warranty_number", "warranty_type_code", "coverage_type_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_warranties/{entity_id}", response_model=FaWarrantiesOut)
async def get_fa_warranties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaWarrantiesService(db).get(entity_id)

@router.post("/fa_warranties", response_model=FaWarrantiesOut, status_code=status.HTTP_201_CREATED)
async def create_fa_warranties(
    data: FaWarrantiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaWarrantiesService(db).create(data)

@router.put("/fa_warranties/{entity_id}", response_model=FaWarrantiesOut)
async def update_fa_warranties(
    entity_id: uuid.UUID,
    data: FaWarrantiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaWarrantiesService(db).update(entity_id, data)

@router.delete("/fa_warranties/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_warranties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaWarrantiesService(db).delete(entity_id)

@router.get("/fa_warranty_claims", response_model=PaginatedResponse[FaWarrantyClaimsOut])
async def list_fa_warranty_claims(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    svc = FaWarrantyClaimsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["claim_number", "claim_type_code", "claim_status_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fa_warranty_claims/{entity_id}", response_model=FaWarrantyClaimsOut)
async def get_fa_warranty_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "view"),
):
    return await FaWarrantyClaimsService(db).get(entity_id)

@router.post("/fa_warranty_claims", response_model=FaWarrantyClaimsOut, status_code=status.HTTP_201_CREATED)
async def create_fa_warranty_claims(
    data: FaWarrantyClaimsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaWarrantyClaimsService(db).create(data)

@router.put("/fa_warranty_claims/{entity_id}", response_model=FaWarrantyClaimsOut)
async def update_fa_warranty_claims(
    entity_id: uuid.UUID,
    data: FaWarrantyClaimsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    return await FaWarrantyClaimsService(db).update(entity_id, data)

@router.delete("/fa_warranty_claims/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fa_warranty_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("fa", "manage"),
):
    await FaWarrantyClaimsService(db).delete(entity_id)
