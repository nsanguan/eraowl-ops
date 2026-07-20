import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.tms.services import (
    AccessorialChargesService,
    AccessorialRateLinesService,
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    CarrierAddressesService,
    CarrierCertificationsService,
    CarrierContactsService,
    CarrierContractsService,
    CarrierEdiCapabilitiesService,
    CarrierEquipmentService,
    CarrierEquipmentTypesService,
    CarrierInsuranceService,
    CarrierPerformanceService,
    CarrierServiceLevelsService,
    CarrierServicesService,
    CarriersService,
    CertificatesOfOriginService,
    ClaimEvidenceService,
    ClaimLinesService,
    ClaimsService,
    ComplianceAccidentsService,
    ComplianceDvirService,
    ComplianceEldService,
    ComplianceIftaService,
    ComplianceViolationsService,
    ContainerSealsService,
    ContainersService,
    CustomsDeclarationLinesService,
    CustomsDeclarationsService,
    DeliveriesService,
    DeliveryLinesService,
    DispatchesService,
    DockAppointmentsService,
    DockDoorsService,
    DocumentDistributionService,
    DocumentTypesService,
    DocumentsService,
    DriverCertificationsService,
    DriverHosService,
    DriverPayrollService,
    DriverTrainingService,
    DriversService,
    EquipmentService,
    EquipmentAssignmentsService,
    EquipmentTrackingDevicesService,
    EquipmentTypesService,
    FreightAuditService,
    FreightCostAllocationsService,
    FreightCostLinesService,
    FreightCostsService,
    FreightInvoiceLinesService,
    FreightInvoicesService,
    FuelConsumptionService,
    FuelSurchargeLinesService,
    FuelSurchargeTablesService,
    FuelTransactionsService,
    GeofenceEventsService,
    GpsPingsService,
    HazmatClassificationsService,
    HazmatIncidentsService,
    HazmatPackagingService,
    HazmatSegregationService,
    HsCodesService,
    IncotermsService,
    InsurancePoliciesService,
    InterfaceErrorLogService,
    InterfaceShipmentImportService,
    KpiDefinitionsService,
    KpiValuesService,
    LaneCarriersService,
    LanePerformanceService,
    LanesService,
    LoadCostsService,
    LoadLegsService,
    LoadLinesService,
    LoadStopsService,
    LoadsService,
    MilestoneAchievementsService,
    MilestonesService,
    PickupLinesService,
    PickupsService,
    PodService,
    RateChartVersionsService,
    RateChartsService,
    RateLinesService,
    RateZonesService,
    RouteAlternativesService,
    RouteStopsService,
    RoutesService,
    ShipmentAppointmentsService,
    ShipmentLinesService,
    ShipmentNotesService,
    ShipmentStatusesService,
    ShipmentTypesService,
    ShipmentsService,
    TemperatureEventsService,
    TenderCascadeService,
    TenderResponsesService,
    TendersService,
    TrackingEventsService,
    TripStopsService,
    TripsService,
    VehicleAssignmentsService,
    VehicleInspectionsService,
    VehicleMaintenanceService,
    VehicleTypesService,
    VehiclesService,
    WorkflowApprovalHierarchiesService,
    WorkflowApprovalHistoryService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
    YardGateTransactionsService,
    YardInventoryService,
    YardLocationsService,
)
from app.modules.tms.schemas import (
    AccessorialChargesCreate,
    AccessorialChargesUpdate,
    AccessorialChargesOut,
    AccessorialRateLinesCreate,
    AccessorialRateLinesUpdate,
    AccessorialRateLinesOut,
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    CarrierAddressesCreate,
    CarrierAddressesUpdate,
    CarrierAddressesOut,
    CarrierCertificationsCreate,
    CarrierCertificationsUpdate,
    CarrierCertificationsOut,
    CarrierContactsCreate,
    CarrierContactsUpdate,
    CarrierContactsOut,
    CarrierContractsCreate,
    CarrierContractsUpdate,
    CarrierContractsOut,
    CarrierEdiCapabilitiesCreate,
    CarrierEdiCapabilitiesUpdate,
    CarrierEdiCapabilitiesOut,
    CarrierEquipmentCreate,
    CarrierEquipmentUpdate,
    CarrierEquipmentOut,
    CarrierEquipmentTypesCreate,
    CarrierEquipmentTypesUpdate,
    CarrierEquipmentTypesOut,
    CarrierInsuranceCreate,
    CarrierInsuranceUpdate,
    CarrierInsuranceOut,
    CarrierPerformanceCreate,
    CarrierPerformanceUpdate,
    CarrierPerformanceOut,
    CarrierServiceLevelsCreate,
    CarrierServiceLevelsUpdate,
    CarrierServiceLevelsOut,
    CarrierServicesCreate,
    CarrierServicesUpdate,
    CarrierServicesOut,
    CarriersCreate,
    CarriersUpdate,
    CarriersOut,
    CertificatesOfOriginCreate,
    CertificatesOfOriginUpdate,
    CertificatesOfOriginOut,
    ClaimEvidenceCreate,
    ClaimEvidenceUpdate,
    ClaimEvidenceOut,
    ClaimLinesCreate,
    ClaimLinesUpdate,
    ClaimLinesOut,
    ClaimsCreate,
    ClaimsUpdate,
    ClaimsOut,
    ComplianceAccidentsCreate,
    ComplianceAccidentsUpdate,
    ComplianceAccidentsOut,
    ComplianceDvirCreate,
    ComplianceDvirUpdate,
    ComplianceDvirOut,
    ComplianceEldCreate,
    ComplianceEldUpdate,
    ComplianceEldOut,
    ComplianceIftaCreate,
    ComplianceIftaUpdate,
    ComplianceIftaOut,
    ComplianceViolationsCreate,
    ComplianceViolationsUpdate,
    ComplianceViolationsOut,
    ContainerSealsCreate,
    ContainerSealsUpdate,
    ContainerSealsOut,
    ContainersCreate,
    ContainersUpdate,
    ContainersOut,
    CustomsDeclarationLinesCreate,
    CustomsDeclarationLinesUpdate,
    CustomsDeclarationLinesOut,
    CustomsDeclarationsCreate,
    CustomsDeclarationsUpdate,
    CustomsDeclarationsOut,
    DeliveriesCreate,
    DeliveriesUpdate,
    DeliveriesOut,
    DeliveryLinesCreate,
    DeliveryLinesUpdate,
    DeliveryLinesOut,
    DispatchesCreate,
    DispatchesUpdate,
    DispatchesOut,
    DockAppointmentsCreate,
    DockAppointmentsUpdate,
    DockAppointmentsOut,
    DockDoorsCreate,
    DockDoorsUpdate,
    DockDoorsOut,
    DocumentDistributionCreate,
    DocumentDistributionUpdate,
    DocumentDistributionOut,
    DocumentTypesCreate,
    DocumentTypesUpdate,
    DocumentTypesOut,
    DocumentsCreate,
    DocumentsUpdate,
    DocumentsOut,
    DriverCertificationsCreate,
    DriverCertificationsUpdate,
    DriverCertificationsOut,
    DriverHosCreate,
    DriverHosUpdate,
    DriverHosOut,
    DriverPayrollCreate,
    DriverPayrollUpdate,
    DriverPayrollOut,
    DriverTrainingCreate,
    DriverTrainingUpdate,
    DriverTrainingOut,
    DriversCreate,
    DriversUpdate,
    DriversOut,
    EquipmentCreate,
    EquipmentUpdate,
    EquipmentOut,
    EquipmentAssignmentsCreate,
    EquipmentAssignmentsUpdate,
    EquipmentAssignmentsOut,
    EquipmentTrackingDevicesCreate,
    EquipmentTrackingDevicesUpdate,
    EquipmentTrackingDevicesOut,
    EquipmentTypesCreate,
    EquipmentTypesUpdate,
    EquipmentTypesOut,
    FreightAuditCreate,
    FreightAuditUpdate,
    FreightAuditOut,
    FreightCostAllocationsCreate,
    FreightCostAllocationsUpdate,
    FreightCostAllocationsOut,
    FreightCostLinesCreate,
    FreightCostLinesUpdate,
    FreightCostLinesOut,
    FreightCostsCreate,
    FreightCostsUpdate,
    FreightCostsOut,
    FreightInvoiceLinesCreate,
    FreightInvoiceLinesUpdate,
    FreightInvoiceLinesOut,
    FreightInvoicesCreate,
    FreightInvoicesUpdate,
    FreightInvoicesOut,
    FuelConsumptionCreate,
    FuelConsumptionUpdate,
    FuelConsumptionOut,
    FuelSurchargeLinesCreate,
    FuelSurchargeLinesUpdate,
    FuelSurchargeLinesOut,
    FuelSurchargeTablesCreate,
    FuelSurchargeTablesUpdate,
    FuelSurchargeTablesOut,
    FuelTransactionsCreate,
    FuelTransactionsUpdate,
    FuelTransactionsOut,
    GeofenceEventsCreate,
    GeofenceEventsUpdate,
    GeofenceEventsOut,
    GpsPingsCreate,
    GpsPingsUpdate,
    GpsPingsOut,
    HazmatClassificationsCreate,
    HazmatClassificationsUpdate,
    HazmatClassificationsOut,
    HazmatIncidentsCreate,
    HazmatIncidentsUpdate,
    HazmatIncidentsOut,
    HazmatPackagingCreate,
    HazmatPackagingUpdate,
    HazmatPackagingOut,
    HazmatSegregationCreate,
    HazmatSegregationUpdate,
    HazmatSegregationOut,
    HsCodesCreate,
    HsCodesUpdate,
    HsCodesOut,
    IncotermsCreate,
    IncotermsUpdate,
    IncotermsOut,
    InsurancePoliciesCreate,
    InsurancePoliciesUpdate,
    InsurancePoliciesOut,
    InterfaceErrorLogCreate,
    InterfaceErrorLogUpdate,
    InterfaceErrorLogOut,
    InterfaceShipmentImportCreate,
    InterfaceShipmentImportUpdate,
    InterfaceShipmentImportOut,
    KpiDefinitionsCreate,
    KpiDefinitionsUpdate,
    KpiDefinitionsOut,
    KpiValuesCreate,
    KpiValuesUpdate,
    KpiValuesOut,
    LaneCarriersCreate,
    LaneCarriersUpdate,
    LaneCarriersOut,
    LanePerformanceCreate,
    LanePerformanceUpdate,
    LanePerformanceOut,
    LanesCreate,
    LanesUpdate,
    LanesOut,
    LoadCostsCreate,
    LoadCostsUpdate,
    LoadCostsOut,
    LoadLegsCreate,
    LoadLegsUpdate,
    LoadLegsOut,
    LoadLinesCreate,
    LoadLinesUpdate,
    LoadLinesOut,
    LoadStopsCreate,
    LoadStopsUpdate,
    LoadStopsOut,
    LoadsCreate,
    LoadsUpdate,
    LoadsOut,
    MilestoneAchievementsCreate,
    MilestoneAchievementsUpdate,
    MilestoneAchievementsOut,
    MilestonesCreate,
    MilestonesUpdate,
    MilestonesOut,
    PickupLinesCreate,
    PickupLinesUpdate,
    PickupLinesOut,
    PickupsCreate,
    PickupsUpdate,
    PickupsOut,
    PodCreate,
    PodUpdate,
    PodOut,
    RateChartVersionsCreate,
    RateChartVersionsUpdate,
    RateChartVersionsOut,
    RateChartsCreate,
    RateChartsUpdate,
    RateChartsOut,
    RateLinesCreate,
    RateLinesUpdate,
    RateLinesOut,
    RateZonesCreate,
    RateZonesUpdate,
    RateZonesOut,
    RouteAlternativesCreate,
    RouteAlternativesUpdate,
    RouteAlternativesOut,
    RouteStopsCreate,
    RouteStopsUpdate,
    RouteStopsOut,
    RoutesCreate,
    RoutesUpdate,
    RoutesOut,
    ShipmentAppointmentsCreate,
    ShipmentAppointmentsUpdate,
    ShipmentAppointmentsOut,
    ShipmentLinesCreate,
    ShipmentLinesUpdate,
    ShipmentLinesOut,
    ShipmentNotesCreate,
    ShipmentNotesUpdate,
    ShipmentNotesOut,
    ShipmentStatusesCreate,
    ShipmentStatusesUpdate,
    ShipmentStatusesOut,
    ShipmentTypesCreate,
    ShipmentTypesUpdate,
    ShipmentTypesOut,
    ShipmentsCreate,
    ShipmentsUpdate,
    ShipmentsOut,
    TemperatureEventsCreate,
    TemperatureEventsUpdate,
    TemperatureEventsOut,
    TenderCascadeCreate,
    TenderCascadeUpdate,
    TenderCascadeOut,
    TenderResponsesCreate,
    TenderResponsesUpdate,
    TenderResponsesOut,
    TendersCreate,
    TendersUpdate,
    TendersOut,
    TrackingEventsCreate,
    TrackingEventsUpdate,
    TrackingEventsOut,
    TripStopsCreate,
    TripStopsUpdate,
    TripStopsOut,
    TripsCreate,
    TripsUpdate,
    TripsOut,
    VehicleAssignmentsCreate,
    VehicleAssignmentsUpdate,
    VehicleAssignmentsOut,
    VehicleInspectionsCreate,
    VehicleInspectionsUpdate,
    VehicleInspectionsOut,
    VehicleMaintenanceCreate,
    VehicleMaintenanceUpdate,
    VehicleMaintenanceOut,
    VehicleTypesCreate,
    VehicleTypesUpdate,
    VehicleTypesOut,
    VehiclesCreate,
    VehiclesUpdate,
    VehiclesOut,
    WorkflowApprovalHierarchiesCreate,
    WorkflowApprovalHierarchiesUpdate,
    WorkflowApprovalHierarchiesOut,
    WorkflowApprovalHistoryCreate,
    WorkflowApprovalHistoryUpdate,
    WorkflowApprovalHistoryOut,
    WorkflowDefinitionsCreate,
    WorkflowDefinitionsUpdate,
    WorkflowDefinitionsOut,
    WorkflowTasksCreate,
    WorkflowTasksUpdate,
    WorkflowTasksOut,
    YardGateTransactionsCreate,
    YardGateTransactionsUpdate,
    YardGateTransactionsOut,
    YardInventoryCreate,
    YardInventoryUpdate,
    YardInventoryOut,
    YardLocationsCreate,
    YardLocationsUpdate,
    YardLocationsOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/accessorial_charges", response_model=PaginatedResponse[AccessorialChargesOut])
async def list_accessorial_charges(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = AccessorialChargesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["charge_code", "charge_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/accessorial_charges/{entity_id}", response_model=AccessorialChargesOut)
async def get_accessorial_charges(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await AccessorialChargesService(db).get(entity_id)

@router.post("/accessorial_charges", response_model=AccessorialChargesOut, status_code=status.HTTP_201_CREATED)
async def create_accessorial_charges(
    data: AccessorialChargesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AccessorialChargesService(db).create(data)

@router.put("/accessorial_charges/{entity_id}", response_model=AccessorialChargesOut)
async def update_accessorial_charges(
    entity_id: uuid.UUID,
    data: AccessorialChargesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AccessorialChargesService(db).update(entity_id, data)

@router.delete("/accessorial_charges/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_accessorial_charges(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await AccessorialChargesService(db).delete(entity_id)

@router.get("/accessorial_rate_lines", response_model=PaginatedResponse[AccessorialRateLinesOut])
async def list_accessorial_rate_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = AccessorialRateLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/accessorial_rate_lines/{entity_id}", response_model=AccessorialRateLinesOut)
async def get_accessorial_rate_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await AccessorialRateLinesService(db).get(entity_id)

@router.post("/accessorial_rate_lines", response_model=AccessorialRateLinesOut, status_code=status.HTTP_201_CREATED)
async def create_accessorial_rate_lines(
    data: AccessorialRateLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AccessorialRateLinesService(db).create(data)

@router.put("/accessorial_rate_lines/{entity_id}", response_model=AccessorialRateLinesOut)
async def update_accessorial_rate_lines(
    entity_id: uuid.UUID,
    data: AccessorialRateLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AccessorialRateLinesService(db).update(entity_id, data)

@router.delete("/accessorial_rate_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_accessorial_rate_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await AccessorialRateLinesService(db).delete(entity_id)

@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = AiDecisionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/carrier_addresses", response_model=PaginatedResponse[CarrierAddressesOut])
async def list_carrier_addresses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierAddressesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["postal_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_addresses/{entity_id}", response_model=CarrierAddressesOut)
async def get_carrier_addresses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierAddressesService(db).get(entity_id)

@router.post("/carrier_addresses", response_model=CarrierAddressesOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_addresses(
    data: CarrierAddressesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierAddressesService(db).create(data)

@router.put("/carrier_addresses/{entity_id}", response_model=CarrierAddressesOut)
async def update_carrier_addresses(
    entity_id: uuid.UUID,
    data: CarrierAddressesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierAddressesService(db).update(entity_id, data)

@router.delete("/carrier_addresses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_addresses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierAddressesService(db).delete(entity_id)

@router.get("/carrier_certifications", response_model=PaginatedResponse[CarrierCertificationsOut])
async def list_carrier_certifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierCertificationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["certification_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_certifications/{entity_id}", response_model=CarrierCertificationsOut)
async def get_carrier_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierCertificationsService(db).get(entity_id)

@router.post("/carrier_certifications", response_model=CarrierCertificationsOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_certifications(
    data: CarrierCertificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierCertificationsService(db).create(data)

@router.put("/carrier_certifications/{entity_id}", response_model=CarrierCertificationsOut)
async def update_carrier_certifications(
    entity_id: uuid.UUID,
    data: CarrierCertificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierCertificationsService(db).update(entity_id, data)

@router.delete("/carrier_certifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierCertificationsService(db).delete(entity_id)

@router.get("/carrier_contacts", response_model=PaginatedResponse[CarrierContactsOut])
async def list_carrier_contacts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierContactsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["first_name", "last_name", "title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_contacts/{entity_id}", response_model=CarrierContactsOut)
async def get_carrier_contacts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierContactsService(db).get(entity_id)

@router.post("/carrier_contacts", response_model=CarrierContactsOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_contacts(
    data: CarrierContactsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierContactsService(db).create(data)

@router.put("/carrier_contacts/{entity_id}", response_model=CarrierContactsOut)
async def update_carrier_contacts(
    entity_id: uuid.UUID,
    data: CarrierContactsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierContactsService(db).update(entity_id, data)

@router.delete("/carrier_contacts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_contacts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierContactsService(db).delete(entity_id)

@router.get("/carrier_contracts", response_model=PaginatedResponse[CarrierContractsOut])
async def list_carrier_contracts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierContractsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["contract_number", "contract_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_contracts/{entity_id}", response_model=CarrierContractsOut)
async def get_carrier_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierContractsService(db).get(entity_id)

@router.post("/carrier_contracts", response_model=CarrierContractsOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_contracts(
    data: CarrierContractsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierContractsService(db).create(data)

@router.put("/carrier_contracts/{entity_id}", response_model=CarrierContractsOut)
async def update_carrier_contracts(
    entity_id: uuid.UUID,
    data: CarrierContractsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierContractsService(db).update(entity_id, data)

@router.delete("/carrier_contracts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_contracts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierContractsService(db).delete(entity_id)

@router.get("/carrier_edi_capabilities", response_model=PaginatedResponse[CarrierEdiCapabilitiesOut])
async def list_carrier_edi_capabilities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierEdiCapabilitiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_edi_capabilities/{entity_id}", response_model=CarrierEdiCapabilitiesOut)
async def get_carrier_edi_capabilities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierEdiCapabilitiesService(db).get(entity_id)

@router.post("/carrier_edi_capabilities", response_model=CarrierEdiCapabilitiesOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_edi_capabilities(
    data: CarrierEdiCapabilitiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEdiCapabilitiesService(db).create(data)

@router.put("/carrier_edi_capabilities/{entity_id}", response_model=CarrierEdiCapabilitiesOut)
async def update_carrier_edi_capabilities(
    entity_id: uuid.UUID,
    data: CarrierEdiCapabilitiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEdiCapabilitiesService(db).update(entity_id, data)

@router.delete("/carrier_edi_capabilities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_edi_capabilities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierEdiCapabilitiesService(db).delete(entity_id)

@router.get("/carrier_equipment", response_model=PaginatedResponse[CarrierEquipmentOut])
async def list_carrier_equipment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierEquipmentService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["unit_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_equipment/{entity_id}", response_model=CarrierEquipmentOut)
async def get_carrier_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierEquipmentService(db).get(entity_id)

@router.post("/carrier_equipment", response_model=CarrierEquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_equipment(
    data: CarrierEquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEquipmentService(db).create(data)

@router.put("/carrier_equipment/{entity_id}", response_model=CarrierEquipmentOut)
async def update_carrier_equipment(
    entity_id: uuid.UUID,
    data: CarrierEquipmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEquipmentService(db).update(entity_id, data)

@router.delete("/carrier_equipment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierEquipmentService(db).delete(entity_id)

@router.get("/carrier_equipment_types", response_model=PaginatedResponse[CarrierEquipmentTypesOut])
async def list_carrier_equipment_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierEquipmentTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["equipment_type_code", "equipment_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_equipment_types/{entity_id}", response_model=CarrierEquipmentTypesOut)
async def get_carrier_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierEquipmentTypesService(db).get(entity_id)

@router.post("/carrier_equipment_types", response_model=CarrierEquipmentTypesOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_equipment_types(
    data: CarrierEquipmentTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEquipmentTypesService(db).create(data)

@router.put("/carrier_equipment_types/{entity_id}", response_model=CarrierEquipmentTypesOut)
async def update_carrier_equipment_types(
    entity_id: uuid.UUID,
    data: CarrierEquipmentTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierEquipmentTypesService(db).update(entity_id, data)

@router.delete("/carrier_equipment_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierEquipmentTypesService(db).delete(entity_id)

@router.get("/carrier_insurance", response_model=PaginatedResponse[CarrierInsuranceOut])
async def list_carrier_insurance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierInsuranceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["policy_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_insurance/{entity_id}", response_model=CarrierInsuranceOut)
async def get_carrier_insurance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierInsuranceService(db).get(entity_id)

@router.post("/carrier_insurance", response_model=CarrierInsuranceOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_insurance(
    data: CarrierInsuranceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierInsuranceService(db).create(data)

@router.put("/carrier_insurance/{entity_id}", response_model=CarrierInsuranceOut)
async def update_carrier_insurance(
    entity_id: uuid.UUID,
    data: CarrierInsuranceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierInsuranceService(db).update(entity_id, data)

@router.delete("/carrier_insurance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_insurance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierInsuranceService(db).delete(entity_id)

@router.get("/carrier_performance", response_model=PaginatedResponse[CarrierPerformanceOut])
async def list_carrier_performance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierPerformanceService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_performance/{entity_id}", response_model=CarrierPerformanceOut)
async def get_carrier_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierPerformanceService(db).get(entity_id)

@router.post("/carrier_performance", response_model=CarrierPerformanceOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_performance(
    data: CarrierPerformanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierPerformanceService(db).create(data)

@router.put("/carrier_performance/{entity_id}", response_model=CarrierPerformanceOut)
async def update_carrier_performance(
    entity_id: uuid.UUID,
    data: CarrierPerformanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierPerformanceService(db).update(entity_id, data)

@router.delete("/carrier_performance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierPerformanceService(db).delete(entity_id)

@router.get("/carrier_service_levels", response_model=PaginatedResponse[CarrierServiceLevelsOut])
async def list_carrier_service_levels(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierServiceLevelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["level_code", "level_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_service_levels/{entity_id}", response_model=CarrierServiceLevelsOut)
async def get_carrier_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierServiceLevelsService(db).get(entity_id)

@router.post("/carrier_service_levels", response_model=CarrierServiceLevelsOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_service_levels(
    data: CarrierServiceLevelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierServiceLevelsService(db).create(data)

@router.put("/carrier_service_levels/{entity_id}", response_model=CarrierServiceLevelsOut)
async def update_carrier_service_levels(
    entity_id: uuid.UUID,
    data: CarrierServiceLevelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierServiceLevelsService(db).update(entity_id, data)

@router.delete("/carrier_service_levels/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_service_levels(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierServiceLevelsService(db).delete(entity_id)

@router.get("/carrier_services", response_model=PaginatedResponse[CarrierServicesOut])
async def list_carrier_services(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarrierServicesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["service_code", "service_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carrier_services/{entity_id}", response_model=CarrierServicesOut)
async def get_carrier_services(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarrierServicesService(db).get(entity_id)

@router.post("/carrier_services", response_model=CarrierServicesOut, status_code=status.HTTP_201_CREATED)
async def create_carrier_services(
    data: CarrierServicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierServicesService(db).create(data)

@router.put("/carrier_services/{entity_id}", response_model=CarrierServicesOut)
async def update_carrier_services(
    entity_id: uuid.UUID,
    data: CarrierServicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarrierServicesService(db).update(entity_id, data)

@router.delete("/carrier_services/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carrier_services(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarrierServicesService(db).delete(entity_id)

@router.get("/carriers", response_model=PaginatedResponse[CarriersOut])
async def list_carriers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CarriersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["carrier_code", "carrier_name", "mc_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/carriers/{entity_id}", response_model=CarriersOut)
async def get_carriers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CarriersService(db).get(entity_id)

@router.post("/carriers", response_model=CarriersOut, status_code=status.HTTP_201_CREATED)
async def create_carriers(
    data: CarriersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarriersService(db).create(data)

@router.put("/carriers/{entity_id}", response_model=CarriersOut)
async def update_carriers(
    entity_id: uuid.UUID,
    data: CarriersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CarriersService(db).update(entity_id, data)

@router.delete("/carriers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carriers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CarriersService(db).delete(entity_id)

@router.get("/certificates_of_origin", response_model=PaginatedResponse[CertificatesOfOriginOut])
async def list_certificates_of_origin(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CertificatesOfOriginService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["certificate_number", "exporter_name", "consignee_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/certificates_of_origin/{entity_id}", response_model=CertificatesOfOriginOut)
async def get_certificates_of_origin(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CertificatesOfOriginService(db).get(entity_id)

@router.post("/certificates_of_origin", response_model=CertificatesOfOriginOut, status_code=status.HTTP_201_CREATED)
async def create_certificates_of_origin(
    data: CertificatesOfOriginCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CertificatesOfOriginService(db).create(data)

@router.put("/certificates_of_origin/{entity_id}", response_model=CertificatesOfOriginOut)
async def update_certificates_of_origin(
    entity_id: uuid.UUID,
    data: CertificatesOfOriginUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CertificatesOfOriginService(db).update(entity_id, data)

@router.delete("/certificates_of_origin/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_certificates_of_origin(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CertificatesOfOriginService(db).delete(entity_id)

@router.get("/claim_evidence", response_model=PaginatedResponse[ClaimEvidenceOut])
async def list_claim_evidence(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ClaimEvidenceService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/claim_evidence/{entity_id}", response_model=ClaimEvidenceOut)
async def get_claim_evidence(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ClaimEvidenceService(db).get(entity_id)

@router.post("/claim_evidence", response_model=ClaimEvidenceOut, status_code=status.HTTP_201_CREATED)
async def create_claim_evidence(
    data: ClaimEvidenceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimEvidenceService(db).create(data)

@router.put("/claim_evidence/{entity_id}", response_model=ClaimEvidenceOut)
async def update_claim_evidence(
    entity_id: uuid.UUID,
    data: ClaimEvidenceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimEvidenceService(db).update(entity_id, data)

@router.delete("/claim_evidence/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_claim_evidence(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ClaimEvidenceService(db).delete(entity_id)

@router.get("/claim_lines", response_model=PaginatedResponse[ClaimLinesOut])
async def list_claim_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ClaimLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/claim_lines/{entity_id}", response_model=ClaimLinesOut)
async def get_claim_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ClaimLinesService(db).get(entity_id)

@router.post("/claim_lines", response_model=ClaimLinesOut, status_code=status.HTTP_201_CREATED)
async def create_claim_lines(
    data: ClaimLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimLinesService(db).create(data)

@router.put("/claim_lines/{entity_id}", response_model=ClaimLinesOut)
async def update_claim_lines(
    entity_id: uuid.UUID,
    data: ClaimLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimLinesService(db).update(entity_id, data)

@router.delete("/claim_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_claim_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ClaimLinesService(db).delete(entity_id)

@router.get("/claims", response_model=PaginatedResponse[ClaimsOut])
async def list_claims(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ClaimsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["claim_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/claims/{entity_id}", response_model=ClaimsOut)
async def get_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ClaimsService(db).get(entity_id)

@router.post("/claims", response_model=ClaimsOut, status_code=status.HTTP_201_CREATED)
async def create_claims(
    data: ClaimsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimsService(db).create(data)

@router.put("/claims/{entity_id}", response_model=ClaimsOut)
async def update_claims(
    entity_id: uuid.UUID,
    data: ClaimsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ClaimsService(db).update(entity_id, data)

@router.delete("/claims/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_claims(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ClaimsService(db).delete(entity_id)

@router.get("/compliance_accidents", response_model=PaginatedResponse[ComplianceAccidentsOut])
async def list_compliance_accidents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ComplianceAccidentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["accident_number", "location_description", "police_report_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/compliance_accidents/{entity_id}", response_model=ComplianceAccidentsOut)
async def get_compliance_accidents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ComplianceAccidentsService(db).get(entity_id)

@router.post("/compliance_accidents", response_model=ComplianceAccidentsOut, status_code=status.HTTP_201_CREATED)
async def create_compliance_accidents(
    data: ComplianceAccidentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceAccidentsService(db).create(data)

@router.put("/compliance_accidents/{entity_id}", response_model=ComplianceAccidentsOut)
async def update_compliance_accidents(
    entity_id: uuid.UUID,
    data: ComplianceAccidentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceAccidentsService(db).update(entity_id, data)

@router.delete("/compliance_accidents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_compliance_accidents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ComplianceAccidentsService(db).delete(entity_id)

@router.get("/compliance_dvir", response_model=PaginatedResponse[ComplianceDvirOut])
async def list_compliance_dvir(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ComplianceDvirService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["dvir_number", "mechanic_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/compliance_dvir/{entity_id}", response_model=ComplianceDvirOut)
async def get_compliance_dvir(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ComplianceDvirService(db).get(entity_id)

@router.post("/compliance_dvir", response_model=ComplianceDvirOut, status_code=status.HTTP_201_CREATED)
async def create_compliance_dvir(
    data: ComplianceDvirCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceDvirService(db).create(data)

@router.put("/compliance_dvir/{entity_id}", response_model=ComplianceDvirOut)
async def update_compliance_dvir(
    entity_id: uuid.UUID,
    data: ComplianceDvirUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceDvirService(db).update(entity_id, data)

@router.delete("/compliance_dvir/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_compliance_dvir(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ComplianceDvirService(db).delete(entity_id)

@router.get("/compliance_eld", response_model=PaginatedResponse[ComplianceEldOut])
async def list_compliance_eld(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ComplianceEldService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/compliance_eld/{entity_id}", response_model=ComplianceEldOut)
async def get_compliance_eld(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ComplianceEldService(db).get(entity_id)

@router.post("/compliance_eld", response_model=ComplianceEldOut, status_code=status.HTTP_201_CREATED)
async def create_compliance_eld(
    data: ComplianceEldCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceEldService(db).create(data)

@router.put("/compliance_eld/{entity_id}", response_model=ComplianceEldOut)
async def update_compliance_eld(
    entity_id: uuid.UUID,
    data: ComplianceEldUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceEldService(db).update(entity_id, data)

@router.delete("/compliance_eld/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_compliance_eld(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ComplianceEldService(db).delete(entity_id)

@router.get("/compliance_ifta", response_model=PaginatedResponse[ComplianceIftaOut])
async def list_compliance_ifta(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ComplianceIftaService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/compliance_ifta/{entity_id}", response_model=ComplianceIftaOut)
async def get_compliance_ifta(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ComplianceIftaService(db).get(entity_id)

@router.post("/compliance_ifta", response_model=ComplianceIftaOut, status_code=status.HTTP_201_CREATED)
async def create_compliance_ifta(
    data: ComplianceIftaCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceIftaService(db).create(data)

@router.put("/compliance_ifta/{entity_id}", response_model=ComplianceIftaOut)
async def update_compliance_ifta(
    entity_id: uuid.UUID,
    data: ComplianceIftaUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceIftaService(db).update(entity_id, data)

@router.delete("/compliance_ifta/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_compliance_ifta(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ComplianceIftaService(db).delete(entity_id)

@router.get("/compliance_violations", response_model=PaginatedResponse[ComplianceViolationsOut])
async def list_compliance_violations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ComplianceViolationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["violation_number", "violation_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/compliance_violations/{entity_id}", response_model=ComplianceViolationsOut)
async def get_compliance_violations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ComplianceViolationsService(db).get(entity_id)

@router.post("/compliance_violations", response_model=ComplianceViolationsOut, status_code=status.HTTP_201_CREATED)
async def create_compliance_violations(
    data: ComplianceViolationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceViolationsService(db).create(data)

@router.put("/compliance_violations/{entity_id}", response_model=ComplianceViolationsOut)
async def update_compliance_violations(
    entity_id: uuid.UUID,
    data: ComplianceViolationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ComplianceViolationsService(db).update(entity_id, data)

@router.delete("/compliance_violations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_compliance_violations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ComplianceViolationsService(db).delete(entity_id)

@router.get("/container_seals", response_model=PaginatedResponse[ContainerSealsOut])
async def list_container_seals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ContainerSealsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["seal_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/container_seals/{entity_id}", response_model=ContainerSealsOut)
async def get_container_seals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ContainerSealsService(db).get(entity_id)

@router.post("/container_seals", response_model=ContainerSealsOut, status_code=status.HTTP_201_CREATED)
async def create_container_seals(
    data: ContainerSealsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ContainerSealsService(db).create(data)

@router.put("/container_seals/{entity_id}", response_model=ContainerSealsOut)
async def update_container_seals(
    entity_id: uuid.UUID,
    data: ContainerSealsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ContainerSealsService(db).update(entity_id, data)

@router.delete("/container_seals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_container_seals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ContainerSealsService(db).delete(entity_id)

@router.get("/containers", response_model=PaginatedResponse[ContainersOut])
async def list_containers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ContainersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["container_number", "size_code", "iso_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/containers/{entity_id}", response_model=ContainersOut)
async def get_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ContainersService(db).get(entity_id)

@router.post("/containers", response_model=ContainersOut, status_code=status.HTTP_201_CREATED)
async def create_containers(
    data: ContainersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ContainersService(db).create(data)

@router.put("/containers/{entity_id}", response_model=ContainersOut)
async def update_containers(
    entity_id: uuid.UUID,
    data: ContainersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ContainersService(db).update(entity_id, data)

@router.delete("/containers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ContainersService(db).delete(entity_id)

@router.get("/customs_declaration_lines", response_model=PaginatedResponse[CustomsDeclarationLinesOut])
async def list_customs_declaration_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CustomsDeclarationLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["preference_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/customs_declaration_lines/{entity_id}", response_model=CustomsDeclarationLinesOut)
async def get_customs_declaration_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CustomsDeclarationLinesService(db).get(entity_id)

@router.post("/customs_declaration_lines", response_model=CustomsDeclarationLinesOut, status_code=status.HTTP_201_CREATED)
async def create_customs_declaration_lines(
    data: CustomsDeclarationLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CustomsDeclarationLinesService(db).create(data)

@router.put("/customs_declaration_lines/{entity_id}", response_model=CustomsDeclarationLinesOut)
async def update_customs_declaration_lines(
    entity_id: uuid.UUID,
    data: CustomsDeclarationLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CustomsDeclarationLinesService(db).update(entity_id, data)

@router.delete("/customs_declaration_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customs_declaration_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CustomsDeclarationLinesService(db).delete(entity_id)

@router.get("/customs_declarations", response_model=PaginatedResponse[CustomsDeclarationsOut])
async def list_customs_declarations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = CustomsDeclarationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["declaration_number", "entry_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/customs_declarations/{entity_id}", response_model=CustomsDeclarationsOut)
async def get_customs_declarations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await CustomsDeclarationsService(db).get(entity_id)

@router.post("/customs_declarations", response_model=CustomsDeclarationsOut, status_code=status.HTTP_201_CREATED)
async def create_customs_declarations(
    data: CustomsDeclarationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CustomsDeclarationsService(db).create(data)

@router.put("/customs_declarations/{entity_id}", response_model=CustomsDeclarationsOut)
async def update_customs_declarations(
    entity_id: uuid.UUID,
    data: CustomsDeclarationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await CustomsDeclarationsService(db).update(entity_id, data)

@router.delete("/customs_declarations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customs_declarations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await CustomsDeclarationsService(db).delete(entity_id)

@router.get("/deliveries", response_model=PaginatedResponse[DeliveriesOut])
async def list_deliveries(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DeliveriesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["delivery_number", "location_name", "postal_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/deliveries/{entity_id}", response_model=DeliveriesOut)
async def get_deliveries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DeliveriesService(db).get(entity_id)

@router.post("/deliveries", response_model=DeliveriesOut, status_code=status.HTTP_201_CREATED)
async def create_deliveries(
    data: DeliveriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DeliveriesService(db).create(data)

@router.put("/deliveries/{entity_id}", response_model=DeliveriesOut)
async def update_deliveries(
    entity_id: uuid.UUID,
    data: DeliveriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DeliveriesService(db).update(entity_id, data)

@router.delete("/deliveries/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_deliveries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DeliveriesService(db).delete(entity_id)

@router.get("/delivery_lines", response_model=PaginatedResponse[DeliveryLinesOut])
async def list_delivery_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DeliveryLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/delivery_lines/{entity_id}", response_model=DeliveryLinesOut)
async def get_delivery_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DeliveryLinesService(db).get(entity_id)

@router.post("/delivery_lines", response_model=DeliveryLinesOut, status_code=status.HTTP_201_CREATED)
async def create_delivery_lines(
    data: DeliveryLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DeliveryLinesService(db).create(data)

@router.put("/delivery_lines/{entity_id}", response_model=DeliveryLinesOut)
async def update_delivery_lines(
    entity_id: uuid.UUID,
    data: DeliveryLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DeliveryLinesService(db).update(entity_id, data)

@router.delete("/delivery_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DeliveryLinesService(db).delete(entity_id)

@router.get("/dispatches", response_model=PaginatedResponse[DispatchesOut])
async def list_dispatches(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DispatchesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["dispatch_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/dispatches/{entity_id}", response_model=DispatchesOut)
async def get_dispatches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DispatchesService(db).get(entity_id)

@router.post("/dispatches", response_model=DispatchesOut, status_code=status.HTTP_201_CREATED)
async def create_dispatches(
    data: DispatchesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DispatchesService(db).create(data)

@router.put("/dispatches/{entity_id}", response_model=DispatchesOut)
async def update_dispatches(
    entity_id: uuid.UUID,
    data: DispatchesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DispatchesService(db).update(entity_id, data)

@router.delete("/dispatches/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dispatches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DispatchesService(db).delete(entity_id)

@router.get("/dock_appointments", response_model=PaginatedResponse[DockAppointmentsOut])
async def list_dock_appointments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DockAppointmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/dock_appointments/{entity_id}", response_model=DockAppointmentsOut)
async def get_dock_appointments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DockAppointmentsService(db).get(entity_id)

@router.post("/dock_appointments", response_model=DockAppointmentsOut, status_code=status.HTTP_201_CREATED)
async def create_dock_appointments(
    data: DockAppointmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DockAppointmentsService(db).create(data)

@router.put("/dock_appointments/{entity_id}", response_model=DockAppointmentsOut)
async def update_dock_appointments(
    entity_id: uuid.UUID,
    data: DockAppointmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DockAppointmentsService(db).update(entity_id, data)

@router.delete("/dock_appointments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dock_appointments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DockAppointmentsService(db).delete(entity_id)

@router.get("/dock_doors", response_model=PaginatedResponse[DockDoorsOut])
async def list_dock_doors(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DockDoorsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["door_code", "door_name", "facility_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/dock_doors/{entity_id}", response_model=DockDoorsOut)
async def get_dock_doors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DockDoorsService(db).get(entity_id)

@router.post("/dock_doors", response_model=DockDoorsOut, status_code=status.HTTP_201_CREATED)
async def create_dock_doors(
    data: DockDoorsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DockDoorsService(db).create(data)

@router.put("/dock_doors/{entity_id}", response_model=DockDoorsOut)
async def update_dock_doors(
    entity_id: uuid.UUID,
    data: DockDoorsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DockDoorsService(db).update(entity_id, data)

@router.delete("/dock_doors/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dock_doors(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DockDoorsService(db).delete(entity_id)

@router.get("/document_distribution", response_model=PaginatedResponse[DocumentDistributionOut])
async def list_document_distribution(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DocumentDistributionService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["recipient_email", "recipient_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/document_distribution/{entity_id}", response_model=DocumentDistributionOut)
async def get_document_distribution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DocumentDistributionService(db).get(entity_id)

@router.post("/document_distribution", response_model=DocumentDistributionOut, status_code=status.HTTP_201_CREATED)
async def create_document_distribution(
    data: DocumentDistributionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentDistributionService(db).create(data)

@router.put("/document_distribution/{entity_id}", response_model=DocumentDistributionOut)
async def update_document_distribution(
    entity_id: uuid.UUID,
    data: DocumentDistributionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentDistributionService(db).update(entity_id, data)

@router.delete("/document_distribution/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document_distribution(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DocumentDistributionService(db).delete(entity_id)

@router.get("/document_types", response_model=PaginatedResponse[DocumentTypesOut])
async def list_document_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DocumentTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["document_type_code", "document_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/document_types/{entity_id}", response_model=DocumentTypesOut)
async def get_document_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DocumentTypesService(db).get(entity_id)

@router.post("/document_types", response_model=DocumentTypesOut, status_code=status.HTTP_201_CREATED)
async def create_document_types(
    data: DocumentTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentTypesService(db).create(data)

@router.put("/document_types/{entity_id}", response_model=DocumentTypesOut)
async def update_document_types(
    entity_id: uuid.UUID,
    data: DocumentTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentTypesService(db).update(entity_id, data)

@router.delete("/document_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DocumentTypesService(db).delete(entity_id)

@router.get("/documents", response_model=PaginatedResponse[DocumentsOut])
async def list_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DocumentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["document_number", "document_title", "file_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/documents/{entity_id}", response_model=DocumentsOut)
async def get_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DocumentsService(db).get(entity_id)

@router.post("/documents", response_model=DocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_documents(
    data: DocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentsService(db).create(data)

@router.put("/documents/{entity_id}", response_model=DocumentsOut)
async def update_documents(
    entity_id: uuid.UUID,
    data: DocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DocumentsService(db).update(entity_id, data)

@router.delete("/documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DocumentsService(db).delete(entity_id)

@router.get("/driver_certifications", response_model=PaginatedResponse[DriverCertificationsOut])
async def list_driver_certifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DriverCertificationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["certification_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/driver_certifications/{entity_id}", response_model=DriverCertificationsOut)
async def get_driver_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DriverCertificationsService(db).get(entity_id)

@router.post("/driver_certifications", response_model=DriverCertificationsOut, status_code=status.HTTP_201_CREATED)
async def create_driver_certifications(
    data: DriverCertificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverCertificationsService(db).create(data)

@router.put("/driver_certifications/{entity_id}", response_model=DriverCertificationsOut)
async def update_driver_certifications(
    entity_id: uuid.UUID,
    data: DriverCertificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverCertificationsService(db).update(entity_id, data)

@router.delete("/driver_certifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver_certifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DriverCertificationsService(db).delete(entity_id)

@router.get("/driver_hos", response_model=PaginatedResponse[DriverHosOut])
async def list_driver_hos(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DriverHosService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/driver_hos/{entity_id}", response_model=DriverHosOut)
async def get_driver_hos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DriverHosService(db).get(entity_id)

@router.post("/driver_hos", response_model=DriverHosOut, status_code=status.HTTP_201_CREATED)
async def create_driver_hos(
    data: DriverHosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverHosService(db).create(data)

@router.put("/driver_hos/{entity_id}", response_model=DriverHosOut)
async def update_driver_hos(
    entity_id: uuid.UUID,
    data: DriverHosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverHosService(db).update(entity_id, data)

@router.delete("/driver_hos/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver_hos(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DriverHosService(db).delete(entity_id)

@router.get("/driver_payroll", response_model=PaginatedResponse[DriverPayrollOut])
async def list_driver_payroll(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DriverPayrollService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/driver_payroll/{entity_id}", response_model=DriverPayrollOut)
async def get_driver_payroll(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DriverPayrollService(db).get(entity_id)

@router.post("/driver_payroll", response_model=DriverPayrollOut, status_code=status.HTTP_201_CREATED)
async def create_driver_payroll(
    data: DriverPayrollCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverPayrollService(db).create(data)

@router.put("/driver_payroll/{entity_id}", response_model=DriverPayrollOut)
async def update_driver_payroll(
    entity_id: uuid.UUID,
    data: DriverPayrollUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverPayrollService(db).update(entity_id, data)

@router.delete("/driver_payroll/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver_payroll(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DriverPayrollService(db).delete(entity_id)

@router.get("/driver_training", response_model=PaginatedResponse[DriverTrainingOut])
async def list_driver_training(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DriverTrainingService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["training_name", "certificate_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/driver_training/{entity_id}", response_model=DriverTrainingOut)
async def get_driver_training(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DriverTrainingService(db).get(entity_id)

@router.post("/driver_training", response_model=DriverTrainingOut, status_code=status.HTTP_201_CREATED)
async def create_driver_training(
    data: DriverTrainingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverTrainingService(db).create(data)

@router.put("/driver_training/{entity_id}", response_model=DriverTrainingOut)
async def update_driver_training(
    entity_id: uuid.UUID,
    data: DriverTrainingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriverTrainingService(db).update(entity_id, data)

@router.delete("/driver_training/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver_training(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DriverTrainingService(db).delete(entity_id)

@router.get("/drivers", response_model=PaginatedResponse[DriversOut])
async def list_drivers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = DriversService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["driver_code", "first_name", "last_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/drivers/{entity_id}", response_model=DriversOut)
async def get_drivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await DriversService(db).get(entity_id)

@router.post("/drivers", response_model=DriversOut, status_code=status.HTTP_201_CREATED)
async def create_drivers(
    data: DriversCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriversService(db).create(data)

@router.put("/drivers/{entity_id}", response_model=DriversOut)
async def update_drivers(
    entity_id: uuid.UUID,
    data: DriversUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await DriversService(db).update(entity_id, data)

@router.delete("/drivers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_drivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await DriversService(db).delete(entity_id)

@router.get("/equipment", response_model=PaginatedResponse[EquipmentOut])
async def list_equipment(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = EquipmentService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["asset_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/equipment/{entity_id}", response_model=EquipmentOut)
async def get_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await EquipmentService(db).get(entity_id)

@router.post("/equipment", response_model=EquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_equipment(
    data: EquipmentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentService(db).create(data)

@router.put("/equipment/{entity_id}", response_model=EquipmentOut)
async def update_equipment(
    entity_id: uuid.UUID,
    data: EquipmentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentService(db).update(entity_id, data)

@router.delete("/equipment/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await EquipmentService(db).delete(entity_id)

@router.get("/equipment_assignments", response_model=PaginatedResponse[EquipmentAssignmentsOut])
async def list_equipment_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = EquipmentAssignmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/equipment_assignments/{entity_id}", response_model=EquipmentAssignmentsOut)
async def get_equipment_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await EquipmentAssignmentsService(db).get(entity_id)

@router.post("/equipment_assignments", response_model=EquipmentAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_equipment_assignments(
    data: EquipmentAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentAssignmentsService(db).create(data)

@router.put("/equipment_assignments/{entity_id}", response_model=EquipmentAssignmentsOut)
async def update_equipment_assignments(
    entity_id: uuid.UUID,
    data: EquipmentAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentAssignmentsService(db).update(entity_id, data)

@router.delete("/equipment_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await EquipmentAssignmentsService(db).delete(entity_id)

@router.get("/equipment_tracking_devices", response_model=PaginatedResponse[EquipmentTrackingDevicesOut])
async def list_equipment_tracking_devices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = EquipmentTrackingDevicesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/equipment_tracking_devices/{entity_id}", response_model=EquipmentTrackingDevicesOut)
async def get_equipment_tracking_devices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await EquipmentTrackingDevicesService(db).get(entity_id)

@router.post("/equipment_tracking_devices", response_model=EquipmentTrackingDevicesOut, status_code=status.HTTP_201_CREATED)
async def create_equipment_tracking_devices(
    data: EquipmentTrackingDevicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentTrackingDevicesService(db).create(data)

@router.put("/equipment_tracking_devices/{entity_id}", response_model=EquipmentTrackingDevicesOut)
async def update_equipment_tracking_devices(
    entity_id: uuid.UUID,
    data: EquipmentTrackingDevicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentTrackingDevicesService(db).update(entity_id, data)

@router.delete("/equipment_tracking_devices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment_tracking_devices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await EquipmentTrackingDevicesService(db).delete(entity_id)

@router.get("/equipment_types", response_model=PaginatedResponse[EquipmentTypesOut])
async def list_equipment_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = EquipmentTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["equipment_type_code", "equipment_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/equipment_types/{entity_id}", response_model=EquipmentTypesOut)
async def get_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await EquipmentTypesService(db).get(entity_id)

@router.post("/equipment_types", response_model=EquipmentTypesOut, status_code=status.HTTP_201_CREATED)
async def create_equipment_types(
    data: EquipmentTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentTypesService(db).create(data)

@router.put("/equipment_types/{entity_id}", response_model=EquipmentTypesOut)
async def update_equipment_types(
    entity_id: uuid.UUID,
    data: EquipmentTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await EquipmentTypesService(db).update(entity_id, data)

@router.delete("/equipment_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await EquipmentTypesService(db).delete(entity_id)

@router.get("/freight_audit", response_model=PaginatedResponse[FreightAuditOut])
async def list_freight_audit(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightAuditService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_audit/{entity_id}", response_model=FreightAuditOut)
async def get_freight_audit(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightAuditService(db).get(entity_id)

@router.post("/freight_audit", response_model=FreightAuditOut, status_code=status.HTTP_201_CREATED)
async def create_freight_audit(
    data: FreightAuditCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightAuditService(db).create(data)

@router.put("/freight_audit/{entity_id}", response_model=FreightAuditOut)
async def update_freight_audit(
    entity_id: uuid.UUID,
    data: FreightAuditUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightAuditService(db).update(entity_id, data)

@router.delete("/freight_audit/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_audit(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightAuditService(db).delete(entity_id)

@router.get("/freight_cost_allocations", response_model=PaginatedResponse[FreightCostAllocationsOut])
async def list_freight_cost_allocations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightCostAllocationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_cost_allocations/{entity_id}", response_model=FreightCostAllocationsOut)
async def get_freight_cost_allocations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightCostAllocationsService(db).get(entity_id)

@router.post("/freight_cost_allocations", response_model=FreightCostAllocationsOut, status_code=status.HTTP_201_CREATED)
async def create_freight_cost_allocations(
    data: FreightCostAllocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostAllocationsService(db).create(data)

@router.put("/freight_cost_allocations/{entity_id}", response_model=FreightCostAllocationsOut)
async def update_freight_cost_allocations(
    entity_id: uuid.UUID,
    data: FreightCostAllocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostAllocationsService(db).update(entity_id, data)

@router.delete("/freight_cost_allocations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_cost_allocations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightCostAllocationsService(db).delete(entity_id)

@router.get("/freight_cost_lines", response_model=PaginatedResponse[FreightCostLinesOut])
async def list_freight_cost_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightCostLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["charge_code", "charge_description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_cost_lines/{entity_id}", response_model=FreightCostLinesOut)
async def get_freight_cost_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightCostLinesService(db).get(entity_id)

@router.post("/freight_cost_lines", response_model=FreightCostLinesOut, status_code=status.HTTP_201_CREATED)
async def create_freight_cost_lines(
    data: FreightCostLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostLinesService(db).create(data)

@router.put("/freight_cost_lines/{entity_id}", response_model=FreightCostLinesOut)
async def update_freight_cost_lines(
    entity_id: uuid.UUID,
    data: FreightCostLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostLinesService(db).update(entity_id, data)

@router.delete("/freight_cost_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_cost_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightCostLinesService(db).delete(entity_id)

@router.get("/freight_costs", response_model=PaginatedResponse[FreightCostsOut])
async def list_freight_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["description", "reference_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_costs/{entity_id}", response_model=FreightCostsOut)
async def get_freight_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightCostsService(db).get(entity_id)

@router.post("/freight_costs", response_model=FreightCostsOut, status_code=status.HTTP_201_CREATED)
async def create_freight_costs(
    data: FreightCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostsService(db).create(data)

@router.put("/freight_costs/{entity_id}", response_model=FreightCostsOut)
async def update_freight_costs(
    entity_id: uuid.UUID,
    data: FreightCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightCostsService(db).update(entity_id, data)

@router.delete("/freight_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightCostsService(db).delete(entity_id)

@router.get("/freight_invoice_lines", response_model=PaginatedResponse[FreightInvoiceLinesOut])
async def list_freight_invoice_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightInvoiceLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["description"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_invoice_lines/{entity_id}", response_model=FreightInvoiceLinesOut)
async def get_freight_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightInvoiceLinesService(db).get(entity_id)

@router.post("/freight_invoice_lines", response_model=FreightInvoiceLinesOut, status_code=status.HTTP_201_CREATED)
async def create_freight_invoice_lines(
    data: FreightInvoiceLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightInvoiceLinesService(db).create(data)

@router.put("/freight_invoice_lines/{entity_id}", response_model=FreightInvoiceLinesOut)
async def update_freight_invoice_lines(
    entity_id: uuid.UUID,
    data: FreightInvoiceLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightInvoiceLinesService(db).update(entity_id, data)

@router.delete("/freight_invoice_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightInvoiceLinesService(db).delete(entity_id)

@router.get("/freight_invoices", response_model=PaginatedResponse[FreightInvoicesOut])
async def list_freight_invoices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FreightInvoicesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["invoice_number", "reference_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/freight_invoices/{entity_id}", response_model=FreightInvoicesOut)
async def get_freight_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FreightInvoicesService(db).get(entity_id)

@router.post("/freight_invoices", response_model=FreightInvoicesOut, status_code=status.HTTP_201_CREATED)
async def create_freight_invoices(
    data: FreightInvoicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightInvoicesService(db).create(data)

@router.put("/freight_invoices/{entity_id}", response_model=FreightInvoicesOut)
async def update_freight_invoices(
    entity_id: uuid.UUID,
    data: FreightInvoicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FreightInvoicesService(db).update(entity_id, data)

@router.delete("/freight_invoices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_freight_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FreightInvoicesService(db).delete(entity_id)

@router.get("/fuel_consumption", response_model=PaginatedResponse[FuelConsumptionOut])
async def list_fuel_consumption(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FuelConsumptionService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fuel_consumption/{entity_id}", response_model=FuelConsumptionOut)
async def get_fuel_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FuelConsumptionService(db).get(entity_id)

@router.post("/fuel_consumption", response_model=FuelConsumptionOut, status_code=status.HTTP_201_CREATED)
async def create_fuel_consumption(
    data: FuelConsumptionCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelConsumptionService(db).create(data)

@router.put("/fuel_consumption/{entity_id}", response_model=FuelConsumptionOut)
async def update_fuel_consumption(
    entity_id: uuid.UUID,
    data: FuelConsumptionUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelConsumptionService(db).update(entity_id, data)

@router.delete("/fuel_consumption/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel_consumption(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FuelConsumptionService(db).delete(entity_id)

@router.get("/fuel_surcharge_lines", response_model=PaginatedResponse[FuelSurchargeLinesOut])
async def list_fuel_surcharge_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FuelSurchargeLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/fuel_surcharge_lines/{entity_id}", response_model=FuelSurchargeLinesOut)
async def get_fuel_surcharge_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FuelSurchargeLinesService(db).get(entity_id)

@router.post("/fuel_surcharge_lines", response_model=FuelSurchargeLinesOut, status_code=status.HTTP_201_CREATED)
async def create_fuel_surcharge_lines(
    data: FuelSurchargeLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelSurchargeLinesService(db).create(data)

@router.put("/fuel_surcharge_lines/{entity_id}", response_model=FuelSurchargeLinesOut)
async def update_fuel_surcharge_lines(
    entity_id: uuid.UUID,
    data: FuelSurchargeLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelSurchargeLinesService(db).update(entity_id, data)

@router.delete("/fuel_surcharge_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel_surcharge_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FuelSurchargeLinesService(db).delete(entity_id)

@router.get("/fuel_surcharge_tables", response_model=PaginatedResponse[FuelSurchargeTablesOut])
async def list_fuel_surcharge_tables(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FuelSurchargeTablesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["table_code", "table_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fuel_surcharge_tables/{entity_id}", response_model=FuelSurchargeTablesOut)
async def get_fuel_surcharge_tables(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FuelSurchargeTablesService(db).get(entity_id)

@router.post("/fuel_surcharge_tables", response_model=FuelSurchargeTablesOut, status_code=status.HTTP_201_CREATED)
async def create_fuel_surcharge_tables(
    data: FuelSurchargeTablesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelSurchargeTablesService(db).create(data)

@router.put("/fuel_surcharge_tables/{entity_id}", response_model=FuelSurchargeTablesOut)
async def update_fuel_surcharge_tables(
    entity_id: uuid.UUID,
    data: FuelSurchargeTablesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelSurchargeTablesService(db).update(entity_id, data)

@router.delete("/fuel_surcharge_tables/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel_surcharge_tables(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FuelSurchargeTablesService(db).delete(entity_id)

@router.get("/fuel_transactions", response_model=PaginatedResponse[FuelTransactionsOut])
async def list_fuel_transactions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = FuelTransactionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["transaction_number", "location_name", "receipt_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fuel_transactions/{entity_id}", response_model=FuelTransactionsOut)
async def get_fuel_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await FuelTransactionsService(db).get(entity_id)

@router.post("/fuel_transactions", response_model=FuelTransactionsOut, status_code=status.HTTP_201_CREATED)
async def create_fuel_transactions(
    data: FuelTransactionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelTransactionsService(db).create(data)

@router.put("/fuel_transactions/{entity_id}", response_model=FuelTransactionsOut)
async def update_fuel_transactions(
    entity_id: uuid.UUID,
    data: FuelTransactionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await FuelTransactionsService(db).update(entity_id, data)

@router.delete("/fuel_transactions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await FuelTransactionsService(db).delete(entity_id)

@router.get("/geofence_events", response_model=PaginatedResponse[GeofenceEventsOut])
async def list_geofence_events(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = GeofenceEventsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["geofence_name", "facility_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/geofence_events/{entity_id}", response_model=GeofenceEventsOut)
async def get_geofence_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await GeofenceEventsService(db).get(entity_id)

@router.post("/geofence_events", response_model=GeofenceEventsOut, status_code=status.HTTP_201_CREATED)
async def create_geofence_events(
    data: GeofenceEventsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await GeofenceEventsService(db).create(data)

@router.put("/geofence_events/{entity_id}", response_model=GeofenceEventsOut)
async def update_geofence_events(
    entity_id: uuid.UUID,
    data: GeofenceEventsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await GeofenceEventsService(db).update(entity_id, data)

@router.delete("/geofence_events/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_geofence_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await GeofenceEventsService(db).delete(entity_id)

@router.get("/gps_pings", response_model=PaginatedResponse[GpsPingsOut])
async def list_gps_pings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = GpsPingsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/gps_pings/{entity_id}", response_model=GpsPingsOut)
async def get_gps_pings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await GpsPingsService(db).get(entity_id)

@router.post("/gps_pings", response_model=GpsPingsOut, status_code=status.HTTP_201_CREATED)
async def create_gps_pings(
    data: GpsPingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await GpsPingsService(db).create(data)

@router.put("/gps_pings/{entity_id}", response_model=GpsPingsOut)
async def update_gps_pings(
    entity_id: uuid.UUID,
    data: GpsPingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await GpsPingsService(db).update(entity_id, data)

@router.delete("/gps_pings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gps_pings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await GpsPingsService(db).delete(entity_id)

@router.get("/hazmat_classifications", response_model=PaginatedResponse[HazmatClassificationsOut])
async def list_hazmat_classifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = HazmatClassificationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["class_code", "class_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/hazmat_classifications/{entity_id}", response_model=HazmatClassificationsOut)
async def get_hazmat_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await HazmatClassificationsService(db).get(entity_id)

@router.post("/hazmat_classifications", response_model=HazmatClassificationsOut, status_code=status.HTTP_201_CREATED)
async def create_hazmat_classifications(
    data: HazmatClassificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatClassificationsService(db).create(data)

@router.put("/hazmat_classifications/{entity_id}", response_model=HazmatClassificationsOut)
async def update_hazmat_classifications(
    entity_id: uuid.UUID,
    data: HazmatClassificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatClassificationsService(db).update(entity_id, data)

@router.delete("/hazmat_classifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hazmat_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await HazmatClassificationsService(db).delete(entity_id)

@router.get("/hazmat_incidents", response_model=PaginatedResponse[HazmatIncidentsOut])
async def list_hazmat_incidents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = HazmatIncidentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["incident_number", "un_number", "authority_report_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/hazmat_incidents/{entity_id}", response_model=HazmatIncidentsOut)
async def get_hazmat_incidents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await HazmatIncidentsService(db).get(entity_id)

@router.post("/hazmat_incidents", response_model=HazmatIncidentsOut, status_code=status.HTTP_201_CREATED)
async def create_hazmat_incidents(
    data: HazmatIncidentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatIncidentsService(db).create(data)

@router.put("/hazmat_incidents/{entity_id}", response_model=HazmatIncidentsOut)
async def update_hazmat_incidents(
    entity_id: uuid.UUID,
    data: HazmatIncidentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatIncidentsService(db).update(entity_id, data)

@router.delete("/hazmat_incidents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hazmat_incidents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await HazmatIncidentsService(db).delete(entity_id)

@router.get("/hazmat_packaging", response_model=PaginatedResponse[HazmatPackagingOut])
async def list_hazmat_packaging(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = HazmatPackagingService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["un_number", "labeling_required"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/hazmat_packaging/{entity_id}", response_model=HazmatPackagingOut)
async def get_hazmat_packaging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await HazmatPackagingService(db).get(entity_id)

@router.post("/hazmat_packaging", response_model=HazmatPackagingOut, status_code=status.HTTP_201_CREATED)
async def create_hazmat_packaging(
    data: HazmatPackagingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatPackagingService(db).create(data)

@router.put("/hazmat_packaging/{entity_id}", response_model=HazmatPackagingOut)
async def update_hazmat_packaging(
    entity_id: uuid.UUID,
    data: HazmatPackagingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatPackagingService(db).update(entity_id, data)

@router.delete("/hazmat_packaging/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hazmat_packaging(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await HazmatPackagingService(db).delete(entity_id)

@router.get("/hazmat_segregation", response_model=PaginatedResponse[HazmatSegregationOut])
async def list_hazmat_segregation(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = HazmatSegregationService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/hazmat_segregation/{entity_id}", response_model=HazmatSegregationOut)
async def get_hazmat_segregation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await HazmatSegregationService(db).get(entity_id)

@router.post("/hazmat_segregation", response_model=HazmatSegregationOut, status_code=status.HTTP_201_CREATED)
async def create_hazmat_segregation(
    data: HazmatSegregationCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatSegregationService(db).create(data)

@router.put("/hazmat_segregation/{entity_id}", response_model=HazmatSegregationOut)
async def update_hazmat_segregation(
    entity_id: uuid.UUID,
    data: HazmatSegregationUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HazmatSegregationService(db).update(entity_id, data)

@router.delete("/hazmat_segregation/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hazmat_segregation(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await HazmatSegregationService(db).delete(entity_id)

@router.get("/hs_codes", response_model=PaginatedResponse[HsCodesOut])
async def list_hs_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = HsCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["hs_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/hs_codes/{entity_id}", response_model=HsCodesOut)
async def get_hs_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await HsCodesService(db).get(entity_id)

@router.post("/hs_codes", response_model=HsCodesOut, status_code=status.HTTP_201_CREATED)
async def create_hs_codes(
    data: HsCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HsCodesService(db).create(data)

@router.put("/hs_codes/{entity_id}", response_model=HsCodesOut)
async def update_hs_codes(
    entity_id: uuid.UUID,
    data: HsCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await HsCodesService(db).update(entity_id, data)

@router.delete("/hs_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hs_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await HsCodesService(db).delete(entity_id)

@router.get("/incoterms", response_model=PaginatedResponse[IncotermsOut])
async def list_incoterms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = IncotermsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["incoterm_code", "incoterm_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/incoterms/{entity_id}", response_model=IncotermsOut)
async def get_incoterms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await IncotermsService(db).get(entity_id)

@router.post("/incoterms", response_model=IncotermsOut, status_code=status.HTTP_201_CREATED)
async def create_incoterms(
    data: IncotermsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await IncotermsService(db).create(data)

@router.put("/incoterms/{entity_id}", response_model=IncotermsOut)
async def update_incoterms(
    entity_id: uuid.UUID,
    data: IncotermsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await IncotermsService(db).update(entity_id, data)

@router.delete("/incoterms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_incoterms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await IncotermsService(db).delete(entity_id)

@router.get("/insurance_policies", response_model=PaginatedResponse[InsurancePoliciesOut])
async def list_insurance_policies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = InsurancePoliciesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["policy_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/insurance_policies/{entity_id}", response_model=InsurancePoliciesOut)
async def get_insurance_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await InsurancePoliciesService(db).get(entity_id)

@router.post("/insurance_policies", response_model=InsurancePoliciesOut, status_code=status.HTTP_201_CREATED)
async def create_insurance_policies(
    data: InsurancePoliciesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InsurancePoliciesService(db).create(data)

@router.put("/insurance_policies/{entity_id}", response_model=InsurancePoliciesOut)
async def update_insurance_policies(
    entity_id: uuid.UUID,
    data: InsurancePoliciesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InsurancePoliciesService(db).update(entity_id, data)

@router.delete("/insurance_policies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_insurance_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await InsurancePoliciesService(db).delete(entity_id)

@router.get("/interface_error_log", response_model=PaginatedResponse[InterfaceErrorLogOut])
async def list_interface_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = InterfaceErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/interface_error_log/{entity_id}", response_model=InterfaceErrorLogOut)
async def get_interface_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await InterfaceErrorLogService(db).get(entity_id)

@router.post("/interface_error_log", response_model=InterfaceErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_interface_error_log(
    data: InterfaceErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InterfaceErrorLogService(db).create(data)

@router.put("/interface_error_log/{entity_id}", response_model=InterfaceErrorLogOut)
async def update_interface_error_log(
    entity_id: uuid.UUID,
    data: InterfaceErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InterfaceErrorLogService(db).update(entity_id, data)

@router.delete("/interface_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_interface_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await InterfaceErrorLogService(db).delete(entity_id)

@router.get("/interface_shipment_import", response_model=PaginatedResponse[InterfaceShipmentImportOut])
async def list_interface_shipment_import(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = InterfaceShipmentImportService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/interface_shipment_import/{entity_id}", response_model=InterfaceShipmentImportOut)
async def get_interface_shipment_import(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await InterfaceShipmentImportService(db).get(entity_id)

@router.post("/interface_shipment_import", response_model=InterfaceShipmentImportOut, status_code=status.HTTP_201_CREATED)
async def create_interface_shipment_import(
    data: InterfaceShipmentImportCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InterfaceShipmentImportService(db).create(data)

@router.put("/interface_shipment_import/{entity_id}", response_model=InterfaceShipmentImportOut)
async def update_interface_shipment_import(
    entity_id: uuid.UUID,
    data: InterfaceShipmentImportUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await InterfaceShipmentImportService(db).update(entity_id, data)

@router.delete("/interface_shipment_import/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_interface_shipment_import(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await InterfaceShipmentImportService(db).delete(entity_id)

@router.get("/kpi_definitions", response_model=PaginatedResponse[KpiDefinitionsOut])
async def list_kpi_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = KpiDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["kpi_code", "kpi_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/kpi_definitions/{entity_id}", response_model=KpiDefinitionsOut)
async def get_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await KpiDefinitionsService(db).get(entity_id)

@router.post("/kpi_definitions", response_model=KpiDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_kpi_definitions(
    data: KpiDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await KpiDefinitionsService(db).create(data)

@router.put("/kpi_definitions/{entity_id}", response_model=KpiDefinitionsOut)
async def update_kpi_definitions(
    entity_id: uuid.UUID,
    data: KpiDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await KpiDefinitionsService(db).update(entity_id, data)

@router.delete("/kpi_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_kpi_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await KpiDefinitionsService(db).delete(entity_id)

@router.get("/kpi_values", response_model=PaginatedResponse[KpiValuesOut])
async def list_kpi_values(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = KpiValuesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/kpi_values/{entity_id}", response_model=KpiValuesOut)
async def get_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await KpiValuesService(db).get(entity_id)

@router.post("/kpi_values", response_model=KpiValuesOut, status_code=status.HTTP_201_CREATED)
async def create_kpi_values(
    data: KpiValuesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await KpiValuesService(db).create(data)

@router.put("/kpi_values/{entity_id}", response_model=KpiValuesOut)
async def update_kpi_values(
    entity_id: uuid.UUID,
    data: KpiValuesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await KpiValuesService(db).update(entity_id, data)

@router.delete("/kpi_values/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_kpi_values(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await KpiValuesService(db).delete(entity_id)

@router.get("/lane_carriers", response_model=PaginatedResponse[LaneCarriersOut])
async def list_lane_carriers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LaneCarriersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/lane_carriers/{entity_id}", response_model=LaneCarriersOut)
async def get_lane_carriers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LaneCarriersService(db).get(entity_id)

@router.post("/lane_carriers", response_model=LaneCarriersOut, status_code=status.HTTP_201_CREATED)
async def create_lane_carriers(
    data: LaneCarriersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LaneCarriersService(db).create(data)

@router.put("/lane_carriers/{entity_id}", response_model=LaneCarriersOut)
async def update_lane_carriers(
    entity_id: uuid.UUID,
    data: LaneCarriersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LaneCarriersService(db).update(entity_id, data)

@router.delete("/lane_carriers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lane_carriers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LaneCarriersService(db).delete(entity_id)

@router.get("/lane_performance", response_model=PaginatedResponse[LanePerformanceOut])
async def list_lane_performance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LanePerformanceService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/lane_performance/{entity_id}", response_model=LanePerformanceOut)
async def get_lane_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LanePerformanceService(db).get(entity_id)

@router.post("/lane_performance", response_model=LanePerformanceOut, status_code=status.HTTP_201_CREATED)
async def create_lane_performance(
    data: LanePerformanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LanePerformanceService(db).create(data)

@router.put("/lane_performance/{entity_id}", response_model=LanePerformanceOut)
async def update_lane_performance(
    entity_id: uuid.UUID,
    data: LanePerformanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LanePerformanceService(db).update(entity_id, data)

@router.delete("/lane_performance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lane_performance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LanePerformanceService(db).delete(entity_id)

@router.get("/lanes", response_model=PaginatedResponse[LanesOut])
async def list_lanes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LanesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["lane_code", "lane_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/lanes/{entity_id}", response_model=LanesOut)
async def get_lanes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LanesService(db).get(entity_id)

@router.post("/lanes", response_model=LanesOut, status_code=status.HTTP_201_CREATED)
async def create_lanes(
    data: LanesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LanesService(db).create(data)

@router.put("/lanes/{entity_id}", response_model=LanesOut)
async def update_lanes(
    entity_id: uuid.UUID,
    data: LanesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LanesService(db).update(entity_id, data)

@router.delete("/lanes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lanes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LanesService(db).delete(entity_id)

@router.get("/load_costs", response_model=PaginatedResponse[LoadCostsOut])
async def list_load_costs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LoadCostsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["description", "reference_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/load_costs/{entity_id}", response_model=LoadCostsOut)
async def get_load_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LoadCostsService(db).get(entity_id)

@router.post("/load_costs", response_model=LoadCostsOut, status_code=status.HTTP_201_CREATED)
async def create_load_costs(
    data: LoadCostsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadCostsService(db).create(data)

@router.put("/load_costs/{entity_id}", response_model=LoadCostsOut)
async def update_load_costs(
    entity_id: uuid.UUID,
    data: LoadCostsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadCostsService(db).update(entity_id, data)

@router.delete("/load_costs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_load_costs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LoadCostsService(db).delete(entity_id)

@router.get("/load_legs", response_model=PaginatedResponse[LoadLegsOut])
async def list_load_legs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LoadLegsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/load_legs/{entity_id}", response_model=LoadLegsOut)
async def get_load_legs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LoadLegsService(db).get(entity_id)

@router.post("/load_legs", response_model=LoadLegsOut, status_code=status.HTTP_201_CREATED)
async def create_load_legs(
    data: LoadLegsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadLegsService(db).create(data)

@router.put("/load_legs/{entity_id}", response_model=LoadLegsOut)
async def update_load_legs(
    entity_id: uuid.UUID,
    data: LoadLegsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadLegsService(db).update(entity_id, data)

@router.delete("/load_legs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_load_legs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LoadLegsService(db).delete(entity_id)

@router.get("/load_lines", response_model=PaginatedResponse[LoadLinesOut])
async def list_load_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LoadLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/load_lines/{entity_id}", response_model=LoadLinesOut)
async def get_load_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LoadLinesService(db).get(entity_id)

@router.post("/load_lines", response_model=LoadLinesOut, status_code=status.HTTP_201_CREATED)
async def create_load_lines(
    data: LoadLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadLinesService(db).create(data)

@router.put("/load_lines/{entity_id}", response_model=LoadLinesOut)
async def update_load_lines(
    entity_id: uuid.UUID,
    data: LoadLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadLinesService(db).update(entity_id, data)

@router.delete("/load_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_load_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LoadLinesService(db).delete(entity_id)

@router.get("/load_stops", response_model=PaginatedResponse[LoadStopsOut])
async def list_load_stops(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LoadStopsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["location_name", "postal_code", "contact_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/load_stops/{entity_id}", response_model=LoadStopsOut)
async def get_load_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LoadStopsService(db).get(entity_id)

@router.post("/load_stops", response_model=LoadStopsOut, status_code=status.HTTP_201_CREATED)
async def create_load_stops(
    data: LoadStopsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadStopsService(db).create(data)

@router.put("/load_stops/{entity_id}", response_model=LoadStopsOut)
async def update_load_stops(
    entity_id: uuid.UUID,
    data: LoadStopsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadStopsService(db).update(entity_id, data)

@router.delete("/load_stops/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_load_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LoadStopsService(db).delete(entity_id)

@router.get("/loads", response_model=PaginatedResponse[LoadsOut])
async def list_loads(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = LoadsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["load_number", "bol_number", "po_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/loads/{entity_id}", response_model=LoadsOut)
async def get_loads(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await LoadsService(db).get(entity_id)

@router.post("/loads", response_model=LoadsOut, status_code=status.HTTP_201_CREATED)
async def create_loads(
    data: LoadsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadsService(db).create(data)

@router.put("/loads/{entity_id}", response_model=LoadsOut)
async def update_loads(
    entity_id: uuid.UUID,
    data: LoadsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await LoadsService(db).update(entity_id, data)

@router.delete("/loads/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_loads(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await LoadsService(db).delete(entity_id)

@router.get("/milestone_achievements", response_model=PaginatedResponse[MilestoneAchievementsOut])
async def list_milestone_achievements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = MilestoneAchievementsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/milestone_achievements/{entity_id}", response_model=MilestoneAchievementsOut)
async def get_milestone_achievements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await MilestoneAchievementsService(db).get(entity_id)

@router.post("/milestone_achievements", response_model=MilestoneAchievementsOut, status_code=status.HTTP_201_CREATED)
async def create_milestone_achievements(
    data: MilestoneAchievementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await MilestoneAchievementsService(db).create(data)

@router.put("/milestone_achievements/{entity_id}", response_model=MilestoneAchievementsOut)
async def update_milestone_achievements(
    entity_id: uuid.UUID,
    data: MilestoneAchievementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await MilestoneAchievementsService(db).update(entity_id, data)

@router.delete("/milestone_achievements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_milestone_achievements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await MilestoneAchievementsService(db).delete(entity_id)

@router.get("/milestones", response_model=PaginatedResponse[MilestonesOut])
async def list_milestones(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = MilestonesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["milestone_code", "milestone_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/milestones/{entity_id}", response_model=MilestonesOut)
async def get_milestones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await MilestonesService(db).get(entity_id)

@router.post("/milestones", response_model=MilestonesOut, status_code=status.HTTP_201_CREATED)
async def create_milestones(
    data: MilestonesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await MilestonesService(db).create(data)

@router.put("/milestones/{entity_id}", response_model=MilestonesOut)
async def update_milestones(
    entity_id: uuid.UUID,
    data: MilestonesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await MilestonesService(db).update(entity_id, data)

@router.delete("/milestones/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_milestones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await MilestonesService(db).delete(entity_id)

@router.get("/pickup_lines", response_model=PaginatedResponse[PickupLinesOut])
async def list_pickup_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = PickupLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/pickup_lines/{entity_id}", response_model=PickupLinesOut)
async def get_pickup_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await PickupLinesService(db).get(entity_id)

@router.post("/pickup_lines", response_model=PickupLinesOut, status_code=status.HTTP_201_CREATED)
async def create_pickup_lines(
    data: PickupLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PickupLinesService(db).create(data)

@router.put("/pickup_lines/{entity_id}", response_model=PickupLinesOut)
async def update_pickup_lines(
    entity_id: uuid.UUID,
    data: PickupLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PickupLinesService(db).update(entity_id, data)

@router.delete("/pickup_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pickup_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await PickupLinesService(db).delete(entity_id)

@router.get("/pickups", response_model=PaginatedResponse[PickupsOut])
async def list_pickups(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = PickupsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["pickup_number", "location_name", "postal_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/pickups/{entity_id}", response_model=PickupsOut)
async def get_pickups(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await PickupsService(db).get(entity_id)

@router.post("/pickups", response_model=PickupsOut, status_code=status.HTTP_201_CREATED)
async def create_pickups(
    data: PickupsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PickupsService(db).create(data)

@router.put("/pickups/{entity_id}", response_model=PickupsOut)
async def update_pickups(
    entity_id: uuid.UUID,
    data: PickupsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PickupsService(db).update(entity_id, data)

@router.delete("/pickups/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pickups(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await PickupsService(db).delete(entity_id)

@router.get("/pod", response_model=PaginatedResponse[PodOut])
async def list_pod(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = PodService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["pod_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/pod/{entity_id}", response_model=PodOut)
async def get_pod(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await PodService(db).get(entity_id)

@router.post("/pod", response_model=PodOut, status_code=status.HTTP_201_CREATED)
async def create_pod(
    data: PodCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PodService(db).create(data)

@router.put("/pod/{entity_id}", response_model=PodOut)
async def update_pod(
    entity_id: uuid.UUID,
    data: PodUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await PodService(db).update(entity_id, data)

@router.delete("/pod/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pod(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await PodService(db).delete(entity_id)

@router.get("/rate_chart_versions", response_model=PaginatedResponse[RateChartVersionsOut])
async def list_rate_chart_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RateChartVersionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["version_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/rate_chart_versions/{entity_id}", response_model=RateChartVersionsOut)
async def get_rate_chart_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RateChartVersionsService(db).get(entity_id)

@router.post("/rate_chart_versions", response_model=RateChartVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_rate_chart_versions(
    data: RateChartVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateChartVersionsService(db).create(data)

@router.put("/rate_chart_versions/{entity_id}", response_model=RateChartVersionsOut)
async def update_rate_chart_versions(
    entity_id: uuid.UUID,
    data: RateChartVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateChartVersionsService(db).update(entity_id, data)

@router.delete("/rate_chart_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rate_chart_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RateChartVersionsService(db).delete(entity_id)

@router.get("/rate_charts", response_model=PaginatedResponse[RateChartsOut])
async def list_rate_charts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RateChartsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["rate_chart_code", "rate_chart_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/rate_charts/{entity_id}", response_model=RateChartsOut)
async def get_rate_charts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RateChartsService(db).get(entity_id)

@router.post("/rate_charts", response_model=RateChartsOut, status_code=status.HTTP_201_CREATED)
async def create_rate_charts(
    data: RateChartsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateChartsService(db).create(data)

@router.put("/rate_charts/{entity_id}", response_model=RateChartsOut)
async def update_rate_charts(
    entity_id: uuid.UUID,
    data: RateChartsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateChartsService(db).update(entity_id, data)

@router.delete("/rate_charts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rate_charts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RateChartsService(db).delete(entity_id)

@router.get("/rate_lines", response_model=PaginatedResponse[RateLinesOut])
async def list_rate_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RateLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/rate_lines/{entity_id}", response_model=RateLinesOut)
async def get_rate_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RateLinesService(db).get(entity_id)

@router.post("/rate_lines", response_model=RateLinesOut, status_code=status.HTTP_201_CREATED)
async def create_rate_lines(
    data: RateLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateLinesService(db).create(data)

@router.put("/rate_lines/{entity_id}", response_model=RateLinesOut)
async def update_rate_lines(
    entity_id: uuid.UUID,
    data: RateLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateLinesService(db).update(entity_id, data)

@router.delete("/rate_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rate_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RateLinesService(db).delete(entity_id)

@router.get("/rate_zones", response_model=PaginatedResponse[RateZonesOut])
async def list_rate_zones(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RateZonesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["zone_code", "zone_name", "postal_code_start"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/rate_zones/{entity_id}", response_model=RateZonesOut)
async def get_rate_zones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RateZonesService(db).get(entity_id)

@router.post("/rate_zones", response_model=RateZonesOut, status_code=status.HTTP_201_CREATED)
async def create_rate_zones(
    data: RateZonesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateZonesService(db).create(data)

@router.put("/rate_zones/{entity_id}", response_model=RateZonesOut)
async def update_rate_zones(
    entity_id: uuid.UUID,
    data: RateZonesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RateZonesService(db).update(entity_id, data)

@router.delete("/rate_zones/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rate_zones(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RateZonesService(db).delete(entity_id)

@router.get("/route_alternatives", response_model=PaginatedResponse[RouteAlternativesOut])
async def list_route_alternatives(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RouteAlternativesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/route_alternatives/{entity_id}", response_model=RouteAlternativesOut)
async def get_route_alternatives(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RouteAlternativesService(db).get(entity_id)

@router.post("/route_alternatives", response_model=RouteAlternativesOut, status_code=status.HTTP_201_CREATED)
async def create_route_alternatives(
    data: RouteAlternativesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RouteAlternativesService(db).create(data)

@router.put("/route_alternatives/{entity_id}", response_model=RouteAlternativesOut)
async def update_route_alternatives(
    entity_id: uuid.UUID,
    data: RouteAlternativesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RouteAlternativesService(db).update(entity_id, data)

@router.delete("/route_alternatives/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_route_alternatives(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RouteAlternativesService(db).delete(entity_id)

@router.get("/route_stops", response_model=PaginatedResponse[RouteStopsOut])
async def list_route_stops(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RouteStopsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_name", "postal_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/route_stops/{entity_id}", response_model=RouteStopsOut)
async def get_route_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RouteStopsService(db).get(entity_id)

@router.post("/route_stops", response_model=RouteStopsOut, status_code=status.HTTP_201_CREATED)
async def create_route_stops(
    data: RouteStopsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RouteStopsService(db).create(data)

@router.put("/route_stops/{entity_id}", response_model=RouteStopsOut)
async def update_route_stops(
    entity_id: uuid.UUID,
    data: RouteStopsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RouteStopsService(db).update(entity_id, data)

@router.delete("/route_stops/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_route_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RouteStopsService(db).delete(entity_id)

@router.get("/routes", response_model=PaginatedResponse[RoutesOut])
async def list_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = RoutesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["route_code", "route_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/routes/{entity_id}", response_model=RoutesOut)
async def get_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await RoutesService(db).get(entity_id)

@router.post("/routes", response_model=RoutesOut, status_code=status.HTTP_201_CREATED)
async def create_routes(
    data: RoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RoutesService(db).create(data)

@router.put("/routes/{entity_id}", response_model=RoutesOut)
async def update_routes(
    entity_id: uuid.UUID,
    data: RoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await RoutesService(db).update(entity_id, data)

@router.delete("/routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await RoutesService(db).delete(entity_id)

@router.get("/shipment_appointments", response_model=PaginatedResponse[ShipmentAppointmentsOut])
async def list_shipment_appointments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentAppointmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["location_name", "postal_code", "contact_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_appointments/{entity_id}", response_model=ShipmentAppointmentsOut)
async def get_shipment_appointments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentAppointmentsService(db).get(entity_id)

@router.post("/shipment_appointments", response_model=ShipmentAppointmentsOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_appointments(
    data: ShipmentAppointmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentAppointmentsService(db).create(data)

@router.put("/shipment_appointments/{entity_id}", response_model=ShipmentAppointmentsOut)
async def update_shipment_appointments(
    entity_id: uuid.UUID,
    data: ShipmentAppointmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentAppointmentsService(db).update(entity_id, data)

@router.delete("/shipment_appointments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_appointments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentAppointmentsService(db).delete(entity_id)

@router.get("/shipment_lines", response_model=PaginatedResponse[ShipmentLinesOut])
async def list_shipment_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "nmfc_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_lines/{entity_id}", response_model=ShipmentLinesOut)
async def get_shipment_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentLinesService(db).get(entity_id)

@router.post("/shipment_lines", response_model=ShipmentLinesOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_lines(
    data: ShipmentLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentLinesService(db).create(data)

@router.put("/shipment_lines/{entity_id}", response_model=ShipmentLinesOut)
async def update_shipment_lines(
    entity_id: uuid.UUID,
    data: ShipmentLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentLinesService(db).update(entity_id, data)

@router.delete("/shipment_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentLinesService(db).delete(entity_id)

@router.get("/shipment_notes", response_model=PaginatedResponse[ShipmentNotesOut])
async def list_shipment_notes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentNotesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_notes/{entity_id}", response_model=ShipmentNotesOut)
async def get_shipment_notes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentNotesService(db).get(entity_id)

@router.post("/shipment_notes", response_model=ShipmentNotesOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_notes(
    data: ShipmentNotesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentNotesService(db).create(data)

@router.put("/shipment_notes/{entity_id}", response_model=ShipmentNotesOut)
async def update_shipment_notes(
    entity_id: uuid.UUID,
    data: ShipmentNotesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentNotesService(db).update(entity_id, data)

@router.delete("/shipment_notes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_notes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentNotesService(db).delete(entity_id)

@router.get("/shipment_statuses", response_model=PaginatedResponse[ShipmentStatusesOut])
async def list_shipment_statuses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentStatusesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["status_code", "status_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_statuses/{entity_id}", response_model=ShipmentStatusesOut)
async def get_shipment_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentStatusesService(db).get(entity_id)

@router.post("/shipment_statuses", response_model=ShipmentStatusesOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_statuses(
    data: ShipmentStatusesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentStatusesService(db).create(data)

@router.put("/shipment_statuses/{entity_id}", response_model=ShipmentStatusesOut)
async def update_shipment_statuses(
    entity_id: uuid.UUID,
    data: ShipmentStatusesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentStatusesService(db).update(entity_id, data)

@router.delete("/shipment_statuses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentStatusesService(db).delete(entity_id)

@router.get("/shipment_types", response_model=PaginatedResponse[ShipmentTypesOut])
async def list_shipment_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["shipment_type_code", "shipment_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipment_types/{entity_id}", response_model=ShipmentTypesOut)
async def get_shipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentTypesService(db).get(entity_id)

@router.post("/shipment_types", response_model=ShipmentTypesOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_types(
    data: ShipmentTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentTypesService(db).create(data)

@router.put("/shipment_types/{entity_id}", response_model=ShipmentTypesOut)
async def update_shipment_types(
    entity_id: uuid.UUID,
    data: ShipmentTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentTypesService(db).update(entity_id, data)

@router.delete("/shipment_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentTypesService(db).delete(entity_id)

@router.get("/shipments", response_model=PaginatedResponse[ShipmentsOut])
async def list_shipments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = ShipmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["shipment_number", "customer_name", "bol_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/shipments/{entity_id}", response_model=ShipmentsOut)
async def get_shipments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await ShipmentsService(db).get(entity_id)

@router.post("/shipments", response_model=ShipmentsOut, status_code=status.HTTP_201_CREATED)
async def create_shipments(
    data: ShipmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentsService(db).create(data)

@router.put("/shipments/{entity_id}", response_model=ShipmentsOut)
async def update_shipments(
    entity_id: uuid.UUID,
    data: ShipmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await ShipmentsService(db).update(entity_id, data)

@router.delete("/shipments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await ShipmentsService(db).delete(entity_id)

@router.get("/temperature_events", response_model=PaginatedResponse[TemperatureEventsOut])
async def list_temperature_events(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TemperatureEventsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/temperature_events/{entity_id}", response_model=TemperatureEventsOut)
async def get_temperature_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TemperatureEventsService(db).get(entity_id)

@router.post("/temperature_events", response_model=TemperatureEventsOut, status_code=status.HTTP_201_CREATED)
async def create_temperature_events(
    data: TemperatureEventsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TemperatureEventsService(db).create(data)

@router.put("/temperature_events/{entity_id}", response_model=TemperatureEventsOut)
async def update_temperature_events(
    entity_id: uuid.UUID,
    data: TemperatureEventsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TemperatureEventsService(db).update(entity_id, data)

@router.delete("/temperature_events/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_temperature_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TemperatureEventsService(db).delete(entity_id)

@router.get("/tender_cascade", response_model=PaginatedResponse[TenderCascadeOut])
async def list_tender_cascade(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TenderCascadeService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tender_cascade/{entity_id}", response_model=TenderCascadeOut)
async def get_tender_cascade(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TenderCascadeService(db).get(entity_id)

@router.post("/tender_cascade", response_model=TenderCascadeOut, status_code=status.HTTP_201_CREATED)
async def create_tender_cascade(
    data: TenderCascadeCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TenderCascadeService(db).create(data)

@router.put("/tender_cascade/{entity_id}", response_model=TenderCascadeOut)
async def update_tender_cascade(
    entity_id: uuid.UUID,
    data: TenderCascadeUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TenderCascadeService(db).update(entity_id, data)

@router.delete("/tender_cascade/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tender_cascade(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TenderCascadeService(db).delete(entity_id)

@router.get("/tender_responses", response_model=PaginatedResponse[TenderResponsesOut])
async def list_tender_responses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TenderResponsesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tender_responses/{entity_id}", response_model=TenderResponsesOut)
async def get_tender_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TenderResponsesService(db).get(entity_id)

@router.post("/tender_responses", response_model=TenderResponsesOut, status_code=status.HTTP_201_CREATED)
async def create_tender_responses(
    data: TenderResponsesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TenderResponsesService(db).create(data)

@router.put("/tender_responses/{entity_id}", response_model=TenderResponsesOut)
async def update_tender_responses(
    entity_id: uuid.UUID,
    data: TenderResponsesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TenderResponsesService(db).update(entity_id, data)

@router.delete("/tender_responses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tender_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TenderResponsesService(db).delete(entity_id)

@router.get("/tenders", response_model=PaginatedResponse[TendersOut])
async def list_tenders(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TendersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["tender_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tenders/{entity_id}", response_model=TendersOut)
async def get_tenders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TendersService(db).get(entity_id)

@router.post("/tenders", response_model=TendersOut, status_code=status.HTTP_201_CREATED)
async def create_tenders(
    data: TendersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TendersService(db).create(data)

@router.put("/tenders/{entity_id}", response_model=TendersOut)
async def update_tenders(
    entity_id: uuid.UUID,
    data: TendersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TendersService(db).update(entity_id, data)

@router.delete("/tenders/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tenders(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TendersService(db).delete(entity_id)

@router.get("/tracking_events", response_model=PaginatedResponse[TrackingEventsOut])
async def list_tracking_events(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TrackingEventsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["event_code", "event_name", "location_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tracking_events/{entity_id}", response_model=TrackingEventsOut)
async def get_tracking_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TrackingEventsService(db).get(entity_id)

@router.post("/tracking_events", response_model=TrackingEventsOut, status_code=status.HTTP_201_CREATED)
async def create_tracking_events(
    data: TrackingEventsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TrackingEventsService(db).create(data)

@router.put("/tracking_events/{entity_id}", response_model=TrackingEventsOut)
async def update_tracking_events(
    entity_id: uuid.UUID,
    data: TrackingEventsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TrackingEventsService(db).update(entity_id, data)

@router.delete("/tracking_events/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tracking_events(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TrackingEventsService(db).delete(entity_id)

@router.get("/trip_stops", response_model=PaginatedResponse[TripStopsOut])
async def list_trip_stops(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TripStopsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["location_name", "postal_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/trip_stops/{entity_id}", response_model=TripStopsOut)
async def get_trip_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TripStopsService(db).get(entity_id)

@router.post("/trip_stops", response_model=TripStopsOut, status_code=status.HTTP_201_CREATED)
async def create_trip_stops(
    data: TripStopsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TripStopsService(db).create(data)

@router.put("/trip_stops/{entity_id}", response_model=TripStopsOut)
async def update_trip_stops(
    entity_id: uuid.UUID,
    data: TripStopsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TripStopsService(db).update(entity_id, data)

@router.delete("/trip_stops/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trip_stops(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TripStopsService(db).delete(entity_id)

@router.get("/trips", response_model=PaginatedResponse[TripsOut])
async def list_trips(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = TripsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["trip_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/trips/{entity_id}", response_model=TripsOut)
async def get_trips(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await TripsService(db).get(entity_id)

@router.post("/trips", response_model=TripsOut, status_code=status.HTTP_201_CREATED)
async def create_trips(
    data: TripsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TripsService(db).create(data)

@router.put("/trips/{entity_id}", response_model=TripsOut)
async def update_trips(
    entity_id: uuid.UUID,
    data: TripsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await TripsService(db).update(entity_id, data)

@router.delete("/trips/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trips(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await TripsService(db).delete(entity_id)

@router.get("/vehicle_assignments", response_model=PaginatedResponse[VehicleAssignmentsOut])
async def list_vehicle_assignments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = VehicleAssignmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/vehicle_assignments/{entity_id}", response_model=VehicleAssignmentsOut)
async def get_vehicle_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await VehicleAssignmentsService(db).get(entity_id)

@router.post("/vehicle_assignments", response_model=VehicleAssignmentsOut, status_code=status.HTTP_201_CREATED)
async def create_vehicle_assignments(
    data: VehicleAssignmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleAssignmentsService(db).create(data)

@router.put("/vehicle_assignments/{entity_id}", response_model=VehicleAssignmentsOut)
async def update_vehicle_assignments(
    entity_id: uuid.UUID,
    data: VehicleAssignmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleAssignmentsService(db).update(entity_id, data)

@router.delete("/vehicle_assignments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle_assignments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await VehicleAssignmentsService(db).delete(entity_id)

@router.get("/vehicle_inspections", response_model=PaginatedResponse[VehicleInspectionsOut])
async def list_vehicle_inspections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = VehicleInspectionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["inspector_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/vehicle_inspections/{entity_id}", response_model=VehicleInspectionsOut)
async def get_vehicle_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await VehicleInspectionsService(db).get(entity_id)

@router.post("/vehicle_inspections", response_model=VehicleInspectionsOut, status_code=status.HTTP_201_CREATED)
async def create_vehicle_inspections(
    data: VehicleInspectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleInspectionsService(db).create(data)

@router.put("/vehicle_inspections/{entity_id}", response_model=VehicleInspectionsOut)
async def update_vehicle_inspections(
    entity_id: uuid.UUID,
    data: VehicleInspectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleInspectionsService(db).update(entity_id, data)

@router.delete("/vehicle_inspections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle_inspections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await VehicleInspectionsService(db).delete(entity_id)

@router.get("/vehicle_maintenance", response_model=PaginatedResponse[VehicleMaintenanceOut])
async def list_vehicle_maintenance(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = VehicleMaintenanceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["work_order_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/vehicle_maintenance/{entity_id}", response_model=VehicleMaintenanceOut)
async def get_vehicle_maintenance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await VehicleMaintenanceService(db).get(entity_id)

@router.post("/vehicle_maintenance", response_model=VehicleMaintenanceOut, status_code=status.HTTP_201_CREATED)
async def create_vehicle_maintenance(
    data: VehicleMaintenanceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleMaintenanceService(db).create(data)

@router.put("/vehicle_maintenance/{entity_id}", response_model=VehicleMaintenanceOut)
async def update_vehicle_maintenance(
    entity_id: uuid.UUID,
    data: VehicleMaintenanceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleMaintenanceService(db).update(entity_id, data)

@router.delete("/vehicle_maintenance/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle_maintenance(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await VehicleMaintenanceService(db).delete(entity_id)

@router.get("/vehicle_types", response_model=PaginatedResponse[VehicleTypesOut])
async def list_vehicle_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = VehicleTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["vehicle_type_code", "vehicle_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/vehicle_types/{entity_id}", response_model=VehicleTypesOut)
async def get_vehicle_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await VehicleTypesService(db).get(entity_id)

@router.post("/vehicle_types", response_model=VehicleTypesOut, status_code=status.HTTP_201_CREATED)
async def create_vehicle_types(
    data: VehicleTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleTypesService(db).create(data)

@router.put("/vehicle_types/{entity_id}", response_model=VehicleTypesOut)
async def update_vehicle_types(
    entity_id: uuid.UUID,
    data: VehicleTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehicleTypesService(db).update(entity_id, data)

@router.delete("/vehicle_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await VehicleTypesService(db).delete(entity_id)

@router.get("/vehicles", response_model=PaginatedResponse[VehiclesOut])
async def list_vehicles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = VehiclesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["vehicle_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/vehicles/{entity_id}", response_model=VehiclesOut)
async def get_vehicles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await VehiclesService(db).get(entity_id)

@router.post("/vehicles", response_model=VehiclesOut, status_code=status.HTTP_201_CREATED)
async def create_vehicles(
    data: VehiclesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehiclesService(db).create(data)

@router.put("/vehicles/{entity_id}", response_model=VehiclesOut)
async def update_vehicles(
    entity_id: uuid.UUID,
    data: VehiclesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await VehiclesService(db).update(entity_id, data)

@router.delete("/vehicles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await VehiclesService(db).delete(entity_id)

@router.get("/workflow_approval_hierarchies", response_model=PaginatedResponse[WorkflowApprovalHierarchiesOut])
async def list_workflow_approval_hierarchies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = WorkflowApprovalHierarchiesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_approval_hierarchies/{entity_id}", response_model=WorkflowApprovalHierarchiesOut)
async def get_workflow_approval_hierarchies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await WorkflowApprovalHierarchiesService(db).get(entity_id)

@router.post("/workflow_approval_hierarchies", response_model=WorkflowApprovalHierarchiesOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_approval_hierarchies(
    data: WorkflowApprovalHierarchiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowApprovalHierarchiesService(db).create(data)

@router.put("/workflow_approval_hierarchies/{entity_id}", response_model=WorkflowApprovalHierarchiesOut)
async def update_workflow_approval_hierarchies(
    entity_id: uuid.UUID,
    data: WorkflowApprovalHierarchiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowApprovalHierarchiesService(db).update(entity_id, data)

@router.delete("/workflow_approval_hierarchies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_approval_hierarchies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await WorkflowApprovalHierarchiesService(db).delete(entity_id)

@router.get("/workflow_approval_history", response_model=PaginatedResponse[WorkflowApprovalHistoryOut])
async def list_workflow_approval_history(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = WorkflowApprovalHistoryService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_approval_history/{entity_id}", response_model=WorkflowApprovalHistoryOut)
async def get_workflow_approval_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await WorkflowApprovalHistoryService(db).get(entity_id)

@router.post("/workflow_approval_history", response_model=WorkflowApprovalHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_approval_history(
    data: WorkflowApprovalHistoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowApprovalHistoryService(db).create(data)

@router.put("/workflow_approval_history/{entity_id}", response_model=WorkflowApprovalHistoryOut)
async def update_workflow_approval_history(
    entity_id: uuid.UUID,
    data: WorkflowApprovalHistoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowApprovalHistoryService(db).update(entity_id, data)

@router.delete("/workflow_approval_history/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_approval_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await WorkflowApprovalHistoryService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["task_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)

@router.get("/yard_gate_transactions", response_model=PaginatedResponse[YardGateTransactionsOut])
async def list_yard_gate_transactions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = YardGateTransactionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["driver_name", "gate_number", "seal_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/yard_gate_transactions/{entity_id}", response_model=YardGateTransactionsOut)
async def get_yard_gate_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await YardGateTransactionsService(db).get(entity_id)

@router.post("/yard_gate_transactions", response_model=YardGateTransactionsOut, status_code=status.HTTP_201_CREATED)
async def create_yard_gate_transactions(
    data: YardGateTransactionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardGateTransactionsService(db).create(data)

@router.put("/yard_gate_transactions/{entity_id}", response_model=YardGateTransactionsOut)
async def update_yard_gate_transactions(
    entity_id: uuid.UUID,
    data: YardGateTransactionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardGateTransactionsService(db).update(entity_id, data)

@router.delete("/yard_gate_transactions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_yard_gate_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await YardGateTransactionsService(db).delete(entity_id)

@router.get("/yard_inventory", response_model=PaginatedResponse[YardInventoryOut])
async def list_yard_inventory(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = YardInventoryService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/yard_inventory/{entity_id}", response_model=YardInventoryOut)
async def get_yard_inventory(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await YardInventoryService(db).get(entity_id)

@router.post("/yard_inventory", response_model=YardInventoryOut, status_code=status.HTTP_201_CREATED)
async def create_yard_inventory(
    data: YardInventoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardInventoryService(db).create(data)

@router.put("/yard_inventory/{entity_id}", response_model=YardInventoryOut)
async def update_yard_inventory(
    entity_id: uuid.UUID,
    data: YardInventoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardInventoryService(db).update(entity_id, data)

@router.delete("/yard_inventory/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_yard_inventory(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await YardInventoryService(db).delete(entity_id)

@router.get("/yard_locations", response_model=PaginatedResponse[YardLocationsOut])
async def list_yard_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    svc = YardLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["yard_code", "yard_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/yard_locations/{entity_id}", response_model=YardLocationsOut)
async def get_yard_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "view"),
):
    return await YardLocationsService(db).get(entity_id)

@router.post("/yard_locations", response_model=YardLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_yard_locations(
    data: YardLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardLocationsService(db).create(data)

@router.put("/yard_locations/{entity_id}", response_model=YardLocationsOut)
async def update_yard_locations(
    entity_id: uuid.UUID,
    data: YardLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    return await YardLocationsService(db).update(entity_id, data)

@router.delete("/yard_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_yard_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tms", "manage"),
):
    await YardLocationsService(db).delete(entity_id)
