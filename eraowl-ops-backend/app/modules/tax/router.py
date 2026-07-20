import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.tax.services import (
    PartnerTaxProfilesService,
    TaxAccountsService,
    TaxAgentDefinitionsService,
    TaxAiAgentLogsService,
    TaxAiDecisionsService,
    TaxAiModelRegistryService,
    TaxAiWorkflowStateService,
    TaxAlgorithmsService,
    TaxArchiveContainersService,
    TaxAssessmentDisputesService,
    TaxAssessmentsService,
    TaxAuditFindingsService,
    TaxAuditResponsesService,
    TaxAuditRouteLocationsService,
    TaxAuditRoutesService,
    TaxAuditsService,
    TaxAuthoritiesService,
    TaxAuthorityContactsService,
    TaxCertificateJurisdictionsService,
    TaxCertificatesService,
    TaxClassificationRulesService,
    TaxClassificationsService,
    TaxCodesService,
    TaxComplianceCalendarsService,
    TaxComplianceObligationsService,
    TaxCreditsService,
    TaxCustomsBondsService,
    TaxCustomsDeclarationsService,
    TaxDocumentArchivesService,
    TaxEinvoiceConfigsService,
    TaxEinvoiceResponsesService,
    TaxEinvoicesService,
    TaxEntityRelationshipsService,
    TaxEntityStructuresService,
    TaxExemptionJurisdictionsService,
    TaxExemptionsService,
    TaxFilingsService,
    TaxHsCodeDutyRatesService,
    TaxHsCodesService,
    TaxIntegrationConnectionsService,
    TaxIntegrationLogsService,
    TaxJurisdictionAddressesService,
    TaxJurisdictionAgreementsService,
    TaxJurisdictionsService,
    TaxLanggraphExecutionsService,
    TaxLanggraphStatesService,
    TaxLanggraphWorkflowsService,
    TaxLinesService,
    TaxLlmConfigsService,
    TaxMlModelsService,
    TaxOptimizationProblemsService,
    TaxOptimizationScenariosService,
    TaxOptimizationSolutionsService,
    TaxOrtoolsProblemsService,
    TaxPenaltiesService,
    TaxPenaltyWaiversService,
    TaxPeriodsService,
    TaxPredictionActualsService,
    TaxPredictionsService,
    TaxPromptTemplatesService,
    TaxRateTiersService,
    TaxRatesService,
    TaxReconciliationsService,
    TaxRefundsService,
    TaxRegimeAttachmentsService,
    TaxRegimeRulesService,
    TaxRegimesService,
    TaxRegistrationsService,
    TaxReportTypesService,
    TaxReportsService,
    TaxReturnAttachmentsService,
    TaxReturnsService,
    TaxRuleConditionsService,
    TaxRuleTaxCodesService,
    TaxRulesService,
    TaxScenariosService,
    TaxScipyAnalysesService,
    TaxSolverConfigsService,
    TaxStatusesService,
    TaxTrainingRunsService,
    TaxTransactionsService,
    TaxTransferPricingAdjustmentsService,
    TaxTransferPricingPoliciesService,
    TaxTransferPricingStudiesService,
    TaxTypesService,
    TaxVectorDocumentsService,
    TaxWithholdingCertificatesService,
    TaxWithholdingConfigsService,
    TaxWithholdingPaymentsService,
)
from app.modules.tax.schemas import (
    PartnerTaxProfilesCreate,
    PartnerTaxProfilesUpdate,
    PartnerTaxProfilesOut,
    TaxAccountsCreate,
    TaxAccountsUpdate,
    TaxAccountsOut,
    TaxAgentDefinitionsCreate,
    TaxAgentDefinitionsUpdate,
    TaxAgentDefinitionsOut,
    TaxAiAgentLogsCreate,
    TaxAiAgentLogsUpdate,
    TaxAiAgentLogsOut,
    TaxAiDecisionsCreate,
    TaxAiDecisionsUpdate,
    TaxAiDecisionsOut,
    TaxAiModelRegistryCreate,
    TaxAiModelRegistryUpdate,
    TaxAiModelRegistryOut,
    TaxAiWorkflowStateCreate,
    TaxAiWorkflowStateUpdate,
    TaxAiWorkflowStateOut,
    TaxAlgorithmsCreate,
    TaxAlgorithmsUpdate,
    TaxAlgorithmsOut,
    TaxArchiveContainersCreate,
    TaxArchiveContainersUpdate,
    TaxArchiveContainersOut,
    TaxAssessmentDisputesCreate,
    TaxAssessmentDisputesUpdate,
    TaxAssessmentDisputesOut,
    TaxAssessmentsCreate,
    TaxAssessmentsUpdate,
    TaxAssessmentsOut,
    TaxAuditFindingsCreate,
    TaxAuditFindingsUpdate,
    TaxAuditFindingsOut,
    TaxAuditResponsesCreate,
    TaxAuditResponsesUpdate,
    TaxAuditResponsesOut,
    TaxAuditRouteLocationsCreate,
    TaxAuditRouteLocationsUpdate,
    TaxAuditRouteLocationsOut,
    TaxAuditRoutesCreate,
    TaxAuditRoutesUpdate,
    TaxAuditRoutesOut,
    TaxAuditsCreate,
    TaxAuditsUpdate,
    TaxAuditsOut,
    TaxAuthoritiesCreate,
    TaxAuthoritiesUpdate,
    TaxAuthoritiesOut,
    TaxAuthorityContactsCreate,
    TaxAuthorityContactsUpdate,
    TaxAuthorityContactsOut,
    TaxCertificateJurisdictionsCreate,
    TaxCertificateJurisdictionsUpdate,
    TaxCertificateJurisdictionsOut,
    TaxCertificatesCreate,
    TaxCertificatesUpdate,
    TaxCertificatesOut,
    TaxClassificationRulesCreate,
    TaxClassificationRulesUpdate,
    TaxClassificationRulesOut,
    TaxClassificationsCreate,
    TaxClassificationsUpdate,
    TaxClassificationsOut,
    TaxCodesCreate,
    TaxCodesUpdate,
    TaxCodesOut,
    TaxComplianceCalendarsCreate,
    TaxComplianceCalendarsUpdate,
    TaxComplianceCalendarsOut,
    TaxComplianceObligationsCreate,
    TaxComplianceObligationsUpdate,
    TaxComplianceObligationsOut,
    TaxCreditsCreate,
    TaxCreditsUpdate,
    TaxCreditsOut,
    TaxCustomsBondsCreate,
    TaxCustomsBondsUpdate,
    TaxCustomsBondsOut,
    TaxCustomsDeclarationsCreate,
    TaxCustomsDeclarationsUpdate,
    TaxCustomsDeclarationsOut,
    TaxDocumentArchivesCreate,
    TaxDocumentArchivesUpdate,
    TaxDocumentArchivesOut,
    TaxEinvoiceConfigsCreate,
    TaxEinvoiceConfigsUpdate,
    TaxEinvoiceConfigsOut,
    TaxEinvoiceResponsesCreate,
    TaxEinvoiceResponsesUpdate,
    TaxEinvoiceResponsesOut,
    TaxEinvoicesCreate,
    TaxEinvoicesUpdate,
    TaxEinvoicesOut,
    TaxEntityRelationshipsCreate,
    TaxEntityRelationshipsUpdate,
    TaxEntityRelationshipsOut,
    TaxEntityStructuresCreate,
    TaxEntityStructuresUpdate,
    TaxEntityStructuresOut,
    TaxExemptionJurisdictionsCreate,
    TaxExemptionJurisdictionsUpdate,
    TaxExemptionJurisdictionsOut,
    TaxExemptionsCreate,
    TaxExemptionsUpdate,
    TaxExemptionsOut,
    TaxFilingsCreate,
    TaxFilingsUpdate,
    TaxFilingsOut,
    TaxHsCodeDutyRatesCreate,
    TaxHsCodeDutyRatesUpdate,
    TaxHsCodeDutyRatesOut,
    TaxHsCodesCreate,
    TaxHsCodesUpdate,
    TaxHsCodesOut,
    TaxIntegrationConnectionsCreate,
    TaxIntegrationConnectionsUpdate,
    TaxIntegrationConnectionsOut,
    TaxIntegrationLogsCreate,
    TaxIntegrationLogsUpdate,
    TaxIntegrationLogsOut,
    TaxJurisdictionAddressesCreate,
    TaxJurisdictionAddressesUpdate,
    TaxJurisdictionAddressesOut,
    TaxJurisdictionAgreementsCreate,
    TaxJurisdictionAgreementsUpdate,
    TaxJurisdictionAgreementsOut,
    TaxJurisdictionsCreate,
    TaxJurisdictionsUpdate,
    TaxJurisdictionsOut,
    TaxLanggraphExecutionsCreate,
    TaxLanggraphExecutionsUpdate,
    TaxLanggraphExecutionsOut,
    TaxLanggraphStatesCreate,
    TaxLanggraphStatesUpdate,
    TaxLanggraphStatesOut,
    TaxLanggraphWorkflowsCreate,
    TaxLanggraphWorkflowsUpdate,
    TaxLanggraphWorkflowsOut,
    TaxLinesCreate,
    TaxLinesUpdate,
    TaxLinesOut,
    TaxLlmConfigsCreate,
    TaxLlmConfigsUpdate,
    TaxLlmConfigsOut,
    TaxMlModelsCreate,
    TaxMlModelsUpdate,
    TaxMlModelsOut,
    TaxOptimizationProblemsCreate,
    TaxOptimizationProblemsUpdate,
    TaxOptimizationProblemsOut,
    TaxOptimizationScenariosCreate,
    TaxOptimizationScenariosUpdate,
    TaxOptimizationScenariosOut,
    TaxOptimizationSolutionsCreate,
    TaxOptimizationSolutionsUpdate,
    TaxOptimizationSolutionsOut,
    TaxOrtoolsProblemsCreate,
    TaxOrtoolsProblemsUpdate,
    TaxOrtoolsProblemsOut,
    TaxPenaltiesCreate,
    TaxPenaltiesUpdate,
    TaxPenaltiesOut,
    TaxPenaltyWaiversCreate,
    TaxPenaltyWaiversUpdate,
    TaxPenaltyWaiversOut,
    TaxPeriodsCreate,
    TaxPeriodsUpdate,
    TaxPeriodsOut,
    TaxPredictionActualsCreate,
    TaxPredictionActualsUpdate,
    TaxPredictionActualsOut,
    TaxPredictionsCreate,
    TaxPredictionsUpdate,
    TaxPredictionsOut,
    TaxPromptTemplatesCreate,
    TaxPromptTemplatesUpdate,
    TaxPromptTemplatesOut,
    TaxRateTiersCreate,
    TaxRateTiersUpdate,
    TaxRateTiersOut,
    TaxRatesCreate,
    TaxRatesUpdate,
    TaxRatesOut,
    TaxReconciliationsCreate,
    TaxReconciliationsUpdate,
    TaxReconciliationsOut,
    TaxRefundsCreate,
    TaxRefundsUpdate,
    TaxRefundsOut,
    TaxRegimeAttachmentsCreate,
    TaxRegimeAttachmentsUpdate,
    TaxRegimeAttachmentsOut,
    TaxRegimeRulesCreate,
    TaxRegimeRulesUpdate,
    TaxRegimeRulesOut,
    TaxRegimesCreate,
    TaxRegimesUpdate,
    TaxRegimesOut,
    TaxRegistrationsCreate,
    TaxRegistrationsUpdate,
    TaxRegistrationsOut,
    TaxReportTypesCreate,
    TaxReportTypesUpdate,
    TaxReportTypesOut,
    TaxReportsCreate,
    TaxReportsUpdate,
    TaxReportsOut,
    TaxReturnAttachmentsCreate,
    TaxReturnAttachmentsUpdate,
    TaxReturnAttachmentsOut,
    TaxReturnsCreate,
    TaxReturnsUpdate,
    TaxReturnsOut,
    TaxRuleConditionsCreate,
    TaxRuleConditionsUpdate,
    TaxRuleConditionsOut,
    TaxRuleTaxCodesCreate,
    TaxRuleTaxCodesUpdate,
    TaxRuleTaxCodesOut,
    TaxRulesCreate,
    TaxRulesUpdate,
    TaxRulesOut,
    TaxScenariosCreate,
    TaxScenariosUpdate,
    TaxScenariosOut,
    TaxScipyAnalysesCreate,
    TaxScipyAnalysesUpdate,
    TaxScipyAnalysesOut,
    TaxSolverConfigsCreate,
    TaxSolverConfigsUpdate,
    TaxSolverConfigsOut,
    TaxStatusesCreate,
    TaxStatusesUpdate,
    TaxStatusesOut,
    TaxTrainingRunsCreate,
    TaxTrainingRunsUpdate,
    TaxTrainingRunsOut,
    TaxTransactionsCreate,
    TaxTransactionsUpdate,
    TaxTransactionsOut,
    TaxTransferPricingAdjustmentsCreate,
    TaxTransferPricingAdjustmentsUpdate,
    TaxTransferPricingAdjustmentsOut,
    TaxTransferPricingPoliciesCreate,
    TaxTransferPricingPoliciesUpdate,
    TaxTransferPricingPoliciesOut,
    TaxTransferPricingStudiesCreate,
    TaxTransferPricingStudiesUpdate,
    TaxTransferPricingStudiesOut,
    TaxTypesCreate,
    TaxTypesUpdate,
    TaxTypesOut,
    TaxVectorDocumentsCreate,
    TaxVectorDocumentsUpdate,
    TaxVectorDocumentsOut,
    TaxWithholdingCertificatesCreate,
    TaxWithholdingCertificatesUpdate,
    TaxWithholdingCertificatesOut,
    TaxWithholdingConfigsCreate,
    TaxWithholdingConfigsUpdate,
    TaxWithholdingConfigsOut,
    TaxWithholdingPaymentsCreate,
    TaxWithholdingPaymentsUpdate,
    TaxWithholdingPaymentsOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/partner_tax_profiles", response_model=PaginatedResponse[PartnerTaxProfilesOut])
async def list_partner_tax_profiles(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = PartnerTaxProfilesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_registration_number", "default_wht_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/partner_tax_profiles/{entity_id}", response_model=PartnerTaxProfilesOut)
async def get_partner_tax_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await PartnerTaxProfilesService(db).get(entity_id)

@router.post("/partner_tax_profiles", response_model=PartnerTaxProfilesOut, status_code=status.HTTP_201_CREATED)
async def create_partner_tax_profiles(
    data: PartnerTaxProfilesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await PartnerTaxProfilesService(db).create(data)

@router.put("/partner_tax_profiles/{entity_id}", response_model=PartnerTaxProfilesOut)
async def update_partner_tax_profiles(
    entity_id: uuid.UUID,
    data: PartnerTaxProfilesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await PartnerTaxProfilesService(db).update(entity_id, data)

@router.delete("/partner_tax_profiles/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_partner_tax_profiles(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await PartnerTaxProfilesService(db).delete(entity_id)

@router.get("/tax_accounts", response_model=PaginatedResponse[TaxAccountsOut])
async def list_tax_accounts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAccountsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["account_code", "account_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_accounts/{entity_id}", response_model=TaxAccountsOut)
async def get_tax_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAccountsService(db).get(entity_id)

@router.post("/tax_accounts", response_model=TaxAccountsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_accounts(
    data: TaxAccountsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAccountsService(db).create(data)

@router.put("/tax_accounts/{entity_id}", response_model=TaxAccountsOut)
async def update_tax_accounts(
    entity_id: uuid.UUID,
    data: TaxAccountsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAccountsService(db).update(entity_id, data)

@router.delete("/tax_accounts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_accounts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAccountsService(db).delete(entity_id)

@router.get("/tax_agent_definitions", response_model=PaginatedResponse[TaxAgentDefinitionsOut])
async def list_tax_agent_definitions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAgentDefinitionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_agent_definitions/{entity_id}", response_model=TaxAgentDefinitionsOut)
async def get_tax_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAgentDefinitionsService(db).get(entity_id)

@router.post("/tax_agent_definitions", response_model=TaxAgentDefinitionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_agent_definitions(
    data: TaxAgentDefinitionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAgentDefinitionsService(db).create(data)

@router.put("/tax_agent_definitions/{entity_id}", response_model=TaxAgentDefinitionsOut)
async def update_tax_agent_definitions(
    entity_id: uuid.UUID,
    data: TaxAgentDefinitionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAgentDefinitionsService(db).update(entity_id, data)

@router.delete("/tax_agent_definitions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_agent_definitions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAgentDefinitionsService(db).delete(entity_id)

@router.get("/tax_ai_agent_logs", response_model=PaginatedResponse[TaxAiAgentLogsOut])
async def list_tax_ai_agent_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAiAgentLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["agent_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ai_agent_logs/{entity_id}", response_model=TaxAiAgentLogsOut)
async def get_tax_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAiAgentLogsService(db).get(entity_id)

@router.post("/tax_ai_agent_logs", response_model=TaxAiAgentLogsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ai_agent_logs(
    data: TaxAiAgentLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiAgentLogsService(db).create(data)

@router.put("/tax_ai_agent_logs/{entity_id}", response_model=TaxAiAgentLogsOut)
async def update_tax_ai_agent_logs(
    entity_id: uuid.UUID,
    data: TaxAiAgentLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiAgentLogsService(db).update(entity_id, data)

@router.delete("/tax_ai_agent_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ai_agent_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAiAgentLogsService(db).delete(entity_id)

@router.get("/tax_ai_decisions", response_model=PaginatedResponse[TaxAiDecisionsOut])
async def list_tax_ai_decisions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAiDecisionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ai_decisions/{entity_id}", response_model=TaxAiDecisionsOut)
async def get_tax_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAiDecisionsService(db).get(entity_id)

@router.post("/tax_ai_decisions", response_model=TaxAiDecisionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ai_decisions(
    data: TaxAiDecisionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiDecisionsService(db).create(data)

@router.put("/tax_ai_decisions/{entity_id}", response_model=TaxAiDecisionsOut)
async def update_tax_ai_decisions(
    entity_id: uuid.UUID,
    data: TaxAiDecisionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiDecisionsService(db).update(entity_id, data)

@router.delete("/tax_ai_decisions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ai_decisions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAiDecisionsService(db).delete(entity_id)

@router.get("/tax_ai_model_registry", response_model=PaginatedResponse[TaxAiModelRegistryOut])
async def list_tax_ai_model_registry(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAiModelRegistryService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ai_model_registry/{entity_id}", response_model=TaxAiModelRegistryOut)
async def get_tax_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAiModelRegistryService(db).get(entity_id)

@router.post("/tax_ai_model_registry", response_model=TaxAiModelRegistryOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ai_model_registry(
    data: TaxAiModelRegistryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiModelRegistryService(db).create(data)

@router.put("/tax_ai_model_registry/{entity_id}", response_model=TaxAiModelRegistryOut)
async def update_tax_ai_model_registry(
    entity_id: uuid.UUID,
    data: TaxAiModelRegistryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiModelRegistryService(db).update(entity_id, data)

@router.delete("/tax_ai_model_registry/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ai_model_registry(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAiModelRegistryService(db).delete(entity_id)

@router.get("/tax_ai_workflow_state", response_model=PaginatedResponse[TaxAiWorkflowStateOut])
async def list_tax_ai_workflow_state(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAiWorkflowStateService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ai_workflow_state/{entity_id}", response_model=TaxAiWorkflowStateOut)
async def get_tax_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAiWorkflowStateService(db).get(entity_id)

@router.post("/tax_ai_workflow_state", response_model=TaxAiWorkflowStateOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ai_workflow_state(
    data: TaxAiWorkflowStateCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiWorkflowStateService(db).create(data)

@router.put("/tax_ai_workflow_state/{entity_id}", response_model=TaxAiWorkflowStateOut)
async def update_tax_ai_workflow_state(
    entity_id: uuid.UUID,
    data: TaxAiWorkflowStateUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAiWorkflowStateService(db).update(entity_id, data)

@router.delete("/tax_ai_workflow_state/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ai_workflow_state(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAiWorkflowStateService(db).delete(entity_id)

@router.get("/tax_algorithms", response_model=PaginatedResponse[TaxAlgorithmsOut])
async def list_tax_algorithms(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAlgorithmsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["algorithm_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_algorithms/{entity_id}", response_model=TaxAlgorithmsOut)
async def get_tax_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAlgorithmsService(db).get(entity_id)

@router.post("/tax_algorithms", response_model=TaxAlgorithmsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_algorithms(
    data: TaxAlgorithmsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAlgorithmsService(db).create(data)

@router.put("/tax_algorithms/{entity_id}", response_model=TaxAlgorithmsOut)
async def update_tax_algorithms(
    entity_id: uuid.UUID,
    data: TaxAlgorithmsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAlgorithmsService(db).update(entity_id, data)

@router.delete("/tax_algorithms/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_algorithms(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAlgorithmsService(db).delete(entity_id)

@router.get("/tax_archive_containers", response_model=PaginatedResponse[TaxArchiveContainersOut])
async def list_tax_archive_containers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxArchiveContainersService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["container_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_archive_containers/{entity_id}", response_model=TaxArchiveContainersOut)
async def get_tax_archive_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxArchiveContainersService(db).get(entity_id)

@router.post("/tax_archive_containers", response_model=TaxArchiveContainersOut, status_code=status.HTTP_201_CREATED)
async def create_tax_archive_containers(
    data: TaxArchiveContainersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxArchiveContainersService(db).create(data)

@router.put("/tax_archive_containers/{entity_id}", response_model=TaxArchiveContainersOut)
async def update_tax_archive_containers(
    entity_id: uuid.UUID,
    data: TaxArchiveContainersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxArchiveContainersService(db).update(entity_id, data)

@router.delete("/tax_archive_containers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_archive_containers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxArchiveContainersService(db).delete(entity_id)

@router.get("/tax_assessment_disputes", response_model=PaginatedResponse[TaxAssessmentDisputesOut])
async def list_tax_assessment_disputes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAssessmentDisputesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_assessment_disputes/{entity_id}", response_model=TaxAssessmentDisputesOut)
async def get_tax_assessment_disputes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAssessmentDisputesService(db).get(entity_id)

@router.post("/tax_assessment_disputes", response_model=TaxAssessmentDisputesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_assessment_disputes(
    data: TaxAssessmentDisputesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAssessmentDisputesService(db).create(data)

@router.put("/tax_assessment_disputes/{entity_id}", response_model=TaxAssessmentDisputesOut)
async def update_tax_assessment_disputes(
    entity_id: uuid.UUID,
    data: TaxAssessmentDisputesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAssessmentDisputesService(db).update(entity_id, data)

@router.delete("/tax_assessment_disputes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_assessment_disputes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAssessmentDisputesService(db).delete(entity_id)

@router.get("/tax_assessments", response_model=PaginatedResponse[TaxAssessmentsOut])
async def list_tax_assessments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAssessmentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["assessment_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_assessments/{entity_id}", response_model=TaxAssessmentsOut)
async def get_tax_assessments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAssessmentsService(db).get(entity_id)

@router.post("/tax_assessments", response_model=TaxAssessmentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_assessments(
    data: TaxAssessmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAssessmentsService(db).create(data)

@router.put("/tax_assessments/{entity_id}", response_model=TaxAssessmentsOut)
async def update_tax_assessments(
    entity_id: uuid.UUID,
    data: TaxAssessmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAssessmentsService(db).update(entity_id, data)

@router.delete("/tax_assessments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_assessments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAssessmentsService(db).delete(entity_id)

@router.get("/tax_audit_findings", response_model=PaginatedResponse[TaxAuditFindingsOut])
async def list_tax_audit_findings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuditFindingsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["finding_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_audit_findings/{entity_id}", response_model=TaxAuditFindingsOut)
async def get_tax_audit_findings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuditFindingsService(db).get(entity_id)

@router.post("/tax_audit_findings", response_model=TaxAuditFindingsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_audit_findings(
    data: TaxAuditFindingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditFindingsService(db).create(data)

@router.put("/tax_audit_findings/{entity_id}", response_model=TaxAuditFindingsOut)
async def update_tax_audit_findings(
    entity_id: uuid.UUID,
    data: TaxAuditFindingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditFindingsService(db).update(entity_id, data)

@router.delete("/tax_audit_findings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_audit_findings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuditFindingsService(db).delete(entity_id)

@router.get("/tax_audit_responses", response_model=PaginatedResponse[TaxAuditResponsesOut])
async def list_tax_audit_responses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuditResponsesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_audit_responses/{entity_id}", response_model=TaxAuditResponsesOut)
async def get_tax_audit_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuditResponsesService(db).get(entity_id)

@router.post("/tax_audit_responses", response_model=TaxAuditResponsesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_audit_responses(
    data: TaxAuditResponsesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditResponsesService(db).create(data)

@router.put("/tax_audit_responses/{entity_id}", response_model=TaxAuditResponsesOut)
async def update_tax_audit_responses(
    entity_id: uuid.UUID,
    data: TaxAuditResponsesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditResponsesService(db).update(entity_id, data)

@router.delete("/tax_audit_responses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_audit_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuditResponsesService(db).delete(entity_id)

@router.get("/tax_audit_route_locations", response_model=PaginatedResponse[TaxAuditRouteLocationsOut])
async def list_tax_audit_route_locations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuditRouteLocationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["location_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_audit_route_locations/{entity_id}", response_model=TaxAuditRouteLocationsOut)
async def get_tax_audit_route_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuditRouteLocationsService(db).get(entity_id)

@router.post("/tax_audit_route_locations", response_model=TaxAuditRouteLocationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_audit_route_locations(
    data: TaxAuditRouteLocationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditRouteLocationsService(db).create(data)

@router.put("/tax_audit_route_locations/{entity_id}", response_model=TaxAuditRouteLocationsOut)
async def update_tax_audit_route_locations(
    entity_id: uuid.UUID,
    data: TaxAuditRouteLocationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditRouteLocationsService(db).update(entity_id, data)

@router.delete("/tax_audit_route_locations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_audit_route_locations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuditRouteLocationsService(db).delete(entity_id)

@router.get("/tax_audit_routes", response_model=PaginatedResponse[TaxAuditRoutesOut])
async def list_tax_audit_routes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuditRoutesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["route_name", "auditor_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_audit_routes/{entity_id}", response_model=TaxAuditRoutesOut)
async def get_tax_audit_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuditRoutesService(db).get(entity_id)

@router.post("/tax_audit_routes", response_model=TaxAuditRoutesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_audit_routes(
    data: TaxAuditRoutesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditRoutesService(db).create(data)

@router.put("/tax_audit_routes/{entity_id}", response_model=TaxAuditRoutesOut)
async def update_tax_audit_routes(
    entity_id: uuid.UUID,
    data: TaxAuditRoutesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditRoutesService(db).update(entity_id, data)

@router.delete("/tax_audit_routes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_audit_routes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuditRoutesService(db).delete(entity_id)

@router.get("/tax_audits", response_model=PaginatedResponse[TaxAuditsOut])
async def list_tax_audits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuditsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_audits/{entity_id}", response_model=TaxAuditsOut)
async def get_tax_audits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuditsService(db).get(entity_id)

@router.post("/tax_audits", response_model=TaxAuditsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_audits(
    data: TaxAuditsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditsService(db).create(data)

@router.put("/tax_audits/{entity_id}", response_model=TaxAuditsOut)
async def update_tax_audits(
    entity_id: uuid.UUID,
    data: TaxAuditsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuditsService(db).update(entity_id, data)

@router.delete("/tax_audits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_audits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuditsService(db).delete(entity_id)

@router.get("/tax_authorities", response_model=PaginatedResponse[TaxAuthoritiesOut])
async def list_tax_authorities(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuthoritiesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["authority_code", "authority_name", "country_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_authorities/{entity_id}", response_model=TaxAuthoritiesOut)
async def get_tax_authorities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuthoritiesService(db).get(entity_id)

@router.post("/tax_authorities", response_model=TaxAuthoritiesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_authorities(
    data: TaxAuthoritiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuthoritiesService(db).create(data)

@router.put("/tax_authorities/{entity_id}", response_model=TaxAuthoritiesOut)
async def update_tax_authorities(
    entity_id: uuid.UUID,
    data: TaxAuthoritiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuthoritiesService(db).update(entity_id, data)

@router.delete("/tax_authorities/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_authorities(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuthoritiesService(db).delete(entity_id)

@router.get("/tax_authority_contacts", response_model=PaginatedResponse[TaxAuthorityContactsOut])
async def list_tax_authority_contacts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxAuthorityContactsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["contact_name", "email"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_authority_contacts/{entity_id}", response_model=TaxAuthorityContactsOut)
async def get_tax_authority_contacts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxAuthorityContactsService(db).get(entity_id)

@router.post("/tax_authority_contacts", response_model=TaxAuthorityContactsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_authority_contacts(
    data: TaxAuthorityContactsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuthorityContactsService(db).create(data)

@router.put("/tax_authority_contacts/{entity_id}", response_model=TaxAuthorityContactsOut)
async def update_tax_authority_contacts(
    entity_id: uuid.UUID,
    data: TaxAuthorityContactsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxAuthorityContactsService(db).update(entity_id, data)

@router.delete("/tax_authority_contacts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_authority_contacts(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxAuthorityContactsService(db).delete(entity_id)

@router.get("/tax_certificate_jurisdictions", response_model=PaginatedResponse[TaxCertificateJurisdictionsOut])
async def list_tax_certificate_jurisdictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCertificateJurisdictionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_certificate_jurisdictions/{entity_id}", response_model=TaxCertificateJurisdictionsOut)
async def get_tax_certificate_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCertificateJurisdictionsService(db).get(entity_id)

@router.post("/tax_certificate_jurisdictions", response_model=TaxCertificateJurisdictionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_certificate_jurisdictions(
    data: TaxCertificateJurisdictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCertificateJurisdictionsService(db).create(data)

@router.put("/tax_certificate_jurisdictions/{entity_id}", response_model=TaxCertificateJurisdictionsOut)
async def update_tax_certificate_jurisdictions(
    entity_id: uuid.UUID,
    data: TaxCertificateJurisdictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCertificateJurisdictionsService(db).update(entity_id, data)

@router.delete("/tax_certificate_jurisdictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_certificate_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCertificateJurisdictionsService(db).delete(entity_id)

@router.get("/tax_certificates", response_model=PaginatedResponse[TaxCertificatesOut])
async def list_tax_certificates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCertificatesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["certificate_number", "certificate_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_certificates/{entity_id}", response_model=TaxCertificatesOut)
async def get_tax_certificates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCertificatesService(db).get(entity_id)

@router.post("/tax_certificates", response_model=TaxCertificatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_certificates(
    data: TaxCertificatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCertificatesService(db).create(data)

@router.put("/tax_certificates/{entity_id}", response_model=TaxCertificatesOut)
async def update_tax_certificates(
    entity_id: uuid.UUID,
    data: TaxCertificatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCertificatesService(db).update(entity_id, data)

@router.delete("/tax_certificates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_certificates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCertificatesService(db).delete(entity_id)

@router.get("/tax_classification_rules", response_model=PaginatedResponse[TaxClassificationRulesOut])
async def list_tax_classification_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxClassificationRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_classification_rules/{entity_id}", response_model=TaxClassificationRulesOut)
async def get_tax_classification_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxClassificationRulesService(db).get(entity_id)

@router.post("/tax_classification_rules", response_model=TaxClassificationRulesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_classification_rules(
    data: TaxClassificationRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxClassificationRulesService(db).create(data)

@router.put("/tax_classification_rules/{entity_id}", response_model=TaxClassificationRulesOut)
async def update_tax_classification_rules(
    entity_id: uuid.UUID,
    data: TaxClassificationRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxClassificationRulesService(db).update(entity_id, data)

@router.delete("/tax_classification_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_classification_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxClassificationRulesService(db).delete(entity_id)

@router.get("/tax_classifications", response_model=PaginatedResponse[TaxClassificationsOut])
async def list_tax_classifications(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxClassificationsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_classifications/{entity_id}", response_model=TaxClassificationsOut)
async def get_tax_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxClassificationsService(db).get(entity_id)

@router.post("/tax_classifications", response_model=TaxClassificationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_classifications(
    data: TaxClassificationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxClassificationsService(db).create(data)

@router.put("/tax_classifications/{entity_id}", response_model=TaxClassificationsOut)
async def update_tax_classifications(
    entity_id: uuid.UUID,
    data: TaxClassificationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxClassificationsService(db).update(entity_id, data)

@router.delete("/tax_classifications/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_classifications(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxClassificationsService(db).delete(entity_id)

@router.get("/tax_codes", response_model=PaginatedResponse[TaxCodesOut])
async def list_tax_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_code", "tax_code_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def get_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCodesService(db).get(entity_id)

@router.post("/tax_codes", response_model=TaxCodesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_codes(
    data: TaxCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCodesService(db).create(data)

@router.put("/tax_codes/{entity_id}", response_model=TaxCodesOut)
async def update_tax_codes(
    entity_id: uuid.UUID,
    data: TaxCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCodesService(db).update(entity_id, data)

@router.delete("/tax_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCodesService(db).delete(entity_id)

@router.get("/tax_compliance_calendars", response_model=PaginatedResponse[TaxComplianceCalendarsOut])
async def list_tax_compliance_calendars(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxComplianceCalendarsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["period_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_compliance_calendars/{entity_id}", response_model=TaxComplianceCalendarsOut)
async def get_tax_compliance_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxComplianceCalendarsService(db).get(entity_id)

@router.post("/tax_compliance_calendars", response_model=TaxComplianceCalendarsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_compliance_calendars(
    data: TaxComplianceCalendarsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxComplianceCalendarsService(db).create(data)

@router.put("/tax_compliance_calendars/{entity_id}", response_model=TaxComplianceCalendarsOut)
async def update_tax_compliance_calendars(
    entity_id: uuid.UUID,
    data: TaxComplianceCalendarsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxComplianceCalendarsService(db).update(entity_id, data)

@router.delete("/tax_compliance_calendars/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_compliance_calendars(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxComplianceCalendarsService(db).delete(entity_id)

@router.get("/tax_compliance_obligations", response_model=PaginatedResponse[TaxComplianceObligationsOut])
async def list_tax_compliance_obligations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxComplianceObligationsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["obligation_code", "obligation_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_compliance_obligations/{entity_id}", response_model=TaxComplianceObligationsOut)
async def get_tax_compliance_obligations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxComplianceObligationsService(db).get(entity_id)

@router.post("/tax_compliance_obligations", response_model=TaxComplianceObligationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_compliance_obligations(
    data: TaxComplianceObligationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxComplianceObligationsService(db).create(data)

@router.put("/tax_compliance_obligations/{entity_id}", response_model=TaxComplianceObligationsOut)
async def update_tax_compliance_obligations(
    entity_id: uuid.UUID,
    data: TaxComplianceObligationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxComplianceObligationsService(db).update(entity_id, data)

@router.delete("/tax_compliance_obligations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_compliance_obligations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxComplianceObligationsService(db).delete(entity_id)

@router.get("/tax_credits", response_model=PaginatedResponse[TaxCreditsOut])
async def list_tax_credits(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCreditsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_credits/{entity_id}", response_model=TaxCreditsOut)
async def get_tax_credits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCreditsService(db).get(entity_id)

@router.post("/tax_credits", response_model=TaxCreditsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_credits(
    data: TaxCreditsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCreditsService(db).create(data)

@router.put("/tax_credits/{entity_id}", response_model=TaxCreditsOut)
async def update_tax_credits(
    entity_id: uuid.UUID,
    data: TaxCreditsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCreditsService(db).update(entity_id, data)

@router.delete("/tax_credits/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_credits(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCreditsService(db).delete(entity_id)

@router.get("/tax_customs_bonds", response_model=PaginatedResponse[TaxCustomsBondsOut])
async def list_tax_customs_bonds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCustomsBondsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["bond_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_customs_bonds/{entity_id}", response_model=TaxCustomsBondsOut)
async def get_tax_customs_bonds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCustomsBondsService(db).get(entity_id)

@router.post("/tax_customs_bonds", response_model=TaxCustomsBondsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_customs_bonds(
    data: TaxCustomsBondsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCustomsBondsService(db).create(data)

@router.put("/tax_customs_bonds/{entity_id}", response_model=TaxCustomsBondsOut)
async def update_tax_customs_bonds(
    entity_id: uuid.UUID,
    data: TaxCustomsBondsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCustomsBondsService(db).update(entity_id, data)

@router.delete("/tax_customs_bonds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_customs_bonds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCustomsBondsService(db).delete(entity_id)

@router.get("/tax_customs_declarations", response_model=PaginatedResponse[TaxCustomsDeclarationsOut])
async def list_tax_customs_declarations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxCustomsDeclarationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["declaration_number", "declarant_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_customs_declarations/{entity_id}", response_model=TaxCustomsDeclarationsOut)
async def get_tax_customs_declarations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxCustomsDeclarationsService(db).get(entity_id)

@router.post("/tax_customs_declarations", response_model=TaxCustomsDeclarationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_customs_declarations(
    data: TaxCustomsDeclarationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCustomsDeclarationsService(db).create(data)

@router.put("/tax_customs_declarations/{entity_id}", response_model=TaxCustomsDeclarationsOut)
async def update_tax_customs_declarations(
    entity_id: uuid.UUID,
    data: TaxCustomsDeclarationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxCustomsDeclarationsService(db).update(entity_id, data)

@router.delete("/tax_customs_declarations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_customs_declarations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxCustomsDeclarationsService(db).delete(entity_id)

@router.get("/tax_document_archives", response_model=PaginatedResponse[TaxDocumentArchivesOut])
async def list_tax_document_archives(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxDocumentArchivesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["jurisdiction_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_document_archives/{entity_id}", response_model=TaxDocumentArchivesOut)
async def get_tax_document_archives(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxDocumentArchivesService(db).get(entity_id)

@router.post("/tax_document_archives", response_model=TaxDocumentArchivesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_document_archives(
    data: TaxDocumentArchivesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxDocumentArchivesService(db).create(data)

@router.put("/tax_document_archives/{entity_id}", response_model=TaxDocumentArchivesOut)
async def update_tax_document_archives(
    entity_id: uuid.UUID,
    data: TaxDocumentArchivesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxDocumentArchivesService(db).update(entity_id, data)

@router.delete("/tax_document_archives/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_document_archives(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxDocumentArchivesService(db).delete(entity_id)

@router.get("/tax_einvoice_configs", response_model=PaginatedResponse[TaxEinvoiceConfigsOut])
async def list_tax_einvoice_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxEinvoiceConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["country_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_einvoice_configs/{entity_id}", response_model=TaxEinvoiceConfigsOut)
async def get_tax_einvoice_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxEinvoiceConfigsService(db).get(entity_id)

@router.post("/tax_einvoice_configs", response_model=TaxEinvoiceConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_einvoice_configs(
    data: TaxEinvoiceConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoiceConfigsService(db).create(data)

@router.put("/tax_einvoice_configs/{entity_id}", response_model=TaxEinvoiceConfigsOut)
async def update_tax_einvoice_configs(
    entity_id: uuid.UUID,
    data: TaxEinvoiceConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoiceConfigsService(db).update(entity_id, data)

@router.delete("/tax_einvoice_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_einvoice_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxEinvoiceConfigsService(db).delete(entity_id)

@router.get("/tax_einvoice_responses", response_model=PaginatedResponse[TaxEinvoiceResponsesOut])
async def list_tax_einvoice_responses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxEinvoiceResponsesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["response_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_einvoice_responses/{entity_id}", response_model=TaxEinvoiceResponsesOut)
async def get_tax_einvoice_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxEinvoiceResponsesService(db).get(entity_id)

@router.post("/tax_einvoice_responses", response_model=TaxEinvoiceResponsesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_einvoice_responses(
    data: TaxEinvoiceResponsesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoiceResponsesService(db).create(data)

@router.put("/tax_einvoice_responses/{entity_id}", response_model=TaxEinvoiceResponsesOut)
async def update_tax_einvoice_responses(
    entity_id: uuid.UUID,
    data: TaxEinvoiceResponsesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoiceResponsesService(db).update(entity_id, data)

@router.delete("/tax_einvoice_responses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_einvoice_responses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxEinvoiceResponsesService(db).delete(entity_id)

@router.get("/tax_einvoices", response_model=PaginatedResponse[TaxEinvoicesOut])
async def list_tax_einvoices(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxEinvoicesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["invoice_number", "qr_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_einvoices/{entity_id}", response_model=TaxEinvoicesOut)
async def get_tax_einvoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxEinvoicesService(db).get(entity_id)

@router.post("/tax_einvoices", response_model=TaxEinvoicesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_einvoices(
    data: TaxEinvoicesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoicesService(db).create(data)

@router.put("/tax_einvoices/{entity_id}", response_model=TaxEinvoicesOut)
async def update_tax_einvoices(
    entity_id: uuid.UUID,
    data: TaxEinvoicesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEinvoicesService(db).update(entity_id, data)

@router.delete("/tax_einvoices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_einvoices(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxEinvoicesService(db).delete(entity_id)

@router.get("/tax_entity_relationships", response_model=PaginatedResponse[TaxEntityRelationshipsOut])
async def list_tax_entity_relationships(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxEntityRelationshipsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_entity_relationships/{entity_id}", response_model=TaxEntityRelationshipsOut)
async def get_tax_entity_relationships(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxEntityRelationshipsService(db).get(entity_id)

@router.post("/tax_entity_relationships", response_model=TaxEntityRelationshipsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_entity_relationships(
    data: TaxEntityRelationshipsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEntityRelationshipsService(db).create(data)

@router.put("/tax_entity_relationships/{entity_id}", response_model=TaxEntityRelationshipsOut)
async def update_tax_entity_relationships(
    entity_id: uuid.UUID,
    data: TaxEntityRelationshipsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEntityRelationshipsService(db).update(entity_id, data)

@router.delete("/tax_entity_relationships/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_entity_relationships(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxEntityRelationshipsService(db).delete(entity_id)

@router.get("/tax_entity_structures", response_model=PaginatedResponse[TaxEntityStructuresOut])
async def list_tax_entity_structures(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxEntityStructuresService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["entity_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_entity_structures/{entity_id}", response_model=TaxEntityStructuresOut)
async def get_tax_entity_structures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxEntityStructuresService(db).get(entity_id)

@router.post("/tax_entity_structures", response_model=TaxEntityStructuresOut, status_code=status.HTTP_201_CREATED)
async def create_tax_entity_structures(
    data: TaxEntityStructuresCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEntityStructuresService(db).create(data)

@router.put("/tax_entity_structures/{entity_id}", response_model=TaxEntityStructuresOut)
async def update_tax_entity_structures(
    entity_id: uuid.UUID,
    data: TaxEntityStructuresUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxEntityStructuresService(db).update(entity_id, data)

@router.delete("/tax_entity_structures/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_entity_structures(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxEntityStructuresService(db).delete(entity_id)

@router.get("/tax_exemption_jurisdictions", response_model=PaginatedResponse[TaxExemptionJurisdictionsOut])
async def list_tax_exemption_jurisdictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxExemptionJurisdictionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_exemption_jurisdictions/{entity_id}", response_model=TaxExemptionJurisdictionsOut)
async def get_tax_exemption_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxExemptionJurisdictionsService(db).get(entity_id)

@router.post("/tax_exemption_jurisdictions", response_model=TaxExemptionJurisdictionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_exemption_jurisdictions(
    data: TaxExemptionJurisdictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxExemptionJurisdictionsService(db).create(data)

@router.put("/tax_exemption_jurisdictions/{entity_id}", response_model=TaxExemptionJurisdictionsOut)
async def update_tax_exemption_jurisdictions(
    entity_id: uuid.UUID,
    data: TaxExemptionJurisdictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxExemptionJurisdictionsService(db).update(entity_id, data)

@router.delete("/tax_exemption_jurisdictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_exemption_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxExemptionJurisdictionsService(db).delete(entity_id)

@router.get("/tax_exemptions", response_model=PaginatedResponse[TaxExemptionsOut])
async def list_tax_exemptions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxExemptionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["exemption_code", "exemption_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_exemptions/{entity_id}", response_model=TaxExemptionsOut)
async def get_tax_exemptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxExemptionsService(db).get(entity_id)

@router.post("/tax_exemptions", response_model=TaxExemptionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_exemptions(
    data: TaxExemptionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxExemptionsService(db).create(data)

@router.put("/tax_exemptions/{entity_id}", response_model=TaxExemptionsOut)
async def update_tax_exemptions(
    entity_id: uuid.UUID,
    data: TaxExemptionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxExemptionsService(db).update(entity_id, data)

@router.delete("/tax_exemptions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_exemptions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxExemptionsService(db).delete(entity_id)

@router.get("/tax_filings", response_model=PaginatedResponse[TaxFilingsOut])
async def list_tax_filings(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxFilingsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["confirmation_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_filings/{entity_id}", response_model=TaxFilingsOut)
async def get_tax_filings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxFilingsService(db).get(entity_id)

@router.post("/tax_filings", response_model=TaxFilingsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_filings(
    data: TaxFilingsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxFilingsService(db).create(data)

@router.put("/tax_filings/{entity_id}", response_model=TaxFilingsOut)
async def update_tax_filings(
    entity_id: uuid.UUID,
    data: TaxFilingsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxFilingsService(db).update(entity_id, data)

@router.delete("/tax_filings/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_filings(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxFilingsService(db).delete(entity_id)

@router.get("/tax_hs_code_duty_rates", response_model=PaginatedResponse[TaxHsCodeDutyRatesOut])
async def list_tax_hs_code_duty_rates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxHsCodeDutyRatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["country_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_hs_code_duty_rates/{entity_id}", response_model=TaxHsCodeDutyRatesOut)
async def get_tax_hs_code_duty_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxHsCodeDutyRatesService(db).get(entity_id)

@router.post("/tax_hs_code_duty_rates", response_model=TaxHsCodeDutyRatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_hs_code_duty_rates(
    data: TaxHsCodeDutyRatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxHsCodeDutyRatesService(db).create(data)

@router.put("/tax_hs_code_duty_rates/{entity_id}", response_model=TaxHsCodeDutyRatesOut)
async def update_tax_hs_code_duty_rates(
    entity_id: uuid.UUID,
    data: TaxHsCodeDutyRatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxHsCodeDutyRatesService(db).update(entity_id, data)

@router.delete("/tax_hs_code_duty_rates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_hs_code_duty_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxHsCodeDutyRatesService(db).delete(entity_id)

@router.get("/tax_hs_codes", response_model=PaginatedResponse[TaxHsCodesOut])
async def list_tax_hs_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxHsCodesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["hs_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_hs_codes/{entity_id}", response_model=TaxHsCodesOut)
async def get_tax_hs_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxHsCodesService(db).get(entity_id)

@router.post("/tax_hs_codes", response_model=TaxHsCodesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_hs_codes(
    data: TaxHsCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxHsCodesService(db).create(data)

@router.put("/tax_hs_codes/{entity_id}", response_model=TaxHsCodesOut)
async def update_tax_hs_codes(
    entity_id: uuid.UUID,
    data: TaxHsCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxHsCodesService(db).update(entity_id, data)

@router.delete("/tax_hs_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_hs_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxHsCodesService(db).delete(entity_id)

@router.get("/tax_integration_connections", response_model=PaginatedResponse[TaxIntegrationConnectionsOut])
async def list_tax_integration_connections(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxIntegrationConnectionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["connection_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_integration_connections/{entity_id}", response_model=TaxIntegrationConnectionsOut)
async def get_tax_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxIntegrationConnectionsService(db).get(entity_id)

@router.post("/tax_integration_connections", response_model=TaxIntegrationConnectionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_integration_connections(
    data: TaxIntegrationConnectionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxIntegrationConnectionsService(db).create(data)

@router.put("/tax_integration_connections/{entity_id}", response_model=TaxIntegrationConnectionsOut)
async def update_tax_integration_connections(
    entity_id: uuid.UUID,
    data: TaxIntegrationConnectionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxIntegrationConnectionsService(db).update(entity_id, data)

@router.delete("/tax_integration_connections/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_integration_connections(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxIntegrationConnectionsService(db).delete(entity_id)

@router.get("/tax_integration_logs", response_model=PaginatedResponse[TaxIntegrationLogsOut])
async def list_tax_integration_logs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxIntegrationLogsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_integration_logs/{entity_id}", response_model=TaxIntegrationLogsOut)
async def get_tax_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxIntegrationLogsService(db).get(entity_id)

@router.post("/tax_integration_logs", response_model=TaxIntegrationLogsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_integration_logs(
    data: TaxIntegrationLogsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxIntegrationLogsService(db).create(data)

@router.put("/tax_integration_logs/{entity_id}", response_model=TaxIntegrationLogsOut)
async def update_tax_integration_logs(
    entity_id: uuid.UUID,
    data: TaxIntegrationLogsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxIntegrationLogsService(db).update(entity_id, data)

@router.delete("/tax_integration_logs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_integration_logs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxIntegrationLogsService(db).delete(entity_id)

@router.get("/tax_jurisdiction_addresses", response_model=PaginatedResponse[TaxJurisdictionAddressesOut])
async def list_tax_jurisdiction_addresses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxJurisdictionAddressesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["postal_code", "country_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_jurisdiction_addresses/{entity_id}", response_model=TaxJurisdictionAddressesOut)
async def get_tax_jurisdiction_addresses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxJurisdictionAddressesService(db).get(entity_id)

@router.post("/tax_jurisdiction_addresses", response_model=TaxJurisdictionAddressesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_jurisdiction_addresses(
    data: TaxJurisdictionAddressesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionAddressesService(db).create(data)

@router.put("/tax_jurisdiction_addresses/{entity_id}", response_model=TaxJurisdictionAddressesOut)
async def update_tax_jurisdiction_addresses(
    entity_id: uuid.UUID,
    data: TaxJurisdictionAddressesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionAddressesService(db).update(entity_id, data)

@router.delete("/tax_jurisdiction_addresses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_jurisdiction_addresses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxJurisdictionAddressesService(db).delete(entity_id)

@router.get("/tax_jurisdiction_agreements", response_model=PaginatedResponse[TaxJurisdictionAgreementsOut])
async def list_tax_jurisdiction_agreements(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxJurisdictionAgreementsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_jurisdiction_agreements/{entity_id}", response_model=TaxJurisdictionAgreementsOut)
async def get_tax_jurisdiction_agreements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxJurisdictionAgreementsService(db).get(entity_id)

@router.post("/tax_jurisdiction_agreements", response_model=TaxJurisdictionAgreementsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_jurisdiction_agreements(
    data: TaxJurisdictionAgreementsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionAgreementsService(db).create(data)

@router.put("/tax_jurisdiction_agreements/{entity_id}", response_model=TaxJurisdictionAgreementsOut)
async def update_tax_jurisdiction_agreements(
    entity_id: uuid.UUID,
    data: TaxJurisdictionAgreementsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionAgreementsService(db).update(entity_id, data)

@router.delete("/tax_jurisdiction_agreements/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_jurisdiction_agreements(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxJurisdictionAgreementsService(db).delete(entity_id)

@router.get("/tax_jurisdictions", response_model=PaginatedResponse[TaxJurisdictionsOut])
async def list_tax_jurisdictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxJurisdictionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["country_code", "jurisdiction_code", "jurisdiction_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_jurisdictions/{entity_id}", response_model=TaxJurisdictionsOut)
async def get_tax_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxJurisdictionsService(db).get(entity_id)

@router.post("/tax_jurisdictions", response_model=TaxJurisdictionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_jurisdictions(
    data: TaxJurisdictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionsService(db).create(data)

@router.put("/tax_jurisdictions/{entity_id}", response_model=TaxJurisdictionsOut)
async def update_tax_jurisdictions(
    entity_id: uuid.UUID,
    data: TaxJurisdictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxJurisdictionsService(db).update(entity_id, data)

@router.delete("/tax_jurisdictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_jurisdictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxJurisdictionsService(db).delete(entity_id)

@router.get("/tax_langgraph_executions", response_model=PaginatedResponse[TaxLanggraphExecutionsOut])
async def list_tax_langgraph_executions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxLanggraphExecutionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["execution_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_langgraph_executions/{entity_id}", response_model=TaxLanggraphExecutionsOut)
async def get_tax_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxLanggraphExecutionsService(db).get(entity_id)

@router.post("/tax_langgraph_executions", response_model=TaxLanggraphExecutionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_langgraph_executions(
    data: TaxLanggraphExecutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphExecutionsService(db).create(data)

@router.put("/tax_langgraph_executions/{entity_id}", response_model=TaxLanggraphExecutionsOut)
async def update_tax_langgraph_executions(
    entity_id: uuid.UUID,
    data: TaxLanggraphExecutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphExecutionsService(db).update(entity_id, data)

@router.delete("/tax_langgraph_executions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_langgraph_executions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxLanggraphExecutionsService(db).delete(entity_id)

@router.get("/tax_langgraph_states", response_model=PaginatedResponse[TaxLanggraphStatesOut])
async def list_tax_langgraph_states(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxLanggraphStatesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_langgraph_states/{entity_id}", response_model=TaxLanggraphStatesOut)
async def get_tax_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxLanggraphStatesService(db).get(entity_id)

@router.post("/tax_langgraph_states", response_model=TaxLanggraphStatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_langgraph_states(
    data: TaxLanggraphStatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphStatesService(db).create(data)

@router.put("/tax_langgraph_states/{entity_id}", response_model=TaxLanggraphStatesOut)
async def update_tax_langgraph_states(
    entity_id: uuid.UUID,
    data: TaxLanggraphStatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphStatesService(db).update(entity_id, data)

@router.delete("/tax_langgraph_states/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_langgraph_states(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxLanggraphStatesService(db).delete(entity_id)

@router.get("/tax_langgraph_workflows", response_model=PaginatedResponse[TaxLanggraphWorkflowsOut])
async def list_tax_langgraph_workflows(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxLanggraphWorkflowsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["workflow_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_langgraph_workflows/{entity_id}", response_model=TaxLanggraphWorkflowsOut)
async def get_tax_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxLanggraphWorkflowsService(db).get(entity_id)

@router.post("/tax_langgraph_workflows", response_model=TaxLanggraphWorkflowsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_langgraph_workflows(
    data: TaxLanggraphWorkflowsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphWorkflowsService(db).create(data)

@router.put("/tax_langgraph_workflows/{entity_id}", response_model=TaxLanggraphWorkflowsOut)
async def update_tax_langgraph_workflows(
    entity_id: uuid.UUID,
    data: TaxLanggraphWorkflowsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLanggraphWorkflowsService(db).update(entity_id, data)

@router.delete("/tax_langgraph_workflows/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_langgraph_workflows(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxLanggraphWorkflowsService(db).delete(entity_id)

@router.get("/tax_lines", response_model=PaginatedResponse[TaxLinesOut])
async def list_tax_lines(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxLinesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_lines/{entity_id}", response_model=TaxLinesOut)
async def get_tax_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxLinesService(db).get(entity_id)

@router.post("/tax_lines", response_model=TaxLinesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_lines(
    data: TaxLinesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLinesService(db).create(data)

@router.put("/tax_lines/{entity_id}", response_model=TaxLinesOut)
async def update_tax_lines(
    entity_id: uuid.UUID,
    data: TaxLinesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLinesService(db).update(entity_id, data)

@router.delete("/tax_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_lines(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxLinesService(db).delete(entity_id)

@router.get("/tax_llm_configs", response_model=PaginatedResponse[TaxLlmConfigsOut])
async def list_tax_llm_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxLlmConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_llm_configs/{entity_id}", response_model=TaxLlmConfigsOut)
async def get_tax_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxLlmConfigsService(db).get(entity_id)

@router.post("/tax_llm_configs", response_model=TaxLlmConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_llm_configs(
    data: TaxLlmConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLlmConfigsService(db).create(data)

@router.put("/tax_llm_configs/{entity_id}", response_model=TaxLlmConfigsOut)
async def update_tax_llm_configs(
    entity_id: uuid.UUID,
    data: TaxLlmConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxLlmConfigsService(db).update(entity_id, data)

@router.delete("/tax_llm_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_llm_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxLlmConfigsService(db).delete(entity_id)

@router.get("/tax_ml_models", response_model=PaginatedResponse[TaxMlModelsOut])
async def list_tax_ml_models(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxMlModelsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["model_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ml_models/{entity_id}", response_model=TaxMlModelsOut)
async def get_tax_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxMlModelsService(db).get(entity_id)

@router.post("/tax_ml_models", response_model=TaxMlModelsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ml_models(
    data: TaxMlModelsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxMlModelsService(db).create(data)

@router.put("/tax_ml_models/{entity_id}", response_model=TaxMlModelsOut)
async def update_tax_ml_models(
    entity_id: uuid.UUID,
    data: TaxMlModelsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxMlModelsService(db).update(entity_id, data)

@router.delete("/tax_ml_models/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ml_models(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxMlModelsService(db).delete(entity_id)

@router.get("/tax_optimization_problems", response_model=PaginatedResponse[TaxOptimizationProblemsOut])
async def list_tax_optimization_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxOptimizationProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_optimization_problems/{entity_id}", response_model=TaxOptimizationProblemsOut)
async def get_tax_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxOptimizationProblemsService(db).get(entity_id)

@router.post("/tax_optimization_problems", response_model=TaxOptimizationProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_optimization_problems(
    data: TaxOptimizationProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationProblemsService(db).create(data)

@router.put("/tax_optimization_problems/{entity_id}", response_model=TaxOptimizationProblemsOut)
async def update_tax_optimization_problems(
    entity_id: uuid.UUID,
    data: TaxOptimizationProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationProblemsService(db).update(entity_id, data)

@router.delete("/tax_optimization_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_optimization_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxOptimizationProblemsService(db).delete(entity_id)

@router.get("/tax_optimization_scenarios", response_model=PaginatedResponse[TaxOptimizationScenariosOut])
async def list_tax_optimization_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxOptimizationScenariosService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_optimization_scenarios/{entity_id}", response_model=TaxOptimizationScenariosOut)
async def get_tax_optimization_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxOptimizationScenariosService(db).get(entity_id)

@router.post("/tax_optimization_scenarios", response_model=TaxOptimizationScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_tax_optimization_scenarios(
    data: TaxOptimizationScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationScenariosService(db).create(data)

@router.put("/tax_optimization_scenarios/{entity_id}", response_model=TaxOptimizationScenariosOut)
async def update_tax_optimization_scenarios(
    entity_id: uuid.UUID,
    data: TaxOptimizationScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationScenariosService(db).update(entity_id, data)

@router.delete("/tax_optimization_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_optimization_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxOptimizationScenariosService(db).delete(entity_id)

@router.get("/tax_optimization_solutions", response_model=PaginatedResponse[TaxOptimizationSolutionsOut])
async def list_tax_optimization_solutions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxOptimizationSolutionsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_optimization_solutions/{entity_id}", response_model=TaxOptimizationSolutionsOut)
async def get_tax_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxOptimizationSolutionsService(db).get(entity_id)

@router.post("/tax_optimization_solutions", response_model=TaxOptimizationSolutionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_optimization_solutions(
    data: TaxOptimizationSolutionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationSolutionsService(db).create(data)

@router.put("/tax_optimization_solutions/{entity_id}", response_model=TaxOptimizationSolutionsOut)
async def update_tax_optimization_solutions(
    entity_id: uuid.UUID,
    data: TaxOptimizationSolutionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOptimizationSolutionsService(db).update(entity_id, data)

@router.delete("/tax_optimization_solutions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_optimization_solutions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxOptimizationSolutionsService(db).delete(entity_id)

@router.get("/tax_ortools_problems", response_model=PaginatedResponse[TaxOrtoolsProblemsOut])
async def list_tax_ortools_problems(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxOrtoolsProblemsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["problem_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_ortools_problems/{entity_id}", response_model=TaxOrtoolsProblemsOut)
async def get_tax_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxOrtoolsProblemsService(db).get(entity_id)

@router.post("/tax_ortools_problems", response_model=TaxOrtoolsProblemsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_ortools_problems(
    data: TaxOrtoolsProblemsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOrtoolsProblemsService(db).create(data)

@router.put("/tax_ortools_problems/{entity_id}", response_model=TaxOrtoolsProblemsOut)
async def update_tax_ortools_problems(
    entity_id: uuid.UUID,
    data: TaxOrtoolsProblemsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxOrtoolsProblemsService(db).update(entity_id, data)

@router.delete("/tax_ortools_problems/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_ortools_problems(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxOrtoolsProblemsService(db).delete(entity_id)

@router.get("/tax_penalties", response_model=PaginatedResponse[TaxPenaltiesOut])
async def list_tax_penalties(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPenaltiesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_penalties/{entity_id}", response_model=TaxPenaltiesOut)
async def get_tax_penalties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPenaltiesService(db).get(entity_id)

@router.post("/tax_penalties", response_model=TaxPenaltiesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_penalties(
    data: TaxPenaltiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPenaltiesService(db).create(data)

@router.put("/tax_penalties/{entity_id}", response_model=TaxPenaltiesOut)
async def update_tax_penalties(
    entity_id: uuid.UUID,
    data: TaxPenaltiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPenaltiesService(db).update(entity_id, data)

@router.delete("/tax_penalties/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_penalties(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPenaltiesService(db).delete(entity_id)

@router.get("/tax_penalty_waivers", response_model=PaginatedResponse[TaxPenaltyWaiversOut])
async def list_tax_penalty_waivers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPenaltyWaiversService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_penalty_waivers/{entity_id}", response_model=TaxPenaltyWaiversOut)
async def get_tax_penalty_waivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPenaltyWaiversService(db).get(entity_id)

@router.post("/tax_penalty_waivers", response_model=TaxPenaltyWaiversOut, status_code=status.HTTP_201_CREATED)
async def create_tax_penalty_waivers(
    data: TaxPenaltyWaiversCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPenaltyWaiversService(db).create(data)

@router.put("/tax_penalty_waivers/{entity_id}", response_model=TaxPenaltyWaiversOut)
async def update_tax_penalty_waivers(
    entity_id: uuid.UUID,
    data: TaxPenaltyWaiversUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPenaltyWaiversService(db).update(entity_id, data)

@router.delete("/tax_penalty_waivers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_penalty_waivers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPenaltyWaiversService(db).delete(entity_id)

@router.get("/tax_periods", response_model=PaginatedResponse[TaxPeriodsOut])
async def list_tax_periods(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPeriodsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["period_name", "period_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_periods/{entity_id}", response_model=TaxPeriodsOut)
async def get_tax_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPeriodsService(db).get(entity_id)

@router.post("/tax_periods", response_model=TaxPeriodsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_periods(
    data: TaxPeriodsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPeriodsService(db).create(data)

@router.put("/tax_periods/{entity_id}", response_model=TaxPeriodsOut)
async def update_tax_periods(
    entity_id: uuid.UUID,
    data: TaxPeriodsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPeriodsService(db).update(entity_id, data)

@router.delete("/tax_periods/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_periods(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPeriodsService(db).delete(entity_id)

@router.get("/tax_prediction_actuals", response_model=PaginatedResponse[TaxPredictionActualsOut])
async def list_tax_prediction_actuals(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPredictionActualsService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_prediction_actuals/{entity_id}", response_model=TaxPredictionActualsOut)
async def get_tax_prediction_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPredictionActualsService(db).get(entity_id)

@router.post("/tax_prediction_actuals", response_model=TaxPredictionActualsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_prediction_actuals(
    data: TaxPredictionActualsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPredictionActualsService(db).create(data)

@router.put("/tax_prediction_actuals/{entity_id}", response_model=TaxPredictionActualsOut)
async def update_tax_prediction_actuals(
    entity_id: uuid.UUID,
    data: TaxPredictionActualsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPredictionActualsService(db).update(entity_id, data)

@router.delete("/tax_prediction_actuals/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_prediction_actuals(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPredictionActualsService(db).delete(entity_id)

@router.get("/tax_predictions", response_model=PaginatedResponse[TaxPredictionsOut])
async def list_tax_predictions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPredictionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_predictions/{entity_id}", response_model=TaxPredictionsOut)
async def get_tax_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPredictionsService(db).get(entity_id)

@router.post("/tax_predictions", response_model=TaxPredictionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_predictions(
    data: TaxPredictionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPredictionsService(db).create(data)

@router.put("/tax_predictions/{entity_id}", response_model=TaxPredictionsOut)
async def update_tax_predictions(
    entity_id: uuid.UUID,
    data: TaxPredictionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPredictionsService(db).update(entity_id, data)

@router.delete("/tax_predictions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_predictions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPredictionsService(db).delete(entity_id)

@router.get("/tax_prompt_templates", response_model=PaginatedResponse[TaxPromptTemplatesOut])
async def list_tax_prompt_templates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxPromptTemplatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["prompt_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_prompt_templates/{entity_id}", response_model=TaxPromptTemplatesOut)
async def get_tax_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxPromptTemplatesService(db).get(entity_id)

@router.post("/tax_prompt_templates", response_model=TaxPromptTemplatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_prompt_templates(
    data: TaxPromptTemplatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPromptTemplatesService(db).create(data)

@router.put("/tax_prompt_templates/{entity_id}", response_model=TaxPromptTemplatesOut)
async def update_tax_prompt_templates(
    entity_id: uuid.UUID,
    data: TaxPromptTemplatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxPromptTemplatesService(db).update(entity_id, data)

@router.delete("/tax_prompt_templates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_prompt_templates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxPromptTemplatesService(db).delete(entity_id)

@router.get("/tax_rate_tiers", response_model=PaginatedResponse[TaxRateTiersOut])
async def list_tax_rate_tiers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRateTiersService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_rate_tiers/{entity_id}", response_model=TaxRateTiersOut)
async def get_tax_rate_tiers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRateTiersService(db).get(entity_id)

@router.post("/tax_rate_tiers", response_model=TaxRateTiersOut, status_code=status.HTTP_201_CREATED)
async def create_tax_rate_tiers(
    data: TaxRateTiersCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRateTiersService(db).create(data)

@router.put("/tax_rate_tiers/{entity_id}", response_model=TaxRateTiersOut)
async def update_tax_rate_tiers(
    entity_id: uuid.UUID,
    data: TaxRateTiersUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRateTiersService(db).update(entity_id, data)

@router.delete("/tax_rate_tiers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_rate_tiers(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRateTiersService(db).delete(entity_id)

@router.get("/tax_rates", response_model=PaginatedResponse[TaxRatesOut])
async def list_tax_rates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRatesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_rates/{entity_id}", response_model=TaxRatesOut)
async def get_tax_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRatesService(db).get(entity_id)

@router.post("/tax_rates", response_model=TaxRatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_rates(
    data: TaxRatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRatesService(db).create(data)

@router.put("/tax_rates/{entity_id}", response_model=TaxRatesOut)
async def update_tax_rates(
    entity_id: uuid.UUID,
    data: TaxRatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRatesService(db).update(entity_id, data)

@router.delete("/tax_rates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_rates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRatesService(db).delete(entity_id)

@router.get("/tax_reconciliations", response_model=PaginatedResponse[TaxReconciliationsOut])
async def list_tax_reconciliations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxReconciliationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_reconciliations/{entity_id}", response_model=TaxReconciliationsOut)
async def get_tax_reconciliations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxReconciliationsService(db).get(entity_id)

@router.post("/tax_reconciliations", response_model=TaxReconciliationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_reconciliations(
    data: TaxReconciliationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReconciliationsService(db).create(data)

@router.put("/tax_reconciliations/{entity_id}", response_model=TaxReconciliationsOut)
async def update_tax_reconciliations(
    entity_id: uuid.UUID,
    data: TaxReconciliationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReconciliationsService(db).update(entity_id, data)

@router.delete("/tax_reconciliations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_reconciliations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxReconciliationsService(db).delete(entity_id)

@router.get("/tax_refunds", response_model=PaginatedResponse[TaxRefundsOut])
async def list_tax_refunds(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRefundsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["claim_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_refunds/{entity_id}", response_model=TaxRefundsOut)
async def get_tax_refunds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRefundsService(db).get(entity_id)

@router.post("/tax_refunds", response_model=TaxRefundsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_refunds(
    data: TaxRefundsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRefundsService(db).create(data)

@router.put("/tax_refunds/{entity_id}", response_model=TaxRefundsOut)
async def update_tax_refunds(
    entity_id: uuid.UUID,
    data: TaxRefundsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRefundsService(db).update(entity_id, data)

@router.delete("/tax_refunds/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_refunds(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRefundsService(db).delete(entity_id)

@router.get("/tax_regime_attachments", response_model=PaginatedResponse[TaxRegimeAttachmentsOut])
async def list_tax_regime_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRegimeAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["file_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_regime_attachments/{entity_id}", response_model=TaxRegimeAttachmentsOut)
async def get_tax_regime_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRegimeAttachmentsService(db).get(entity_id)

@router.post("/tax_regime_attachments", response_model=TaxRegimeAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_regime_attachments(
    data: TaxRegimeAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimeAttachmentsService(db).create(data)

@router.put("/tax_regime_attachments/{entity_id}", response_model=TaxRegimeAttachmentsOut)
async def update_tax_regime_attachments(
    entity_id: uuid.UUID,
    data: TaxRegimeAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimeAttachmentsService(db).update(entity_id, data)

@router.delete("/tax_regime_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_regime_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRegimeAttachmentsService(db).delete(entity_id)

@router.get("/tax_regime_rules", response_model=PaginatedResponse[TaxRegimeRulesOut])
async def list_tax_regime_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRegimeRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_regime_rules/{entity_id}", response_model=TaxRegimeRulesOut)
async def get_tax_regime_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRegimeRulesService(db).get(entity_id)

@router.post("/tax_regime_rules", response_model=TaxRegimeRulesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_regime_rules(
    data: TaxRegimeRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimeRulesService(db).create(data)

@router.put("/tax_regime_rules/{entity_id}", response_model=TaxRegimeRulesOut)
async def update_tax_regime_rules(
    entity_id: uuid.UUID,
    data: TaxRegimeRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimeRulesService(db).update(entity_id, data)

@router.delete("/tax_regime_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_regime_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRegimeRulesService(db).delete(entity_id)

@router.get("/tax_regimes", response_model=PaginatedResponse[TaxRegimesOut])
async def list_tax_regimes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRegimesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["country_code", "tax_regime_code", "tax_regime_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_regimes/{entity_id}", response_model=TaxRegimesOut)
async def get_tax_regimes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRegimesService(db).get(entity_id)

@router.post("/tax_regimes", response_model=TaxRegimesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_regimes(
    data: TaxRegimesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimesService(db).create(data)

@router.put("/tax_regimes/{entity_id}", response_model=TaxRegimesOut)
async def update_tax_regimes(
    entity_id: uuid.UUID,
    data: TaxRegimesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegimesService(db).update(entity_id, data)

@router.delete("/tax_regimes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_regimes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRegimesService(db).delete(entity_id)

@router.get("/tax_registrations", response_model=PaginatedResponse[TaxRegistrationsOut])
async def list_tax_registrations(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRegistrationsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["registration_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_registrations/{entity_id}", response_model=TaxRegistrationsOut)
async def get_tax_registrations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRegistrationsService(db).get(entity_id)

@router.post("/tax_registrations", response_model=TaxRegistrationsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_registrations(
    data: TaxRegistrationsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegistrationsService(db).create(data)

@router.put("/tax_registrations/{entity_id}", response_model=TaxRegistrationsOut)
async def update_tax_registrations(
    entity_id: uuid.UUID,
    data: TaxRegistrationsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRegistrationsService(db).update(entity_id, data)

@router.delete("/tax_registrations/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_registrations(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRegistrationsService(db).delete(entity_id)

@router.get("/tax_report_types", response_model=PaginatedResponse[TaxReportTypesOut])
async def list_tax_report_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxReportTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["report_type_code", "report_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_report_types/{entity_id}", response_model=TaxReportTypesOut)
async def get_tax_report_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxReportTypesService(db).get(entity_id)

@router.post("/tax_report_types", response_model=TaxReportTypesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_report_types(
    data: TaxReportTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReportTypesService(db).create(data)

@router.put("/tax_report_types/{entity_id}", response_model=TaxReportTypesOut)
async def update_tax_report_types(
    entity_id: uuid.UUID,
    data: TaxReportTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReportTypesService(db).update(entity_id, data)

@router.delete("/tax_report_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_report_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxReportTypesService(db).delete(entity_id)

@router.get("/tax_reports", response_model=PaginatedResponse[TaxReportsOut])
async def list_tax_reports(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxReportsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["report_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_reports/{entity_id}", response_model=TaxReportsOut)
async def get_tax_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxReportsService(db).get(entity_id)

@router.post("/tax_reports", response_model=TaxReportsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_reports(
    data: TaxReportsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReportsService(db).create(data)

@router.put("/tax_reports/{entity_id}", response_model=TaxReportsOut)
async def update_tax_reports(
    entity_id: uuid.UUID,
    data: TaxReportsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReportsService(db).update(entity_id, data)

@router.delete("/tax_reports/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_reports(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxReportsService(db).delete(entity_id)

@router.get("/tax_return_attachments", response_model=PaginatedResponse[TaxReturnAttachmentsOut])
async def list_tax_return_attachments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxReturnAttachmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["file_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_return_attachments/{entity_id}", response_model=TaxReturnAttachmentsOut)
async def get_tax_return_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxReturnAttachmentsService(db).get(entity_id)

@router.post("/tax_return_attachments", response_model=TaxReturnAttachmentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_return_attachments(
    data: TaxReturnAttachmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReturnAttachmentsService(db).create(data)

@router.put("/tax_return_attachments/{entity_id}", response_model=TaxReturnAttachmentsOut)
async def update_tax_return_attachments(
    entity_id: uuid.UUID,
    data: TaxReturnAttachmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReturnAttachmentsService(db).update(entity_id, data)

@router.delete("/tax_return_attachments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_return_attachments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxReturnAttachmentsService(db).delete(entity_id)

@router.get("/tax_returns", response_model=PaginatedResponse[TaxReturnsOut])
async def list_tax_returns(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxReturnsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["return_number", "period_name", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_returns/{entity_id}", response_model=TaxReturnsOut)
async def get_tax_returns(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxReturnsService(db).get(entity_id)

@router.post("/tax_returns", response_model=TaxReturnsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_returns(
    data: TaxReturnsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReturnsService(db).create(data)

@router.put("/tax_returns/{entity_id}", response_model=TaxReturnsOut)
async def update_tax_returns(
    entity_id: uuid.UUID,
    data: TaxReturnsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxReturnsService(db).update(entity_id, data)

@router.delete("/tax_returns/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_returns(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxReturnsService(db).delete(entity_id)

@router.get("/tax_rule_conditions", response_model=PaginatedResponse[TaxRuleConditionsOut])
async def list_tax_rule_conditions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRuleConditionsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["field_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_rule_conditions/{entity_id}", response_model=TaxRuleConditionsOut)
async def get_tax_rule_conditions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRuleConditionsService(db).get(entity_id)

@router.post("/tax_rule_conditions", response_model=TaxRuleConditionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_rule_conditions(
    data: TaxRuleConditionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRuleConditionsService(db).create(data)

@router.put("/tax_rule_conditions/{entity_id}", response_model=TaxRuleConditionsOut)
async def update_tax_rule_conditions(
    entity_id: uuid.UUID,
    data: TaxRuleConditionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRuleConditionsService(db).update(entity_id, data)

@router.delete("/tax_rule_conditions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_rule_conditions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRuleConditionsService(db).delete(entity_id)

@router.get("/tax_rule_tax_codes", response_model=PaginatedResponse[TaxRuleTaxCodesOut])
async def list_tax_rule_tax_codes(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRuleTaxCodesService(db)
    result = await svc.list(page, page_size, filters=None)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_rule_tax_codes/{entity_id}", response_model=TaxRuleTaxCodesOut)
async def get_tax_rule_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRuleTaxCodesService(db).get(entity_id)

@router.post("/tax_rule_tax_codes", response_model=TaxRuleTaxCodesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_rule_tax_codes(
    data: TaxRuleTaxCodesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRuleTaxCodesService(db).create(data)

@router.put("/tax_rule_tax_codes/{entity_id}", response_model=TaxRuleTaxCodesOut)
async def update_tax_rule_tax_codes(
    entity_id: uuid.UUID,
    data: TaxRuleTaxCodesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRuleTaxCodesService(db).update(entity_id, data)

@router.delete("/tax_rule_tax_codes/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_rule_tax_codes(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRuleTaxCodesService(db).delete(entity_id)

@router.get("/tax_rules", response_model=PaginatedResponse[TaxRulesOut])
async def list_tax_rules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxRulesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["rule_code", "rule_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_rules/{entity_id}", response_model=TaxRulesOut)
async def get_tax_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxRulesService(db).get(entity_id)

@router.post("/tax_rules", response_model=TaxRulesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_rules(
    data: TaxRulesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRulesService(db).create(data)

@router.put("/tax_rules/{entity_id}", response_model=TaxRulesOut)
async def update_tax_rules(
    entity_id: uuid.UUID,
    data: TaxRulesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxRulesService(db).update(entity_id, data)

@router.delete("/tax_rules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_rules(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxRulesService(db).delete(entity_id)

@router.get("/tax_scenarios", response_model=PaginatedResponse[TaxScenariosOut])
async def list_tax_scenarios(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxScenariosService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["scenario_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_scenarios/{entity_id}", response_model=TaxScenariosOut)
async def get_tax_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxScenariosService(db).get(entity_id)

@router.post("/tax_scenarios", response_model=TaxScenariosOut, status_code=status.HTTP_201_CREATED)
async def create_tax_scenarios(
    data: TaxScenariosCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxScenariosService(db).create(data)

@router.put("/tax_scenarios/{entity_id}", response_model=TaxScenariosOut)
async def update_tax_scenarios(
    entity_id: uuid.UUID,
    data: TaxScenariosUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxScenariosService(db).update(entity_id, data)

@router.delete("/tax_scenarios/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_scenarios(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxScenariosService(db).delete(entity_id)

@router.get("/tax_scipy_analyses", response_model=PaginatedResponse[TaxScipyAnalysesOut])
async def list_tax_scipy_analyses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxScipyAnalysesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["analysis_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_scipy_analyses/{entity_id}", response_model=TaxScipyAnalysesOut)
async def get_tax_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxScipyAnalysesService(db).get(entity_id)

@router.post("/tax_scipy_analyses", response_model=TaxScipyAnalysesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_scipy_analyses(
    data: TaxScipyAnalysesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxScipyAnalysesService(db).create(data)

@router.put("/tax_scipy_analyses/{entity_id}", response_model=TaxScipyAnalysesOut)
async def update_tax_scipy_analyses(
    entity_id: uuid.UUID,
    data: TaxScipyAnalysesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxScipyAnalysesService(db).update(entity_id, data)

@router.delete("/tax_scipy_analyses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_scipy_analyses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxScipyAnalysesService(db).delete(entity_id)

@router.get("/tax_solver_configs", response_model=PaginatedResponse[TaxSolverConfigsOut])
async def list_tax_solver_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxSolverConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["solver_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_solver_configs/{entity_id}", response_model=TaxSolverConfigsOut)
async def get_tax_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxSolverConfigsService(db).get(entity_id)

@router.post("/tax_solver_configs", response_model=TaxSolverConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_solver_configs(
    data: TaxSolverConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxSolverConfigsService(db).create(data)

@router.put("/tax_solver_configs/{entity_id}", response_model=TaxSolverConfigsOut)
async def update_tax_solver_configs(
    entity_id: uuid.UUID,
    data: TaxSolverConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxSolverConfigsService(db).update(entity_id, data)

@router.delete("/tax_solver_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_solver_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxSolverConfigsService(db).delete(entity_id)

@router.get("/tax_statuses", response_model=PaginatedResponse[TaxStatusesOut])
async def list_tax_statuses(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxStatusesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["tax_status_code", "tax_status_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_statuses/{entity_id}", response_model=TaxStatusesOut)
async def get_tax_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxStatusesService(db).get(entity_id)

@router.post("/tax_statuses", response_model=TaxStatusesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_statuses(
    data: TaxStatusesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxStatusesService(db).create(data)

@router.put("/tax_statuses/{entity_id}", response_model=TaxStatusesOut)
async def update_tax_statuses(
    entity_id: uuid.UUID,
    data: TaxStatusesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxStatusesService(db).update(entity_id, data)

@router.delete("/tax_statuses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_statuses(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxStatusesService(db).delete(entity_id)

@router.get("/tax_training_runs", response_model=PaginatedResponse[TaxTrainingRunsOut])
async def list_tax_training_runs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTrainingRunsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_training_runs/{entity_id}", response_model=TaxTrainingRunsOut)
async def get_tax_training_runs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTrainingRunsService(db).get(entity_id)

@router.post("/tax_training_runs", response_model=TaxTrainingRunsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_training_runs(
    data: TaxTrainingRunsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTrainingRunsService(db).create(data)

@router.put("/tax_training_runs/{entity_id}", response_model=TaxTrainingRunsOut)
async def update_tax_training_runs(
    entity_id: uuid.UUID,
    data: TaxTrainingRunsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTrainingRunsService(db).update(entity_id, data)

@router.delete("/tax_training_runs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_training_runs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTrainingRunsService(db).delete(entity_id)

@router.get("/tax_transactions", response_model=PaginatedResponse[TaxTransactionsOut])
async def list_tax_transactions(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTransactionsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["doc_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_transactions/{entity_id}", response_model=TaxTransactionsOut)
async def get_tax_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTransactionsService(db).get(entity_id)

@router.post("/tax_transactions", response_model=TaxTransactionsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_transactions(
    data: TaxTransactionsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransactionsService(db).create(data)

@router.put("/tax_transactions/{entity_id}", response_model=TaxTransactionsOut)
async def update_tax_transactions(
    entity_id: uuid.UUID,
    data: TaxTransactionsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransactionsService(db).update(entity_id, data)

@router.delete("/tax_transactions/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_transactions(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTransactionsService(db).delete(entity_id)

@router.get("/tax_transfer_pricing_adjustments", response_model=PaginatedResponse[TaxTransferPricingAdjustmentsOut])
async def list_tax_transfer_pricing_adjustments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTransferPricingAdjustmentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_transfer_pricing_adjustments/{entity_id}", response_model=TaxTransferPricingAdjustmentsOut)
async def get_tax_transfer_pricing_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTransferPricingAdjustmentsService(db).get(entity_id)

@router.post("/tax_transfer_pricing_adjustments", response_model=TaxTransferPricingAdjustmentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_transfer_pricing_adjustments(
    data: TaxTransferPricingAdjustmentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingAdjustmentsService(db).create(data)

@router.put("/tax_transfer_pricing_adjustments/{entity_id}", response_model=TaxTransferPricingAdjustmentsOut)
async def update_tax_transfer_pricing_adjustments(
    entity_id: uuid.UUID,
    data: TaxTransferPricingAdjustmentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingAdjustmentsService(db).update(entity_id, data)

@router.delete("/tax_transfer_pricing_adjustments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_transfer_pricing_adjustments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTransferPricingAdjustmentsService(db).delete(entity_id)

@router.get("/tax_transfer_pricing_policies", response_model=PaginatedResponse[TaxTransferPricingPoliciesOut])
async def list_tax_transfer_pricing_policies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTransferPricingPoliciesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["policy_code", "policy_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_transfer_pricing_policies/{entity_id}", response_model=TaxTransferPricingPoliciesOut)
async def get_tax_transfer_pricing_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTransferPricingPoliciesService(db).get(entity_id)

@router.post("/tax_transfer_pricing_policies", response_model=TaxTransferPricingPoliciesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_transfer_pricing_policies(
    data: TaxTransferPricingPoliciesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingPoliciesService(db).create(data)

@router.put("/tax_transfer_pricing_policies/{entity_id}", response_model=TaxTransferPricingPoliciesOut)
async def update_tax_transfer_pricing_policies(
    entity_id: uuid.UUID,
    data: TaxTransferPricingPoliciesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingPoliciesService(db).update(entity_id, data)

@router.delete("/tax_transfer_pricing_policies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_transfer_pricing_policies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTransferPricingPoliciesService(db).delete(entity_id)

@router.get("/tax_transfer_pricing_studies", response_model=PaginatedResponse[TaxTransferPricingStudiesOut])
async def list_tax_transfer_pricing_studies(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTransferPricingStudiesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["study_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_transfer_pricing_studies/{entity_id}", response_model=TaxTransferPricingStudiesOut)
async def get_tax_transfer_pricing_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTransferPricingStudiesService(db).get(entity_id)

@router.post("/tax_transfer_pricing_studies", response_model=TaxTransferPricingStudiesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_transfer_pricing_studies(
    data: TaxTransferPricingStudiesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingStudiesService(db).create(data)

@router.put("/tax_transfer_pricing_studies/{entity_id}", response_model=TaxTransferPricingStudiesOut)
async def update_tax_transfer_pricing_studies(
    entity_id: uuid.UUID,
    data: TaxTransferPricingStudiesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTransferPricingStudiesService(db).update(entity_id, data)

@router.delete("/tax_transfer_pricing_studies/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_transfer_pricing_studies(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTransferPricingStudiesService(db).delete(entity_id)

@router.get("/tax_types", response_model=PaginatedResponse[TaxTypesOut])
async def list_tax_types(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxTypesService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["country_code", "tax_type_code", "tax_type_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_types/{entity_id}", response_model=TaxTypesOut)
async def get_tax_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxTypesService(db).get(entity_id)

@router.post("/tax_types", response_model=TaxTypesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_types(
    data: TaxTypesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTypesService(db).create(data)

@router.put("/tax_types/{entity_id}", response_model=TaxTypesOut)
async def update_tax_types(
    entity_id: uuid.UUID,
    data: TaxTypesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxTypesService(db).update(entity_id, data)

@router.delete("/tax_types/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_types(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxTypesService(db).delete(entity_id)

@router.get("/tax_vector_documents", response_model=PaginatedResponse[TaxVectorDocumentsOut])
async def list_tax_vector_documents(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxVectorDocumentsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["title"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_vector_documents/{entity_id}", response_model=TaxVectorDocumentsOut)
async def get_tax_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxVectorDocumentsService(db).get(entity_id)

@router.post("/tax_vector_documents", response_model=TaxVectorDocumentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_vector_documents(
    data: TaxVectorDocumentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxVectorDocumentsService(db).create(data)

@router.put("/tax_vector_documents/{entity_id}", response_model=TaxVectorDocumentsOut)
async def update_tax_vector_documents(
    entity_id: uuid.UUID,
    data: TaxVectorDocumentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxVectorDocumentsService(db).update(entity_id, data)

@router.delete("/tax_vector_documents/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_vector_documents(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxVectorDocumentsService(db).delete(entity_id)

@router.get("/tax_withholding_certificates", response_model=PaginatedResponse[TaxWithholdingCertificatesOut])
async def list_tax_withholding_certificates(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxWithholdingCertificatesService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["certificate_number", "currency_code"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_withholding_certificates/{entity_id}", response_model=TaxWithholdingCertificatesOut)
async def get_tax_withholding_certificates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxWithholdingCertificatesService(db).get(entity_id)

@router.post("/tax_withholding_certificates", response_model=TaxWithholdingCertificatesOut, status_code=status.HTTP_201_CREATED)
async def create_tax_withholding_certificates(
    data: TaxWithholdingCertificatesCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingCertificatesService(db).create(data)

@router.put("/tax_withholding_certificates/{entity_id}", response_model=TaxWithholdingCertificatesOut)
async def update_tax_withholding_certificates(
    entity_id: uuid.UUID,
    data: TaxWithholdingCertificatesUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingCertificatesService(db).update(entity_id, data)

@router.delete("/tax_withholding_certificates/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_withholding_certificates(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxWithholdingCertificatesService(db).delete(entity_id)

@router.get("/tax_withholding_configs", response_model=PaginatedResponse[TaxWithholdingConfigsOut])
async def list_tax_withholding_configs(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxWithholdingConfigsService(db)
    result = await svc.list(page, page_size, filters=None, search_cols=["wht_code", "wht_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_withholding_configs/{entity_id}", response_model=TaxWithholdingConfigsOut)
async def get_tax_withholding_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxWithholdingConfigsService(db).get(entity_id)

@router.post("/tax_withholding_configs", response_model=TaxWithholdingConfigsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_withholding_configs(
    data: TaxWithholdingConfigsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingConfigsService(db).create(data)

@router.put("/tax_withholding_configs/{entity_id}", response_model=TaxWithholdingConfigsOut)
async def update_tax_withholding_configs(
    entity_id: uuid.UUID,
    data: TaxWithholdingConfigsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingConfigsService(db).update(entity_id, data)

@router.delete("/tax_withholding_configs/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_withholding_configs(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxWithholdingConfigsService(db).delete(entity_id)

@router.get("/tax_withholding_payments", response_model=PaginatedResponse[TaxWithholdingPaymentsOut])
async def list_tax_withholding_payments(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100), status_filter: Optional[str] = Query(None, alias="status"), search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    svc = TaxWithholdingPaymentsService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters, search_cols=["reference_number"], search_term=search)
    return PaginatedResponse(**result.model_dump())

@router.get("/tax_withholding_payments/{entity_id}", response_model=TaxWithholdingPaymentsOut)
async def get_tax_withholding_payments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "view"),
):
    return await TaxWithholdingPaymentsService(db).get(entity_id)

@router.post("/tax_withholding_payments", response_model=TaxWithholdingPaymentsOut, status_code=status.HTTP_201_CREATED)
async def create_tax_withholding_payments(
    data: TaxWithholdingPaymentsCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingPaymentsService(db).create(data)

@router.put("/tax_withholding_payments/{entity_id}", response_model=TaxWithholdingPaymentsOut)
async def update_tax_withholding_payments(
    entity_id: uuid.UUID,
    data: TaxWithholdingPaymentsUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    return await TaxWithholdingPaymentsService(db).update(entity_id, data)

@router.delete("/tax_withholding_payments/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tax_withholding_payments(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("tax", "manage"),
):
    await TaxWithholdingPaymentsService(db).delete(entity_id)
