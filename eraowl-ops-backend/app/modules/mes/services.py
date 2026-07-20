from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.mes.models import JobOrders
from app.modules.mes.models import MachineTelemetry
from app.modules.mes.models import MesAiAgentLogs
from app.modules.mes.models import MesAiFeatureStore
from app.modules.mes.models import MesAiModelRegistry
from app.modules.mes.models import MesAiWorkflowStates
from app.modules.mes.models import MesAlerts
from app.modules.mes.models import MesAlgorithms
from app.modules.mes.models import MesAndonBoards
from app.modules.mes.models import MesAndonTriggers
from app.modules.mes.models import MesBatchRecordMaterials
from app.modules.mes.models import MesBatchRecordSteps
from app.modules.mes.models import MesBatchRecords
from app.modules.mes.models import MesCrewAssignments
from app.modules.mes.models import MesCrews
from app.modules.mes.models import MesCribCompartments
from app.modules.mes.models import MesCribPackingResults
from app.modules.mes.models import MesDeliveryRequests
from app.modules.mes.models import MesDeliveryRoutes
from app.modules.mes.models import MesDigitalTwinModels
from app.modules.mes.models import MesDocumentInstances
from app.modules.mes.models import MesDocuments
from app.modules.mes.models import MesDowntimeEvents
from app.modules.mes.models import MesDowntimeReasons
from app.modules.mes.models import MesEnergyMeters
from app.modules.mes.models import MesEnergyReadings
from app.modules.mes.models import MesEquipment
from app.modules.mes.models import MesEquipmentAssignments
from app.modules.mes.models import MesEquipmentCapabilities
from app.modules.mes.models import MesEquipmentCertifications
from app.modules.mes.models import MesEquipmentClasses
from app.modules.mes.models import MesEquipmentConnections
from app.modules.mes.models import MesEquipmentDataPoints
from app.modules.mes.models import MesEquipmentLocations
from app.modules.mes.models import MesEquipmentStatuses
from app.modules.mes.models import MesEquipmentTypes
from app.modules.mes.models import MesGenealogy
from app.modules.mes.models import MesGenealogySnapshots
from app.modules.mes.models import MesInstructionAcknowledgments
from app.modules.mes.models import MesInstructionVersions
from app.modules.mes.models import MesInstructions
from app.modules.mes.models import MesIntegrationConnections
from app.modules.mes.models import MesIntegrationLogs
from app.modules.mes.models import MesKpiActuals
from app.modules.mes.models import MesKpiDefinitions
from app.modules.mes.models import MesLaborAssignments
from app.modules.mes.models import MesLaborTimeCollection
from app.modules.mes.models import MesLineBalancing
from app.modules.mes.models import MesLlmConfigs
from app.modules.mes.models import MesMachineAlarms
from app.modules.mes.models import MesMachineDataValues
from app.modules.mes.models import MesMachineEvents
from app.modules.mes.models import MesMachinePrograms
from app.modules.mes.models import MesMaintenanceHistory
from app.modules.mes.models import MesMaintenanceParts
from app.modules.mes.models import MesMaintenanceSchedules
from app.modules.mes.models import MesMaintenanceWorkOrders
from app.modules.mes.models import MesMaterialConsumption
from app.modules.mes.models import MesMaterialIssues
from app.modules.mes.models import MesMaterialReturns
from app.modules.mes.models import MesMlModelVersions
from app.modules.mes.models import MesMlModels
from app.modules.mes.models import MesNotifications
from app.modules.mes.models import MesOeeCalculations
from app.modules.mes.models import MesOeeLosses
from app.modules.mes.models import MesOeeTargets
from app.modules.mes.models import MesOperationExecution
from app.modules.mes.models import MesOperationSteps
from app.modules.mes.models import MesOperatorAssignments
from app.modules.mes.models import MesOperatorCertifications
from app.modules.mes.models import MesOperatorPerformance
from app.modules.mes.models import MesOperatorSchedules
from app.modules.mes.models import MesOperatorSkills
from app.modules.mes.models import MesOperatorTraining
from app.modules.mes.models import MesOperators
from app.modules.mes.models import MesOptimizationProblems
from app.modules.mes.models import MesOptimizationResults
from app.modules.mes.models import MesOrtoolsProblems
from app.modules.mes.models import MesPerformanceActuals
from app.modules.mes.models import MesPerformanceMetrics
from app.modules.mes.models import MesPredictions
from app.modules.mes.models import MesProductionCells
from app.modules.mes.models import MesProductionLines
from app.modules.mes.models import MesPromptTemplates
from app.modules.mes.models import MesQualityHolds
from app.modules.mes.models import MesQualityInspections
from app.modules.mes.models import MesQualitySpcData
from app.modules.mes.models import MesResourceAvailability
from app.modules.mes.models import MesResourceCosts
from app.modules.mes.models import MesResourceTypes
from app.modules.mes.models import MesResources
from app.modules.mes.models import MesScenarios
from app.modules.mes.models import MesScheduleResults
from app.modules.mes.models import MesSchedulingProblems
from app.modules.mes.models import MesScipyAnalyses
from app.modules.mes.models import MesSensorCalibrations
from app.modules.mes.models import MesSensors
from app.modules.mes.models import MesShiftHandovers
from app.modules.mes.models import MesShiftSchedules
from app.modules.mes.models import MesShifts
from app.modules.mes.models import MesSolverConfigs
from app.modules.mes.models import MesStationAssignments
from app.modules.mes.models import MesStationTypes
from app.modules.mes.models import MesStations
from app.modules.mes.models import MesToolCribs
from app.modules.mes.models import MesToolingAssignments
from app.modules.mes.models import MesToolingLifeTracking
from app.modules.mes.models import MesToolingMaster
from app.modules.mes.models import MesToolingTypes
from app.modules.mes.models import MesVectorStoreConfigs
from app.modules.mes.models import MesVectorStoreDocuments
from app.modules.mes.models import MesWorkCenterCalendars
from app.modules.mes.models import MesWorkCenterCapacities
from app.modules.mes.models import MesWorkCenterConstraints
from app.modules.mes.models import MesWorkCenterTypes
from app.modules.mes.models import MesWorkCenters
from app.modules.mes.models import MesWorkOrderExecution
from app.modules.mes.models import MesWorkOrderHolds
from app.modules.mes.models import MesWorkOrderSignatures
from app.modules.mes.models import MesWorkflowDefinitions
from app.modules.mes.models import MesWorkflowExecutions
from app.modules.mes.models import WorkCenters

