import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.om.services import (
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    CustomerAttributesService,
    ImportErrorLogService,
    LineTypesService,
    OmHeadersService,
    OmLinesService,
    OmShipmentsService,
    OrderImportInterfaceService,
    OrderTypesService,
    ShipmentTrackingService,
    WmsCallbacksService,
    WmsTaskQueueService,
    WorkflowAssignmentsService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.om.schemas import (
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    CustomerAttributesCreate,
    CustomerAttributesUpdate,
    CustomerAttributesOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    LineTypesCreate,
    LineTypesUpdate,
    LineTypesOut,
    OmHeadersCreate,
    OmHeadersUpdate,
    OmHeadersOut,
    OmLinesCreate,
    OmLinesUpdate,
    OmLinesOut,
    OmShipmentsCreate,
    OmShipmentsUpdate,
    OmShipmentsOut,
    OrderImportInterfaceCreate,
    OrderImportInterfaceUpdate,
    OrderImportInterfaceOut,
    OrderTypesCreate,
    OrderTypesUpdate,
    OrderTypesOut,
    ShipmentTrackingCreate,
    ShipmentTrackingUpdate,
    ShipmentTrackingOut,
    WmsCallbacksCreate,
    WmsCallbacksUpdate,
    WmsCallbacksOut,
    WmsTaskQueueCreate,
    WmsTaskQueueUpdate,
    WmsTaskQueueOut,
    WorkflowAssignmentsCreate,
    WorkflowAssignmentsUpdate,
    WorkflowAssignmentsOut,
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
    _priv=check_privilege("om", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/customer_attributes", response_model=PaginatedResponse[CustomerAttributesOut])
async def list_customer_attributes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = CustomerAttributesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/customer_attributes/{entity_id}", response_model=CustomerAttributesOut)
async def get_customer_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await CustomerAttributesService(db).get(entity_id)

@router.post("/customer_attributes", response_model=CustomerAttributesOut, status_code=status.HTTP_201_CREATED)
async def create_customer_attributes(
    data: CustomerAttributesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await CustomerAttributesService(db).create(data)

@router.put("/customer_attributes/{entity_id}", response_model=CustomerAttributesOut)
async def update_customer_attributes(
    entity_id: uuid.UUID,
    data: CustomerAttributesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await CustomerAttributesService(db).update(entity_id, data)

@router.delete("/customer_attributes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_attributes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await CustomerAttributesService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/line_types", response_model=PaginatedResponse[LineTypesOut])
async def list_line_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = LineTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["line_type_code", "line_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/line_types/{entity_id}", response_model=LineTypesOut)
async def get_line_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await LineTypesService(db).get(entity_id)

@router.post("/line_types", response_model=LineTypesOut, status_code=status.HTTP_201_CREATED)
async def create_line_types(
    data: LineTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await LineTypesService(db).create(data)

@router.put("/line_types/{entity_id}", response_model=LineTypesOut)
async def update_line_types(
    entity_id: uuid.UUID,
    data: LineTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await LineTypesService(db).update(entity_id, data)

@router.delete("/line_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_line_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await LineTypesService(db).delete(entity_id)

@router.get("/om_headers", response_model=PaginatedResponse[OmHeadersOut])
async def list_om_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = OmHeadersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["so_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/om_headers/{entity_id}", response_model=OmHeadersOut)
async def get_om_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await OmHeadersService(db).get(entity_id)

@router.post("/om_headers", response_model=OmHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_om_headers(
    data: OmHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmHeadersService(db).create(data)

@router.put("/om_headers/{entity_id}", response_model=OmHeadersOut)
async def update_om_headers(
    entity_id: uuid.UUID,
    data: OmHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmHeadersService(db).update(entity_id, data)

@router.delete("/om_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_om_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await OmHeadersService(db).delete(entity_id)

@router.get("/om_lines", response_model=PaginatedResponse[OmLinesOut])
async def list_om_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = OmLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/om_lines/{entity_id}", response_model=OmLinesOut)
async def get_om_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await OmLinesService(db).get(entity_id)

@router.post("/om_lines", response_model=OmLinesOut, status_code=status.HTTP_201_CREATED)
async def create_om_lines(
    data: OmLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmLinesService(db).create(data)

@router.put("/om_lines/{entity_id}", response_model=OmLinesOut)
async def update_om_lines(
    entity_id: uuid.UUID,
    data: OmLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmLinesService(db).update(entity_id, data)

@router.delete("/om_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_om_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await OmLinesService(db).delete(entity_id)

@router.get("/om_shipments", response_model=PaginatedResponse[OmShipmentsOut])
async def list_om_shipments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = OmShipmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["carrier_code", "tracking_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/om_shipments/{entity_id}", response_model=OmShipmentsOut)
async def get_om_shipments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await OmShipmentsService(db).get(entity_id)

@router.post("/om_shipments", response_model=OmShipmentsOut, status_code=status.HTTP_201_CREATED)
async def create_om_shipments(
    data: OmShipmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmShipmentsService(db).create(data)

@router.put("/om_shipments/{entity_id}", response_model=OmShipmentsOut)
async def update_om_shipments(
    entity_id: uuid.UUID,
    data: OmShipmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OmShipmentsService(db).update(entity_id, data)

@router.delete("/om_shipments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_om_shipments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await OmShipmentsService(db).delete(entity_id)

@router.get("/order_import_interface", response_model=PaginatedResponse[OrderImportInterfaceOut])
async def list_order_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = OrderImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/order_import_interface/{entity_id}", response_model=OrderImportInterfaceOut)
async def get_order_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await OrderImportInterfaceService(db).get(entity_id)

@router.post("/order_import_interface", response_model=OrderImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_order_import_interface(
    data: OrderImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OrderImportInterfaceService(db).create(data)

@router.put("/order_import_interface/{entity_id}", response_model=OrderImportInterfaceOut)
async def update_order_import_interface(
    entity_id: uuid.UUID,
    data: OrderImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OrderImportInterfaceService(db).update(entity_id, data)

@router.delete("/order_import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await OrderImportInterfaceService(db).delete(entity_id)

@router.get("/order_types", response_model=PaginatedResponse[OrderTypesOut])
async def list_order_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = OrderTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["order_type_code", "order_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/order_types/{entity_id}", response_model=OrderTypesOut)
async def get_order_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await OrderTypesService(db).get(entity_id)

@router.post("/order_types", response_model=OrderTypesOut, status_code=status.HTTP_201_CREATED)
async def create_order_types(
    data: OrderTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OrderTypesService(db).create(data)

@router.put("/order_types/{entity_id}", response_model=OrderTypesOut)
async def update_order_types(
    entity_id: uuid.UUID,
    data: OrderTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await OrderTypesService(db).update(entity_id, data)

@router.delete("/order_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await OrderTypesService(db).delete(entity_id)

@router.get("/shipment_tracking", response_model=PaginatedResponse[ShipmentTrackingOut])
async def list_shipment_tracking(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = ShipmentTrackingService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["carrier_code", "tracking_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_tracking/{entity_id}", response_model=ShipmentTrackingOut)
async def get_shipment_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await ShipmentTrackingService(db).get(entity_id)

@router.post("/shipment_tracking", response_model=ShipmentTrackingOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_tracking(
    data: ShipmentTrackingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await ShipmentTrackingService(db).create(data)

@router.put("/shipment_tracking/{entity_id}", response_model=ShipmentTrackingOut)
async def update_shipment_tracking(
    entity_id: uuid.UUID,
    data: ShipmentTrackingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await ShipmentTrackingService(db).update(entity_id, data)

@router.delete("/shipment_tracking/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await ShipmentTrackingService(db).delete(entity_id)

@router.get("/wms_callbacks", response_model=PaginatedResponse[WmsCallbacksOut])
async def list_wms_callbacks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = WmsCallbacksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/wms_callbacks/{entity_id}", response_model=WmsCallbacksOut)
async def get_wms_callbacks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await WmsCallbacksService(db).get(entity_id)

@router.post("/wms_callbacks", response_model=WmsCallbacksOut, status_code=status.HTTP_201_CREATED)
async def create_wms_callbacks(
    data: WmsCallbacksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WmsCallbacksService(db).create(data)

@router.put("/wms_callbacks/{entity_id}", response_model=WmsCallbacksOut)
async def update_wms_callbacks(
    entity_id: uuid.UUID,
    data: WmsCallbacksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WmsCallbacksService(db).update(entity_id, data)

@router.delete("/wms_callbacks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wms_callbacks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await WmsCallbacksService(db).delete(entity_id)

@router.get("/wms_task_queue", response_model=PaginatedResponse[WmsTaskQueueOut])
async def list_wms_task_queue(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = WmsTaskQueueService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/wms_task_queue/{entity_id}", response_model=WmsTaskQueueOut)
async def get_wms_task_queue(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await WmsTaskQueueService(db).get(entity_id)

@router.post("/wms_task_queue", response_model=WmsTaskQueueOut, status_code=status.HTTP_201_CREATED)
async def create_wms_task_queue(
    data: WmsTaskQueueCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WmsTaskQueueService(db).create(data)

@router.put("/wms_task_queue/{entity_id}", response_model=WmsTaskQueueOut)
async def update_wms_task_queue(
    entity_id: uuid.UUID,
    data: WmsTaskQueueUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WmsTaskQueueService(db).update(entity_id, data)

@router.delete("/wms_task_queue/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wms_task_queue(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await WmsTaskQueueService(db).delete(entity_id)

@router.get("/workflow_assignments", response_model=PaginatedResponse[WorkflowAssignmentsOut])
async def list_workflow_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = WorkflowAssignmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_assignments/{entity_id}", response_model=WorkflowAssignmentsOut)
async def get_workflow_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await WorkflowAssignmentsService(db).get(entity_id)

@router.post("/workflow_assignments", response_model=WorkflowAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_assignments(
    data: WorkflowAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowAssignmentsService(db).create(data)

@router.put("/workflow_assignments/{entity_id}", response_model=WorkflowAssignmentsOut)
async def update_workflow_assignments(
    entity_id: uuid.UUID,
    data: WorkflowAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowAssignmentsService(db).update(entity_id, data)

@router.delete("/workflow_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await WorkflowAssignmentsService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("om", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
