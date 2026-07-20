from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.eam.models import EamAiAgentLogs
from app.modules.eam.models import EamAiDecisions
from app.modules.eam.models import EamAiWorkflowState
from app.modules.eam.models import EamAlerts
from app.modules.eam.models import EamAssetAttachments
from app.modules.eam.models import EamAssetBom
from app.modules.eam.models import EamAssetCategories
from app.modules.eam.models import EamAssetCriticality
from app.modules.eam.models import EamAssetHierarchy
from app.modules.eam.models import EamAssetTypes
from app.modules.eam.models import EamAssetVendors
from app.modules.eam.models import EamAssets
from app.modules.eam.models import EamAuditLog
from app.modules.eam.models import EamBudgets
from app.modules.eam.models import EamCalibrationRequirements
from app.modules.eam.models import EamCalibrationResults
from app.modules.eam.models import EamComplianceRecords
from app.modules.eam.models import EamComplianceRequirements
from app.modules.eam.models import EamComponents
from app.modules.eam.models import EamConditionMonitoringPrograms
from app.modules.eam.models import EamConditionReadings
from app.modules.eam.models import EamContractAssets
from app.modules.eam.models import EamCrafts
from app.modules.eam.models import EamDecommissionPlans
from app.modules.eam.models import EamDocumentAssignments
from app.modules.eam.models import EamDocuments
from app.modules.eam.models import EamFailureCodes
from app.modules.eam.models import EamFailureHistory
from app.modules.eam.models import EamFmeaItems
from app.modules.eam.models import EamFmeaStudies
from app.modules.eam.models import EamFunctionalLocations
from app.modules.eam.models import EamInspections
from app.modules.eam.models import EamIntegrationConnections
from app.modules.eam.models import EamIntegrationLogs
from app.modules.eam.models import EamJsa
from app.modules.eam.models import EamJsaSteps
from app.modules.eam.models import EamKitContents
from app.modules.eam.models import EamKits
from app.modules.eam.models import EamKpiDefinitions
from app.modules.eam.models import EamKpiValues
from app.modules.eam.models import EamLanggraphWorkflows
from app.modules.eam.models import EamLlmConfigs
from app.modules.eam.models import EamLoto
from app.modules.eam.models import EamMaintenanceCosts
from app.modules.eam.models import EamMeterAssignments
from app.modules.eam.models import EamMeterReadings
from app.modules.eam.models import EamMeters
from app.modules.eam.models import EamMlModels
from app.modules.eam.models import EamNotifications
from app.modules.eam.models import EamOptimizationProblems
from app.modules.eam.models import EamOptimizationSolutions
from app.modules.eam.models import EamOrtoolsProblems
from app.modules.eam.models import EamPermits
from app.modules.eam.models import EamPhysicalLocations
from app.modules.eam.models import EamPmAssignments
from app.modules.eam.models import EamPmScheduleOptimized
from app.modules.eam.models import EamPmSchedules
from app.modules.eam.models import EamPmSchedulingProblems
from app.modules.eam.models import EamPmTemplates
from app.modules.eam.models import EamPredictions
from app.modules.eam.models import EamPredictiveMaintenance
from app.modules.eam.models import EamPromptTemplates
from app.modules.eam.models import EamRcaActions
from app.modules.eam.models import EamRcaCauses
from app.modules.eam.models import EamRcaStudies
from app.modules.eam.models import EamRcmAnalyses
from app.modules.eam.models import EamRcmStudies
from app.modules.eam.models import EamSafetyPlans
from app.modules.eam.models import EamScenarios
from app.modules.eam.models import EamScipyAnalyses
from app.modules.eam.models import EamServiceContracts
from app.modules.eam.models import EamSparePartsConsumption
from app.modules.eam.models import EamSparePartsStorage
from app.modules.eam.models import EamStorageLocations
from app.modules.eam.models import EamStorageOptimizationProblems
from app.modules.eam.models import EamTechnicianCertifications
from app.modules.eam.models import EamTechnicianRoutes
from app.modules.eam.models import EamTechnicianRoutingProblems
from app.modules.eam.models import EamTechnicianSkills
from app.modules.eam.models import EamTechnicians
from app.modules.eam.models import EamTools
from app.modules.eam.models import EamVectorDocuments
from app.modules.eam.models import EamWarranties
from app.modules.eam.models import EamWarrantyClaims
from app.modules.eam.models import EamWoLabor
from app.modules.eam.models import EamWoOperations
from app.modules.eam.models import EamWoTasks
from app.modules.eam.models import EamWoTools
from app.modules.eam.models import EamWorkOrderStatuses
from app.modules.eam.models import EamWorkOrderTypes
from app.modules.eam.models import EamWorkOrders

