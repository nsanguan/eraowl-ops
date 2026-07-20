import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.prd.services import (
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    BomComponentsExtService,
    EngineeringChangeOrdersService,
    ImportErrorLogService,
    ImportInterfaceService,
    MpsEntriesService,
    MrpRecommendationsService,
    ProdWorkOrdersService,
    ProductionCalendarService,
    ResourcesService,
    RoutingHeadersService,
    RoutingOperationsService,
    WipMovementsService,
    WorkCentersService,
    WorkOrderOperationsService,
    WorkOrderRequirementsService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.prd.schemas import (
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    BomComponentsExtCreate,
    BomComponentsExtUpdate,
    BomComponentsExtOut,
    EngineeringChangeOrdersCreate,
    EngineeringChangeOrdersUpdate,
    EngineeringChangeOrdersOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    ImportInterfaceCreate,
    ImportInterfaceUpdate,
    ImportInterfaceOut,
    MpsEntriesCreate,
    MpsEntriesUpdate,
    MpsEntriesOut,
    MrpRecommendationsCreate,
    MrpRecommendationsUpdate,
    MrpRecommendationsOut,
    ProdWorkOrdersCreate,
    ProdWorkOrdersUpdate,
    ProdWorkOrdersOut,
    ProductionCalendarCreate,
    ProductionCalendarUpdate,
    ProductionCalendarOut,
    ResourcesCreate,
    ResourcesUpdate,
    ResourcesOut,
    RoutingHeadersCreate,
    RoutingHeadersUpdate,
    RoutingHeadersOut,
    RoutingOperationsCreate,
    RoutingOperationsUpdate,
    RoutingOperationsOut,
    WipMovementsCreate,
    WipMovementsUpdate,
    WipMovementsOut,
    WorkCentersCreate,
    WorkCentersUpdate,
    WorkCentersOut,
    WorkOrderOperationsCreate,
    WorkOrderOperationsUpdate,
    WorkOrderOperationsOut,
    WorkOrderRequirementsCreate,
    WorkOrderRequirementsUpdate,
    WorkOrderRequirementsOut,
    WorkflowDefinitionsCreate,
    WorkflowDefinitionsUpdate,
    WorkflowDefinitionsOut,
    WorkflowTasksCreate,
    WorkflowTasksUpdate,
    WorkflowTasksOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/bom_components_ext", response_model=PaginatedResponse[BomComponentsExtOut])
async def list_bom_components_ext(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = BomComponentsExtService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/bom_components_ext/{entity_id}", response_model=BomComponentsExtOut)
async def get_bom_components_ext(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await BomComponentsExtService(db).get(entity_id)

@router.post("/bom_components_ext", response_model=BomComponentsExtOut, status_code=status.HTTP_201_CREATED)
async def create_bom_components_ext(
    data: BomComponentsExtCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await BomComponentsExtService(db).create(data)

@router.put("/bom_components_ext/{entity_id}", response_model=BomComponentsExtOut)
async def update_bom_components_ext(
    entity_id: uuid.UUID,
    data: BomComponentsExtUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await BomComponentsExtService(db).update(entity_id, data)

@router.delete("/bom_components_ext/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bom_components_ext(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await BomComponentsExtService(db).delete(entity_id)

@router.get("/engineering_change_orders", response_model=PaginatedResponse[EngineeringChangeOrdersOut])
async def list_engineering_change_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = EngineeringChangeOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["eco_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/engineering_change_orders/{entity_id}", response_model=EngineeringChangeOrdersOut)
async def get_engineering_change_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await EngineeringChangeOrdersService(db).get(entity_id)

@router.post("/engineering_change_orders", response_model=EngineeringChangeOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_engineering_change_orders(
    data: EngineeringChangeOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await EngineeringChangeOrdersService(db).create(data)

@router.put("/engineering_change_orders/{entity_id}", response_model=EngineeringChangeOrdersOut)
async def update_engineering_change_orders(
    entity_id: uuid.UUID,
    data: EngineeringChangeOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await EngineeringChangeOrdersService(db).update(entity_id, data)

@router.delete("/engineering_change_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_engineering_change_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await EngineeringChangeOrdersService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/import_interface", response_model=PaginatedResponse[ImportInterfaceOut])
async def list_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = ImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def get_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await ImportInterfaceService(db).get(entity_id)

@router.post("/import_interface", response_model=ImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_import_interface(
    data: ImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ImportInterfaceService(db).create(data)

@router.put("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def update_import_interface(
    entity_id: uuid.UUID,
    data: ImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ImportInterfaceService(db).update(entity_id, data)

@router.delete("/import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await ImportInterfaceService(db).delete(entity_id)

@router.get("/mps_entries", response_model=PaginatedResponse[MpsEntriesOut])
async def list_mps_entries(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = MpsEntriesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mps_entries/{entity_id}", response_model=MpsEntriesOut)
async def get_mps_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await MpsEntriesService(db).get(entity_id)

@router.post("/mps_entries", response_model=MpsEntriesOut, status_code=status.HTTP_201_CREATED)
async def create_mps_entries(
    data: MpsEntriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await MpsEntriesService(db).create(data)

@router.put("/mps_entries/{entity_id}", response_model=MpsEntriesOut)
async def update_mps_entries(
    entity_id: uuid.UUID,
    data: MpsEntriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await MpsEntriesService(db).update(entity_id, data)

@router.delete("/mps_entries/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mps_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await MpsEntriesService(db).delete(entity_id)

@router.get("/mrp_recommendations", response_model=PaginatedResponse[MrpRecommendationsOut])
async def list_mrp_recommendations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = MrpRecommendationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/mrp_recommendations/{entity_id}", response_model=MrpRecommendationsOut)
async def get_mrp_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await MrpRecommendationsService(db).get(entity_id)

@router.post("/mrp_recommendations", response_model=MrpRecommendationsOut, status_code=status.HTTP_201_CREATED)
async def create_mrp_recommendations(
    data: MrpRecommendationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await MrpRecommendationsService(db).create(data)

@router.put("/mrp_recommendations/{entity_id}", response_model=MrpRecommendationsOut)
async def update_mrp_recommendations(
    entity_id: uuid.UUID,
    data: MrpRecommendationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await MrpRecommendationsService(db).update(entity_id, data)

@router.delete("/mrp_recommendations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mrp_recommendations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await MrpRecommendationsService(db).delete(entity_id)

@router.get("/prod_work_orders", response_model=PaginatedResponse[ProdWorkOrdersOut])
async def list_prod_work_orders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = ProdWorkOrdersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["wo_number", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/prod_work_orders/{entity_id}", response_model=ProdWorkOrdersOut)
async def get_prod_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await ProdWorkOrdersService(db).get(entity_id)

@router.post("/prod_work_orders", response_model=ProdWorkOrdersOut, status_code=status.HTTP_201_CREATED)
async def create_prod_work_orders(
    data: ProdWorkOrdersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ProdWorkOrdersService(db).create(data)

@router.put("/prod_work_orders/{entity_id}", response_model=ProdWorkOrdersOut)
async def update_prod_work_orders(
    entity_id: uuid.UUID,
    data: ProdWorkOrdersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ProdWorkOrdersService(db).update(entity_id, data)

@router.delete("/prod_work_orders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prod_work_orders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await ProdWorkOrdersService(db).delete(entity_id)

@router.get("/production_calendar", response_model=PaginatedResponse[ProductionCalendarOut])
async def list_production_calendar(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = ProductionCalendarService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["calendar_code", "calendar_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/production_calendar/{entity_id}", response_model=ProductionCalendarOut)
async def get_production_calendar(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await ProductionCalendarService(db).get(entity_id)

@router.post("/production_calendar", response_model=ProductionCalendarOut, status_code=status.HTTP_201_CREATED)
async def create_production_calendar(
    data: ProductionCalendarCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ProductionCalendarService(db).create(data)

@router.put("/production_calendar/{entity_id}", response_model=ProductionCalendarOut)
async def update_production_calendar(
    entity_id: uuid.UUID,
    data: ProductionCalendarUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ProductionCalendarService(db).update(entity_id, data)

@router.delete("/production_calendar/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_production_calendar(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await ProductionCalendarService(db).delete(entity_id)

@router.get("/resources", response_model=PaginatedResponse[ResourcesOut])
async def list_resources(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = ResourcesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["resource_code", "resource_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/resources/{entity_id}", response_model=ResourcesOut)
async def get_resources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await ResourcesService(db).get(entity_id)

@router.post("/resources", response_model=ResourcesOut, status_code=status.HTTP_201_CREATED)
async def create_resources(
    data: ResourcesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ResourcesService(db).create(data)

@router.put("/resources/{entity_id}", response_model=ResourcesOut)
async def update_resources(
    entity_id: uuid.UUID,
    data: ResourcesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await ResourcesService(db).update(entity_id, data)

@router.delete("/resources/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await ResourcesService(db).delete(entity_id)

@router.get("/routing_headers", response_model=PaginatedResponse[RoutingHeadersOut])
async def list_routing_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = RoutingHeadersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["routing_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/routing_headers/{entity_id}", response_model=RoutingHeadersOut)
async def get_routing_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await RoutingHeadersService(db).get(entity_id)

@router.post("/routing_headers", response_model=RoutingHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_routing_headers(
    data: RoutingHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await RoutingHeadersService(db).create(data)

@router.put("/routing_headers/{entity_id}", response_model=RoutingHeadersOut)
async def update_routing_headers(
    entity_id: uuid.UUID,
    data: RoutingHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await RoutingHeadersService(db).update(entity_id, data)

@router.delete("/routing_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_routing_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await RoutingHeadersService(db).delete(entity_id)

@router.get("/routing_operations", response_model=PaginatedResponse[RoutingOperationsOut])
async def list_routing_operations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = RoutingOperationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["operation_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/routing_operations/{entity_id}", response_model=RoutingOperationsOut)
async def get_routing_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await RoutingOperationsService(db).get(entity_id)

@router.post("/routing_operations", response_model=RoutingOperationsOut, status_code=status.HTTP_201_CREATED)
async def create_routing_operations(
    data: RoutingOperationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await RoutingOperationsService(db).create(data)

@router.put("/routing_operations/{entity_id}", response_model=RoutingOperationsOut)
async def update_routing_operations(
    entity_id: uuid.UUID,
    data: RoutingOperationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await RoutingOperationsService(db).update(entity_id, data)

@router.delete("/routing_operations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_routing_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await RoutingOperationsService(db).delete(entity_id)

@router.get("/wip_movements", response_model=PaginatedResponse[WipMovementsOut])
async def list_wip_movements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WipMovementsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/wip_movements/{entity_id}", response_model=WipMovementsOut)
async def get_wip_movements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WipMovementsService(db).get(entity_id)

@router.post("/wip_movements", response_model=WipMovementsOut, status_code=status.HTTP_201_CREATED)
async def create_wip_movements(
    data: WipMovementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WipMovementsService(db).create(data)

@router.put("/wip_movements/{entity_id}", response_model=WipMovementsOut)
async def update_wip_movements(
    entity_id: uuid.UUID,
    data: WipMovementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WipMovementsService(db).update(entity_id, data)

@router.delete("/wip_movements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wip_movements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WipMovementsService(db).delete(entity_id)

@router.get("/work_centers", response_model=PaginatedResponse[WorkCentersOut])
async def list_work_centers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WorkCentersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["center_code", "center_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/work_centers/{entity_id}", response_model=WorkCentersOut)
async def get_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WorkCentersService(db).get(entity_id)

@router.post("/work_centers", response_model=WorkCentersOut, status_code=status.HTTP_201_CREATED)
async def create_work_centers(
    data: WorkCentersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkCentersService(db).create(data)

@router.put("/work_centers/{entity_id}", response_model=WorkCentersOut)
async def update_work_centers(
    entity_id: uuid.UUID,
    data: WorkCentersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkCentersService(db).update(entity_id, data)

@router.delete("/work_centers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_centers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WorkCentersService(db).delete(entity_id)

@router.get("/work_order_operations", response_model=PaginatedResponse[WorkOrderOperationsOut])
async def list_work_order_operations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WorkOrderOperationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["operation_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/work_order_operations/{entity_id}", response_model=WorkOrderOperationsOut)
async def get_work_order_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WorkOrderOperationsService(db).get(entity_id)

@router.post("/work_order_operations", response_model=WorkOrderOperationsOut, status_code=status.HTTP_201_CREATED)
async def create_work_order_operations(
    data: WorkOrderOperationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkOrderOperationsService(db).create(data)

@router.put("/work_order_operations/{entity_id}", response_model=WorkOrderOperationsOut)
async def update_work_order_operations(
    entity_id: uuid.UUID,
    data: WorkOrderOperationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkOrderOperationsService(db).update(entity_id, data)

@router.delete("/work_order_operations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_order_operations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WorkOrderOperationsService(db).delete(entity_id)

@router.get("/work_order_requirements", response_model=PaginatedResponse[WorkOrderRequirementsOut])
async def list_work_order_requirements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WorkOrderRequirementsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/work_order_requirements/{entity_id}", response_model=WorkOrderRequirementsOut)
async def get_work_order_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WorkOrderRequirementsService(db).get(entity_id)

@router.post("/work_order_requirements", response_model=WorkOrderRequirementsOut, status_code=status.HTTP_201_CREATED)
async def create_work_order_requirements(
    data: WorkOrderRequirementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkOrderRequirementsService(db).create(data)

@router.put("/work_order_requirements/{entity_id}", response_model=WorkOrderRequirementsOut)
async def update_work_order_requirements(
    entity_id: uuid.UUID,
    data: WorkOrderRequirementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkOrderRequirementsService(db).update(entity_id, data)

@router.delete("/work_order_requirements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_order_requirements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WorkOrderRequirementsService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("prd", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
