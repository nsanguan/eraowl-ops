from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.tax.models import PartnerTaxProfiles
from app.modules.tax.models import TaxAccounts
from app.modules.tax.models import TaxAgentDefinitions
from app.modules.tax.models import TaxAiAgentLogs
from app.modules.tax.models import TaxAiDecisions
from app.modules.tax.models import TaxAiModelRegistry
from app.modules.tax.models import TaxAiWorkflowState
from app.modules.tax.models import TaxAlgorithms
from app.modules.tax.models import TaxArchiveContainers
from app.modules.tax.models import TaxAssessmentDisputes
from app.modules.tax.models import TaxAssessments
from app.modules.tax.models import TaxAuditFindings
from app.modules.tax.models import TaxAuditResponses
from app.modules.tax.models import TaxAuditRouteLocations
from app.modules.tax.models import TaxAuditRoutes
from app.modules.tax.models import TaxAudits
from app.modules.tax.models import TaxAuthorities
from app.modules.tax.models import TaxAuthorityContacts
from app.modules.tax.models import TaxCertificateJurisdictions
from app.modules.tax.models import TaxCertificates
from app.modules.tax.models import TaxClassificationRules
from app.modules.tax.models import TaxClassifications
from app.modules.tax.models import TaxCodes
from app.modules.tax.models import TaxComplianceCalendars
from app.modules.tax.models import TaxComplianceObligations
from app.modules.tax.models import TaxCredits
from app.modules.tax.models import TaxCustomsBonds
from app.modules.tax.models import TaxCustomsDeclarations
from app.modules.tax.models import TaxDocumentArchives
from app.modules.tax.models import TaxEinvoiceConfigs
from app.modules.tax.models import TaxEinvoiceResponses
from app.modules.tax.models import TaxEinvoices
from app.modules.tax.models import TaxEntityRelationships
from app.modules.tax.models import TaxEntityStructures
from app.modules.tax.models import TaxExemptionJurisdictions
from app.modules.tax.models import TaxExemptions
from app.modules.tax.models import TaxFilings
from app.modules.tax.models import TaxHsCodeDutyRates
from app.modules.tax.models import TaxHsCodes
from app.modules.tax.models import TaxIntegrationConnections
from app.modules.tax.models import TaxIntegrationLogs
from app.modules.tax.models import TaxJurisdictionAddresses
from app.modules.tax.models import TaxJurisdictionAgreements
from app.modules.tax.models import TaxJurisdictions
from app.modules.tax.models import TaxLanggraphExecutions
from app.modules.tax.models import TaxLanggraphStates
from app.modules.tax.models import TaxLanggraphWorkflows
from app.modules.tax.models import TaxLines
from app.modules.tax.models import TaxLlmConfigs
from app.modules.tax.models import TaxMlModels
from app.modules.tax.models import TaxOptimizationProblems
from app.modules.tax.models import TaxOptimizationScenarios
from app.modules.tax.models import TaxOptimizationSolutions
from app.modules.tax.models import TaxOrtoolsProblems
from app.modules.tax.models import TaxPenalties
from app.modules.tax.models import TaxPenaltyWaivers
from app.modules.tax.models import TaxPeriods
from app.modules.tax.models import TaxPredictionActuals
from app.modules.tax.models import TaxPredictions
from app.modules.tax.models import TaxPromptTemplates
from app.modules.tax.models import TaxRateTiers
from app.modules.tax.models import TaxRates
from app.modules.tax.models import TaxReconciliations
from app.modules.tax.models import TaxRefunds
from app.modules.tax.models import TaxRegimeAttachments
from app.modules.tax.models import TaxRegimeRules
from app.modules.tax.models import TaxRegimes
from app.modules.tax.models import TaxRegistrations
from app.modules.tax.models import TaxReportTypes
from app.modules.tax.models import TaxReports
from app.modules.tax.models import TaxReturnAttachments
from app.modules.tax.models import TaxReturns
from app.modules.tax.models import TaxRuleConditions
from app.modules.tax.models import TaxRuleTaxCodes
from app.modules.tax.models import TaxRules
from app.modules.tax.models import TaxScenarios
from app.modules.tax.models import TaxScipyAnalyses
from app.modules.tax.models import TaxSolverConfigs
from app.modules.tax.models import TaxStatuses
from app.modules.tax.models import TaxTrainingRuns
from app.modules.tax.models import TaxTransactions
from app.modules.tax.models import TaxTransferPricingAdjustments
from app.modules.tax.models import TaxTransferPricingPolicies
from app.modules.tax.models import TaxTransferPricingStudies
from app.modules.tax.models import TaxTypes
from app.modules.tax.models import TaxVectorDocuments
from app.modules.tax.models import TaxWithholdingCertificates
from app.modules.tax.models import TaxWithholdingConfigs
from app.modules.tax.models import TaxWithholdingPayments