class EamAiAgentLogsService(BaseCRUDService[EamAiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAiAgentLogs)

class EamAiDecisionsService(BaseCRUDService[EamAiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAiDecisions)

class EamAiWorkflowStateService(BaseCRUDService[EamAiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAiWorkflowState)

class EamAlertsService(BaseCRUDService[EamAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAlerts)

class EamAssetAttachmentsService(BaseCRUDService[EamAssetAttachments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetAttachments)

class EamAssetBomService(BaseCRUDService[EamAssetBom]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetBom)

class EamAssetCategoriesService(BaseCRUDService[EamAssetCategories]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetCategories)

class EamAssetCriticalityService(BaseCRUDService[EamAssetCriticality]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetCriticality)

class EamAssetHierarchyService(BaseCRUDService[EamAssetHierarchy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetHierarchy)

class EamAssetTypesService(BaseCRUDService[EamAssetTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetTypes)

class EamAssetVendorsService(BaseCRUDService[EamAssetVendors]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssetVendors)

class EamAssetsService(BaseCRUDService[EamAssets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAssets)

class EamAuditLogService(BaseCRUDService[EamAuditLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamAuditLog)

class EamBudgetsService(BaseCRUDService[EamBudgets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamBudgets)

class EamCalibrationRequirementsService(BaseCRUDService[EamCalibrationRequirements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamCalibrationRequirements)

class EamCalibrationResultsService(BaseCRUDService[EamCalibrationResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamCalibrationResults)

class EamComplianceRecordsService(BaseCRUDService[EamComplianceRecords]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamComplianceRecords)

class EamComplianceRequirementsService(BaseCRUDService[EamComplianceRequirements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamComplianceRequirements)

class EamComponentsService(BaseCRUDService[EamComponents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamComponents)

class EamConditionMonitoringProgramsService(BaseCRUDService[EamConditionMonitoringPrograms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamConditionMonitoringPrograms)

class EamConditionReadingsService(BaseCRUDService[EamConditionReadings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamConditionReadings)

class EamContractAssetsService(BaseCRUDService[EamContractAssets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamContractAssets)

class EamCraftsService(BaseCRUDService[EamCrafts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamCrafts)

class EamDecommissionPlansService(BaseCRUDService[EamDecommissionPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamDecommissionPlans)

class EamDocumentAssignmentsService(BaseCRUDService[EamDocumentAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamDocumentAssignments)

class EamDocumentsService(BaseCRUDService[EamDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamDocuments)

class EamFailureCodesService(BaseCRUDService[EamFailureCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamFailureCodes)

class EamFailureHistoryService(BaseCRUDService[EamFailureHistory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamFailureHistory)

class EamFmeaItemsService(BaseCRUDService[EamFmeaItems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamFmeaItems)

class EamFmeaStudiesService(BaseCRUDService[EamFmeaStudies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamFmeaStudies)

class EamFunctionalLocationsService(BaseCRUDService[EamFunctionalLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamFunctionalLocations)

class EamInspectionsService(BaseCRUDService[EamInspections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamInspections)

class EamIntegrationConnectionsService(BaseCRUDService[EamIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamIntegrationConnections)

class EamIntegrationLogsService(BaseCRUDService[EamIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamIntegrationLogs)

class EamJsaService(BaseCRUDService[EamJsa]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamJsa)

class EamJsaStepsService(BaseCRUDService[EamJsaSteps]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamJsaSteps)

class EamKitContentsService(BaseCRUDService[EamKitContents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamKitContents)

class EamKitsService(BaseCRUDService[EamKits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamKits)

class EamKpiDefinitionsService(BaseCRUDService[EamKpiDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamKpiDefinitions)

class EamKpiValuesService(BaseCRUDService[EamKpiValues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamKpiValues)

class EamLanggraphWorkflowsService(BaseCRUDService[EamLanggraphWorkflows]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamLanggraphWorkflows)

class EamLlmConfigsService(BaseCRUDService[EamLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamLlmConfigs)

class EamLotoService(BaseCRUDService[EamLoto]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamLoto)

class EamMaintenanceCostsService(BaseCRUDService[EamMaintenanceCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamMaintenanceCosts)

class EamMeterAssignmentsService(BaseCRUDService[EamMeterAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamMeterAssignments)

class EamMeterReadingsService(BaseCRUDService[EamMeterReadings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamMeterReadings)

class EamMetersService(BaseCRUDService[EamMeters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamMeters)

class EamMlModelsService(BaseCRUDService[EamMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamMlModels)

class EamNotificationsService(BaseCRUDService[EamNotifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamNotifications)

class EamOptimizationProblemsService(BaseCRUDService[EamOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamOptimizationProblems)

class EamOptimizationSolutionsService(BaseCRUDService[EamOptimizationSolutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamOptimizationSolutions)

class EamOrtoolsProblemsService(BaseCRUDService[EamOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamOrtoolsProblems)

class EamPermitsService(BaseCRUDService[EamPermits]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPermits)

class EamPhysicalLocationsService(BaseCRUDService[EamPhysicalLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPhysicalLocations)

class EamPmAssignmentsService(BaseCRUDService[EamPmAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPmAssignments)

class EamPmScheduleOptimizedService(BaseCRUDService[EamPmScheduleOptimized]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPmScheduleOptimized)

class EamPmSchedulesService(BaseCRUDService[EamPmSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPmSchedules)

class EamPmSchedulingProblemsService(BaseCRUDService[EamPmSchedulingProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPmSchedulingProblems)

class EamPmTemplatesService(BaseCRUDService[EamPmTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPmTemplates)

class EamPredictionsService(BaseCRUDService[EamPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPredictions)

class EamPredictiveMaintenanceService(BaseCRUDService[EamPredictiveMaintenance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPredictiveMaintenance)

class EamPromptTemplatesService(BaseCRUDService[EamPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamPromptTemplates)

class EamRcaActionsService(BaseCRUDService[EamRcaActions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamRcaActions)

class EamRcaCausesService(BaseCRUDService[EamRcaCauses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamRcaCauses)

class EamRcaStudiesService(BaseCRUDService[EamRcaStudies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamRcaStudies)

class EamRcmAnalysesService(BaseCRUDService[EamRcmAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamRcmAnalyses)

class EamRcmStudiesService(BaseCRUDService[EamRcmStudies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamRcmStudies)

class EamSafetyPlansService(BaseCRUDService[EamSafetyPlans]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamSafetyPlans)

class EamScenariosService(BaseCRUDService[EamScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamScenarios)

class EamScipyAnalysesService(BaseCRUDService[EamScipyAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamScipyAnalyses)

class EamServiceContractsService(BaseCRUDService[EamServiceContracts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamServiceContracts)

class EamSparePartsConsumptionService(BaseCRUDService[EamSparePartsConsumption]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamSparePartsConsumption)

class EamSparePartsStorageService(BaseCRUDService[EamSparePartsStorage]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamSparePartsStorage)

class EamStorageLocationsService(BaseCRUDService[EamStorageLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamStorageLocations)

class EamStorageOptimizationProblemsService(BaseCRUDService[EamStorageOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamStorageOptimizationProblems)

class EamTechnicianCertificationsService(BaseCRUDService[EamTechnicianCertifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTechnicianCertifications)

class EamTechnicianRoutesService(BaseCRUDService[EamTechnicianRoutes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTechnicianRoutes)

class EamTechnicianRoutingProblemsService(BaseCRUDService[EamTechnicianRoutingProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTechnicianRoutingProblems)

class EamTechnicianSkillsService(BaseCRUDService[EamTechnicianSkills]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTechnicianSkills)

class EamTechniciansService(BaseCRUDService[EamTechnicians]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTechnicians)

class EamToolsService(BaseCRUDService[EamTools]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamTools)

class EamVectorDocumentsService(BaseCRUDService[EamVectorDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamVectorDocuments)

class EamWarrantiesService(BaseCRUDService[EamWarranties]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWarranties)

class EamWarrantyClaimsService(BaseCRUDService[EamWarrantyClaims]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWarrantyClaims)

class EamWoLaborService(BaseCRUDService[EamWoLabor]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWoLabor)

class EamWoOperationsService(BaseCRUDService[EamWoOperations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWoOperations)

class EamWoTasksService(BaseCRUDService[EamWoTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWoTasks)

class EamWoToolsService(BaseCRUDService[EamWoTools]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWoTools)

class EamWorkOrderStatusesService(BaseCRUDService[EamWorkOrderStatuses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWorkOrderStatuses)

class EamWorkOrderTypesService(BaseCRUDService[EamWorkOrderTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWorkOrderTypes)

class EamWorkOrdersService(BaseCRUDService[EamWorkOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EamWorkOrders)
