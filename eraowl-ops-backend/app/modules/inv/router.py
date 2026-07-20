import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.inv.services import (
    AbcAssignmentsService,
    AbcClassesService,
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    CostTypesService,
    CycleCountSchedulesService,
    ImportErrorLogService,
    ImportInterfaceService,
    InspectionPlansService,
    InspectionResultsService,
    InvCycleCountsService,
    InvOnhandBalancesService,
    InvReservationsService,
    InvTransactionTypesService,
    ItemAttributesService,
    ItemCostsService,
    LotGenealogyService,
    LotMasterService,
    LotOnhandService,
    LpnContentsService,
    LpnMasterService,
    MaterialTransactionsService,
    MoveOrderHeadersService,
    MoveOrderLinesService,
    PhysicalInventoryHeadersService,
    PhysicalInventoryLinesService,
    ReplenishmentRulesService,
    SerialService,
    SerialGenealogyService,
    TransferOrderLinesService,
    TransferOrdersService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.inv.schemas import (
    AbcAssignmentsCreate,
    AbcAssignmentsUpdate,
    AbcAssignmentsOut,
    AbcClassesCreate,
    AbcClassesUpdate,
    AbcClassesOut,
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    CostTypesCreate,
    CostTypesUpdate,
    CostTypesOut,
    CycleCountSchedulesCreate,
    CycleCountSchedulesUpdate,
    CycleCountSchedulesOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    ImportInterfaceCreate,
    ImportInterfaceUpdate,
    ImportInterfaceOut,
    InspectionPlansCreate,
    InspectionPlansUpdate,
    InspectionPlansOut,
    InspectionResultsCreate,
    InspectionResultsUpdate,
    InspectionResultsOut,
    InvCycleCountsCreate,
    InvCycleCountsUpdate,
    InvCycleCountsOut,
    InvOnhandBalancesCreate,
    InvOnhandBalancesUpdate,
    InvOnhandBalancesOut,
    InvReservationsCreate,
    InvReservationsUpdate,
    InvReservationsOut,
    InvTransactionTypesCreate,
    InvTransactionTypesUpdate,
    InvTransactionTypesOut,
    ItemAttributesCreate,
    ItemAttributesUpdate,
    ItemAttributesOut,
    ItemCostsCreate,
    ItemCostsUpdate,
    ItemCostsOut,
    LotGenealogyCreate,
    LotGenealogyUpdate,
    LotGenealogyOut,
    LotMasterCreate,
    LotMasterUpdate,
    LotMasterOut,
    LotOnhandCreate,
    LotOnhandUpdate,
    LotOnhandOut,
    LpnContentsCreate,
    LpnContentsUpdate,
    LpnContentsOut,
    LpnMasterCreate,
    LpnMasterUpdate,
    LpnMasterOut,
    MaterialTransactionsCreate,
    MaterialTransactionsUpdate,
    MaterialTransactionsOut,
    MoveOrderHeadersCreate,
    MoveOrderHeadersUpdate,
    MoveOrderHeadersOut,
    MoveOrderLinesCreate,
    MoveOrderLinesUpdate,
    MoveOrderLinesOut,
    PhysicalInventoryHeadersCreate,
    PhysicalInventoryHeadersUpdate,
    PhysicalInventoryHeadersOut,
    PhysicalInventoryLinesCreate,
    PhysicalInventoryLinesUpdate,
    PhysicalInventoryLinesOut,
    ReplenishmentRulesCreate,
    ReplenishmentRulesUpdate,
    ReplenishmentRulesOut,
    SerialCreate,
    SerialUpdate,
    SerialOut,
    SerialGenealogyCreate,
    SerialGenealogyUpdate,
    SerialGenealogyOut,
    TransferOrderLinesCreate,
    TransferOrderLinesUpdate,
    TransferOrderLinesOut,
    TransferOrdersCreate,
    TransferOrdersUpdate,
    TransferOrdersOut,
    WorkflowDefinitionsCreate,
    WorkflowDefinitionsUpdate,
    WorkflowDefinitionsOut,
    WorkflowTasksCreate,
    WorkflowTasksUpdate,
    WorkflowTasksOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/abc_assignments", response_model=PaginatedResponse[AbcAssignmentsOut])
async def list_abc_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = AbcAssignmentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/abc_assignments/{entity_id}", response_model=AbcAssignmentsOut)
async def get_abc_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await AbcAssignmentsService(db).get(entity_id)

@router.post("/abc_assignments", response_model=AbcAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_abc_assignments(
    data: AbcAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AbcAssignmentsService(db).create(data)

@router.put("/abc_assignments/{entity_id}", response_model=AbcAssignmentsOut)
async def update_abc_assignments(
    entity_id: uuid.UUID,
    data: AbcAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AbcAssignmentsService(db).update(entity_id, data)

@router.delete("/abc_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_abc_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await AbcAssignmentsService(db).delete(entity_id)

@router.get("/abc_classes", response_model=PaginatedResponse[AbcClassesOut])
async def list_abc_classes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = AbcClassesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["class_code", "class_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/abc_classes/{entity_id}", response_model=AbcClassesOut)
async def get_abc_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await AbcClassesService(db).get(entity_id)

@router.post("/abc_classes", response_model=AbcClassesOut, status_code=status.HTTP_201_CREATED)
async def create_abc_classes(
    data: AbcClassesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AbcClassesService(db).create(data)

@router.put("/abc_classes/{entity_id}", response_model=AbcClassesOut)
async def update_abc_classes(
    entity_id: uuid.UUID,
    data: AbcClassesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AbcClassesService(db).update(entity_id, data)

@router.delete("/abc_classes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_abc_classes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await AbcClassesService(db).delete(entity_id)

@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/cost_types", response_model=PaginatedResponse[CostTypesOut])
async def list_cost_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = CostTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["cost_type_code", "cost_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/cost_types/{entity_id}", response_model=CostTypesOut)
async def get_cost_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await CostTypesService(db).get(entity_id)

@router.post("/cost_types", response_model=CostTypesOut, status_code=status.HTTP_201_CREATED)
async def create_cost_types(
    data: CostTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await CostTypesService(db).create(data)

@router.put("/cost_types/{entity_id}", response_model=CostTypesOut)
async def update_cost_types(
    entity_id: uuid.UUID,
    data: CostTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await CostTypesService(db).update(entity_id, data)

@router.delete("/cost_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cost_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await CostTypesService(db).delete(entity_id)

@router.get("/cycle_count_schedules", response_model=PaginatedResponse[CycleCountSchedulesOut])
async def list_cycle_count_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = CycleCountSchedulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["schedule_code", "schedule_name", "class_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/cycle_count_schedules/{entity_id}", response_model=CycleCountSchedulesOut)
async def get_cycle_count_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await CycleCountSchedulesService(db).get(entity_id)

@router.post("/cycle_count_schedules", response_model=CycleCountSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_cycle_count_schedules(
    data: CycleCountSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await CycleCountSchedulesService(db).create(data)

@router.put("/cycle_count_schedules/{entity_id}", response_model=CycleCountSchedulesOut)
async def update_cycle_count_schedules(
    entity_id: uuid.UUID,
    data: CycleCountSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await CycleCountSchedulesService(db).update(entity_id, data)

@router.delete("/cycle_count_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cycle_count_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await CycleCountSchedulesService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/import_interface", response_model=PaginatedResponse[ImportInterfaceOut])
async def list_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = ImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def get_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await ImportInterfaceService(db).get(entity_id)

@router.post("/import_interface", response_model=ImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_import_interface(
    data: ImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ImportInterfaceService(db).create(data)

@router.put("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def update_import_interface(
    entity_id: uuid.UUID,
    data: ImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ImportInterfaceService(db).update(entity_id, data)

@router.delete("/import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await ImportInterfaceService(db).delete(entity_id)

@router.get("/inspection_plans", response_model=PaginatedResponse[InspectionPlansOut])
async def list_inspection_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InspectionPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_code", "plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_plans/{entity_id}", response_model=InspectionPlansOut)
async def get_inspection_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InspectionPlansService(db).get(entity_id)

@router.post("/inspection_plans", response_model=InspectionPlansOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_plans(
    data: InspectionPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InspectionPlansService(db).create(data)

@router.put("/inspection_plans/{entity_id}", response_model=InspectionPlansOut)
async def update_inspection_plans(
    entity_id: uuid.UUID,
    data: InspectionPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InspectionPlansService(db).update(entity_id, data)

@router.delete("/inspection_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InspectionPlansService(db).delete(entity_id)

@router.get("/inspection_results", response_model=PaginatedResponse[InspectionResultsOut])
async def list_inspection_results(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InspectionResultsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/inspection_results/{entity_id}", response_model=InspectionResultsOut)
async def get_inspection_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InspectionResultsService(db).get(entity_id)

@router.post("/inspection_results", response_model=InspectionResultsOut, status_code=status.HTTP_201_CREATED)
async def create_inspection_results(
    data: InspectionResultsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InspectionResultsService(db).create(data)

@router.put("/inspection_results/{entity_id}", response_model=InspectionResultsOut)
async def update_inspection_results(
    entity_id: uuid.UUID,
    data: InspectionResultsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InspectionResultsService(db).update(entity_id, data)

@router.delete("/inspection_results/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inspection_results(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InspectionResultsService(db).delete(entity_id)

@router.get("/inv_cycle_counts", response_model=PaginatedResponse[InvCycleCountsOut])
async def list_inv_cycle_counts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InvCycleCountsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/inv_cycle_counts/{entity_id}", response_model=InvCycleCountsOut)
async def get_inv_cycle_counts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InvCycleCountsService(db).get(entity_id)

@router.post("/inv_cycle_counts", response_model=InvCycleCountsOut, status_code=status.HTTP_201_CREATED)
async def create_inv_cycle_counts(
    data: InvCycleCountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvCycleCountsService(db).create(data)

@router.put("/inv_cycle_counts/{entity_id}", response_model=InvCycleCountsOut)
async def update_inv_cycle_counts(
    entity_id: uuid.UUID,
    data: InvCycleCountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvCycleCountsService(db).update(entity_id, data)

@router.delete("/inv_cycle_counts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inv_cycle_counts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InvCycleCountsService(db).delete(entity_id)

@router.get("/inv_onhand_balances", response_model=PaginatedResponse[InvOnhandBalancesOut])
async def list_inv_onhand_balances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InvOnhandBalancesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lot_number", "serial_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inv_onhand_balances/{entity_id}", response_model=InvOnhandBalancesOut)
async def get_inv_onhand_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InvOnhandBalancesService(db).get(entity_id)

@router.post("/inv_onhand_balances", response_model=InvOnhandBalancesOut, status_code=status.HTTP_201_CREATED)
async def create_inv_onhand_balances(
    data: InvOnhandBalancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvOnhandBalancesService(db).create(data)

@router.put("/inv_onhand_balances/{entity_id}", response_model=InvOnhandBalancesOut)
async def update_inv_onhand_balances(
    entity_id: uuid.UUID,
    data: InvOnhandBalancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvOnhandBalancesService(db).update(entity_id, data)

@router.delete("/inv_onhand_balances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inv_onhand_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InvOnhandBalancesService(db).delete(entity_id)

@router.get("/inv_reservations", response_model=PaginatedResponse[InvReservationsOut])
async def list_inv_reservations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InvReservationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["lot_number", "serial_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inv_reservations/{entity_id}", response_model=InvReservationsOut)
async def get_inv_reservations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InvReservationsService(db).get(entity_id)

@router.post("/inv_reservations", response_model=InvReservationsOut, status_code=status.HTTP_201_CREATED)
async def create_inv_reservations(
    data: InvReservationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvReservationsService(db).create(data)

@router.put("/inv_reservations/{entity_id}", response_model=InvReservationsOut)
async def update_inv_reservations(
    entity_id: uuid.UUID,
    data: InvReservationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvReservationsService(db).update(entity_id, data)

@router.delete("/inv_reservations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inv_reservations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InvReservationsService(db).delete(entity_id)

@router.get("/inv_transaction_types", response_model=PaginatedResponse[InvTransactionTypesOut])
async def list_inv_transaction_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = InvTransactionTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["transaction_type_code", "transaction_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/inv_transaction_types/{entity_id}", response_model=InvTransactionTypesOut)
async def get_inv_transaction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await InvTransactionTypesService(db).get(entity_id)

@router.post("/inv_transaction_types", response_model=InvTransactionTypesOut, status_code=status.HTTP_201_CREATED)
async def create_inv_transaction_types(
    data: InvTransactionTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvTransactionTypesService(db).create(data)

@router.put("/inv_transaction_types/{entity_id}", response_model=InvTransactionTypesOut)
async def update_inv_transaction_types(
    entity_id: uuid.UUID,
    data: InvTransactionTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await InvTransactionTypesService(db).update(entity_id, data)

@router.delete("/inv_transaction_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inv_transaction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await InvTransactionTypesService(db).delete(entity_id)

@router.get("/item_attributes", response_model=PaginatedResponse[ItemAttributesOut])
async def list_item_attributes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = ItemAttributesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/item_attributes/{entity_id}", response_model=ItemAttributesOut)
async def get_item_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await ItemAttributesService(db).get(entity_id)

@router.post("/item_attributes", response_model=ItemAttributesOut, status_code=status.HTTP_201_CREATED)
async def create_item_attributes(
    data: ItemAttributesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ItemAttributesService(db).create(data)

@router.put("/item_attributes/{entity_id}", response_model=ItemAttributesOut)
async def update_item_attributes(
    entity_id: uuid.UUID,
    data: ItemAttributesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ItemAttributesService(db).update(entity_id, data)

@router.delete("/item_attributes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await ItemAttributesService(db).delete(entity_id)

@router.get("/item_costs", response_model=PaginatedResponse[ItemCostsOut])
async def list_item_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = ItemCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/item_costs/{entity_id}", response_model=ItemCostsOut)
async def get_item_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await ItemCostsService(db).get(entity_id)

@router.post("/item_costs", response_model=ItemCostsOut, status_code=status.HTTP_201_CREATED)
async def create_item_costs(
    data: ItemCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ItemCostsService(db).create(data)

@router.put("/item_costs/{entity_id}", response_model=ItemCostsOut)
async def update_item_costs(
    entity_id: uuid.UUID,
    data: ItemCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ItemCostsService(db).update(entity_id, data)

@router.delete("/item_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await ItemCostsService(db).delete(entity_id)

@router.get("/lot_genealogy", response_model=PaginatedResponse[LotGenealogyOut])
async def list_lot_genealogy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = LotGenealogyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/lot_genealogy/{entity_id}", response_model=LotGenealogyOut)
async def get_lot_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await LotGenealogyService(db).get(entity_id)

@router.post("/lot_genealogy", response_model=LotGenealogyOut, status_code=status.HTTP_201_CREATED)
async def create_lot_genealogy(
    data: LotGenealogyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotGenealogyService(db).create(data)

@router.put("/lot_genealogy/{entity_id}", response_model=LotGenealogyOut)
async def update_lot_genealogy(
    entity_id: uuid.UUID,
    data: LotGenealogyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotGenealogyService(db).update(entity_id, data)

@router.delete("/lot_genealogy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lot_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await LotGenealogyService(db).delete(entity_id)

@router.get("/lot_master", response_model=PaginatedResponse[LotMasterOut])
async def list_lot_master(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = LotMasterService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lot_number", "supplier_lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/lot_master/{entity_id}", response_model=LotMasterOut)
async def get_lot_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await LotMasterService(db).get(entity_id)

@router.post("/lot_master", response_model=LotMasterOut, status_code=status.HTTP_201_CREATED)
async def create_lot_master(
    data: LotMasterCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotMasterService(db).create(data)

@router.put("/lot_master/{entity_id}", response_model=LotMasterOut)
async def update_lot_master(
    entity_id: uuid.UUID,
    data: LotMasterUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotMasterService(db).update(entity_id, data)

@router.delete("/lot_master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lot_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await LotMasterService(db).delete(entity_id)

@router.get("/lot_onhand", response_model=PaginatedResponse[LotOnhandOut])
async def list_lot_onhand(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = LotOnhandService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/lot_onhand/{entity_id}", response_model=LotOnhandOut)
async def get_lot_onhand(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await LotOnhandService(db).get(entity_id)

@router.post("/lot_onhand", response_model=LotOnhandOut, status_code=status.HTTP_201_CREATED)
async def create_lot_onhand(
    data: LotOnhandCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotOnhandService(db).create(data)

@router.put("/lot_onhand/{entity_id}", response_model=LotOnhandOut)
async def update_lot_onhand(
    entity_id: uuid.UUID,
    data: LotOnhandUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LotOnhandService(db).update(entity_id, data)

@router.delete("/lot_onhand/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lot_onhand(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await LotOnhandService(db).delete(entity_id)

@router.get("/lpn_contents", response_model=PaginatedResponse[LpnContentsOut])
async def list_lpn_contents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = LpnContentsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/lpn_contents/{entity_id}", response_model=LpnContentsOut)
async def get_lpn_contents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await LpnContentsService(db).get(entity_id)

@router.post("/lpn_contents", response_model=LpnContentsOut, status_code=status.HTTP_201_CREATED)
async def create_lpn_contents(
    data: LpnContentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LpnContentsService(db).create(data)

@router.put("/lpn_contents/{entity_id}", response_model=LpnContentsOut)
async def update_lpn_contents(
    entity_id: uuid.UUID,
    data: LpnContentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LpnContentsService(db).update(entity_id, data)

@router.delete("/lpn_contents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lpn_contents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await LpnContentsService(db).delete(entity_id)

@router.get("/lpn_master", response_model=PaginatedResponse[LpnMasterOut])
async def list_lpn_master(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = LpnMasterService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["lpn_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/lpn_master/{entity_id}", response_model=LpnMasterOut)
async def get_lpn_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await LpnMasterService(db).get(entity_id)

@router.post("/lpn_master", response_model=LpnMasterOut, status_code=status.HTTP_201_CREATED)
async def create_lpn_master(
    data: LpnMasterCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LpnMasterService(db).create(data)

@router.put("/lpn_master/{entity_id}", response_model=LpnMasterOut)
async def update_lpn_master(
    entity_id: uuid.UUID,
    data: LpnMasterUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await LpnMasterService(db).update(entity_id, data)

@router.delete("/lpn_master/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lpn_master(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await LpnMasterService(db).delete(entity_id)

@router.get("/material_transactions", response_model=PaginatedResponse[MaterialTransactionsOut])
async def list_material_transactions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = MaterialTransactionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["lot_number", "serial_number", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/material_transactions/{entity_id}", response_model=MaterialTransactionsOut)
async def get_material_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await MaterialTransactionsService(db).get(entity_id)

@router.post("/material_transactions", response_model=MaterialTransactionsOut, status_code=status.HTTP_201_CREATED)
async def create_material_transactions(
    data: MaterialTransactionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MaterialTransactionsService(db).create(data)

@router.put("/material_transactions/{entity_id}", response_model=MaterialTransactionsOut)
async def update_material_transactions(
    entity_id: uuid.UUID,
    data: MaterialTransactionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MaterialTransactionsService(db).update(entity_id, data)

@router.delete("/material_transactions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_material_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await MaterialTransactionsService(db).delete(entity_id)

@router.get("/move_order_headers", response_model=PaginatedResponse[MoveOrderHeadersOut])
async def list_move_order_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = MoveOrderHeadersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["move_order_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/move_order_headers/{entity_id}", response_model=MoveOrderHeadersOut)
async def get_move_order_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await MoveOrderHeadersService(db).get(entity_id)

@router.post("/move_order_headers", response_model=MoveOrderHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_move_order_headers(
    data: MoveOrderHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MoveOrderHeadersService(db).create(data)

@router.put("/move_order_headers/{entity_id}", response_model=MoveOrderHeadersOut)
async def update_move_order_headers(
    entity_id: uuid.UUID,
    data: MoveOrderHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MoveOrderHeadersService(db).update(entity_id, data)

@router.delete("/move_order_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_move_order_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await MoveOrderHeadersService(db).delete(entity_id)

@router.get("/move_order_lines", response_model=PaginatedResponse[MoveOrderLinesOut])
async def list_move_order_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = MoveOrderLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/move_order_lines/{entity_id}", response_model=MoveOrderLinesOut)
async def get_move_order_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await MoveOrderLinesService(db).get(entity_id)

@router.post("/move_order_lines", response_model=MoveOrderLinesOut, status_code=status.HTTP_201_CREATED)
async def create_move_order_lines(
    data: MoveOrderLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MoveOrderLinesService(db).create(data)

@router.put("/move_order_lines/{entity_id}", response_model=MoveOrderLinesOut)
async def update_move_order_lines(
    entity_id: uuid.UUID,
    data: MoveOrderLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await MoveOrderLinesService(db).update(entity_id, data)

@router.delete("/move_order_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_move_order_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await MoveOrderLinesService(db).delete(entity_id)

@router.get("/physical_inventory_headers", response_model=PaginatedResponse[PhysicalInventoryHeadersOut])
async def list_physical_inventory_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = PhysicalInventoryHeadersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["inventory_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/physical_inventory_headers/{entity_id}", response_model=PhysicalInventoryHeadersOut)
async def get_physical_inventory_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await PhysicalInventoryHeadersService(db).get(entity_id)

@router.post("/physical_inventory_headers", response_model=PhysicalInventoryHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_physical_inventory_headers(
    data: PhysicalInventoryHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await PhysicalInventoryHeadersService(db).create(data)

@router.put("/physical_inventory_headers/{entity_id}", response_model=PhysicalInventoryHeadersOut)
async def update_physical_inventory_headers(
    entity_id: uuid.UUID,
    data: PhysicalInventoryHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await PhysicalInventoryHeadersService(db).update(entity_id, data)

@router.delete("/physical_inventory_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_physical_inventory_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await PhysicalInventoryHeadersService(db).delete(entity_id)

@router.get("/physical_inventory_lines", response_model=PaginatedResponse[PhysicalInventoryLinesOut])
async def list_physical_inventory_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = PhysicalInventoryLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/physical_inventory_lines/{entity_id}", response_model=PhysicalInventoryLinesOut)
async def get_physical_inventory_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await PhysicalInventoryLinesService(db).get(entity_id)

@router.post("/physical_inventory_lines", response_model=PhysicalInventoryLinesOut, status_code=status.HTTP_201_CREATED)
async def create_physical_inventory_lines(
    data: PhysicalInventoryLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await PhysicalInventoryLinesService(db).create(data)

@router.put("/physical_inventory_lines/{entity_id}", response_model=PhysicalInventoryLinesOut)
async def update_physical_inventory_lines(
    entity_id: uuid.UUID,
    data: PhysicalInventoryLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await PhysicalInventoryLinesService(db).update(entity_id, data)

@router.delete("/physical_inventory_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_physical_inventory_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await PhysicalInventoryLinesService(db).delete(entity_id)

@router.get("/replenishment_rules", response_model=PaginatedResponse[ReplenishmentRulesOut])
async def list_replenishment_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = ReplenishmentRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/replenishment_rules/{entity_id}", response_model=ReplenishmentRulesOut)
async def get_replenishment_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await ReplenishmentRulesService(db).get(entity_id)

@router.post("/replenishment_rules", response_model=ReplenishmentRulesOut, status_code=status.HTTP_201_CREATED)
async def create_replenishment_rules(
    data: ReplenishmentRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ReplenishmentRulesService(db).create(data)

@router.put("/replenishment_rules/{entity_id}", response_model=ReplenishmentRulesOut)
async def update_replenishment_rules(
    entity_id: uuid.UUID,
    data: ReplenishmentRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await ReplenishmentRulesService(db).update(entity_id, data)

@router.delete("/replenishment_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_replenishment_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await ReplenishmentRulesService(db).delete(entity_id)

@router.get("/serial", response_model=PaginatedResponse[SerialOut])
async def list_serial(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = SerialService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["serial_number", "lot_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/serial/{entity_id}", response_model=SerialOut)
async def get_serial(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await SerialService(db).get(entity_id)

@router.post("/serial", response_model=SerialOut, status_code=status.HTTP_201_CREATED)
async def create_serial(
    data: SerialCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await SerialService(db).create(data)

@router.put("/serial/{entity_id}", response_model=SerialOut)
async def update_serial(
    entity_id: uuid.UUID,
    data: SerialUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await SerialService(db).update(entity_id, data)

@router.delete("/serial/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_serial(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await SerialService(db).delete(entity_id)

@router.get("/serial_genealogy", response_model=PaginatedResponse[SerialGenealogyOut])
async def list_serial_genealogy(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = SerialGenealogyService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/serial_genealogy/{entity_id}", response_model=SerialGenealogyOut)
async def get_serial_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await SerialGenealogyService(db).get(entity_id)

@router.post("/serial_genealogy", response_model=SerialGenealogyOut, status_code=status.HTTP_201_CREATED)
async def create_serial_genealogy(
    data: SerialGenealogyCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await SerialGenealogyService(db).create(data)

@router.put("/serial_genealogy/{entity_id}", response_model=SerialGenealogyOut)
async def update_serial_genealogy(
    entity_id: uuid.UUID,
    data: SerialGenealogyUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await SerialGenealogyService(db).update(entity_id, data)

@router.delete("/serial_genealogy/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_serial_genealogy(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await SerialGenealogyService(db).delete(entity_id)

@router.get("/transfer_order_lines", response_model=PaginatedResponse[TransferOrderLinesOut])
async def list_transfer_order_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = TransferOrderLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/transfer_order_lines/{entity_id}", response_model=TransferOrderLinesOut)
async def get_transfer_order_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await TransferOrderLinesService(db).get(entity_id)

@router.post("/transfer_order_lines", response_model=TransferOrderLinesOut, status_code=status.HTTP_201_CREATED)
async def create_transfer_order_lines(
    data: TransferOrderLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await TransferOrderLinesService(db).create(data)

@router.put("/transfer_order_lines/{entity_id}", response_model=TransferOrderLinesOut)
async def update_transfer_order_lines(
    entity_id: uuid.UUID,
    data: TransferOrderLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await TransferOrderLinesService(db).update(entity_id, data)

@router.delete("/transfer_order_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transfer_order_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await TransferOrderLinesService(db).delete(entity_id)

@router.get("/transfer_orders", response_model=PaginatedResponse[TransferOrdersOut])
async def list_transfer_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = TransferOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["transfer_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/transfer_orders/{entity_id}", response_model=TransferOrdersOut)
async def get_transfer_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await TransferOrdersService(db).get(entity_id)

@router.post("/transfer_orders", response_model=TransferOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_transfer_orders(
    data: TransferOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await TransferOrdersService(db).create(data)

@router.put("/transfer_orders/{entity_id}", response_model=TransferOrdersOut)
async def update_transfer_orders(
    entity_id: uuid.UUID,
    data: TransferOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await TransferOrdersService(db).update(entity_id, data)

@router.delete("/transfer_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transfer_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await TransferOrdersService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("inv", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