class JobOrdersService(BaseCRUDService[JobOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, JobOrders)

class MachineTelemetryService(BaseCRUDService[MachineTelemetry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MachineTelemetry)

class MesAiAgentLogsService(BaseCRUDService[MesAiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAiAgentLogs)

class MesAiFeatureStoreService(BaseCRUDService[MesAiFeatureStore]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAiFeatureStore)

class MesAiModelRegistryService(BaseCRUDService[MesAiModelRegistry]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAiModelRegistry)

class MesAiWorkflowStatesService(BaseCRUDService[MesAiWorkflowStates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAiWorkflowStates)

class MesAlertsService(BaseCRUDService[MesAlerts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAlerts)

class MesAlgorithmsService(BaseCRUDService[MesAlgorithms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAlgorithms)

class MesAndonBoardsService(BaseCRUDService[MesAndonBoards]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAndonBoards)

class MesAndonTriggersService(BaseCRUDService[MesAndonTriggers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesAndonTriggers)

class MesBatchRecordMaterialsService(BaseCRUDService[MesBatchRecordMaterials]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesBatchRecordMaterials)

class MesBatchRecordStepsService(BaseCRUDService[MesBatchRecordSteps]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesBatchRecordSteps)

class MesBatchRecordsService(BaseCRUDService[MesBatchRecords]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesBatchRecords)

class MesCrewAssignmentsService(BaseCRUDService[MesCrewAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesCrewAssignments)

class MesCrewsService(BaseCRUDService[MesCrews]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesCrews)

class MesCribCompartmentsService(BaseCRUDService[MesCribCompartments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesCribCompartments)

class MesCribPackingResultsService(BaseCRUDService[MesCribPackingResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesCribPackingResults)

class MesDeliveryRequestsService(BaseCRUDService[MesDeliveryRequests]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDeliveryRequests)

class MesDeliveryRoutesService(BaseCRUDService[MesDeliveryRoutes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDeliveryRoutes)

class MesDigitalTwinModelsService(BaseCRUDService[MesDigitalTwinModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDigitalTwinModels)

class MesDocumentInstancesService(BaseCRUDService[MesDocumentInstances]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDocumentInstances)

class MesDocumentsService(BaseCRUDService[MesDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDocuments)

class MesDowntimeEventsService(BaseCRUDService[MesDowntimeEvents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDowntimeEvents)

class MesDowntimeReasonsService(BaseCRUDService[MesDowntimeReasons]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesDowntimeReasons)

class MesEnergyMetersService(BaseCRUDService[MesEnergyMeters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEnergyMeters)

class MesEnergyReadingsService(BaseCRUDService[MesEnergyReadings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEnergyReadings)

class MesEquipmentService(BaseCRUDService[MesEquipment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipment)

class MesEquipmentAssignmentsService(BaseCRUDService[MesEquipmentAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentAssignments)

class MesEquipmentCapabilitiesService(BaseCRUDService[MesEquipmentCapabilities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentCapabilities)

class MesEquipmentCertificationsService(BaseCRUDService[MesEquipmentCertifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentCertifications)

class MesEquipmentClassesService(BaseCRUDService[MesEquipmentClasses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentClasses)

class MesEquipmentConnectionsService(BaseCRUDService[MesEquipmentConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentConnections)

class MesEquipmentDataPointsService(BaseCRUDService[MesEquipmentDataPoints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentDataPoints)

class MesEquipmentLocationsService(BaseCRUDService[MesEquipmentLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentLocations)

class MesEquipmentStatusesService(BaseCRUDService[MesEquipmentStatuses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentStatuses)

class MesEquipmentTypesService(BaseCRUDService[MesEquipmentTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesEquipmentTypes)

class MesGenealogyService(BaseCRUDService[MesGenealogy]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesGenealogy)

class MesGenealogySnapshotsService(BaseCRUDService[MesGenealogySnapshots]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesGenealogySnapshots)

class MesInstructionAcknowledgmentsService(BaseCRUDService[MesInstructionAcknowledgments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesInstructionAcknowledgments)

class MesInstructionVersionsService(BaseCRUDService[MesInstructionVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesInstructionVersions)

class MesInstructionsService(BaseCRUDService[MesInstructions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesInstructions)

class MesIntegrationConnectionsService(BaseCRUDService[MesIntegrationConnections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesIntegrationConnections)

class MesIntegrationLogsService(BaseCRUDService[MesIntegrationLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesIntegrationLogs)

class MesKpiActualsService(BaseCRUDService[MesKpiActuals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesKpiActuals)

class MesKpiDefinitionsService(BaseCRUDService[MesKpiDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesKpiDefinitions)

class MesLaborAssignmentsService(BaseCRUDService[MesLaborAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesLaborAssignments)

class MesLaborTimeCollectionService(BaseCRUDService[MesLaborTimeCollection]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesLaborTimeCollection)

class MesLineBalancingService(BaseCRUDService[MesLineBalancing]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesLineBalancing)

class MesLlmConfigsService(BaseCRUDService[MesLlmConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesLlmConfigs)

class MesMachineAlarmsService(BaseCRUDService[MesMachineAlarms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMachineAlarms)

class MesMachineDataValuesService(BaseCRUDService[MesMachineDataValues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMachineDataValues)

class MesMachineEventsService(BaseCRUDService[MesMachineEvents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMachineEvents)

class MesMachineProgramsService(BaseCRUDService[MesMachinePrograms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMachinePrograms)

class MesMaintenanceHistoryService(BaseCRUDService[MesMaintenanceHistory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaintenanceHistory)

class MesMaintenancePartsService(BaseCRUDService[MesMaintenanceParts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaintenanceParts)

class MesMaintenanceSchedulesService(BaseCRUDService[MesMaintenanceSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaintenanceSchedules)

class MesMaintenanceWorkOrdersService(BaseCRUDService[MesMaintenanceWorkOrders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaintenanceWorkOrders)

class MesMaterialConsumptionService(BaseCRUDService[MesMaterialConsumption]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaterialConsumption)

class MesMaterialIssuesService(BaseCRUDService[MesMaterialIssues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaterialIssues)

class MesMaterialReturnsService(BaseCRUDService[MesMaterialReturns]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMaterialReturns)

class MesMlModelVersionsService(BaseCRUDService[MesMlModelVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMlModelVersions)

class MesMlModelsService(BaseCRUDService[MesMlModels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesMlModels)

class MesNotificationsService(BaseCRUDService[MesNotifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesNotifications)

class MesOeeCalculationsService(BaseCRUDService[MesOeeCalculations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOeeCalculations)

class MesOeeLossesService(BaseCRUDService[MesOeeLosses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOeeLosses)

class MesOeeTargetsService(BaseCRUDService[MesOeeTargets]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOeeTargets)

class MesOperationExecutionService(BaseCRUDService[MesOperationExecution]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperationExecution)

class MesOperationStepsService(BaseCRUDService[MesOperationSteps]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperationSteps)

class MesOperatorAssignmentsService(BaseCRUDService[MesOperatorAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorAssignments)

class MesOperatorCertificationsService(BaseCRUDService[MesOperatorCertifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorCertifications)

class MesOperatorPerformanceService(BaseCRUDService[MesOperatorPerformance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorPerformance)

class MesOperatorSchedulesService(BaseCRUDService[MesOperatorSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorSchedules)

class MesOperatorSkillsService(BaseCRUDService[MesOperatorSkills]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorSkills)

class MesOperatorTrainingService(BaseCRUDService[MesOperatorTraining]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperatorTraining)

class MesOperatorsService(BaseCRUDService[MesOperators]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOperators)

class MesOptimizationProblemsService(BaseCRUDService[MesOptimizationProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOptimizationProblems)

class MesOptimizationResultsService(BaseCRUDService[MesOptimizationResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOptimizationResults)

class MesOrtoolsProblemsService(BaseCRUDService[MesOrtoolsProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesOrtoolsProblems)

class MesPerformanceActualsService(BaseCRUDService[MesPerformanceActuals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesPerformanceActuals)

class MesPerformanceMetricsService(BaseCRUDService[MesPerformanceMetrics]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesPerformanceMetrics)

class MesPredictionsService(BaseCRUDService[MesPredictions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesPredictions)

class MesProductionCellsService(BaseCRUDService[MesProductionCells]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesProductionCells)

class MesProductionLinesService(BaseCRUDService[MesProductionLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesProductionLines)

class MesPromptTemplatesService(BaseCRUDService[MesPromptTemplates]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesPromptTemplates)

class MesQualityHoldsService(BaseCRUDService[MesQualityHolds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesQualityHolds)

class MesQualityInspectionsService(BaseCRUDService[MesQualityInspections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesQualityInspections)

class MesQualitySpcDataService(BaseCRUDService[MesQualitySpcData]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesQualitySpcData)

class MesResourceAvailabilityService(BaseCRUDService[MesResourceAvailability]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesResourceAvailability)

class MesResourceCostsService(BaseCRUDService[MesResourceCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesResourceCosts)

class MesResourceTypesService(BaseCRUDService[MesResourceTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesResourceTypes)

class MesResourcesService(BaseCRUDService[MesResources]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesResources)

class MesScenariosService(BaseCRUDService[MesScenarios]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesScenarios)

class MesScheduleResultsService(BaseCRUDService[MesScheduleResults]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesScheduleResults)

class MesSchedulingProblemsService(BaseCRUDService[MesSchedulingProblems]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesSchedulingProblems)

class MesScipyAnalysesService(BaseCRUDService[MesScipyAnalyses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesScipyAnalyses)

class MesSensorCalibrationsService(BaseCRUDService[MesSensorCalibrations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesSensorCalibrations)

class MesSensorsService(BaseCRUDService[MesSensors]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesSensors)

class MesShiftHandoversService(BaseCRUDService[MesShiftHandovers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesShiftHandovers)

class MesShiftSchedulesService(BaseCRUDService[MesShiftSchedules]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesShiftSchedules)

class MesShiftsService(BaseCRUDService[MesShifts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesShifts)

class MesSolverConfigsService(BaseCRUDService[MesSolverConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesSolverConfigs)

class MesStationAssignmentsService(BaseCRUDService[MesStationAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesStationAssignments)

class MesStationTypesService(BaseCRUDService[MesStationTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesStationTypes)

class MesStationsService(BaseCRUDService[MesStations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesStations)

class MesToolCribsService(BaseCRUDService[MesToolCribs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesToolCribs)

class MesToolingAssignmentsService(BaseCRUDService[MesToolingAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesToolingAssignments)

class MesToolingLifeTrackingService(BaseCRUDService[MesToolingLifeTracking]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesToolingLifeTracking)

class MesToolingMasterService(BaseCRUDService[MesToolingMaster]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesToolingMaster)

class MesToolingTypesService(BaseCRUDService[MesToolingTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesToolingTypes)

class MesVectorStoreConfigsService(BaseCRUDService[MesVectorStoreConfigs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesVectorStoreConfigs)

class MesVectorStoreDocumentsService(BaseCRUDService[MesVectorStoreDocuments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesVectorStoreDocuments)

class MesWorkCenterCalendarsService(BaseCRUDService[MesWorkCenterCalendars]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkCenterCalendars)

class MesWorkCenterCapacitiesService(BaseCRUDService[MesWorkCenterCapacities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkCenterCapacities)

class MesWorkCenterConstraintsService(BaseCRUDService[MesWorkCenterConstraints]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkCenterConstraints)

class MesWorkCenterTypesService(BaseCRUDService[MesWorkCenterTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkCenterTypes)

class MesWorkCentersService(BaseCRUDService[MesWorkCenters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkCenters)

class MesWorkOrderExecutionService(BaseCRUDService[MesWorkOrderExecution]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkOrderExecution)

class MesWorkOrderHoldsService(BaseCRUDService[MesWorkOrderHolds]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkOrderHolds)

class MesWorkOrderSignaturesService(BaseCRUDService[MesWorkOrderSignatures]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkOrderSignatures)

class MesWorkflowDefinitionsService(BaseCRUDService[MesWorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkflowDefinitions)

class MesWorkflowExecutionsService(BaseCRUDService[MesWorkflowExecutions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MesWorkflowExecutions)

class WorkCentersService(BaseCRUDService[WorkCenters]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkCenters)
