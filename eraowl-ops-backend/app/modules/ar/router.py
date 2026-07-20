import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.ar.services import (
    AccountingEntriesService,
    AdjustmentsService,
    AgingSnapshotsService,
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    ArCustomerLocationsService,
    ArCustomerSitesService,
    ArCustomersService,
    ArInvoiceLinesService,
    ArInvoicesService,
    BankAccountsService,
    CashReceiptsService,
    CollectionTasksService,
    CreditHoldsService,
    CreditProfilesService,
    CustSiteUsesService,
    CustomerDepositsService,
    DepositApplicationsService,
    DunningHistoryService,
    DunningPlansService,
    ImportErrorLogService,
    ImportInterfaceService,
    InvoiceDistributionsService,
    PaymentSchedulesService,
    PeriodStatusService,
    ReceiptApplicationsService,
    ReceiptBatchesService,
    RevenueSchedulesService,
    TaxCodesService,
    TransactionTypesService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.ar.schemas import (
    AccountingEntriesCreate,
    AccountingEntriesUpdate,
    AccountingEntriesOut,
    AdjustmentsCreate,
    AdjustmentsUpdate,
    AdjustmentsOut,
    AgingSnapshotsCreate,
    AgingSnapshotsUpdate,
    AgingSnapshotsOut,
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    ArCustomerLocationsCreate,
    ArCustomerLocationsUpdate,
    ArCustomerLocationsOut,
    ArCustomerSitesCreate,
    ArCustomerSitesUpdate,
    ArCustomerSitesOut,
    ArCustomersCreate,
    ArCustomersUpdate,
    ArCustomersOut,
    ArInvoiceLinesCreate,
    ArInvoiceLinesUpdate,
    ArInvoiceLinesOut,
    ArInvoicesCreate,
    ArInvoicesUpdate,
    ArInvoicesOut,
    BankAccountsCreate,
    BankAccountsUpdate,
    BankAccountsOut,
    CashReceiptsCreate,
    CashReceiptsUpdate,
    CashReceiptsOut,
    CollectionTasksCreate,
    CollectionTasksUpdate,
    CollectionTasksOut,
    CreditHoldsCreate,
    CreditHoldsUpdate,
    CreditHoldsOut,
    CreditProfilesCreate,
    CreditProfilesUpdate,
    CreditProfilesOut,
    CustSiteUsesCreate,
    CustSiteUsesUpdate,
    CustSiteUsesOut,
    CustomerDepositsCreate,
    CustomerDepositsUpdate,
    CustomerDepositsOut,
    DepositApplicationsCreate,
    DepositApplicationsUpdate,
    DepositApplicationsOut,
    DunningHistoryCreate,
    DunningHistoryUpdate,
    DunningHistoryOut,
    DunningPlansCreate,
    DunningPlansUpdate,
    DunningPlansOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    ImportInterfaceCreate,
    ImportInterfaceUpdate,
    ImportInterfaceOut,
    InvoiceDistributionsCreate,
    InvoiceDistributionsUpdate,
    InvoiceDistributionsOut,
    PaymentSchedulesCreate,
    PaymentSchedulesUpdate,
    PaymentSchedulesOut,
    PeriodStatusCreate,
    PeriodStatusUpdate,
    PeriodStatusOut,
    ReceiptApplicationsCreate,
    ReceiptApplicationsUpdate,
    ReceiptApplicationsOut,
    ReceiptBatchesCreate,
    ReceiptBatchesUpdate,
    ReceiptBatchesOut,
    RevenueSchedulesCreate,
    RevenueSchedulesUpdate,
    RevenueSchedulesOut,
    TaxCodesCreate,
    TaxCodesUpdate,
    TaxCodesOut,
    TransactionTypesCreate,
    TransactionTypesUpdate,
    TransactionTypesOut,
    WorkflowDefinitionsCreate,
    WorkflowDefinitionsUpdate,
    WorkflowDefinitionsOut,
    WorkflowTasksCreate,
    WorkflowTasksUpdate,
    WorkflowTasksOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/accounting_entries", response_model=PaginatedResponse[AccountingEntriesOut])
async def list_accounting_entries(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AccountingEntriesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code", "period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/accounting_entries/{entity_id}", response_model=AccountingEntriesOut)
async def get_accounting_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AccountingEntriesService(db).get(entity_id)

@router.post("/accounting_entries", response_model=AccountingEntriesOut, status_code=status.HTTP_201_CREATED)
async def create_accounting_entries(
    data: AccountingEntriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AccountingEntriesService(db).create(data)

@router.put("/accounting_entries/{entity_id}", response_model=AccountingEntriesOut)
async def update_accounting_entries(
    entity_id: uuid.UUID,
    data: AccountingEntriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AccountingEntriesService(db).update(entity_id, data)

@router.delete("/accounting_entries/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_accounting_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AccountingEntriesService(db).delete(entity_id)

@router.get("/adjustments", response_model=PaginatedResponse[AdjustmentsOut])
async def list_adjustments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AdjustmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/adjustments/{entity_id}", response_model=AdjustmentsOut)
async def get_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AdjustmentsService(db).get(entity_id)

@router.post("/adjustments", response_model=AdjustmentsOut, status_code=status.HTTP_201_CREATED)
async def create_adjustments(
    data: AdjustmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AdjustmentsService(db).create(data)

@router.put("/adjustments/{entity_id}", response_model=AdjustmentsOut)
async def update_adjustments(
    entity_id: uuid.UUID,
    data: AdjustmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AdjustmentsService(db).update(entity_id, data)

@router.delete("/adjustments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AdjustmentsService(db).delete(entity_id)

@router.get("/aging_snapshots", response_model=PaginatedResponse[AgingSnapshotsOut])
async def list_aging_snapshots(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AgingSnapshotsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/aging_snapshots/{entity_id}", response_model=AgingSnapshotsOut)
async def get_aging_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AgingSnapshotsService(db).get(entity_id)

@router.post("/aging_snapshots", response_model=AgingSnapshotsOut, status_code=status.HTTP_201_CREATED)
async def create_aging_snapshots(
    data: AgingSnapshotsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AgingSnapshotsService(db).create(data)

@router.put("/aging_snapshots/{entity_id}", response_model=AgingSnapshotsOut)
async def update_aging_snapshots(
    entity_id: uuid.UUID,
    data: AgingSnapshotsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AgingSnapshotsService(db).update(entity_id, data)

@router.delete("/aging_snapshots/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aging_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AgingSnapshotsService(db).delete(entity_id)

@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/ar_customer_locations", response_model=PaginatedResponse[ArCustomerLocationsOut])
async def list_ar_customer_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ArCustomerLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_code", "location_name", "contact_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ar_customer_locations/{entity_id}", response_model=ArCustomerLocationsOut)
async def get_ar_customer_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ArCustomerLocationsService(db).get(entity_id)

@router.post("/ar_customer_locations", response_model=ArCustomerLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_ar_customer_locations(
    data: ArCustomerLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomerLocationsService(db).create(data)

@router.put("/ar_customer_locations/{entity_id}", response_model=ArCustomerLocationsOut)
async def update_ar_customer_locations(
    entity_id: uuid.UUID,
    data: ArCustomerLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomerLocationsService(db).update(entity_id, data)

@router.delete("/ar_customer_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ar_customer_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ArCustomerLocationsService(db).delete(entity_id)

@router.get("/ar_customer_sites", response_model=PaginatedResponse[ArCustomerSitesOut])
async def list_ar_customer_sites(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ArCustomerSitesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["site_name", "contact_name", "contact_email"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ar_customer_sites/{entity_id}", response_model=ArCustomerSitesOut)
async def get_ar_customer_sites(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ArCustomerSitesService(db).get(entity_id)

@router.post("/ar_customer_sites", response_model=ArCustomerSitesOut, status_code=status.HTTP_201_CREATED)
async def create_ar_customer_sites(
    data: ArCustomerSitesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomerSitesService(db).create(data)

@router.put("/ar_customer_sites/{entity_id}", response_model=ArCustomerSitesOut)
async def update_ar_customer_sites(
    entity_id: uuid.UUID,
    data: ArCustomerSitesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomerSitesService(db).update(entity_id, data)

@router.delete("/ar_customer_sites/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ar_customer_sites(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ArCustomerSitesService(db).delete(entity_id)

@router.get("/ar_customers", response_model=PaginatedResponse[ArCustomersOut])
async def list_ar_customers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ArCustomersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["account_number", "tax_registration_number", "industry_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ar_customers/{entity_id}", response_model=ArCustomersOut)
async def get_ar_customers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ArCustomersService(db).get(entity_id)

@router.post("/ar_customers", response_model=ArCustomersOut, status_code=status.HTTP_201_CREATED)
async def create_ar_customers(
    data: ArCustomersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomersService(db).create(data)

@router.put("/ar_customers/{entity_id}", response_model=ArCustomersOut)
async def update_ar_customers(
    entity_id: uuid.UUID,
    data: ArCustomersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArCustomersService(db).update(entity_id, data)

@router.delete("/ar_customers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ar_customers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ArCustomersService(db).delete(entity_id)

@router.get("/ar_invoice_lines", response_model=PaginatedResponse[ArInvoiceLinesOut])
async def list_ar_invoice_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ArInvoiceLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["uom_code", "tax_exempt_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ar_invoice_lines/{entity_id}", response_model=ArInvoiceLinesOut)
async def get_ar_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ArInvoiceLinesService(db).get(entity_id)

@router.post("/ar_invoice_lines", response_model=ArInvoiceLinesOut, status_code=status.HTTP_201_CREATED)
async def create_ar_invoice_lines(
    data: ArInvoiceLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArInvoiceLinesService(db).create(data)

@router.put("/ar_invoice_lines/{entity_id}", response_model=ArInvoiceLinesOut)
async def update_ar_invoice_lines(
    entity_id: uuid.UUID,
    data: ArInvoiceLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArInvoiceLinesService(db).update(entity_id, data)

@router.delete("/ar_invoice_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ar_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ArInvoiceLinesService(db).delete(entity_id)

@router.get("/ar_invoices", response_model=PaginatedResponse[ArInvoicesOut])
async def list_ar_invoices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ArInvoicesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["invoice_number", "currency_code", "reference_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ar_invoices/{entity_id}", response_model=ArInvoicesOut)
async def get_ar_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ArInvoicesService(db).get(entity_id)

@router.post("/ar_invoices", response_model=ArInvoicesOut, status_code=status.HTTP_201_CREATED)
async def create_ar_invoices(
    data: ArInvoicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArInvoicesService(db).create(data)

@router.put("/ar_invoices/{entity_id}", response_model=ArInvoicesOut)
async def update_ar_invoices(
    entity_id: uuid.UUID,
    data: ArInvoicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ArInvoicesService(db).update(entity_id, data)

@router.delete("/ar_invoices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ar_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ArInvoicesService(db).delete(entity_id)

@router.get("/bank_accounts", response_model=PaginatedResponse[BankAccountsOut])
async def list_bank_accounts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = BankAccountsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["account_name", "account_number", "bank_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/bank_accounts/{entity_id}", response_model=BankAccountsOut)
async def get_bank_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await BankAccountsService(db).get(entity_id)

@router.post("/bank_accounts", response_model=BankAccountsOut, status_code=status.HTTP_201_CREATED)
async def create_bank_accounts(
    data: BankAccountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await BankAccountsService(db).create(data)

@router.put("/bank_accounts/{entity_id}", response_model=BankAccountsOut)
async def update_bank_accounts(
    entity_id: uuid.UUID,
    data: BankAccountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await BankAccountsService(db).update(entity_id, data)

@router.delete("/bank_accounts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await BankAccountsService(db).delete(entity_id)

@router.get("/cash_receipts", response_model=PaginatedResponse[CashReceiptsOut])
async def list_cash_receipts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CashReceiptsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["receipt_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/cash_receipts/{entity_id}", response_model=CashReceiptsOut)
async def get_cash_receipts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CashReceiptsService(db).get(entity_id)

@router.post("/cash_receipts", response_model=CashReceiptsOut, status_code=status.HTTP_201_CREATED)
async def create_cash_receipts(
    data: CashReceiptsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CashReceiptsService(db).create(data)

@router.put("/cash_receipts/{entity_id}", response_model=CashReceiptsOut)
async def update_cash_receipts(
    entity_id: uuid.UUID,
    data: CashReceiptsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CashReceiptsService(db).update(entity_id, data)

@router.delete("/cash_receipts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cash_receipts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CashReceiptsService(db).delete(entity_id)

@router.get("/collection_tasks", response_model=PaginatedResponse[CollectionTasksOut])
async def list_collection_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CollectionTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/collection_tasks/{entity_id}", response_model=CollectionTasksOut)
async def get_collection_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CollectionTasksService(db).get(entity_id)

@router.post("/collection_tasks", response_model=CollectionTasksOut, status_code=status.HTTP_201_CREATED)
async def create_collection_tasks(
    data: CollectionTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CollectionTasksService(db).create(data)

@router.put("/collection_tasks/{entity_id}", response_model=CollectionTasksOut)
async def update_collection_tasks(
    entity_id: uuid.UUID,
    data: CollectionTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CollectionTasksService(db).update(entity_id, data)

@router.delete("/collection_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_collection_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CollectionTasksService(db).delete(entity_id)

@router.get("/credit_holds", response_model=PaginatedResponse[CreditHoldsOut])
async def list_credit_holds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CreditHoldsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/credit_holds/{entity_id}", response_model=CreditHoldsOut)
async def get_credit_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CreditHoldsService(db).get(entity_id)

@router.post("/credit_holds", response_model=CreditHoldsOut, status_code=status.HTTP_201_CREATED)
async def create_credit_holds(
    data: CreditHoldsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CreditHoldsService(db).create(data)

@router.put("/credit_holds/{entity_id}", response_model=CreditHoldsOut)
async def update_credit_holds(
    entity_id: uuid.UUID,
    data: CreditHoldsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CreditHoldsService(db).update(entity_id, data)

@router.delete("/credit_holds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_credit_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CreditHoldsService(db).delete(entity_id)

@router.get("/credit_profiles", response_model=PaginatedResponse[CreditProfilesOut])
async def list_credit_profiles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CreditProfilesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/credit_profiles/{entity_id}", response_model=CreditProfilesOut)
async def get_credit_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CreditProfilesService(db).get(entity_id)

@router.post("/credit_profiles", response_model=CreditProfilesOut, status_code=status.HTTP_201_CREATED)
async def create_credit_profiles(
    data: CreditProfilesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CreditProfilesService(db).create(data)

@router.put("/credit_profiles/{entity_id}", response_model=CreditProfilesOut)
async def update_credit_profiles(
    entity_id: uuid.UUID,
    data: CreditProfilesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CreditProfilesService(db).update(entity_id, data)

@router.delete("/credit_profiles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_credit_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CreditProfilesService(db).delete(entity_id)

@router.get("/cust_site_uses", response_model=PaginatedResponse[CustSiteUsesOut])
async def list_cust_site_uses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CustSiteUsesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["site_use_code", "site_use_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/cust_site_uses/{entity_id}", response_model=CustSiteUsesOut)
async def get_cust_site_uses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CustSiteUsesService(db).get(entity_id)

@router.post("/cust_site_uses", response_model=CustSiteUsesOut, status_code=status.HTTP_201_CREATED)
async def create_cust_site_uses(
    data: CustSiteUsesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CustSiteUsesService(db).create(data)

@router.put("/cust_site_uses/{entity_id}", response_model=CustSiteUsesOut)
async def update_cust_site_uses(
    entity_id: uuid.UUID,
    data: CustSiteUsesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CustSiteUsesService(db).update(entity_id, data)

@router.delete("/cust_site_uses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cust_site_uses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CustSiteUsesService(db).delete(entity_id)

@router.get("/customer_deposits", response_model=PaginatedResponse[CustomerDepositsOut])
async def list_customer_deposits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = CustomerDepositsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["deposit_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/customer_deposits/{entity_id}", response_model=CustomerDepositsOut)
async def get_customer_deposits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await CustomerDepositsService(db).get(entity_id)

@router.post("/customer_deposits", response_model=CustomerDepositsOut, status_code=status.HTTP_201_CREATED)
async def create_customer_deposits(
    data: CustomerDepositsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CustomerDepositsService(db).create(data)

@router.put("/customer_deposits/{entity_id}", response_model=CustomerDepositsOut)
async def update_customer_deposits(
    entity_id: uuid.UUID,
    data: CustomerDepositsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await CustomerDepositsService(db).update(entity_id, data)

@router.delete("/customer_deposits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_deposits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await CustomerDepositsService(db).delete(entity_id)

@router.get("/deposit_applications", response_model=PaginatedResponse[DepositApplicationsOut])
async def list_deposit_applications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = DepositApplicationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/deposit_applications/{entity_id}", response_model=DepositApplicationsOut)
async def get_deposit_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await DepositApplicationsService(db).get(entity_id)

@router.post("/deposit_applications", response_model=DepositApplicationsOut, status_code=status.HTTP_201_CREATED)
async def create_deposit_applications(
    data: DepositApplicationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DepositApplicationsService(db).create(data)

@router.put("/deposit_applications/{entity_id}", response_model=DepositApplicationsOut)
async def update_deposit_applications(
    entity_id: uuid.UUID,
    data: DepositApplicationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DepositApplicationsService(db).update(entity_id, data)

@router.delete("/deposit_applications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_deposit_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await DepositApplicationsService(db).delete(entity_id)

@router.get("/dunning_history", response_model=PaginatedResponse[DunningHistoryOut])
async def list_dunning_history(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = DunningHistoryService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/dunning_history/{entity_id}", response_model=DunningHistoryOut)
async def get_dunning_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await DunningHistoryService(db).get(entity_id)

@router.post("/dunning_history", response_model=DunningHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_dunning_history(
    data: DunningHistoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DunningHistoryService(db).create(data)

@router.put("/dunning_history/{entity_id}", response_model=DunningHistoryOut)
async def update_dunning_history(
    entity_id: uuid.UUID,
    data: DunningHistoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DunningHistoryService(db).update(entity_id, data)

@router.delete("/dunning_history/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dunning_history(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await DunningHistoryService(db).delete(entity_id)

@router.get("/dunning_plans", response_model=PaginatedResponse[DunningPlansOut])
async def list_dunning_plans(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = DunningPlansService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["plan_code", "plan_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/dunning_plans/{entity_id}", response_model=DunningPlansOut)
async def get_dunning_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await DunningPlansService(db).get(entity_id)

@router.post("/dunning_plans", response_model=DunningPlansOut, status_code=status.HTTP_201_CREATED)
async def create_dunning_plans(
    data: DunningPlansCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DunningPlansService(db).create(data)

@router.put("/dunning_plans/{entity_id}", response_model=DunningPlansOut)
async def update_dunning_plans(
    entity_id: uuid.UUID,
    data: DunningPlansUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await DunningPlansService(db).update(entity_id, data)

@router.delete("/dunning_plans/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dunning_plans(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await DunningPlansService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/import_interface", response_model=PaginatedResponse[ImportInterfaceOut])
async def list_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def get_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ImportInterfaceService(db).get(entity_id)

@router.post("/import_interface", response_model=ImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_import_interface(
    data: ImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ImportInterfaceService(db).create(data)

@router.put("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def update_import_interface(
    entity_id: uuid.UUID,
    data: ImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ImportInterfaceService(db).update(entity_id, data)

@router.delete("/import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ImportInterfaceService(db).delete(entity_id)

@router.get("/invoice_distributions", response_model=PaginatedResponse[InvoiceDistributionsOut])
async def list_invoice_distributions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = InvoiceDistributionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/invoice_distributions/{entity_id}", response_model=InvoiceDistributionsOut)
async def get_invoice_distributions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await InvoiceDistributionsService(db).get(entity_id)

@router.post("/invoice_distributions", response_model=InvoiceDistributionsOut, status_code=status.HTTP_201_CREATED)
async def create_invoice_distributions(
    data: InvoiceDistributionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await InvoiceDistributionsService(db).create(data)

@router.put("/invoice_distributions/{entity_id}", response_model=InvoiceDistributionsOut)
async def update_invoice_distributions(
    entity_id: uuid.UUID,
    data: InvoiceDistributionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await InvoiceDistributionsService(db).update(entity_id, data)

@router.delete("/invoice_distributions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice_distributions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await InvoiceDistributionsService(db).delete(entity_id)

@router.get("/payment_schedules", response_model=PaginatedResponse[PaymentSchedulesOut])
async def list_payment_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = PaymentSchedulesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/payment_schedules/{entity_id}", response_model=PaymentSchedulesOut)
async def get_payment_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await PaymentSchedulesService(db).get(entity_id)

@router.post("/payment_schedules", response_model=PaymentSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_payment_schedules(
    data: PaymentSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await PaymentSchedulesService(db).create(data)

@router.put("/payment_schedules/{entity_id}", response_model=PaymentSchedulesOut)
async def update_payment_schedules(
    entity_id: uuid.UUID,
    data: PaymentSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await PaymentSchedulesService(db).update(entity_id, data)

@router.delete("/payment_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await PaymentSchedulesService(db).delete(entity_id)

@router.get("/period_status", response_model=PaginatedResponse[PeriodStatusOut])
async def list_period_status(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = PeriodStatusService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/period_status/{entity_id}", response_model=PeriodStatusOut)
async def get_period_status(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await PeriodStatusService(db).get(entity_id)

@router.post("/period_status", response_model=PeriodStatusOut, status_code=status.HTTP_201_CREATED)
async def create_period_status(
    data: PeriodStatusCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await PeriodStatusService(db).create(data)

@router.put("/period_status/{entity_id}", response_model=PeriodStatusOut)
async def update_period_status(
    entity_id: uuid.UUID,
    data: PeriodStatusUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await PeriodStatusService(db).update(entity_id, data)

@router.delete("/period_status/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_period_status(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await PeriodStatusService(db).delete(entity_id)

@router.get("/receipt_applications", response_model=PaginatedResponse[ReceiptApplicationsOut])
async def list_receipt_applications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ReceiptApplicationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/receipt_applications/{entity_id}", response_model=ReceiptApplicationsOut)
async def get_receipt_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ReceiptApplicationsService(db).get(entity_id)

@router.post("/receipt_applications", response_model=ReceiptApplicationsOut, status_code=status.HTTP_201_CREATED)
async def create_receipt_applications(
    data: ReceiptApplicationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ReceiptApplicationsService(db).create(data)

@router.put("/receipt_applications/{entity_id}", response_model=ReceiptApplicationsOut)
async def update_receipt_applications(
    entity_id: uuid.UUID,
    data: ReceiptApplicationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ReceiptApplicationsService(db).update(entity_id, data)

@router.delete("/receipt_applications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_receipt_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ReceiptApplicationsService(db).delete(entity_id)

@router.get("/receipt_batches", response_model=PaginatedResponse[ReceiptBatchesOut])
async def list_receipt_batches(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = ReceiptBatchesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["batch_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/receipt_batches/{entity_id}", response_model=ReceiptBatchesOut)
async def get_receipt_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await ReceiptBatchesService(db).get(entity_id)

@router.post("/receipt_batches", response_model=ReceiptBatchesOut, status_code=status.HTTP_201_CREATED)
async def create_receipt_batches(
    data: ReceiptBatchesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ReceiptBatchesService(db).create(data)

@router.put("/receipt_batches/{entity_id}", response_model=ReceiptBatchesOut)
async def update_receipt_batches(
    entity_id: uuid.UUID,
    data: ReceiptBatchesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await ReceiptBatchesService(db).update(entity_id, data)

@router.delete("/receipt_batches/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_receipt_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await ReceiptBatchesService(db).delete(entity_id)

@router.get("/revenue_schedules", response_model=PaginatedResponse[RevenueSchedulesOut])
async def list_revenue_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = RevenueSchedulesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/revenue_schedules/{entity_id}", response_model=RevenueSchedulesOut)
async def get_revenue_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await RevenueSchedulesService(db).get(entity_id)

@router.post("/revenue_schedules", response_model=RevenueSchedulesOut, status_code=status.HTTP_201_CREATED)
async def create_revenue_schedules(
    data: RevenueSchedulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await RevenueSchedulesService(db).create(data)

@router.put("/revenue_schedules/{entity_id}", response_model=RevenueSchedulesOut)
async def update_revenue_schedules(
    entity_id: uuid.UUID,
    data: RevenueSchedulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await RevenueSchedulesService(db).update(entity_id, data)

@router.delete("/revenue_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_revenue_schedules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await RevenueSchedulesService(db).delete(entity_id)

@router.get("/tax_codes", response_model=PaginatedResponse[TaxCodesOut])
async def list_tax_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = TaxCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_code", "tax_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def get_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await TaxCodesService(db).get(entity_id)

@router.post("/tax_codes", response_model=TaxCodesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_codes(
    data: TaxCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await TaxCodesService(db).create(data)

@router.put("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def update_tax_codes(
    entity_id: uuid.UUID,
    data: TaxCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await TaxCodesService(db).update(entity_id, data)

@router.delete("/tax_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await TaxCodesService(db).delete(entity_id)

@router.get("/transaction_types", response_model=PaginatedResponse[TransactionTypesOut])
async def list_transaction_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = TransactionTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["type_code", "type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/transaction_types/{entity_id}", response_model=TransactionTypesOut)
async def get_transaction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await TransactionTypesService(db).get(entity_id)

@router.post("/transaction_types", response_model=TransactionTypesOut, status_code=status.HTTP_201_CREATED)
async def create_transaction_types(
    data: TransactionTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await TransactionTypesService(db).create(data)

@router.put("/transaction_types/{entity_id}", response_model=TransactionTypesOut)
async def update_transaction_types(
    entity_id: uuid.UUID,
    data: TransactionTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await TransactionTypesService(db).update(entity_id, data)

@router.delete("/transaction_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await TransactionTypesService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ar", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