class PartnerTaxProfilesService(BaseCRUDService[PartnerTaxProfiles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PartnerTaxProfiles)

class TaxAccountsService(BaseCRUDService[TaxAccounts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAccounts)

class TaxAgentDefinitionsService(BaseCRUDService[TaxAgentDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAgentDefinitions)

class TaxAiAgentLogsService(BaseCRUDService[TaxAiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAiAgentLogs)

class TaxAiDecisionsService(BaseCRUDService[TaxAiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAiDecisions)

class TaxAiModelRegistryService(BaseCRUDService[TaxAiModelRegistry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAiModelRegistry)

class TaxAiWorkflowStateService(BaseCRUDService[TaxAiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAiWorkflowState)

class TaxAlgorithmsService(BaseCRUDService[TaxAlgorithms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAlgorithms)

class TaxArchiveContainersService(BaseCRUDService[TaxArchiveContainers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxArchiveContainers)

class TaxAssessmentDisputesService(BaseCRUDService[TaxAssessmentDisputes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAssessmentDisputes)

class TaxAssessmentsService(BaseCRUDService[TaxAssessments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAssessments)

class TaxAuditFindingsService(BaseCRUDService[TaxAuditFindings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuditFindings)

class TaxAuditResponsesService(BaseCRUDService[TaxAuditResponses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuditResponses)

class TaxAuditRouteLocationsService(BaseCRUDService[TaxAuditRouteLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuditRouteLocations)

class TaxAuditRoutesService(BaseCRUDService[TaxAuditRoutes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuditRoutes)

class TaxAuditsService(BaseCRUDService[TaxAudits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAudits)

class TaxAuthoritiesService(BaseCRUDService[TaxAuthorities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuthorities)

class TaxAuthorityContactsService(BaseCRUDService[TaxAuthorityContacts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxAuthorityContacts)

class TaxCertificateJurisdictionsService(BaseCRUDService[TaxCertificateJurisdictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCertificateJurisdictions)

class TaxCertificatesService(BaseCRUDService[TaxCertificates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCertificates)

class TaxClassificationRulesService(BaseCRUDService[TaxClassificationRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxClassificationRules)

class TaxClassificationsService(BaseCRUDService[TaxClassifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxClassifications)

class TaxCodesService(BaseCRUDService[TaxCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCodes)

class TaxComplianceCalendarsService(BaseCRUDService[TaxComplianceCalendars]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxComplianceCalendars)

class TaxComplianceObligationsService(BaseCRUDService[TaxComplianceObligations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxComplianceObligations)

class TaxCreditsService(BaseCRUDService[TaxCredits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCredits)

class TaxCustomsBondsService(BaseCRUDService[TaxCustomsBonds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCustomsBonds)

class TaxCustomsDeclarationsService(BaseCRUDService[TaxCustomsDeclarations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxCustomsDeclarations)

class TaxDocumentArchivesService(BaseCRUDService[TaxDocumentArchives]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxDocumentArchives)

class TaxEinvoiceConfigsService(BaseCRUDService[TaxEinvoiceConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxEinvoiceConfigs)

class TaxEinvoiceResponsesService(BaseCRUDService[TaxEinvoiceResponses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxEinvoiceResponses)

class TaxEinvoicesService(BaseCRUDService[TaxEinvoices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxEinvoices)

class TaxEntityRelationshipsService(BaseCRUDService[TaxEntityRelationships]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxEntityRelationships)

class TaxEntityStructuresService(BaseCRUDService[TaxEntityStructures]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxEntityStructures)

class TaxExemptionJurisdictionsService(BaseCRUDService[TaxExemptionJurisdictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxExemptionJurisdictions)

class TaxExemptionsService(BaseCRUDService[TaxExemptions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxExemptions)

class TaxFilingsService(BaseCRUDService[TaxFilings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxFilings)

class TaxHsCodeDutyRatesService(BaseCRUDService[TaxHsCodeDutyRates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxHsCodeDutyRates)

class TaxHsCodesService(BaseCRUDService[TaxHsCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxHsCodes)

class TaxIntegrationConnectionsService(BaseCRUDService[TaxIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxIntegrationConnections)

class TaxIntegrationLogsService(BaseCRUDService[TaxIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxIntegrationLogs)

class TaxJurisdictionAddressesService(BaseCRUDService[TaxJurisdictionAddresses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxJurisdictionAddresses)

class TaxJurisdictionAgreementsService(BaseCRUDService[TaxJurisdictionAgreements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxJurisdictionAgreements)

class TaxJurisdictionsService(BaseCRUDService[TaxJurisdictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxJurisdictions)

class TaxLanggraphExecutionsService(BaseCRUDService[TaxLanggraphExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxLanggraphExecutions)

class TaxLanggraphStatesService(BaseCRUDService[TaxLanggraphStates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxLanggraphStates)

class TaxLanggraphWorkflowsService(BaseCRUDService[TaxLanggraphWorkflows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxLanggraphWorkflows)

class TaxLinesService(BaseCRUDService[TaxLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxLines)

class TaxLlmConfigsService(BaseCRUDService[TaxLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxLlmConfigs)

class TaxMlModelsService(BaseCRUDService[TaxMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxMlModels)

class TaxOptimizationProblemsService(BaseCRUDService[TaxOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxOptimizationProblems)

class TaxOptimizationScenariosService(BaseCRUDService[TaxOptimizationScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxOptimizationScenarios)

class TaxOptimizationSolutionsService(BaseCRUDService[TaxOptimizationSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxOptimizationSolutions)

class TaxOrtoolsProblemsService(BaseCRUDService[TaxOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxOrtoolsProblems)

class TaxPenaltiesService(BaseCRUDService[TaxPenalties]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPenalties)

class TaxPenaltyWaiversService(BaseCRUDService[TaxPenaltyWaivers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPenaltyWaivers)

class TaxPeriodsService(BaseCRUDService[TaxPeriods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPeriods)

class TaxPredictionActualsService(BaseCRUDService[TaxPredictionActuals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPredictionActuals)

class TaxPredictionsService(BaseCRUDService[TaxPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPredictions)

class TaxPromptTemplatesService(BaseCRUDService[TaxPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxPromptTemplates)

class TaxRateTiersService(BaseCRUDService[TaxRateTiers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRateTiers)

class TaxRatesService(BaseCRUDService[TaxRates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRates)

class TaxReconciliationsService(BaseCRUDService[TaxReconciliations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxReconciliations)

class TaxRefundsService(BaseCRUDService[TaxRefunds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRefunds)

class TaxRegimeAttachmentsService(BaseCRUDService[TaxRegimeAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRegimeAttachments)

class TaxRegimeRulesService(BaseCRUDService[TaxRegimeRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRegimeRules)

class TaxRegimesService(BaseCRUDService[TaxRegimes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRegimes)

class TaxRegistrationsService(BaseCRUDService[TaxRegistrations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRegistrations)

class TaxReportTypesService(BaseCRUDService[TaxReportTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxReportTypes)

class TaxReportsService(BaseCRUDService[TaxReports]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxReports)

class TaxReturnAttachmentsService(BaseCRUDService[TaxReturnAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxReturnAttachments)

class TaxReturnsService(BaseCRUDService[TaxReturns]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxReturns)

class TaxRuleConditionsService(BaseCRUDService[TaxRuleConditions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRuleConditions)

class TaxRuleTaxCodesService(BaseCRUDService[TaxRuleTaxCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRuleTaxCodes)

class TaxRulesService(BaseCRUDService[TaxRules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxRules)

class TaxScenariosService(BaseCRUDService[TaxScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxScenarios)

class TaxScipyAnalysesService(BaseCRUDService[TaxScipyAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxScipyAnalyses)

class TaxSolverConfigsService(BaseCRUDService[TaxSolverConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxSolverConfigs)

class TaxStatusesService(BaseCRUDService[TaxStatuses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxStatuses)

class TaxTrainingRunsService(BaseCRUDService[TaxTrainingRuns]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTrainingRuns)

class TaxTransactionsService(BaseCRUDService[TaxTransactions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTransactions)

class TaxTransferPricingAdjustmentsService(BaseCRUDService[TaxTransferPricingAdjustments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTransferPricingAdjustments)

class TaxTransferPricingPoliciesService(BaseCRUDService[TaxTransferPricingPolicies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTransferPricingPolicies)

class TaxTransferPricingStudiesService(BaseCRUDService[TaxTransferPricingStudies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTransferPricingStudies)

class TaxTypesService(BaseCRUDService[TaxTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxTypes)

class TaxVectorDocumentsService(BaseCRUDService[TaxVectorDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxVectorDocuments)

class TaxWithholdingCertificatesService(BaseCRUDService[TaxWithholdingCertificates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxWithholdingCertificates)

class TaxWithholdingConfigsService(BaseCRUDService[TaxWithholdingConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxWithholdingConfigs)

class TaxWithholdingPaymentsService(BaseCRUDService[TaxWithholdingPayments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TaxWithholdingPayments)
