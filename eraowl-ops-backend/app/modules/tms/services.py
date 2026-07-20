from sqlalchemy.ext.asyncio import AsyncSession

from app.shared.module_base.crud import BaseCRUDService

from app.modules.tms.models import AccessorialCharges
from app.modules.tms.models import AccessorialRateLines
from app.modules.tms.models import AiAgentLogs
from app.modules.tms.models import AiDecisions
from app.modules.tms.models import AiWorkflowState
from app.modules.tms.models import CarrierAddresses
from app.modules.tms.models import CarrierCertifications
from app.modules.tms.models import CarrierContacts
from app.modules.tms.models import CarrierContracts
from app.modules.tms.models import CarrierEdiCapabilities
from app.modules.tms.models import CarrierEquipment
from app.modules.tms.models import CarrierEquipmentTypes
from app.modules.tms.models import CarrierInsurance
from app.modules.tms.models import CarrierPerformance
from app.modules.tms.models import CarrierServiceLevels
from app.modules.tms.models import CarrierServices
from app.modules.tms.models import Carriers
from app.modules.tms.models import CertificatesOfOrigin
from app.modules.tms.models import ClaimEvidence
from app.modules.tms.models import ClaimLines
from app.modules.tms.models import Claims
from app.modules.tms.models import ComplianceAccidents
from app.modules.tms.models import ComplianceDvir
from app.modules.tms.models import ComplianceEld
from app.modules.tms.models import ComplianceIfta
from app.modules.tms.models import ComplianceViolations
from app.modules.tms.models import ContainerSeals
from app.modules.tms.models import Containers
from app.modules.tms.models import CustomsDeclarationLines
from app.modules.tms.models import CustomsDeclarations
from app.modules.tms.models import Deliveries
from app.modules.tms.models import DeliveryLines
from app.modules.tms.models import Dispatches
from app.modules.tms.models import DockAppointments
from app.modules.tms.models import DockDoors
from app.modules.tms.models import DocumentDistribution
from app.modules.tms.models import DocumentTypes
from app.modules.tms.models import Documents
from app.modules.tms.models import DriverCertifications
from app.modules.tms.models import DriverHos
from app.modules.tms.models import DriverPayroll
from app.modules.tms.models import DriverTraining
from app.modules.tms.models import Drivers
from app.modules.tms.models import Equipment
from app.modules.tms.models import EquipmentAssignments
from app.modules.tms.models import EquipmentTrackingDevices
from app.modules.tms.models import EquipmentTypes
from app.modules.tms.models import FreightAudit
from app.modules.tms.models import FreightCostAllocations
from app.modules.tms.models import FreightCostLines
from app.modules.tms.models import FreightCosts
from app.modules.tms.models import FreightInvoiceLines
from app.modules.tms.models import FreightInvoices
from app.modules.tms.models import FuelConsumption
from app.modules.tms.models import FuelSurchargeLines
from app.modules.tms.models import FuelSurchargeTables
from app.modules.tms.models import FuelTransactions
from app.modules.tms.models import GeofenceEvents
from app.modules.tms.models import GpsPings
from app.modules.tms.models import HazmatClassifications
from app.modules.tms.models import HazmatIncidents
from app.modules.tms.models import HazmatPackaging
from app.modules.tms.models import HazmatSegregation
from app.modules.tms.models import HsCodes
from app.modules.tms.models import Incoterms
from app.modules.tms.models import InsurancePolicies
from app.modules.tms.models import InterfaceErrorLog
from app.modules.tms.models import InterfaceShipmentImport
from app.modules.tms.models import KpiDefinitions
from app.modules.tms.models import KpiValues
from app.modules.tms.models import LaneCarriers
from app.modules.tms.models import LanePerformance
from app.modules.tms.models import Lanes
from app.modules.tms.models import LoadCosts
from app.modules.tms.models import LoadLegs
from app.modules.tms.models import LoadLines
from app.modules.tms.models import LoadStops
from app.modules.tms.models import Loads
from app.modules.tms.models import MilestoneAchievements
from app.modules.tms.models import Milestones
from app.modules.tms.models import PickupLines
from app.modules.tms.models import Pickups
from app.modules.tms.models import Pod
from app.modules.tms.models import RateChartVersions
from app.modules.tms.models import RateCharts
from app.modules.tms.models import RateLines
from app.modules.tms.models import RateZones
from app.modules.tms.models import RouteAlternatives
from app.modules.tms.models import RouteStops
from app.modules.tms.models import Routes
from app.modules.tms.models import ShipmentAppointments
from app.modules.tms.models import ShipmentLines
from app.modules.tms.models import ShipmentNotes
from app.modules.tms.models import ShipmentStatuses
from app.modules.tms.models import ShipmentTypes
from app.modules.tms.models import Shipments
from app.modules.tms.models import TemperatureEvents
from app.modules.tms.models import TenderCascade
from app.modules.tms.models import TenderResponses
from app.modules.tms.models import Tenders
from app.modules.tms.models import TrackingEvents
from app.modules.tms.models import TripStops
from app.modules.tms.models import Trips
from app.modules.tms.models import VehicleAssignments
from app.modules.tms.models import VehicleInspections
from app.modules.tms.models import VehicleMaintenance
from app.modules.tms.models import VehicleTypes
from app.modules.tms.models import Vehicles
from app.modules.tms.models import WorkflowApprovalHierarchies
from app.modules.tms.models import WorkflowApprovalHistory
from app.modules.tms.models import WorkflowDefinitions
from app.modules.tms.models import WorkflowTasks
from app.modules.tms.models import YardGateTransactions
from app.modules.tms.models import YardInventory
from app.modules.tms.models import YardLocations

