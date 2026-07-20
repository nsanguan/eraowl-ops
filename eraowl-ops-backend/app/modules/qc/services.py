from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.qc.models import AiAgentLogs
from app.modules.qc.models import AiDecisions
from app.modules.qc.models import AiModelRegistry
from app.modules.qc.models import AiWorkflowState
from app.modules.qc.models import InspectionChecklist
from app.modules.qc.models import InspectionOrders
from app.modules.qc.models import InspectionPlans
from app.modules.qc.models import InspectionResults
from app.modules.qc.models import QcAgentDefinitions
from app.modules.qc.models import QcAlgorithms
from app.modules.qc.models import QcAuditFindings
from app.modules.qc.models import QcAudits
from app.modules.qc.models import QcCapaActions
from app.modules.qc.models import QcCapaHeaders
from app.modules.qc.models import QcCharacteristicValueSets
from app.modules.qc.models import QcCharacteristics
from app.modules.qc.models import QcComplaintInvestigations
from app.modules.qc.models import QcControlPlanCharacteristics
from app.modules.qc.models import QcControlPlans
from app.modules.qc.models import QcCostOfQuality
from app.modules.qc.models import QcCustomerComplaints
from app.modules.qc.models import QcDefectMaster
from app.modules.qc.models import QcDefectOccurrences
from app.modules.qc.models import QcDocuments
from app.modules.qc.models import QcEquipmentCalibration
from app.modules.qc.models import QcFailureAnalysis
from app.modules.qc.models import QcFmeaActions
from app.modules.qc.models import QcFmeaHeaders
from app.modules.qc.models import QcFmeaItems
from app.modules.qc.models import QcHolds
from app.modules.qc.models import QcInspectionEquipment
from app.modules.qc.models import QcInspectionLots
from app.modules.qc.models import QcInspectionRoutes
from app.modules.qc.models import QcInspections
from app.modules.qc.models import QcIntegrationConnections
from app.modules.qc.models import QcIntegrationLogs
from app.modules.qc.models import QcKpiActuals
from app.modules.qc.models import QcKpiDefinitions
from app.modules.qc.models import QcLanggraphExecutions
from app.modules.qc.models import QcLanggraphStates
from app.modules.qc.models import QcLanggraphWorkflows
from app.modules.qc.models import QcLlmConfigs
from app.modules.qc.models import QcLotDispositions
from app.modules.qc.models import QcMlModels
from app.modules.qc.models import QcMsaMeasurements
from app.modules.qc.models import QcMsaStudies
from app.modules.qc.models import QcNcrAttachments
from app.modules.qc.models import QcNcrContainment
from app.modules.qc.models import QcNcrHeaders
from app.modules.qc.models import QcNotifications
from app.modules.qc.models import QcOptimizationProblems
from app.modules.qc.models import QcOrtoolsProblems
from app.modules.qc.models import QcPlanAttachments
from app.modules.qc.models import QcPlanElements
from app.modules.qc.models import QcPlanTriggers
from app.modules.qc.models import QcPlans
from app.modules.qc.models import QcPpapSubmissions
from app.modules.qc.models import QcPredictions
from app.modules.qc.models import QcPromptTemplates
from app.modules.qc.models import QcRootCauseAnalysis
from app.modules.qc.models import QcRootCauseCauses
from app.modules.qc.models import QcSampleContainers
from app.modules.qc.models import QcSamplePackingResults
from app.modules.qc.models import QcSamplingPlanLines
from app.modules.qc.models import QcSamplingPlans
from app.modules.qc.models import QcScenarios
from app.modules.qc.models import QcScipyAnalyses
from app.modules.qc.models import QcSolverConfigs
from app.modules.qc.models import QcSpcAlerts
from app.modules.qc.models import QcSpcCharts
from app.modules.qc.models import QcSpcDataPoints
from app.modules.qc.models import QcSpecLimits
from app.modules.qc.models import QcSpecs
from app.modules.qc.models import QcSupplierProfiles
from app.modules.qc.models import QcSupplierScorecards
from app.modules.qc.models import QcTestEquipment
from app.modules.qc.models import QcTestMethods
from app.modules.qc.models import QcTestResultLines
from app.modules.qc.models import QcTestResults
from app.modules.qc.models import QcTrainingAttendees
from app.modules.qc.models import QcTrainingCourses
from app.modules.qc.models import QcVectorDocuments

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiModelRegistryService(BaseCRUDService[AiModelRegistry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiModelRegistry)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class InspectionChecklistService(BaseCRUDService[InspectionChecklist]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionChecklist)

class InspectionOrdersService(BaseCRUDService[InspectionOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionOrders)

class InspectionPlansService(BaseCRUDService[InspectionPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionPlans)

class InspectionResultsService(BaseCRUDService[InspectionResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InspectionResults)

class QcAgentDefinitionsService(BaseCRUDService[QcAgentDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcAgentDefinitions)

class QcAlgorithmsService(BaseCRUDService[QcAlgorithms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcAlgorithms)

class QcAuditFindingsService(BaseCRUDService[QcAuditFindings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcAuditFindings)

class QcAuditsService(BaseCRUDService[QcAudits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcAudits)

class QcCapaActionsService(BaseCRUDService[QcCapaActions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCapaActions)

class QcCapaHeadersService(BaseCRUDService[QcCapaHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCapaHeaders)

class QcCharacteristicValueSetsService(BaseCRUDService[QcCharacteristicValueSets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCharacteristicValueSets)

class QcCharacteristicsService(BaseCRUDService[QcCharacteristics]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCharacteristics)

class QcComplaintInvestigationsService(BaseCRUDService[QcComplaintInvestigations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcComplaintInvestigations)

class QcControlPlanCharacteristicsService(BaseCRUDService[QcControlPlanCharacteristics]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcControlPlanCharacteristics)

class QcControlPlansService(BaseCRUDService[QcControlPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcControlPlans)

class QcCostOfQualityService(BaseCRUDService[QcCostOfQuality]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCostOfQuality)

class QcCustomerComplaintsService(BaseCRUDService[QcCustomerComplaints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcCustomerComplaints)

class QcDefectMasterService(BaseCRUDService[QcDefectMaster]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcDefectMaster)

class QcDefectOccurrencesService(BaseCRUDService[QcDefectOccurrences]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcDefectOccurrences)

class QcDocumentsService(BaseCRUDService[QcDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcDocuments)

class QcEquipmentCalibrationService(BaseCRUDService[QcEquipmentCalibration]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcEquipmentCalibration)

class QcFailureAnalysisService(BaseCRUDService[QcFailureAnalysis]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcFailureAnalysis)

class QcFmeaActionsService(BaseCRUDService[QcFmeaActions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcFmeaActions)

class QcFmeaHeadersService(BaseCRUDService[QcFmeaHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcFmeaHeaders)

class QcFmeaItemsService(BaseCRUDService[QcFmeaItems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcFmeaItems)

class QcHoldsService(BaseCRUDService[QcHolds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcHolds)

class QcInspectionEquipmentService(BaseCRUDService[QcInspectionEquipment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcInspectionEquipment)

class QcInspectionLotsService(BaseCRUDService[QcInspectionLots]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcInspectionLots)

class QcInspectionRoutesService(BaseCRUDService[QcInspectionRoutes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcInspectionRoutes)

class QcInspectionsService(BaseCRUDService[QcInspections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcInspections)

class QcIntegrationConnectionsService(BaseCRUDService[QcIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcIntegrationConnections)

class QcIntegrationLogsService(BaseCRUDService[QcIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcIntegrationLogs)

class QcKpiActualsService(BaseCRUDService[QcKpiActuals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcKpiActuals)

class QcKpiDefinitionsService(BaseCRUDService[QcKpiDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcKpiDefinitions)

class QcLanggraphExecutionsService(BaseCRUDService[QcLanggraphExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcLanggraphExecutions)

class QcLanggraphStatesService(BaseCRUDService[QcLanggraphStates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcLanggraphStates)

class QcLanggraphWorkflowsService(BaseCRUDService[QcLanggraphWorkflows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcLanggraphWorkflows)

class QcLlmConfigsService(BaseCRUDService[QcLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcLlmConfigs)

class QcLotDispositionsService(BaseCRUDService[QcLotDispositions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcLotDispositions)

class QcMlModelsService(BaseCRUDService[QcMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcMlModels)

class QcMsaMeasurementsService(BaseCRUDService[QcMsaMeasurements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcMsaMeasurements)

class QcMsaStudiesService(BaseCRUDService[QcMsaStudies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcMsaStudies)

class QcNcrAttachmentsService(BaseCRUDService[QcNcrAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcNcrAttachments)

class QcNcrContainmentService(BaseCRUDService[QcNcrContainment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcNcrContainment)

class QcNcrHeadersService(BaseCRUDService[QcNcrHeaders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcNcrHeaders)

class QcNotificationsService(BaseCRUDService[QcNotifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcNotifications)

class QcOptimizationProblemsService(BaseCRUDService[QcOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcOptimizationProblems)

class QcOrtoolsProblemsService(BaseCRUDService[QcOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcOrtoolsProblems)

class QcPlanAttachmentsService(BaseCRUDService[QcPlanAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPlanAttachments)

class QcPlanElementsService(BaseCRUDService[QcPlanElements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPlanElements)

class QcPlanTriggersService(BaseCRUDService[QcPlanTriggers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPlanTriggers)

class QcPlansService(BaseCRUDService[QcPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPlans)

class QcPpapSubmissionsService(BaseCRUDService[QcPpapSubmissions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPpapSubmissions)

class QcPredictionsService(BaseCRUDService[QcPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPredictions)

class QcPromptTemplatesService(BaseCRUDService[QcPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcPromptTemplates)

class QcRootCauseAnalysisService(BaseCRUDService[QcRootCauseAnalysis]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcRootCauseAnalysis)

class QcRootCauseCausesService(BaseCRUDService[QcRootCauseCauses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcRootCauseCauses)

class QcSampleContainersService(BaseCRUDService[QcSampleContainers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSampleContainers)

class QcSamplePackingResultsService(BaseCRUDService[QcSamplePackingResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSamplePackingResults)

class QcSamplingPlanLinesService(BaseCRUDService[QcSamplingPlanLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSamplingPlanLines)

class QcSamplingPlansService(BaseCRUDService[QcSamplingPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSamplingPlans)

class QcScenariosService(BaseCRUDService[QcScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcScenarios)

class QcScipyAnalysesService(BaseCRUDService[QcScipyAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcScipyAnalyses)

class QcSolverConfigsService(BaseCRUDService[QcSolverConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSolverConfigs)

class QcSpcAlertsService(BaseCRUDService[QcSpcAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSpcAlerts)

class QcSpcChartsService(BaseCRUDService[QcSpcCharts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSpcCharts)

class QcSpcDataPointsService(BaseCRUDService[QcSpcDataPoints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSpcDataPoints)

class QcSpecLimitsService(BaseCRUDService[QcSpecLimits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSpecLimits)

class QcSpecsService(BaseCRUDService[QcSpecs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSpecs)

class QcSupplierProfilesService(BaseCRUDService[QcSupplierProfiles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSupplierProfiles)

class QcSupplierScorecardsService(BaseCRUDService[QcSupplierScorecards]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcSupplierScorecards)

class QcTestEquipmentService(BaseCRUDService[QcTestEquipment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTestEquipment)

class QcTestMethodsService(BaseCRUDService[QcTestMethods]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTestMethods)

class QcTestResultLinesService(BaseCRUDService[QcTestResultLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTestResultLines)

class QcTestResultsService(BaseCRUDService[QcTestResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTestResults)

class QcTrainingAttendeesService(BaseCRUDService[QcTrainingAttendees]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTrainingAttendees)

class QcTrainingCoursesService(BaseCRUDService[QcTrainingCourses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcTrainingCourses)

class QcVectorDocumentsService(BaseCRUDService[QcVectorDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, QcVectorDocuments)
