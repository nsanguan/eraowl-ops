import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.gl.services import (
    AccountCombinationsService,
    AccountingBooksService,
    AiAgentLogsService,
    AiDecisionsService,
    AiWorkflowCheckpointsService,
    AiWorkflowStateService,
    BalancesService,
    BudgetBalancesService,
    BudgetVersionsService,
    ChartOfAccountsService,
    ExchangeRatesService,
    FiscalPeriodsService,
    ImportErrorLogService,
    ImportInterfaceService,
    JournalCategoriesService,
    JournalHeadersService,
    JournalLinesService,
    JournalSourcesService,
    LedgersService,
    PeriodStatusesService,
    WorkflowDefinitionsService,
    WorkflowTasksService,
)
from app.modules.gl.schemas import (
    AccountCombinationsCreate,
    AccountCombinationsUpdate,
    AccountCombinationsOut,
    AccountingBooksCreate,
    AccountingBooksUpdate,
    AccountingBooksOut,
    AiAgentLogsCreate,
    AiAgentLogsUpdate,
    AiAgentLogsOut,
    AiDecisionsCreate,
    AiDecisionsUpdate,
    AiDecisionsOut,
    AiWorkflowCheckpointsCreate,
    AiWorkflowCheckpointsUpdate,
    AiWorkflowCheckpointsOut,
    AiWorkflowStateCreate,
    AiWorkflowStateUpdate,
    AiWorkflowStateOut,
    BalancesCreate,
    BalancesUpdate,
    BalancesOut,
    BudgetBalancesCreate,
    BudgetBalancesUpdate,
    BudgetBalancesOut,
    BudgetVersionsCreate,
    BudgetVersionsUpdate,
    BudgetVersionsOut,
    ChartOfAccountsCreate,
    ChartOfAccountsUpdate,
    ChartOfAccountsOut,
    ExchangeRatesCreate,
    ExchangeRatesUpdate,
    ExchangeRatesOut,
    FiscalPeriodsCreate,
    FiscalPeriodsUpdate,
    FiscalPeriodsOut,
    ImportErrorLogCreate,
    ImportErrorLogUpdate,
    ImportErrorLogOut,
    ImportInterfaceCreate,
    ImportInterfaceUpdate,
    ImportInterfaceOut,
    JournalCategoriesCreate,
    JournalCategoriesUpdate,
    JournalCategoriesOut,
    JournalHeadersCreate,
    JournalHeadersUpdate,
    JournalHeadersOut,
    JournalLinesCreate,
    JournalLinesUpdate,
    JournalLinesOut,
    JournalSourcesCreate,
    JournalSourcesUpdate,
    JournalSourcesOut,
    LedgersCreate,
    LedgersUpdate,
    LedgersOut,
    PeriodStatusesCreate,
    PeriodStatusesUpdate,
    PeriodStatusesOut,
    WorkflowDefinitionsCreate,
    WorkflowDefinitionsUpdate,
    WorkflowDefinitionsOut,
    WorkflowTasksCreate,
    WorkflowTasksUpdate,
    WorkflowTasksOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/account_combinations", response_model=PaginatedResponse[AccountCombinationsOut])
async def list_account_combinations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AccountCombinationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/account_combinations/{entity_id}", response_model=AccountCombinationsOut)
async def get_account_combinations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AccountCombinationsService(db).get(entity_id)

@router.post("/account_combinations", response_model=AccountCombinationsOut, status_code=status.HTTP_201_CREATED)
async def create_account_combinations(
    data: AccountCombinationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AccountCombinationsService(db).create(data)

@router.put("/account_combinations/{entity_id}", response_model=AccountCombinationsOut)
async def update_account_combinations(
    entity_id: uuid.UUID,
    data: AccountCombinationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AccountCombinationsService(db).update(entity_id, data)

@router.delete("/account_combinations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account_combinations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AccountCombinationsService(db).delete(entity_id)

@router.get("/accounting_books", response_model=PaginatedResponse[AccountingBooksOut])
async def list_accounting_books(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AccountingBooksService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["book_code", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/accounting_books/{entity_id}", response_model=AccountingBooksOut)
async def get_accounting_books(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AccountingBooksService(db).get(entity_id)

@router.post("/accounting_books", response_model=AccountingBooksOut, status_code=status.HTTP_201_CREATED)
async def create_accounting_books(
    data: AccountingBooksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AccountingBooksService(db).create(data)

@router.put("/accounting_books/{entity_id}", response_model=AccountingBooksOut)
async def update_accounting_books(
    entity_id: uuid.UUID,
    data: AccountingBooksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AccountingBooksService(db).update(entity_id, data)

@router.delete("/accounting_books/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_accounting_books(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AccountingBooksService(db).delete(entity_id)

@router.get("/ai_agent_logs", response_model=PaginatedResponse[AiAgentLogsOut])
async def list_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def get_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AiAgentLogsService(db).get(entity_id)

@router.post("/ai_agent_logs", response_model=AiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_agent_logs(
    data: AiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiAgentLogsService(db).create(data)

@router.put("/ai_agent_logs/{entity_id}", response_model=AiAgentLogsOut)
async def update_ai_agent_logs(
    entity_id: uuid.UUID,
    data: AiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiAgentLogsService(db).update(entity_id, data)

@router.delete("/ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AiAgentLogsService(db).delete(entity_id)

@router.get("/ai_decisions", response_model=PaginatedResponse[AiDecisionsOut])
async def list_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AiDecisionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def get_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AiDecisionsService(db).get(entity_id)

@router.post("/ai_decisions", response_model=AiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_decisions(
    data: AiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiDecisionsService(db).create(data)

@router.put("/ai_decisions/{entity_id}", response_model=AiDecisionsOut)
async def update_ai_decisions(
    entity_id: uuid.UUID,
    data: AiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiDecisionsService(db).update(entity_id, data)

@router.delete("/ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AiDecisionsService(db).delete(entity_id)

@router.get("/ai_workflow_checkpoints", response_model=PaginatedResponse[AiWorkflowCheckpointsOut])
async def list_ai_workflow_checkpoints(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AiWorkflowCheckpointsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_checkpoints/{entity_id}", response_model=AiWorkflowCheckpointsOut)
async def get_ai_workflow_checkpoints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AiWorkflowCheckpointsService(db).get(entity_id)

@router.post("/ai_workflow_checkpoints", response_model=AiWorkflowCheckpointsOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_checkpoints(
    data: AiWorkflowCheckpointsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiWorkflowCheckpointsService(db).create(data)

@router.put("/ai_workflow_checkpoints/{entity_id}", response_model=AiWorkflowCheckpointsOut)
async def update_ai_workflow_checkpoints(
    entity_id: uuid.UUID,
    data: AiWorkflowCheckpointsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiWorkflowCheckpointsService(db).update(entity_id, data)

@router.delete("/ai_workflow_checkpoints/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_checkpoints(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AiWorkflowCheckpointsService(db).delete(entity_id)

@router.get("/ai_workflow_state", response_model=PaginatedResponse[AiWorkflowStateOut])
async def list_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = AiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def get_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await AiWorkflowStateService(db).get(entity_id)

@router.post("/ai_workflow_state", response_model=AiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_ai_workflow_state(
    data: AiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiWorkflowStateService(db).create(data)

@router.put("/ai_workflow_state/{entity_id}", response_model=AiWorkflowStateOut)
async def update_ai_workflow_state(
    entity_id: uuid.UUID,
    data: AiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await AiWorkflowStateService(db).update(entity_id, data)

@router.delete("/ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await AiWorkflowStateService(db).delete(entity_id)

@router.get("/balances", response_model=PaginatedResponse[BalancesOut])
async def list_balances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = BalancesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/balances/{entity_id}", response_model=BalancesOut)
async def get_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await BalancesService(db).get(entity_id)

@router.post("/balances", response_model=BalancesOut, status_code=status.HTTP_201_CREATED)
async def create_balances(
    data: BalancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BalancesService(db).create(data)

@router.put("/balances/{entity_id}", response_model=BalancesOut)
async def update_balances(
    entity_id: uuid.UUID,
    data: BalancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BalancesService(db).update(entity_id, data)

@router.delete("/balances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await BalancesService(db).delete(entity_id)

@router.get("/budget_balances", response_model=PaginatedResponse[BudgetBalancesOut])
async def list_budget_balances(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = BudgetBalancesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/budget_balances/{entity_id}", response_model=BudgetBalancesOut)
async def get_budget_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await BudgetBalancesService(db).get(entity_id)

@router.post("/budget_balances", response_model=BudgetBalancesOut, status_code=status.HTTP_201_CREATED)
async def create_budget_balances(
    data: BudgetBalancesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BudgetBalancesService(db).create(data)

@router.put("/budget_balances/{entity_id}", response_model=BudgetBalancesOut)
async def update_budget_balances(
    entity_id: uuid.UUID,
    data: BudgetBalancesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BudgetBalancesService(db).update(entity_id, data)

@router.delete("/budget_balances/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_budget_balances(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await BudgetBalancesService(db).delete(entity_id)

@router.get("/budget_versions", response_model=PaginatedResponse[BudgetVersionsOut])
async def list_budget_versions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = BudgetVersionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["version_code", "version_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/budget_versions/{entity_id}", response_model=BudgetVersionsOut)
async def get_budget_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await BudgetVersionsService(db).get(entity_id)

@router.post("/budget_versions", response_model=BudgetVersionsOut, status_code=status.HTTP_201_CREATED)
async def create_budget_versions(
    data: BudgetVersionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BudgetVersionsService(db).create(data)

@router.put("/budget_versions/{entity_id}", response_model=BudgetVersionsOut)
async def update_budget_versions(
    entity_id: uuid.UUID,
    data: BudgetVersionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await BudgetVersionsService(db).update(entity_id, data)

@router.delete("/budget_versions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_budget_versions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await BudgetVersionsService(db).delete(entity_id)

@router.get("/chart_of_accounts", response_model=PaginatedResponse[ChartOfAccountsOut])
async def list_chart_of_accounts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = ChartOfAccountsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["account_code", "account_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/chart_of_accounts/{entity_id}", response_model=ChartOfAccountsOut)
async def get_chart_of_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await ChartOfAccountsService(db).get(entity_id)

@router.post("/chart_of_accounts", response_model=ChartOfAccountsOut, status_code=status.HTTP_201_CREATED)
async def create_chart_of_accounts(
    data: ChartOfAccountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ChartOfAccountsService(db).create(data)

@router.put("/chart_of_accounts/{entity_id}", response_model=ChartOfAccountsOut)
async def update_chart_of_accounts(
    entity_id: uuid.UUID,
    data: ChartOfAccountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ChartOfAccountsService(db).update(entity_id, data)

@router.delete("/chart_of_accounts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chart_of_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await ChartOfAccountsService(db).delete(entity_id)

@router.get("/exchange_rates", response_model=PaginatedResponse[ExchangeRatesOut])
async def list_exchange_rates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = ExchangeRatesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/exchange_rates/{entity_id}", response_model=ExchangeRatesOut)
async def get_exchange_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await ExchangeRatesService(db).get(entity_id)

@router.post("/exchange_rates", response_model=ExchangeRatesOut, status_code=status.HTTP_201_CREATED)
async def create_exchange_rates(
    data: ExchangeRatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ExchangeRatesService(db).create(data)

@router.put("/exchange_rates/{entity_id}", response_model=ExchangeRatesOut)
async def update_exchange_rates(
    entity_id: uuid.UUID,
    data: ExchangeRatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ExchangeRatesService(db).update(entity_id, data)

@router.delete("/exchange_rates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exchange_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await ExchangeRatesService(db).delete(entity_id)

@router.get("/fiscal_periods", response_model=PaginatedResponse[FiscalPeriodsOut])
async def list_fiscal_periods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = FiscalPeriodsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/fiscal_periods/{entity_id}", response_model=FiscalPeriodsOut)
async def get_fiscal_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await FiscalPeriodsService(db).get(entity_id)

@router.post("/fiscal_periods", response_model=FiscalPeriodsOut, status_code=status.HTTP_201_CREATED)
async def create_fiscal_periods(
    data: FiscalPeriodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await FiscalPeriodsService(db).create(data)

@router.put("/fiscal_periods/{entity_id}", response_model=FiscalPeriodsOut)
async def update_fiscal_periods(
    entity_id: uuid.UUID,
    data: FiscalPeriodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await FiscalPeriodsService(db).update(entity_id, data)

@router.delete("/fiscal_periods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fiscal_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await FiscalPeriodsService(db).delete(entity_id)

@router.get("/import_error_log", response_model=PaginatedResponse[ImportErrorLogOut])
async def list_import_error_log(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = ImportErrorLogService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["error_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def get_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await ImportErrorLogService(db).get(entity_id)

@router.post("/import_error_log", response_model=ImportErrorLogOut, status_code=status.HTTP_201_CREATED)
async def create_import_error_log(
    data: ImportErrorLogCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ImportErrorLogService(db).create(data)

@router.put("/import_error_log/{entity_id}", response_model=ImportErrorLogOut)
async def update_import_error_log(
    entity_id: uuid.UUID,
    data: ImportErrorLogUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ImportErrorLogService(db).update(entity_id, data)

@router.delete("/import_error_log/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_error_log(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await ImportErrorLogService(db).delete(entity_id)

@router.get("/import_interface", response_model=PaginatedResponse[ImportInterfaceOut])
async def list_import_interface(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = ImportInterfaceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def get_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await ImportInterfaceService(db).get(entity_id)

@router.post("/import_interface", response_model=ImportInterfaceOut, status_code=status.HTTP_201_CREATED)
async def create_import_interface(
    data: ImportInterfaceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ImportInterfaceService(db).create(data)

@router.put("/import_interface/{entity_id}", response_model=ImportInterfaceOut)
async def update_import_interface(
    entity_id: uuid.UUID,
    data: ImportInterfaceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await ImportInterfaceService(db).update(entity_id, data)

@router.delete("/import_interface/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import_interface(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await ImportInterfaceService(db).delete(entity_id)

@router.get("/journal_categories", response_model=PaginatedResponse[JournalCategoriesOut])
async def list_journal_categories(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = JournalCategoriesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["category_code", "category_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/journal_categories/{entity_id}", response_model=JournalCategoriesOut)
async def get_journal_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await JournalCategoriesService(db).get(entity_id)

@router.post("/journal_categories", response_model=JournalCategoriesOut, status_code=status.HTTP_201_CREATED)
async def create_journal_categories(
    data: JournalCategoriesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalCategoriesService(db).create(data)

@router.put("/journal_categories/{entity_id}", response_model=JournalCategoriesOut)
async def update_journal_categories(
    entity_id: uuid.UUID,
    data: JournalCategoriesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalCategoriesService(db).update(entity_id, data)

@router.delete("/journal_categories/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_categories(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await JournalCategoriesService(db).delete(entity_id)

@router.get("/journal_headers", response_model=PaginatedResponse[JournalHeadersOut])
async def list_journal_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = JournalHeadersService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/journal_headers/{entity_id}", response_model=JournalHeadersOut)
async def get_journal_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await JournalHeadersService(db).get(entity_id)

@router.post("/journal_headers", response_model=JournalHeadersOut, status_code=status.HTTP_201_CREATED)
async def create_journal_headers(
    data: JournalHeadersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalHeadersService(db).create(data)

@router.put("/journal_headers/{entity_id}", response_model=JournalHeadersOut)
async def update_journal_headers(
    entity_id: uuid.UUID,
    data: JournalHeadersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalHeadersService(db).update(entity_id, data)

@router.delete("/journal_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_headers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await JournalHeadersService(db).delete(entity_id)

@router.get("/journal_lines", response_model=PaginatedResponse[JournalLinesOut])
async def list_journal_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = JournalLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/journal_lines/{entity_id}", response_model=JournalLinesOut)
async def get_journal_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await JournalLinesService(db).get(entity_id)

@router.post("/journal_lines", response_model=JournalLinesOut, status_code=status.HTTP_201_CREATED)
async def create_journal_lines(
    data: JournalLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalLinesService(db).create(data)

@router.put("/journal_lines/{entity_id}", response_model=JournalLinesOut)
async def update_journal_lines(
    entity_id: uuid.UUID,
    data: JournalLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalLinesService(db).update(entity_id, data)

@router.delete("/journal_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await JournalLinesService(db).delete(entity_id)

@router.get("/journal_sources", response_model=PaginatedResponse[JournalSourcesOut])
async def list_journal_sources(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = JournalSourcesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["source_code", "source_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/journal_sources/{entity_id}", response_model=JournalSourcesOut)
async def get_journal_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await JournalSourcesService(db).get(entity_id)

@router.post("/journal_sources", response_model=JournalSourcesOut, status_code=status.HTTP_201_CREATED)
async def create_journal_sources(
    data: JournalSourcesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalSourcesService(db).create(data)

@router.put("/journal_sources/{entity_id}", response_model=JournalSourcesOut)
async def update_journal_sources(
    entity_id: uuid.UUID,
    data: JournalSourcesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await JournalSourcesService(db).update(entity_id, data)

@router.delete("/journal_sources/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_journal_sources(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await JournalSourcesService(db).delete(entity_id)

@router.get("/ledgers", response_model=PaginatedResponse[LedgersOut])
async def list_ledgers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = LedgersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["ledger_code", "ledger_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/ledgers/{entity_id}", response_model=LedgersOut)
async def get_ledgers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await LedgersService(db).get(entity_id)

@router.post("/ledgers", response_model=LedgersOut, status_code=status.HTTP_201_CREATED)
async def create_ledgers(
    data: LedgersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await LedgersService(db).create(data)

@router.put("/ledgers/{entity_id}", response_model=LedgersOut)
async def update_ledgers(
    entity_id: uuid.UUID,
    data: LedgersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await LedgersService(db).update(entity_id, data)

@router.delete("/ledgers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ledgers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await LedgersService(db).delete(entity_id)

@router.get("/period_statuses", response_model=PaginatedResponse[PeriodStatusesOut])
async def list_period_statuses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = PeriodStatusesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/period_statuses/{entity_id}", response_model=PeriodStatusesOut)
async def get_period_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await PeriodStatusesService(db).get(entity_id)

@router.post("/period_statuses", response_model=PeriodStatusesOut, status_code=status.HTTP_201_CREATED)
async def create_period_statuses(
    data: PeriodStatusesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await PeriodStatusesService(db).create(data)

@router.put("/period_statuses/{entity_id}", response_model=PeriodStatusesOut)
async def update_period_statuses(
    entity_id: uuid.UUID,
    data: PeriodStatusesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await PeriodStatusesService(db).update(entity_id, data)

@router.delete("/period_statuses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_period_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await PeriodStatusesService(db).delete(entity_id)

@router.get("/workflow_definitions", response_model=PaginatedResponse[WorkflowDefinitionsOut])
async def list_workflow_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = WorkflowDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["workflow_code", "workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def get_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await WorkflowDefinitionsService(db).get(entity_id)

@router.post("/workflow_definitions", response_model=WorkflowDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_definitions(
    data: WorkflowDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await WorkflowDefinitionsService(db).create(data)

@router.put("/workflow_definitions/{entity_id}", response_model=WorkflowDefinitionsOut)
async def update_workflow_definitions(
    entity_id: uuid.UUID,
    data: WorkflowDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await WorkflowDefinitionsService(db).update(entity_id, data)

@router.delete("/workflow_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await WorkflowDefinitionsService(db).delete(entity_id)

@router.get("/workflow_tasks", response_model=PaginatedResponse[WorkflowTasksOut])
async def list_workflow_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    svc = WorkflowTasksService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["step_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def get_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "view"),
):
    return await WorkflowTasksService(db).get(entity_id)

@router.post("/workflow_tasks", response_model=WorkflowTasksOut, status_code=status.HTTP_201_CREATED)
async def create_workflow_tasks(
    data: WorkflowTasksCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await WorkflowTasksService(db).create(data)

@router.put("/workflow_tasks/{entity_id}", response_model=WorkflowTasksOut)
async def update_workflow_tasks(
    entity_id: uuid.UUID,
    data: WorkflowTasksUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    return await WorkflowTasksService(db).update(entity_id, data)

@router.delete("/workflow_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow_tasks(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("gl", "manage"),
):
    await WorkflowTasksService(db).delete(entity_id)