class AccessorialChargesService(BaseCRUDService[AccessorialCharges]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccessorialCharges)

class AccessorialRateLinesService(BaseCRUDService[AccessorialRateLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AccessorialRateLines)

class AiAgentLogsService(BaseCRUDService[AiAgentLogs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiAgentLogs)

class AiDecisionsService(BaseCRUDService[AiDecisions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiDecisions)

class AiWorkflowStateService(BaseCRUDService[AiWorkflowState]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, AiWorkflowState)

class CarrierAddressesService(BaseCRUDService[CarrierAddresses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierAddresses)

class CarrierCertificationsService(BaseCRUDService[CarrierCertifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierCertifications)

class CarrierContactsService(BaseCRUDService[CarrierContacts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierContacts)

class CarrierContractsService(BaseCRUDService[CarrierContracts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierContracts)

class CarrierEdiCapabilitiesService(BaseCRUDService[CarrierEdiCapabilities]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierEdiCapabilities)

class CarrierEquipmentService(BaseCRUDService[CarrierEquipment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierEquipment)

class CarrierEquipmentTypesService(BaseCRUDService[CarrierEquipmentTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierEquipmentTypes)

class CarrierInsuranceService(BaseCRUDService[CarrierInsurance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierInsurance)

class CarrierPerformanceService(BaseCRUDService[CarrierPerformance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierPerformance)

class CarrierServiceLevelsService(BaseCRUDService[CarrierServiceLevels]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierServiceLevels)

class CarrierServicesService(BaseCRUDService[CarrierServices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CarrierServices)

class CarriersService(BaseCRUDService[Carriers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Carriers)

class CertificatesOfOriginService(BaseCRUDService[CertificatesOfOrigin]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CertificatesOfOrigin)

class ClaimEvidenceService(BaseCRUDService[ClaimEvidence]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ClaimEvidence)

class ClaimLinesService(BaseCRUDService[ClaimLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ClaimLines)

class ClaimsService(BaseCRUDService[Claims]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Claims)

class ComplianceAccidentsService(BaseCRUDService[ComplianceAccidents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ComplianceAccidents)

class ComplianceDvirService(BaseCRUDService[ComplianceDvir]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ComplianceDvir)

class ComplianceEldService(BaseCRUDService[ComplianceEld]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ComplianceEld)

class ComplianceIftaService(BaseCRUDService[ComplianceIfta]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ComplianceIfta)

class ComplianceViolationsService(BaseCRUDService[ComplianceViolations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ComplianceViolations)

class ContainerSealsService(BaseCRUDService[ContainerSeals]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ContainerSeals)

class ContainersService(BaseCRUDService[Containers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Containers)

class CustomsDeclarationLinesService(BaseCRUDService[CustomsDeclarationLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CustomsDeclarationLines)

class CustomsDeclarationsService(BaseCRUDService[CustomsDeclarations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, CustomsDeclarations)

class DeliveriesService(BaseCRUDService[Deliveries]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Deliveries)

class DeliveryLinesService(BaseCRUDService[DeliveryLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DeliveryLines)

class DispatchesService(BaseCRUDService[Dispatches]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Dispatches)

class DockAppointmentsService(BaseCRUDService[DockAppointments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DockAppointments)

class DockDoorsService(BaseCRUDService[DockDoors]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DockDoors)

class DocumentDistributionService(BaseCRUDService[DocumentDistribution]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DocumentDistribution)

class DocumentTypesService(BaseCRUDService[DocumentTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DocumentTypes)

class DocumentsService(BaseCRUDService[Documents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Documents)

class DriverCertificationsService(BaseCRUDService[DriverCertifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DriverCertifications)

class DriverHosService(BaseCRUDService[DriverHos]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DriverHos)

class DriverPayrollService(BaseCRUDService[DriverPayroll]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DriverPayroll)

class DriverTrainingService(BaseCRUDService[DriverTraining]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, DriverTraining)

class DriversService(BaseCRUDService[Drivers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Drivers)

class EquipmentService(BaseCRUDService[Equipment]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Equipment)

class EquipmentAssignmentsService(BaseCRUDService[EquipmentAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EquipmentAssignments)

class EquipmentTrackingDevicesService(BaseCRUDService[EquipmentTrackingDevices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EquipmentTrackingDevices)

class EquipmentTypesService(BaseCRUDService[EquipmentTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, EquipmentTypes)

class FreightAuditService(BaseCRUDService[FreightAudit]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightAudit)

class FreightCostAllocationsService(BaseCRUDService[FreightCostAllocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightCostAllocations)

class FreightCostLinesService(BaseCRUDService[FreightCostLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightCostLines)

class FreightCostsService(BaseCRUDService[FreightCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightCosts)

class FreightInvoiceLinesService(BaseCRUDService[FreightInvoiceLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightInvoiceLines)

class FreightInvoicesService(BaseCRUDService[FreightInvoices]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FreightInvoices)

class FuelConsumptionService(BaseCRUDService[FuelConsumption]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FuelConsumption)

class FuelSurchargeLinesService(BaseCRUDService[FuelSurchargeLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FuelSurchargeLines)

class FuelSurchargeTablesService(BaseCRUDService[FuelSurchargeTables]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FuelSurchargeTables)

class FuelTransactionsService(BaseCRUDService[FuelTransactions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, FuelTransactions)

class GeofenceEventsService(BaseCRUDService[GeofenceEvents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, GeofenceEvents)

class GpsPingsService(BaseCRUDService[GpsPings]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, GpsPings)

class HazmatClassificationsService(BaseCRUDService[HazmatClassifications]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, HazmatClassifications)

class HazmatIncidentsService(BaseCRUDService[HazmatIncidents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, HazmatIncidents)

class HazmatPackagingService(BaseCRUDService[HazmatPackaging]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, HazmatPackaging)

class HazmatSegregationService(BaseCRUDService[HazmatSegregation]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, HazmatSegregation)

class HsCodesService(BaseCRUDService[HsCodes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, HsCodes)

class IncotermsService(BaseCRUDService[Incoterms]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Incoterms)

class InsurancePoliciesService(BaseCRUDService[InsurancePolicies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InsurancePolicies)

class InterfaceErrorLogService(BaseCRUDService[InterfaceErrorLog]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InterfaceErrorLog)

class InterfaceShipmentImportService(BaseCRUDService[InterfaceShipmentImport]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, InterfaceShipmentImport)

class KpiDefinitionsService(BaseCRUDService[KpiDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KpiDefinitions)

class KpiValuesService(BaseCRUDService[KpiValues]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, KpiValues)

class LaneCarriersService(BaseCRUDService[LaneCarriers]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LaneCarriers)

class LanePerformanceService(BaseCRUDService[LanePerformance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LanePerformance)

class LanesService(BaseCRUDService[Lanes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Lanes)

class LoadCostsService(BaseCRUDService[LoadCosts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LoadCosts)

class LoadLegsService(BaseCRUDService[LoadLegs]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LoadLegs)

class LoadLinesService(BaseCRUDService[LoadLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LoadLines)

class LoadStopsService(BaseCRUDService[LoadStops]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LoadStops)

class LoadsService(BaseCRUDService[Loads]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Loads)

class MilestoneAchievementsService(BaseCRUDService[MilestoneAchievements]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, MilestoneAchievements)

class MilestonesService(BaseCRUDService[Milestones]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Milestones)

class PickupLinesService(BaseCRUDService[PickupLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, PickupLines)

class PickupsService(BaseCRUDService[Pickups]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Pickups)

class PodService(BaseCRUDService[Pod]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Pod)

class RateChartVersionsService(BaseCRUDService[RateChartVersions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RateChartVersions)

class RateChartsService(BaseCRUDService[RateCharts]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RateCharts)

class RateLinesService(BaseCRUDService[RateLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RateLines)

class RateZonesService(BaseCRUDService[RateZones]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RateZones)

class RouteAlternativesService(BaseCRUDService[RouteAlternatives]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RouteAlternatives)

class RouteStopsService(BaseCRUDService[RouteStops]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, RouteStops)

class RoutesService(BaseCRUDService[Routes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Routes)

class ShipmentAppointmentsService(BaseCRUDService[ShipmentAppointments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentAppointments)

class ShipmentLinesService(BaseCRUDService[ShipmentLines]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentLines)

class ShipmentNotesService(BaseCRUDService[ShipmentNotes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentNotes)

class ShipmentStatusesService(BaseCRUDService[ShipmentStatuses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentStatuses)

class ShipmentTypesService(BaseCRUDService[ShipmentTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, ShipmentTypes)

class ShipmentsService(BaseCRUDService[Shipments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Shipments)

class TemperatureEventsService(BaseCRUDService[TemperatureEvents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TemperatureEvents)

class TenderCascadeService(BaseCRUDService[TenderCascade]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TenderCascade)

class TenderResponsesService(BaseCRUDService[TenderResponses]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TenderResponses)

class TendersService(BaseCRUDService[Tenders]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Tenders)

class TrackingEventsService(BaseCRUDService[TrackingEvents]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TrackingEvents)

class TripStopsService(BaseCRUDService[TripStops]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, TripStops)

class TripsService(BaseCRUDService[Trips]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Trips)

class VehicleAssignmentsService(BaseCRUDService[VehicleAssignments]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, VehicleAssignments)

class VehicleInspectionsService(BaseCRUDService[VehicleInspections]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, VehicleInspections)

class VehicleMaintenanceService(BaseCRUDService[VehicleMaintenance]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, VehicleMaintenance)

class VehicleTypesService(BaseCRUDService[VehicleTypes]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, VehicleTypes)

class VehiclesService(BaseCRUDService[Vehicles]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Vehicles)

class WorkflowApprovalHierarchiesService(BaseCRUDService[WorkflowApprovalHierarchies]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowApprovalHierarchies)

class WorkflowApprovalHistoryService(BaseCRUDService[WorkflowApprovalHistory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowApprovalHistory)

class WorkflowDefinitionsService(BaseCRUDService[WorkflowDefinitions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowDefinitions)

class WorkflowTasksService(BaseCRUDService[WorkflowTasks]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, WorkflowTasks)

class YardGateTransactionsService(BaseCRUDService[YardGateTransactions]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, YardGateTransactions)

class YardInventoryService(BaseCRUDService[YardInventory]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, YardInventory)

class YardLocationsService(BaseCRUDService[YardLocations]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, YardLocations)
