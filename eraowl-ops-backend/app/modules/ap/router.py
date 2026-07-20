import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.ap.services import (
    AccountingEntriesService,
    AgingSnapshotsService,
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowStateService,
    ApInvoiceLinesService,
    ApInvoicesService,
    ApSupplierLocationsService,
    ApSupplierSitesService,
    ApSuppliersService,
    BankAccountsService,
    BankStatementLinesService,
    BankStatementsService,
    DiscountTrackingService,
    ExpenseReportLinesService,
    ExpenseReportsService,
    GlMappingRulesService,
    ImportErrorLogService,
    ImportInterfaceService,
    InvoiceAttachmentsService,
    InvoiceDistributionsService,
    InvoiceHoldsService,
    MatchExceptionsService,
    MatchingRulesService,
    PaymentBatchesService,
    PaymentInstructionsService,
    PaymentMethodsService,
    PaymentTermsService,
    PeriodStatusService,
    PrepaymentApplicationsService,
    PrepaymentsService,
    TaxCodesService,
    WithholdingTaxService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.ap.schemas import (
    AccountingEntriesCreate,
    AccountingEntriesUpdate,
    AccountingEntriesOut,
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
    ApInvoiceLinesCreate,
    ApInvoiceLinesUpdate,
    ApInvoiceLinesOut,
    ApInvoicesCreate,
    ApInvoicesUpdate,
    ApInvoicesOut,
    ApSupplierLocationsCreate,
    ApSupplierLocationsUpdate,
    ApSupplierLocationsOut,
    ApSupplierSitesCreate,
    ApSupplierSitesUpdate,
    ApSupplierSitesOut,
    ApSuppliersCreate,
    ApSuppliersUpdate,
    ApSuppliersOut,
    BankAccountsCreate,
    BankAccountsUpdate,
    BankAccountsOut,
    BankStatementLinesCreate,
    BankStatementLinesUpdate,
    BankStatementLinesOut,
    BankStatementsCreate,
    BankStatementsUpdate,
    BankStatementsOut,
    DiscountTrackingCreate,
    DiscountTrackingUpdate,
    DiscountTrackingOut,
    ExpenseReportLinesCreate,
    ExpenseReportLinesUpdate,
    ExpenseReportLinesOut,
    ExpenseReportsCreate,
    ExpenseReportsUpdate,
    ExpenseReportsOut,
    GlMappingRulesCreate,
    GlMappingRulesUpdate,
    GlMappingRulesOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    ImportInterfaceCreate,
    ImportInterfaceUpdate,
    ImportInterfaceOut,
    InvoiceAttachmentsCreate,
    InvoiceAttachmentsUpdate,
    InvoiceAttachmentsOut,
    InvoiceDistributionsCreate,
    InvoiceDistributionsUpdate,
    InvoiceDistributionsOut,
    InvoiceHoldsCreate,
    InvoiceHoldsUpdate,
    InvoiceHoldsOut,
    MatchExceptionsCreate,
    MatchExceptionsUpdate,
    MatchExceptionsOut,
    MatchingRulesCreate,
    MatchingRulesUpdate,
    MatchingRulesOut,
    PaymentBatchesCreate,
    PaymentBatchesUpdate,
    PaymentBatchesOut,
    PaymentInstructionsCreate,
    PaymentInstructionsUpdate,
    PaymentInstructionsOut,
    PaymentMethodsCreate,
    PaymentMethodsUpdate,
    PaymentMethodsOut,
    PaymentTermsCreate,
    PaymentTermsUpdate,
    PaymentTermsOut,
    PeriodStatusCreate,
    PeriodStatusUpdate,
    PeriodStatusOut,
    PrepaymentApplicationsCreate,
    PrepaymentApplicationsUpdate,
    PrepaymentApplicationsOut,
    PrepaymentsCreate,
    PrepaymentsUpdate,
    PrepaymentsOut,
    TaxCodesCreate,
    TaxCodesUpdate,
    TaxCodesOut,
    WithholdingTaxCreate,
    WithholdingTaxUpdate,
    WithholdingTaxOut,
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
    _priv=check_privilege("ap", "view"),
):
    svc = AccountingEntriesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code", "period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/accounting_entries/{entity_id}", response_model=AccountingEntriesOut)
async def get_accounting_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await AccountingEntriesService(db).get(entity_id)

@router.post("/accounting_entries", response_model=AccountingEntriesOut, status_code=status.HTTP_201_CREATED)
async def create_accounting_entries(
    data: AccountingEntriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AccountingEntriesService(db).create(data)

@router.put("/accounting_entries/{entity_id}", response_model=AccountingEntriesOut)
async def update_accounting_entries(
    entity_id: uuid.UUID,
    data: AccountingEntriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AccountingEntriesService(db).update(entity_id, data)

@router.delete("/accounting_entries/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_accounting_entries(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await AccountingEntriesService(db).delete(entity_id)

@router.get("/aging_snapshots", response_model=PaginatedResponse[AgingSnapshotsOut])
async def list_aging_snapshots(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = AgingSnapshotsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/aging_snapshots/{entity_id}", response_model=AgingSnapshotsOut)
async def get_aging_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await AgingSnapshotsService(db).get(entity_id)

@router.post("/aging_snapshots", response_model=AgingSnapshotsOut, status_code=status.HTTP_201_CREATED)
async def create_aging_snapshots(
    data: AgingSnapshotsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AgingSnapshotsService(db).create(data)

@router.put("/aging_snapshots/{entity_id}", response_model=AgingSnapshotsOut)
async def update_aging_snapshots(
    entity_id: uuid.UUID,
    data: AgingSnapshotsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AgingSnapshotsService(db).update(entity_id, data)

@router.delete("/aging_snapshots/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aging_snapshots(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await AgingSnapshotsService(db).delete(entity_id)

@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/ap_invoice_lines", response_model=PaginatedResponse[ApInvoiceLinesOut])
async def list_ap_invoice_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ApInvoiceLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["item_code", "uom_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ap_invoice_lines/{entity_id}", response_model=ApInvoiceLinesOut)
async def get_ap_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ApInvoiceLinesService(db).get(entity_id)

@router.post("/ap_invoice_lines", response_model=ApInvoiceLinesOut, status_code=status.HTTP_201_CREATED)
async def create_ap_invoice_lines(
    data: ApInvoiceLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApInvoiceLinesService(db).create(data)

@router.put("/ap_invoice_lines/{entity_id}", response_model=ApInvoiceLinesOut)
async def update_ap_invoice_lines(
    entity_id: uuid.UUID,
    data: ApInvoiceLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApInvoiceLinesService(db).update(entity_id, data)

@router.delete("/ap_invoice_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ap_invoice_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ApInvoiceLinesService(db).delete(entity_id)

@router.get("/ap_invoices", response_model=PaginatedResponse[ApInvoicesOut])
async def list_ap_invoices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ApInvoicesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["invoice_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ap_invoices/{entity_id}", response_model=ApInvoicesOut)
async def get_ap_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ApInvoicesService(db).get(entity_id)

@router.post("/ap_invoices", response_model=ApInvoicesOut, status_code=status.HTTP_201_CREATED)
async def create_ap_invoices(
    data: ApInvoicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApInvoicesService(db).create(data)

@router.put("/ap_invoices/{entity_id}", response_model=ApInvoicesOut)
async def update_ap_invoices(
    entity_id: uuid.UUID,
    data: ApInvoicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApInvoicesService(db).update(entity_id, data)

@router.delete("/ap_invoices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ap_invoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ApInvoicesService(db).delete(entity_id)

@router.get("/ap_supplier_locations", response_model=PaginatedResponse[ApSupplierLocationsOut])
async def list_ap_supplier_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ApSupplierLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ap_supplier_locations/{entity_id}", response_model=ApSupplierLocationsOut)
async def get_ap_supplier_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ApSupplierLocationsService(db).get(entity_id)

@router.post("/ap_supplier_locations", response_model=ApSupplierLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_ap_supplier_locations(
    data: ApSupplierLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSupplierLocationsService(db).create(data)

@router.put("/ap_supplier_locations/{entity_id}", response_model=ApSupplierLocationsOut)
async def update_ap_supplier_locations(
    entity_id: uuid.UUID,
    data: ApSupplierLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSupplierLocationsService(db).update(entity_id, data)

@router.delete("/ap_supplier_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ap_supplier_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ApSupplierLocationsService(db).delete(entity_id)

@router.get("/ap_supplier_sites", response_model=PaginatedResponse[ApSupplierSitesOut])
async def list_ap_supplier_sites(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ApSupplierSitesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["bank_account_name", "bank_account_number", "bank_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ap_supplier_sites/{entity_id}", response_model=ApSupplierSitesOut)
async def get_ap_supplier_sites(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ApSupplierSitesService(db).get(entity_id)

@router.post("/ap_supplier_sites", response_model=ApSupplierSitesOut, status_code=status.HTTP_201_CREATED)
async def create_ap_supplier_sites(
    data: ApSupplierSitesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSupplierSitesService(db).create(data)

@router.put("/ap_supplier_sites/{entity_id}", response_model=ApSupplierSitesOut)
async def update_ap_supplier_sites(
    entity_id: uuid.UUID,
    data: ApSupplierSitesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSupplierSitesService(db).update(entity_id, data)

@router.delete("/ap_supplier_sites/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ap_supplier_sites(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ApSupplierSitesService(db).delete(entity_id)

@router.get("/ap_suppliers", response_model=PaginatedResponse[ApSuppliersOut])
async def list_ap_suppliers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ApSuppliersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["supplier_number", "tax_registration_number", "po_supplier_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ap_suppliers/{entity_id}", response_model=ApSuppliersOut)
async def get_ap_suppliers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ApSuppliersService(db).get(entity_id)

@router.post("/ap_suppliers", response_model=ApSuppliersOut, status_code=status.HTTP_201_CREATED)
async def create_ap_suppliers(
    data: ApSuppliersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSuppliersService(db).create(data)

@router.put("/ap_suppliers/{entity_id}", response_model=ApSuppliersOut)
async def update_ap_suppliers(
    entity_id: uuid.UUID,
    data: ApSuppliersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ApSuppliersService(db).update(entity_id, data)

@router.delete("/ap_suppliers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ap_suppliers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ApSuppliersService(db).delete(entity_id)

@router.get("/bank_accounts", response_model=PaginatedResponse[BankAccountsOut])
async def list_bank_accounts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = BankAccountsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["account_name", "account_number", "bank_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/bank_accounts/{entity_id}", response_model=BankAccountsOut)
async def get_bank_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await BankAccountsService(db).get(entity_id)

@router.post("/bank_accounts", response_model=BankAccountsOut, status_code=status.HTTP_201_CREATED)
async def create_bank_accounts(
    data: BankAccountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankAccountsService(db).create(data)

@router.put("/bank_accounts/{entity_id}", response_model=BankAccountsOut)
async def update_bank_accounts(
    entity_id: uuid.UUID,
    data: BankAccountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankAccountsService(db).update(entity_id, data)

@router.delete("/bank_accounts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await BankAccountsService(db).delete(entity_id)

@router.get("/bank_statement_lines", response_model=PaginatedResponse[BankStatementLinesOut])
async def list_bank_statement_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = BankStatementLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/bank_statement_lines/{entity_id}", response_model=BankStatementLinesOut)
async def get_bank_statement_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await BankStatementLinesService(db).get(entity_id)

@router.post("/bank_statement_lines", response_model=BankStatementLinesOut, status_code=status.HTTP_201_CREATED)
async def create_bank_statement_lines(
    data: BankStatementLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankStatementLinesService(db).create(data)

@router.put("/bank_statement_lines/{entity_id}", response_model=BankStatementLinesOut)
async def update_bank_statement_lines(
    entity_id: uuid.UUID,
    data: BankStatementLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankStatementLinesService(db).update(entity_id, data)

@router.delete("/bank_statement_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank_statement_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await BankStatementLinesService(db).delete(entity_id)

@router.get("/bank_statements", response_model=PaginatedResponse[BankStatementsOut])
async def list_bank_statements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = BankStatementsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/bank_statements/{entity_id}", response_model=BankStatementsOut)
async def get_bank_statements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await BankStatementsService(db).get(entity_id)

@router.post("/bank_statements", response_model=BankStatementsOut, status_code=status.HTTP_201_CREATED)
async def create_bank_statements(
    data: BankStatementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankStatementsService(db).create(data)

@router.put("/bank_statements/{entity_id}", response_model=BankStatementsOut)
async def update_bank_statements(
    entity_id: uuid.UUID,
    data: BankStatementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await BankStatementsService(db).update(entity_id, data)

@router.delete("/bank_statements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank_statements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await BankStatementsService(db).delete(entity_id)

@router.get("/discount_tracking", response_model=PaginatedResponse[DiscountTrackingOut])
async def list_discount_tracking(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = DiscountTrackingService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/discount_tracking/{entity_id}", response_model=DiscountTrackingOut)
async def get_discount_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await DiscountTrackingService(db).get(entity_id)

@router.post("/discount_tracking", response_model=DiscountTrackingOut, status_code=status.HTTP_201_CREATED)
async def create_discount_tracking(
    data: DiscountTrackingCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await DiscountTrackingService(db).create(data)

@router.put("/discount_tracking/{entity_id}", response_model=DiscountTrackingOut)
async def update_discount_tracking(
    entity_id: uuid.UUID,
    data: DiscountTrackingUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await DiscountTrackingService(db).update(entity_id, data)

@router.delete("/discount_tracking/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_discount_tracking(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await DiscountTrackingService(db).delete(entity_id)

@router.get("/expense_report_lines", response_model=PaginatedResponse[ExpenseReportLinesOut])
async def list_expense_report_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ExpenseReportLinesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/expense_report_lines/{entity_id}", response_model=ExpenseReportLinesOut)
async def get_expense_report_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ExpenseReportLinesService(db).get(entity_id)

@router.post("/expense_report_lines", response_model=ExpenseReportLinesOut, status_code=status.HTTP_201_CREATED)
async def create_expense_report_lines(
    data: ExpenseReportLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ExpenseReportLinesService(db).create(data)

@router.put("/expense_report_lines/{entity_id}", response_model=ExpenseReportLinesOut)
async def update_expense_report_lines(
    entity_id: uuid.UUID,
    data: ExpenseReportLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ExpenseReportLinesService(db).update(entity_id, data)

@router.delete("/expense_report_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense_report_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ExpenseReportLinesService(db).delete(entity_id)

@router.get("/expense_reports", response_model=PaginatedResponse[ExpenseReportsOut])
async def list_expense_reports(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ExpenseReportsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["report_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/expense_reports/{entity_id}", response_model=ExpenseReportsOut)
async def get_expense_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ExpenseReportsService(db).get(entity_id)

@router.post("/expense_reports", response_model=ExpenseReportsOut, status_code=status.HTTP_201_CREATED)
async def create_expense_reports(
    data: ExpenseReportsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ExpenseReportsService(db).create(data)

@router.put("/expense_reports/{entity_id}", response_model=ExpenseReportsOut)
async def update_expense_reports(
    entity_id: uuid.UUID,
    data: ExpenseReportsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ExpenseReportsService(db).update(entity_id, data)

@router.delete("/expense_reports/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ExpenseReportsService(db).delete(entity_id)

@router.get("/gl_mapping_rules", response_model=PaginatedResponse[GlMappingRulesOut])
async def list_gl_mapping_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = GlMappingRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/gl_mapping_rules/{entity_id}", response_model=GlMappingRulesOut)
async def get_gl_mapping_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await GlMappingRulesService(db).get(entity_id)

@router.post("/gl_mapping_rules", response_model=GlMappingRulesOut, status_code=status.HTTP_201_CREATED)
async def create_gl_mapping_rules(
    data: GlMappingRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await GlMappingRulesService(db).create(data)

@router.put("/gl_mapping_rules/{entity_id}", response_model=GlMappingRulesOut)
async def update_gl_mapping_rules(
    entity_id: uuid.UUID,
    data: GlMappingRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await GlMappingRulesService(db).update(entity_id, data)

@router.delete("/gl_mapping_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gl_mapping_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await GlMappingRulesService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/import_interface", response_model=PaginatedResponse[ImportInterfaceOut])
async def list_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = ImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def get_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await ImportInterfaceService(db).get(entity_id)

@router.post("/import_interface", response_model=ImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_import_interface(
    data: ImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ImportInterfaceService(db).create(data)

@router.put("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def update_import_interface(
    entity_id: uuid.UUID,
    data: ImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await ImportInterfaceService(db).update(entity_id, data)

@router.delete("/import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await ImportInterfaceService(db).delete(entity_id)

@router.get("/invoice_attachments", response_model=PaginatedResponse[InvoiceAttachmentsOut])
async def list_invoice_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = InvoiceAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["file_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/invoice_attachments/{entity_id}", response_model=InvoiceAttachmentsOut)
async def get_invoice_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await InvoiceAttachmentsService(db).get(entity_id)

@router.post("/invoice_attachments", response_model=InvoiceAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_invoice_attachments(
    data: InvoiceAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceAttachmentsService(db).create(data)

@router.put("/invoice_attachments/{entity_id}", response_model=InvoiceAttachmentsOut)
async def update_invoice_attachments(
    entity_id: uuid.UUID,
    data: InvoiceAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceAttachmentsService(db).update(entity_id, data)

@router.delete("/invoice_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await InvoiceAttachmentsService(db).delete(entity_id)

@router.get("/invoice_distributions", response_model=PaginatedResponse[InvoiceDistributionsOut])
async def list_invoice_distributions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = InvoiceDistributionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/invoice_distributions/{entity_id}", response_model=InvoiceDistributionsOut)
async def get_invoice_distributions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await InvoiceDistributionsService(db).get(entity_id)

@router.post("/invoice_distributions", response_model=InvoiceDistributionsOut, status_code=status.HTTP_201_CREATED)
async def create_invoice_distributions(
    data: InvoiceDistributionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceDistributionsService(db).create(data)

@router.put("/invoice_distributions/{entity_id}", response_model=InvoiceDistributionsOut)
async def update_invoice_distributions(
    entity_id: uuid.UUID,
    data: InvoiceDistributionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceDistributionsService(db).update(entity_id, data)

@router.delete("/invoice_distributions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice_distributions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await InvoiceDistributionsService(db).delete(entity_id)

@router.get("/invoice_holds", response_model=PaginatedResponse[InvoiceHoldsOut])
async def list_invoice_holds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = InvoiceHoldsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/invoice_holds/{entity_id}", response_model=InvoiceHoldsOut)
async def get_invoice_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await InvoiceHoldsService(db).get(entity_id)

@router.post("/invoice_holds", response_model=InvoiceHoldsOut, status_code=status.HTTP_201_CREATED)
async def create_invoice_holds(
    data: InvoiceHoldsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceHoldsService(db).create(data)

@router.put("/invoice_holds/{entity_id}", response_model=InvoiceHoldsOut)
async def update_invoice_holds(
    entity_id: uuid.UUID,
    data: InvoiceHoldsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await InvoiceHoldsService(db).update(entity_id, data)

@router.delete("/invoice_holds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice_holds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await InvoiceHoldsService(db).delete(entity_id)

@router.get("/match_exceptions", response_model=PaginatedResponse[MatchExceptionsOut])
async def list_match_exceptions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = MatchExceptionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["exception_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/match_exceptions/{entity_id}", response_model=MatchExceptionsOut)
async def get_match_exceptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await MatchExceptionsService(db).get(entity_id)

@router.post("/match_exceptions", response_model=MatchExceptionsOut, status_code=status.HTTP_201_CREATED)
async def create_match_exceptions(
    data: MatchExceptionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await MatchExceptionsService(db).create(data)

@router.put("/match_exceptions/{entity_id}", response_model=MatchExceptionsOut)
async def update_match_exceptions(
    entity_id: uuid.UUID,
    data: MatchExceptionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await MatchExceptionsService(db).update(entity_id, data)

@router.delete("/match_exceptions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_match_exceptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await MatchExceptionsService(db).delete(entity_id)

@router.get("/matching_rules", response_model=PaginatedResponse[MatchingRulesOut])
async def list_matching_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = MatchingRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/matching_rules/{entity_id}", response_model=MatchingRulesOut)
async def get_matching_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await MatchingRulesService(db).get(entity_id)

@router.post("/matching_rules", response_model=MatchingRulesOut, status_code=status.HTTP_201_CREATED)
async def create_matching_rules(
    data: MatchingRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await MatchingRulesService(db).create(data)

@router.put("/matching_rules/{entity_id}", response_model=MatchingRulesOut)
async def update_matching_rules(
    entity_id: uuid.UUID,
    data: MatchingRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await MatchingRulesService(db).update(entity_id, data)

@router.delete("/matching_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_matching_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await MatchingRulesService(db).delete(entity_id)

@router.get("/payment_batches", response_model=PaginatedResponse[PaymentBatchesOut])
async def list_payment_batches(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PaymentBatchesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["batch_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/payment_batches/{entity_id}", response_model=PaymentBatchesOut)
async def get_payment_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PaymentBatchesService(db).get(entity_id)

@router.post("/payment_batches", response_model=PaymentBatchesOut, status_code=status.HTTP_201_CREATED)
async def create_payment_batches(
    data: PaymentBatchesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentBatchesService(db).create(data)

@router.put("/payment_batches/{entity_id}", response_model=PaymentBatchesOut)
async def update_payment_batches(
    entity_id: uuid.UUID,
    data: PaymentBatchesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentBatchesService(db).update(entity_id, data)

@router.delete("/payment_batches/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_batches(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PaymentBatchesService(db).delete(entity_id)

@router.get("/payment_instructions", response_model=PaginatedResponse[PaymentInstructionsOut])
async def list_payment_instructions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PaymentInstructionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["payment_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/payment_instructions/{entity_id}", response_model=PaymentInstructionsOut)
async def get_payment_instructions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PaymentInstructionsService(db).get(entity_id)

@router.post("/payment_instructions", response_model=PaymentInstructionsOut, status_code=status.HTTP_201_CREATED)
async def create_payment_instructions(
    data: PaymentInstructionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentInstructionsService(db).create(data)

@router.put("/payment_instructions/{entity_id}", response_model=PaymentInstructionsOut)
async def update_payment_instructions(
    entity_id: uuid.UUID,
    data: PaymentInstructionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentInstructionsService(db).update(entity_id, data)

@router.delete("/payment_instructions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_instructions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PaymentInstructionsService(db).delete(entity_id)

@router.get("/payment_methods", response_model=PaginatedResponse[PaymentMethodsOut])
async def list_payment_methods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PaymentMethodsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["method_code", "method_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/payment_methods/{entity_id}", response_model=PaymentMethodsOut)
async def get_payment_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PaymentMethodsService(db).get(entity_id)

@router.post("/payment_methods", response_model=PaymentMethodsOut, status_code=status.HTTP_201_CREATED)
async def create_payment_methods(
    data: PaymentMethodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentMethodsService(db).create(data)

@router.put("/payment_methods/{entity_id}", response_model=PaymentMethodsOut)
async def update_payment_methods(
    entity_id: uuid.UUID,
    data: PaymentMethodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentMethodsService(db).update(entity_id, data)

@router.delete("/payment_methods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_methods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PaymentMethodsService(db).delete(entity_id)

@router.get("/payment_terms", response_model=PaginatedResponse[PaymentTermsOut])
async def list_payment_terms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PaymentTermsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["term_code", "term_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/payment_terms/{entity_id}", response_model=PaymentTermsOut)
async def get_payment_terms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PaymentTermsService(db).get(entity_id)

@router.post("/payment_terms", response_model=PaymentTermsOut, status_code=status.HTTP_201_CREATED)
async def create_payment_terms(
    data: PaymentTermsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentTermsService(db).create(data)

@router.put("/payment_terms/{entity_id}", response_model=PaymentTermsOut)
async def update_payment_terms(
    entity_id: uuid.UUID,
    data: PaymentTermsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PaymentTermsService(db).update(entity_id, data)

@router.delete("/payment_terms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_terms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PaymentTermsService(db).delete(entity_id)

@router.get("/period_status", response_model=PaginatedResponse[PeriodStatusOut])
async def list_period_status(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PeriodStatusService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/period_status/{entity_id}", response_model=PeriodStatusOut)
async def get_period_status(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PeriodStatusService(db).get(entity_id)

@router.post("/period_status", response_model=PeriodStatusOut, status_code=status.HTTP_201_CREATED)
async def create_period_status(
    data: PeriodStatusCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PeriodStatusService(db).create(data)

@router.put("/period_status/{entity_id}", response_model=PeriodStatusOut)
async def update_period_status(
    entity_id: uuid.UUID,
    data: PeriodStatusUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PeriodStatusService(db).update(entity_id, data)

@router.delete("/period_status/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_period_status(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PeriodStatusService(db).delete(entity_id)

@router.get("/prepayment_applications", response_model=PaginatedResponse[PrepaymentApplicationsOut])
async def list_prepayment_applications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PrepaymentApplicationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/prepayment_applications/{entity_id}", response_model=PrepaymentApplicationsOut)
async def get_prepayment_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PrepaymentApplicationsService(db).get(entity_id)

@router.post("/prepayment_applications", response_model=PrepaymentApplicationsOut, status_code=status.HTTP_201_CREATED)
async def create_prepayment_applications(
    data: PrepaymentApplicationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PrepaymentApplicationsService(db).create(data)

@router.put("/prepayment_applications/{entity_id}", response_model=PrepaymentApplicationsOut)
async def update_prepayment_applications(
    entity_id: uuid.UUID,
    data: PrepaymentApplicationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PrepaymentApplicationsService(db).update(entity_id, data)

@router.delete("/prepayment_applications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prepayment_applications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PrepaymentApplicationsService(db).delete(entity_id)

@router.get("/prepayments", response_model=PaginatedResponse[PrepaymentsOut])
async def list_prepayments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = PrepaymentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["prepayment_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/prepayments/{entity_id}", response_model=PrepaymentsOut)
async def get_prepayments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await PrepaymentsService(db).get(entity_id)

@router.post("/prepayments", response_model=PrepaymentsOut, status_code=status.HTTP_201_CREATED)
async def create_prepayments(
    data: PrepaymentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PrepaymentsService(db).create(data)

@router.put("/prepayments/{entity_id}", response_model=PrepaymentsOut)
async def update_prepayments(
    entity_id: uuid.UUID,
    data: PrepaymentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await PrepaymentsService(db).update(entity_id, data)

@router.delete("/prepayments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prepayments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await PrepaymentsService(db).delete(entity_id)

@router.get("/tax_codes", response_model=PaginatedResponse[TaxCodesOut])
async def list_tax_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = TaxCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_code", "tax_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def get_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await TaxCodesService(db).get(entity_id)

@router.post("/tax_codes", response_model=TaxCodesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_codes(
    data: TaxCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await TaxCodesService(db).create(data)

@router.put("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def update_tax_codes(
    entity_id: uuid.UUID,
    data: TaxCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await TaxCodesService(db).update(entity_id, data)

@router.delete("/tax_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await TaxCodesService(db).delete(entity_id)

@router.get("/withholding_tax", response_model=PaginatedResponse[WithholdingTaxOut])
async def list_withholding_tax(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = WithholdingTaxService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["wht_code", "wht_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/withholding_tax/{entity_id}", response_model=WithholdingTaxOut)
async def get_withholding_tax(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await WithholdingTaxService(db).get(entity_id)

@router.post("/withholding_tax", response_model=WithholdingTaxOut, status_code=status.HTTP_201_CREATED)
async def create_withholding_tax(
    data: WithholdingTaxCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WithholdingTaxService(db).create(data)

@router.put("/withholding_tax/{entity_id}", response_model=WithholdingTaxOut)
async def update_withholding_tax(
    entity_id: uuid.UUID,
    data: WithholdingTaxUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WithholdingTaxService(db).update(entity_id, data)

@router.delete("/withholding_tax/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_withholding_tax(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await WithholdingTaxService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("ap", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
