import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AgentProposalsCreate(BaseModel):
    proposal_id: uuid.UUID
    conflict_id: Optional[uuid.UUID] = None
    agent_id: str
    agent_type: str
    proposal: dict
    utility_score: Optional[float] = None
    confidence: Optional[float] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AgentProposalsUpdate(BaseModel):
    proposal_id: Optional[uuid.UUID] = None
    conflict_id: Optional[uuid.UUID] = None
    agent_id: Optional[str] = None
    agent_type: Optional[str] = None
    proposal: Optional[dict] = None
    utility_score: Optional[float] = None
    confidence: Optional[float] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AgentProposalsOut(BaseModel):
    proposal_id: uuid.UUID
    conflict_id: Optional[uuid.UUID] = None
    agent_id: str
    agent_type: str
    proposal: dict
    utility_score: Optional[float] = None
    confidence: Optional[float] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class BusinessWeightsCreate(BaseModel):
    weight_id: uuid.UUID
    config_name: str
    cost_weight: Optional[float] = None
    service_weight: Optional[float] = None
    quality_weight: Optional[float] = None
    speed_weight: Optional[float] = None
    sustainability_weight: Optional[float] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BusinessWeightsUpdate(BaseModel):
    weight_id: Optional[uuid.UUID] = None
    config_name: Optional[str] = None
    cost_weight: Optional[float] = None
    service_weight: Optional[float] = None
    quality_weight: Optional[float] = None
    speed_weight: Optional[float] = None
    sustainability_weight: Optional[float] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BusinessWeightsOut(BaseModel):
    weight_id: uuid.UUID
    config_name: str
    cost_weight: Optional[float] = None
    service_weight: Optional[float] = None
    quality_weight: Optional[float] = None
    speed_weight: Optional[float] = None
    sustainability_weight: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ConflictsCreate(BaseModel):
    conflict_id: uuid.UUID
    conflict_type: str
    affected_items: Optional[str] = None
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ConflictsUpdate(BaseModel):
    conflict_id: Optional[uuid.UUID] = None
    conflict_type: Optional[str] = None
    affected_items: Optional[str] = None
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ConflictsOut(BaseModel):
    conflict_id: uuid.UUID
    conflict_type: str
    affected_items: Optional[str] = None
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ControlTowerActivitiesCreate(BaseModel):
    activity_id: uuid.UUID
    activity_type: str
    description: str
    source: Optional[str] = None
    meta_data: Optional[dict] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ControlTowerActivitiesUpdate(BaseModel):
    activity_id: Optional[uuid.UUID] = None
    activity_type: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    meta_data: Optional[dict] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ControlTowerActivitiesOut(BaseModel):
    activity_id: uuid.UUID
    activity_type: str
    description: str
    source: Optional[str] = None
    meta_data: Optional[dict] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ControlTowerAlertsCreate(BaseModel):
    alert_id: uuid.UUID
    severity: str
    message: str
    source: str
    acknowledged: Optional[bool] = None
    acknowledged_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ControlTowerAlertsUpdate(BaseModel):
    alert_id: Optional[uuid.UUID] = None
    severity: Optional[str] = None
    message: Optional[str] = None
    source: Optional[str] = None
    acknowledged: Optional[bool] = None
    acknowledged_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ControlTowerAlertsOut(BaseModel):
    alert_id: uuid.UUID
    severity: str
    message: str
    source: str
    acknowledged: Optional[bool] = None
    acknowledged_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DemandForecastsCreate(BaseModel):
    forecast_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    forecast_date: date
    forecasted_qty: float
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class DemandForecastsUpdate(BaseModel):
    forecast_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    forecast_date: Optional[date] = None
    forecasted_qty: Optional[float] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class DemandForecastsOut(BaseModel):
    forecast_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    forecast_date: date
    forecasted_qty: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DisruptionScenariosCreate(BaseModel):
    scenario_id: str
    name: str
    description: str
    disruption_type: str
    parameters: dict
    expected_impact: dict
    test_results: Optional[dict] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DisruptionScenariosUpdate(BaseModel):
    scenario_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    disruption_type: Optional[str] = None
    parameters: Optional[dict] = None
    expected_impact: Optional[dict] = None
    test_results: Optional[dict] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DisruptionScenariosOut(BaseModel):
    scenario_id: str
    name: str
    description: str
    disruption_type: str
    parameters: dict
    expected_impact: dict
    test_results: Optional[dict] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EscalationTicketsCreate(BaseModel):
    ticket_id: str
    level: int
    issue_type: str
    description: str
    urgency: float
    impact: float
    strategic_alignment: float
    deadline: datetime
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class EscalationTicketsUpdate(BaseModel):
    ticket_id: Optional[str] = None
    level: Optional[int] = None
    issue_type: Optional[str] = None
    description: Optional[str] = None
    urgency: Optional[float] = None
    impact: Optional[float] = None
    strategic_alignment: Optional[float] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class EscalationTicketsOut(BaseModel):
    ticket_id: str
    level: int
    issue_type: str
    description: str
    urgency: float
    impact: float
    strategic_alignment: float
    deadline: datetime
    status: Optional[str] = None
    resolution: Optional[dict] = None
    resolved_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ExperienceLedgerCreate(BaseModel):
    entry_id: str
    category: str
    context: dict
    decision: dict
    outcome: dict
    confidence: float
    learned_at: datetime
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExperienceLedgerUpdate(BaseModel):
    entry_id: Optional[str] = None
    category: Optional[str] = None
    context: Optional[dict] = None
    decision: Optional[dict] = None
    outcome: Optional[dict] = None
    confidence: Optional[float] = None
    learned_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExperienceLedgerOut(BaseModel):
    entry_id: str
    category: str
    context: dict
    decision: dict
    outcome: dict
    confidence: float
    learned_at: datetime
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ExperienceLedgerColdCreate(BaseModel):
    entry_id: str
    category: str
    context: dict
    decision: dict
    outcome: dict
    confidence: float
    learned_at: datetime
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExperienceLedgerColdUpdate(BaseModel):
    entry_id: Optional[str] = None
    category: Optional[str] = None
    context: Optional[dict] = None
    decision: Optional[dict] = None
    outcome: Optional[dict] = None
    confidence: Optional[float] = None
    learned_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExperienceLedgerColdOut(BaseModel):
    entry_id: str
    category: str
    context: dict
    decision: dict
    outcome: dict
    confidence: float
    learned_at: datetime
    expires_at: Optional[datetime] = None
    access_count: Optional[int] = None
    last_accessed: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class LotSizePoliciesCreate(BaseModel):
    policy_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    policy_type: str
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    fixed_order_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    carrying_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class LotSizePoliciesUpdate(BaseModel):
    policy_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    policy_type: Optional[str] = None
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    fixed_order_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    carrying_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class LotSizePoliciesOut(BaseModel):
    policy_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    policy_type: str
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    fixed_order_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    carrying_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpActionMessagesCreate(BaseModel):
    action_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    exception_id: Optional[uuid.UUID] = None
    action_type: str
    item_id: uuid.UUID
    current_value: Optional[str] = None
    suggested_value: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    executed_by: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpActionMessagesUpdate(BaseModel):
    action_id: Optional[uuid.UUID] = None
    mrp_plan_id: Optional[uuid.UUID] = None
    exception_id: Optional[uuid.UUID] = None
    action_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    current_value: Optional[str] = None
    suggested_value: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    executed_by: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpActionMessagesOut(BaseModel):
    action_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    exception_id: Optional[uuid.UUID] = None
    action_type: str
    item_id: uuid.UUID
    current_value: Optional[str] = None
    suggested_value: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    executed_by: Optional[str] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpDemandRecordsCreate(BaseModel):
    demand_record_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    period: int
    gross_quantity: float
    source_type: str
    source_id: Optional[uuid.UUID] = None
    bom_level: Optional[int] = None
    bom_path: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpDemandRecordsUpdate(BaseModel):
    demand_record_id: Optional[uuid.UUID] = None
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    period: Optional[int] = None
    gross_quantity: Optional[float] = None
    source_type: Optional[str] = None
    source_id: Optional[uuid.UUID] = None
    bom_level: Optional[int] = None
    bom_path: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpDemandRecordsOut(BaseModel):
    demand_record_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    period: int
    gross_quantity: float
    source_type: str
    source_id: Optional[uuid.UUID] = None
    bom_level: Optional[int] = None
    bom_path: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpExceptionsCreate(BaseModel):
    exception_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    exception_type: str
    severity: str
    message: str
    suggested_action: Optional[str] = None
    period: Optional[int] = None
    quantity_impact: Optional[float] = None
    cost_impact: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpExceptionsUpdate(BaseModel):
    exception_id: Optional[uuid.UUID] = None
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    exception_type: Optional[str] = None
    severity: Optional[str] = None
    message: Optional[str] = None
    suggested_action: Optional[str] = None
    period: Optional[int] = None
    quantity_impact: Optional[float] = None
    cost_impact: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpExceptionsOut(BaseModel):
    exception_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    exception_type: str
    severity: str
    message: str
    suggested_action: Optional[str] = None
    period: Optional[int] = None
    quantity_impact: Optional[float] = None
    cost_impact: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpPeggingCreate(BaseModel):
    pegging_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    demand_record_id: Optional[uuid.UUID] = None
    supply_record_id: Optional[uuid.UUID] = None
    peg_type: str
    quantity_pegged: float
    bom_level: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpPeggingUpdate(BaseModel):
    pegging_id: Optional[uuid.UUID] = None
    mrp_plan_id: Optional[uuid.UUID] = None
    demand_record_id: Optional[uuid.UUID] = None
    supply_record_id: Optional[uuid.UUID] = None
    peg_type: Optional[str] = None
    quantity_pegged: Optional[float] = None
    bom_level: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpPeggingOut(BaseModel):
    pegging_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    demand_record_id: Optional[uuid.UUID] = None
    supply_record_id: Optional[uuid.UUID] = None
    peg_type: str
    quantity_pegged: float
    bom_level: Optional[int] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpPlansCreate(BaseModel):
    mrp_plan_id: uuid.UUID
    plan_name: str
    plan_type: str
    planning_horizon_days: int
    bucket_size: str
    planning_date: date
    frozen_days: Optional[int] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpPlansUpdate(BaseModel):
    mrp_plan_id: Optional[uuid.UUID] = None
    plan_name: Optional[str] = None
    plan_type: Optional[str] = None
    planning_horizon_days: Optional[int] = None
    bucket_size: Optional[str] = None
    planning_date: Optional[date] = None
    frozen_days: Optional[int] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpPlansOut(BaseModel):
    mrp_plan_id: uuid.UUID
    plan_name: str
    plan_type: str
    planning_horizon_days: int
    bucket_size: str
    planning_date: date
    frozen_days: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MrpSupplyRecordsCreate(BaseModel):
    supply_record_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    period: int
    release_period: int
    quantity: float
    order_type: str
    source_type: Optional[str] = None
    location_id: Optional[uuid.UUID] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpSupplyRecordsUpdate(BaseModel):
    supply_record_id: Optional[uuid.UUID] = None
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    period: Optional[int] = None
    release_period: Optional[int] = None
    quantity: Optional[float] = None
    order_type: Optional[str] = None
    source_type: Optional[str] = None
    location_id: Optional[uuid.UUID] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpSupplyRecordsOut(BaseModel):
    supply_record_id: uuid.UUID
    mrp_plan_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    period: int
    release_period: int
    quantity: float
    order_type: str
    source_type: Optional[str] = None
    location_id: Optional[uuid.UUID] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    pegging_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PlanScenariosCreate(BaseModel):
    scenario_id: uuid.UUID
    base_plan_id: Optional[uuid.UUID] = None
    scenario_plan_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    comparison_metrics: Optional[dict] = None
    recommendation: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PlanScenariosUpdate(BaseModel):
    scenario_id: Optional[uuid.UUID] = None
    base_plan_id: Optional[uuid.UUID] = None
    scenario_plan_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    comparison_metrics: Optional[dict] = None
    recommendation: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PlanScenariosOut(BaseModel):
    scenario_id: uuid.UUID
    base_plan_id: Optional[uuid.UUID] = None
    scenario_plan_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    comparison_metrics: Optional[dict] = None
    recommendation: Optional[str] = None
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PlanningTimeFencesCreate(BaseModel):
    fence_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    organization_id: Optional[str] = None
    demand_time_fence_days: Optional[int] = None
    planning_time_fence_days: Optional[int] = None
    demand_fence_action: Optional[str] = None
    planning_fence_action: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PlanningTimeFencesUpdate(BaseModel):
    fence_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    organization_id: Optional[str] = None
    demand_time_fence_days: Optional[int] = None
    planning_time_fence_days: Optional[int] = None
    demand_fence_action: Optional[str] = None
    planning_fence_action: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PlanningTimeFencesOut(BaseModel):
    fence_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    organization_id: Optional[str] = None
    demand_time_fence_days: Optional[int] = None
    planning_time_fence_days: Optional[int] = None
    demand_fence_action: Optional[str] = None
    planning_fence_action: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ReplenishmentPlansCreate(BaseModel):
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    target_site_id: Optional[uuid.UUID] = None
    recommended_qty: float
    source_type: str
    status: str
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReplenishmentPlansUpdate(BaseModel):
    plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    target_site_id: Optional[uuid.UUID] = None
    recommended_qty: Optional[float] = None
    source_type: Optional[str] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReplenishmentPlansOut(BaseModel):
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    target_site_id: Optional[uuid.UUID] = None
    recommended_qty: float
    source_type: str
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiAgentExecutionLogsCreate(BaseModel):
    ai_agent_log_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    token_count: Optional[int] = None
    cost_usd: Optional[float] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiAgentExecutionLogsUpdate(BaseModel):
    ai_agent_log_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    token_count: Optional[int] = None
    cost_usd: Optional[float] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiAgentExecutionLogsOut(BaseModel):
    ai_agent_log_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    token_count: Optional[int] = None
    cost_usd: Optional[float] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiCostTrackingCreate(BaseModel):
    cost_tracking_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    model_name: Optional[str] = None
    provider: Optional[str] = None
    token_count: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    cost_per_token: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    cost_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiCostTrackingUpdate(BaseModel):
    cost_tracking_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    model_name: Optional[str] = None
    provider: Optional[str] = None
    token_count: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    cost_per_token: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    cost_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiCostTrackingOut(BaseModel):
    cost_tracking_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    model_name: Optional[str] = None
    provider: Optional[str] = None
    token_count: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    cost_per_token: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    cost_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiDecisionsCreate(BaseModel):
    ai_decision_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiDecisionsUpdate(BaseModel):
    ai_decision_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiDecisionsOut(BaseModel):
    ai_decision_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiExperimentTrackingCreate(BaseModel):
    experiment_id: uuid.UUID
    experiment_name: str
    description: Optional[str] = None
    ml_model_id: Optional[uuid.UUID] = None
    hyperparameters: Optional[dict] = None
    metrics: Optional[dict] = None
    artifacts: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    run_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiExperimentTrackingUpdate(BaseModel):
    experiment_id: Optional[uuid.UUID] = None
    experiment_name: Optional[str] = None
    description: Optional[str] = None
    ml_model_id: Optional[uuid.UUID] = None
    hyperparameters: Optional[dict] = None
    metrics: Optional[dict] = None
    artifacts: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    run_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiExperimentTrackingOut(BaseModel):
    experiment_id: uuid.UUID
    experiment_name: str
    description: Optional[str] = None
    ml_model_id: Optional[uuid.UUID] = None
    hyperparameters: Optional[dict] = None
    metrics: Optional[dict] = None
    artifacts: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    run_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiFeatureStoreCreate(BaseModel):
    feature_id: uuid.UUID
    feature_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_value: Optional[float] = None
    feature_timestamp: datetime
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiFeatureStoreUpdate(BaseModel):
    feature_id: Optional[uuid.UUID] = None
    feature_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_value: Optional[float] = None
    feature_timestamp: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiFeatureStoreOut(BaseModel):
    feature_id: uuid.UUID
    feature_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_value: Optional[float] = None
    feature_timestamp: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiModelRegistryCreate(BaseModel):
    model_registry_id: uuid.UUID
    model_code: str
    model_name: str
    model_type: str
    framework: Optional[str] = None
    version: Optional[str] = None
    deployment_status: Optional[str] = None
    meta_data: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiModelRegistryUpdate(BaseModel):
    model_registry_id: Optional[uuid.UUID] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    model_type: Optional[str] = None
    framework: Optional[str] = None
    version: Optional[str] = None
    deployment_status: Optional[str] = None
    meta_data: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiModelRegistryOut(BaseModel):
    model_registry_id: uuid.UUID
    model_code: str
    model_name: str
    model_type: str
    framework: Optional[str] = None
    version: Optional[str] = None
    deployment_status: Optional[str] = None
    meta_data: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAiWorkflowStateCreate(BaseModel):
    ai_state_id: uuid.UUID
    workflow_code: Optional[str] = None
    execution_id: Optional[uuid.UUID] = None
    state_key: str
    state_value: dict
    thread_id: Optional[str] = None
    checkpoint: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiWorkflowStateUpdate(BaseModel):
    ai_state_id: Optional[uuid.UUID] = None
    workflow_code: Optional[str] = None
    execution_id: Optional[uuid.UUID] = None
    state_key: Optional[str] = None
    state_value: Optional[dict] = None
    thread_id: Optional[str] = None
    checkpoint: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAiWorkflowStateOut(BaseModel):
    ai_state_id: uuid.UUID
    workflow_code: Optional[str] = None
    execution_id: Optional[uuid.UUID] = None
    state_key: str
    state_value: dict
    thread_id: Optional[str] = None
    checkpoint: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlertEscalationsCreate(BaseModel):
    escalation_id: uuid.UUID
    alert_id: uuid.UUID
    escalated_to: uuid.UUID
    escalation_level: int
    escalated_at: datetime
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertEscalationsUpdate(BaseModel):
    escalation_id: Optional[uuid.UUID] = None
    alert_id: Optional[uuid.UUID] = None
    escalated_to: Optional[uuid.UUID] = None
    escalation_level: Optional[int] = None
    escalated_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertEscalationsOut(BaseModel):
    escalation_id: uuid.UUID
    alert_id: uuid.UUID
    escalated_to: uuid.UUID
    escalation_level: int
    escalated_at: datetime
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlertNotificationsCreate(BaseModel):
    notification_id: uuid.UUID
    alert_id: uuid.UUID
    channel: str
    recipient: str
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertNotificationsUpdate(BaseModel):
    notification_id: Optional[uuid.UUID] = None
    alert_id: Optional[uuid.UUID] = None
    channel: Optional[str] = None
    recipient: Optional[str] = None
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertNotificationsOut(BaseModel):
    notification_id: uuid.UUID
    alert_id: uuid.UUID
    channel: str
    recipient: str
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlertRulesCreate(BaseModel):
    alert_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    alert_type_id: Optional[uuid.UUID] = None
    condition_config: dict
    severity: str
    escalation_minutes: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertRulesUpdate(BaseModel):
    alert_rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    alert_type_id: Optional[uuid.UUID] = None
    condition_config: Optional[dict] = None
    severity: Optional[str] = None
    escalation_minutes: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertRulesOut(BaseModel):
    alert_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    alert_type_id: Optional[uuid.UUID] = None
    condition_config: dict
    severity: str
    escalation_minutes: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlertTypesCreate(BaseModel):
    alert_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    default_severity: str
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertTypesUpdate(BaseModel):
    alert_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    default_severity: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertTypesOut(BaseModel):
    alert_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    default_severity: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlertsCreate(BaseModel):
    alert_id: uuid.UUID
    alert_rule_id: Optional[uuid.UUID] = None
    alert_type_id: Optional[uuid.UUID] = None
    severity: str
    title: str
    description: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    alert_data: Optional[dict] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalated_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertsUpdate(BaseModel):
    alert_id: Optional[uuid.UUID] = None
    alert_rule_id: Optional[uuid.UUID] = None
    alert_type_id: Optional[uuid.UUID] = None
    severity: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    alert_data: Optional[dict] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalated_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlertsOut(BaseModel):
    alert_id: uuid.UUID
    alert_rule_id: Optional[uuid.UUID] = None
    alert_type_id: Optional[uuid.UUID] = None
    severity: str
    title: str
    description: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    alert_data: Optional[dict] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalated_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlgorithmTestsCreate(BaseModel):
    algo_test_id: uuid.UUID
    algo_version_id: uuid.UUID
    test_name: str
    test_input: Optional[dict] = None
    expected_output: Optional[dict] = None
    actual_output: Optional[dict] = None
    passed: Optional[bool] = None
    duration_ms: Optional[int] = None
    tested_by: Optional[uuid.UUID] = None
    tested_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmTestsUpdate(BaseModel):
    algo_test_id: Optional[uuid.UUID] = None
    algo_version_id: Optional[uuid.UUID] = None
    test_name: Optional[str] = None
    test_input: Optional[dict] = None
    expected_output: Optional[dict] = None
    actual_output: Optional[dict] = None
    passed: Optional[bool] = None
    duration_ms: Optional[int] = None
    tested_by: Optional[uuid.UUID] = None
    tested_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmTestsOut(BaseModel):
    algo_test_id: uuid.UUID
    algo_version_id: uuid.UUID
    test_name: str
    test_input: Optional[dict] = None
    expected_output: Optional[dict] = None
    actual_output: Optional[dict] = None
    passed: Optional[bool] = None
    duration_ms: Optional[int] = None
    tested_by: Optional[uuid.UUID] = None
    tested_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlgorithmVersionsCreate(BaseModel):
    algo_version_id: uuid.UUID
    algorithm_id: uuid.UUID
    version_label: str
    config: Optional[dict] = None
    release_notes: Optional[str] = None
    status: Optional[str] = None
    validated_by: Optional[uuid.UUID] = None
    validated_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmVersionsUpdate(BaseModel):
    algo_version_id: Optional[uuid.UUID] = None
    algorithm_id: Optional[uuid.UUID] = None
    version_label: Optional[str] = None
    config: Optional[dict] = None
    release_notes: Optional[str] = None
    status: Optional[str] = None
    validated_by: Optional[uuid.UUID] = None
    validated_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmVersionsOut(BaseModel):
    algo_version_id: uuid.UUID
    algorithm_id: uuid.UUID
    version_label: str
    config: Optional[dict] = None
    release_notes: Optional[str] = None
    status: Optional[str] = None
    validated_by: Optional[uuid.UUID] = None
    validated_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmAlgorithmsCreate(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_code: str
    algorithm_name: str
    algorithm_type: str
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    default_params: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    version: Optional[str] = None
    code_repository_url: Optional[str] = None
    documentation_url: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmsUpdate(BaseModel):
    algorithm_id: Optional[uuid.UUID] = None
    algorithm_code: Optional[str] = None
    algorithm_name: Optional[str] = None
    algorithm_type: Optional[str] = None
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    default_params: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    version: Optional[str] = None
    code_repository_url: Optional[str] = None
    documentation_url: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmAlgorithmsOut(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_code: str
    algorithm_name: str
    algorithm_type: str
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    default_params: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    version: Optional[str] = None
    code_repository_url: Optional[str] = None
    documentation_url: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmBinPackingItemsCreate(BaseModel):
    packing_item_id: uuid.UUID
    item_id: uuid.UUID
    length_mm: float
    width_mm: float
    height_mm: float
    weight_kg: float
    allow_rotate: Optional[bool] = None
    is_fragile: Optional[bool] = None
    stackable: Optional[bool] = None
    hazmat_class: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingItemsUpdate(BaseModel):
    packing_item_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    length_mm: Optional[float] = None
    width_mm: Optional[float] = None
    height_mm: Optional[float] = None
    weight_kg: Optional[float] = None
    allow_rotate: Optional[bool] = None
    is_fragile: Optional[bool] = None
    stackable: Optional[bool] = None
    hazmat_class: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingItemsOut(BaseModel):
    packing_item_id: uuid.UUID
    item_id: uuid.UUID
    length_mm: float
    width_mm: float
    height_mm: float
    weight_kg: float
    allow_rotate: Optional[bool] = None
    is_fragile: Optional[bool] = None
    stackable: Optional[bool] = None
    hazmat_class: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmBinPackingMetricsCreate(BaseModel):
    packing_metric_id: uuid.UUID
    packing_problem_id: uuid.UUID
    bin_number: int
    volume_utilization_pct: Optional[float] = None
    weight_utilization_pct: Optional[float] = None
    wasted_volume_cbm: Optional[float] = None
    center_of_gravity_x: Optional[float] = None
    center_of_gravity_y: Optional[float] = None
    center_of_gravity_z: Optional[float] = None
    stability_score: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingMetricsUpdate(BaseModel):
    packing_metric_id: Optional[uuid.UUID] = None
    packing_problem_id: Optional[uuid.UUID] = None
    bin_number: Optional[int] = None
    volume_utilization_pct: Optional[float] = None
    weight_utilization_pct: Optional[float] = None
    wasted_volume_cbm: Optional[float] = None
    center_of_gravity_x: Optional[float] = None
    center_of_gravity_y: Optional[float] = None
    center_of_gravity_z: Optional[float] = None
    stability_score: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingMetricsOut(BaseModel):
    packing_metric_id: uuid.UUID
    packing_problem_id: uuid.UUID
    bin_number: int
    volume_utilization_pct: Optional[float] = None
    weight_utilization_pct: Optional[float] = None
    wasted_volume_cbm: Optional[float] = None
    center_of_gravity_x: Optional[float] = None
    center_of_gravity_y: Optional[float] = None
    center_of_gravity_z: Optional[float] = None
    stability_score: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmBinPackingProblemsCreate(BaseModel):
    packing_problem_id: uuid.UUID
    problem_name: str
    description: Optional[str] = None
    bin_type_id: Optional[uuid.UUID] = None
    bin_count_available: Optional[int] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    total_items: Optional[int] = None
    bins_used: Optional[int] = None
    utilization_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingProblemsUpdate(BaseModel):
    packing_problem_id: Optional[uuid.UUID] = None
    problem_name: Optional[str] = None
    description: Optional[str] = None
    bin_type_id: Optional[uuid.UUID] = None
    bin_count_available: Optional[int] = None
    objective_type: Optional[str] = None
    algorithm: Optional[str] = None
    status: Optional[str] = None
    total_items: Optional[int] = None
    bins_used: Optional[int] = None
    utilization_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingProblemsOut(BaseModel):
    packing_problem_id: uuid.UUID
    problem_name: str
    description: Optional[str] = None
    bin_type_id: Optional[uuid.UUID] = None
    bin_count_available: Optional[int] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    total_items: Optional[int] = None
    bins_used: Optional[int] = None
    utilization_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmBinPackingResultsCreate(BaseModel):
    packing_result_id: uuid.UUID
    packing_problem_id: uuid.UUID
    bin_number: int
    bin_type_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    orientation: Optional[str] = None
    weight_kg: Optional[float] = None
    sequence_num: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingResultsUpdate(BaseModel):
    packing_result_id: Optional[uuid.UUID] = None
    packing_problem_id: Optional[uuid.UUID] = None
    bin_number: Optional[int] = None
    bin_type_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    orientation: Optional[str] = None
    weight_kg: Optional[float] = None
    sequence_num: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinPackingResultsOut(BaseModel):
    packing_result_id: uuid.UUID
    packing_problem_id: uuid.UUID
    bin_number: int
    bin_type_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    orientation: Optional[str] = None
    weight_kg: Optional[float] = None
    sequence_num: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmBinTypesCreate(BaseModel):
    bin_type_id: uuid.UUID
    bin_type_code: str
    bin_type_name: str
    length_mm: float
    width_mm: float
    height_mm: float
    max_weight_kg: Optional[float] = None
    max_volume_cbm: Optional[float] = None
    tare_weight_kg: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinTypesUpdate(BaseModel):
    bin_type_id: Optional[uuid.UUID] = None
    bin_type_code: Optional[str] = None
    bin_type_name: Optional[str] = None
    length_mm: Optional[float] = None
    width_mm: Optional[float] = None
    height_mm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    max_volume_cbm: Optional[float] = None
    tare_weight_kg: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmBinTypesOut(BaseModel):
    bin_type_id: uuid.UUID
    bin_type_code: str
    bin_type_name: str
    length_mm: float
    width_mm: float
    height_mm: float
    max_weight_kg: Optional[float] = None
    max_volume_cbm: Optional[float] = None
    tare_weight_kg: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDemandClassesCreate(BaseModel):
    demand_class_id: uuid.UUID
    class_code: str
    class_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandClassesUpdate(BaseModel):
    demand_class_id: Optional[uuid.UUID] = None
    class_code: Optional[str] = None
    class_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandClassesOut(BaseModel):
    demand_class_id: uuid.UUID
    class_code: str
    class_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDemandDriversCreate(BaseModel):
    demand_driver_id: uuid.UUID
    driver_code: str
    driver_name: str
    driver_type: Optional[str] = None
    data_source: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandDriversUpdate(BaseModel):
    demand_driver_id: Optional[uuid.UUID] = None
    driver_code: Optional[str] = None
    driver_name: Optional[str] = None
    driver_type: Optional[str] = None
    data_source: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandDriversOut(BaseModel):
    demand_driver_id: uuid.UUID
    driver_code: str
    driver_name: str
    driver_type: Optional[str] = None
    data_source: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDemandSourcesCreate(BaseModel):
    demand_source_id: uuid.UUID
    source_code: str
    source_name: str
    source_type: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandSourcesUpdate(BaseModel):
    demand_source_id: Optional[uuid.UUID] = None
    source_code: Optional[str] = None
    source_name: Optional[str] = None
    source_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandSourcesOut(BaseModel):
    demand_source_id: uuid.UUID
    source_code: str
    source_name: str
    source_type: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDemandTimeSeriesCreate(BaseModel):
    time_series_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    demand_class_id: Optional[uuid.UUID] = None
    bucket_type: str
    bucket_start: date
    bucket_end: date
    quantity: float
    source_id: Optional[uuid.UUID] = None
    is_actual: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandTimeSeriesUpdate(BaseModel):
    time_series_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    demand_class_id: Optional[uuid.UUID] = None
    bucket_type: Optional[str] = None
    bucket_start: Optional[date] = None
    bucket_end: Optional[date] = None
    quantity: Optional[float] = None
    source_id: Optional[uuid.UUID] = None
    is_actual: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDemandTimeSeriesOut(BaseModel):
    time_series_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    demand_class_id: Optional[uuid.UUID] = None
    bucket_type: str
    bucket_start: date
    bucket_end: date
    quantity: float
    source_id: Optional[uuid.UUID] = None
    is_actual: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionAllocationRulesCreate(BaseModel):
    allocation_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    rule_config: Optional[dict] = None
    priority: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionAllocationRulesUpdate(BaseModel):
    allocation_rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    rule_type: Optional[str] = None
    rule_config: Optional[dict] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionAllocationRulesOut(BaseModel):
    allocation_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    rule_config: Optional[dict] = None
    priority: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionCostToServeCreate(BaseModel):
    cost_to_serve_id: uuid.UUID
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    cost_type: str
    cost_value: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionCostToServeUpdate(BaseModel):
    cost_to_serve_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    cost_type: Optional[str] = None
    cost_value: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionCostToServeOut(BaseModel):
    cost_to_serve_id: uuid.UUID
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    cost_type: str
    cost_value: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionNetworkCreate(BaseModel):
    dist_network_id: uuid.UUID
    node_code: str
    node_name: str
    node_type: str
    location_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionNetworkUpdate(BaseModel):
    dist_network_id: Optional[uuid.UUID] = None
    node_code: Optional[str] = None
    node_name: Optional[str] = None
    node_type: Optional[str] = None
    location_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionNetworkOut(BaseModel):
    dist_network_id: uuid.UUID
    node_code: str
    node_name: str
    node_type: str
    location_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionPlanLinesCreate(BaseModel):
    dist_plan_line_id: uuid.UUID
    dist_plan_id: uuid.UUID
    item_id: uuid.UUID
    from_node_id: Optional[uuid.UUID] = None
    to_node_id: Optional[uuid.UUID] = None
    quantity: float
    uom_code: Optional[str] = None
    planned_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionPlanLinesUpdate(BaseModel):
    dist_plan_line_id: Optional[uuid.UUID] = None
    dist_plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    from_node_id: Optional[uuid.UUID] = None
    to_node_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    planned_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionPlanLinesOut(BaseModel):
    dist_plan_line_id: uuid.UUID
    dist_plan_id: uuid.UUID
    item_id: uuid.UUID
    from_node_id: Optional[uuid.UUID] = None
    to_node_id: Optional[uuid.UUID] = None
    quantity: float
    uom_code: Optional[str] = None
    planned_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionPlansCreate(BaseModel):
    dist_plan_id: uuid.UUID
    plan_name: str
    description: Optional[str] = None
    plan_type: str
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionPlansUpdate(BaseModel):
    dist_plan_id: Optional[uuid.UUID] = None
    plan_name: Optional[str] = None
    description: Optional[str] = None
    plan_type: Optional[str] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionPlansOut(BaseModel):
    dist_plan_id: uuid.UUID
    plan_name: str
    description: Optional[str] = None
    plan_type: str
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmDistributionServiceLevelsCreate(BaseModel):
    service_level_id: uuid.UUID
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    target_service_level: Optional[float] = None
    target_fill_rate: Optional[float] = None
    target_otif: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionServiceLevelsUpdate(BaseModel):
    service_level_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    target_service_level: Optional[float] = None
    target_fill_rate: Optional[float] = None
    target_otif: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmDistributionServiceLevelsOut(BaseModel):
    service_level_id: uuid.UUID
    customer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    target_service_level: Optional[float] = None
    target_fill_rate: Optional[float] = None
    target_otif: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmForecastAccuracyCreate(BaseModel):
    accuracy_id: uuid.UUID
    forecast_version_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: date
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    sample_count: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastAccuracyUpdate(BaseModel):
    accuracy_id: Optional[uuid.UUID] = None
    forecast_version_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    sample_count: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastAccuracyOut(BaseModel):
    accuracy_id: uuid.UUID
    forecast_version_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: date
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    sample_count: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmForecastModelsCreate(BaseModel):
    forecast_model_id: uuid.UUID
    model_code: str
    model_name: str
    model_type: str
    model_framework: Optional[str] = None
    model_params: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastModelsUpdate(BaseModel):
    forecast_model_id: Optional[uuid.UUID] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    model_type: Optional[str] = None
    model_framework: Optional[str] = None
    model_params: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastModelsOut(BaseModel):
    forecast_model_id: uuid.UUID
    model_code: str
    model_name: str
    model_type: str
    model_framework: Optional[str] = None
    model_params: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmForecastValuesCreate(BaseModel):
    forecast_value_id: uuid.UUID
    forecast_version_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    bucket_start: date
    bucket_end: date
    point_forecast: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    actual_quantity: Optional[float] = None
    forecast_error: Optional[float] = None
    mape: Optional[float] = None
    is_overridden: Optional[bool] = None
    override_reason: Optional[str] = None
    override_by: Optional[uuid.UUID] = None
    override_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastValuesUpdate(BaseModel):
    forecast_value_id: Optional[uuid.UUID] = None
    forecast_version_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    bucket_start: Optional[date] = None
    bucket_end: Optional[date] = None
    point_forecast: Optional[float] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    actual_quantity: Optional[float] = None
    forecast_error: Optional[float] = None
    mape: Optional[float] = None
    is_overridden: Optional[bool] = None
    override_reason: Optional[str] = None
    override_by: Optional[uuid.UUID] = None
    override_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastValuesOut(BaseModel):
    forecast_value_id: uuid.UUID
    forecast_version_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    bucket_start: date
    bucket_end: date
    point_forecast: float
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    actual_quantity: Optional[float] = None
    forecast_error: Optional[float] = None
    mape: Optional[float] = None
    is_overridden: Optional[bool] = None
    override_reason: Optional[str] = None
    override_by: Optional[uuid.UUID] = None
    override_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmForecastVersionsCreate(BaseModel):
    forecast_version_id: uuid.UUID
    version_label: str
    description: Optional[str] = None
    forecast_model_id: Optional[uuid.UUID] = None
    forecast_horizon_days: Optional[int] = None
    bucket_type: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastVersionsUpdate(BaseModel):
    forecast_version_id: Optional[uuid.UUID] = None
    version_label: Optional[str] = None
    description: Optional[str] = None
    forecast_model_id: Optional[uuid.UUID] = None
    forecast_horizon_days: Optional[int] = None
    bucket_type: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmForecastVersionsOut(BaseModel):
    forecast_version_id: uuid.UUID
    version_label: str
    description: Optional[str] = None
    forecast_model_id: Optional[uuid.UUID] = None
    forecast_horizon_days: Optional[int] = None
    bucket_type: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmIntegrationConnectionsCreate(BaseModel):
    connection_id: uuid.UUID
    connection_code: str
    connection_name: str
    connection_type: str
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[uuid.UUID] = None
    connection_code: Optional[str] = None
    connection_name: Optional[str] = None
    connection_type: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationConnectionsOut(BaseModel):
    connection_id: uuid.UUID
    connection_code: str
    connection_name: str
    connection_type: str
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmIntegrationLogsCreate(BaseModel):
    integration_log_id: uuid.UUID
    connection_id: Optional[uuid.UUID] = None
    direction: str
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: str
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: datetime
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationLogsUpdate(BaseModel):
    integration_log_id: Optional[uuid.UUID] = None
    connection_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationLogsOut(BaseModel):
    integration_log_id: uuid.UUID
    connection_id: Optional[uuid.UUID] = None
    direction: str
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: str
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmIntegrationMappingsCreate(BaseModel):
    mapping_id: uuid.UUID
    connection_id: uuid.UUID
    mapping_name: str
    source_field: str
    target_field: str
    transformation: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationMappingsUpdate(BaseModel):
    mapping_id: Optional[uuid.UUID] = None
    connection_id: Optional[uuid.UUID] = None
    mapping_name: Optional[str] = None
    source_field: Optional[str] = None
    target_field: Optional[str] = None
    transformation: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmIntegrationMappingsOut(BaseModel):
    mapping_id: uuid.UUID
    connection_id: uuid.UUID
    mapping_name: str
    source_field: str
    target_field: str
    transformation: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryAgingCreate(BaseModel):
    aging_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    batch_ref: Optional[str] = None
    quantity: float
    receipt_date: date
    age_days: Optional[int] = None
    expiry_date: Optional[date] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryAgingUpdate(BaseModel):
    aging_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    batch_ref: Optional[str] = None
    quantity: Optional[float] = None
    receipt_date: Optional[date] = None
    age_days: Optional[int] = None
    expiry_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryAgingOut(BaseModel):
    aging_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    batch_ref: Optional[str] = None
    quantity: float
    receipt_date: date
    age_days: Optional[int] = None
    expiry_date: Optional[date] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryClassificationsCreate(BaseModel):
    classification_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    abc_class: Optional[str] = None
    xyz_class: Optional[str] = None
    fsn_class: Optional[str] = None
    ved_class: Optional[str] = None
    classification_date: date
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryClassificationsUpdate(BaseModel):
    classification_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    abc_class: Optional[str] = None
    xyz_class: Optional[str] = None
    fsn_class: Optional[str] = None
    ved_class: Optional[str] = None
    classification_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryClassificationsOut(BaseModel):
    classification_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    abc_class: Optional[str] = None
    xyz_class: Optional[str] = None
    fsn_class: Optional[str] = None
    ved_class: Optional[str] = None
    classification_date: date
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryHealthCreate(BaseModel):
    health_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: date
    inventory_turns: Optional[float] = None
    days_of_supply: Optional[int] = None
    excess_qty: Optional[float] = None
    obsolescence_qty: Optional[float] = None
    stockout_count: Optional[int] = None
    fill_rate: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryHealthUpdate(BaseModel):
    health_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    inventory_turns: Optional[float] = None
    days_of_supply: Optional[int] = None
    excess_qty: Optional[float] = None
    obsolescence_qty: Optional[float] = None
    stockout_count: Optional[int] = None
    fill_rate: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryHealthOut(BaseModel):
    health_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    evaluation_date: date
    inventory_turns: Optional[float] = None
    days_of_supply: Optional[int] = None
    excess_qty: Optional[float] = None
    obsolescence_qty: Optional[float] = None
    stockout_count: Optional[int] = None
    fill_rate: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryOptimizationParamsCreate(BaseModel):
    param_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    holding_cost: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    target_service_level: Optional[float] = None
    demand_variance: Optional[float] = None
    lead_time_variance: Optional[float] = None
    review_period_days: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryOptimizationParamsUpdate(BaseModel):
    param_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    holding_cost: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    target_service_level: Optional[float] = None
    demand_variance: Optional[float] = None
    lead_time_variance: Optional[float] = None
    review_period_days: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryOptimizationParamsOut(BaseModel):
    param_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    holding_cost: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    target_service_level: Optional[float] = None
    demand_variance: Optional[float] = None
    lead_time_variance: Optional[float] = None
    review_period_days: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryPoliciesCreate(BaseModel):
    inventory_policy_id: uuid.UUID
    policy_code: str
    policy_name: str
    policy_type: str
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    min_quantity: Optional[float] = None
    max_quantity: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    safety_stock: Optional[float] = None
    target_service_level: Optional[float] = None
    holding_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryPoliciesUpdate(BaseModel):
    inventory_policy_id: Optional[uuid.UUID] = None
    policy_code: Optional[str] = None
    policy_name: Optional[str] = None
    policy_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    min_quantity: Optional[float] = None
    max_quantity: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    safety_stock: Optional[float] = None
    target_service_level: Optional[float] = None
    holding_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryPoliciesOut(BaseModel):
    inventory_policy_id: uuid.UUID
    policy_code: str
    policy_name: str
    policy_type: str
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    min_quantity: Optional[float] = None
    max_quantity: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_qty: Optional[float] = None
    safety_stock: Optional[float] = None
    target_service_level: Optional[float] = None
    holding_cost_pct: Optional[float] = None
    ordering_cost: Optional[float] = None
    shortage_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryRecommendationsCreate(BaseModel):
    recommendation_id: uuid.UUID
    rec_type: str
    item_id: uuid.UUID
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    quantity: float
    priority: Optional[int] = None
    reason_code: Optional[str] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryRecommendationsUpdate(BaseModel):
    recommendation_id: Optional[uuid.UUID] = None
    rec_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    priority: Optional[int] = None
    reason_code: Optional[str] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryRecommendationsOut(BaseModel):
    recommendation_id: uuid.UUID
    rec_type: str
    item_id: uuid.UUID
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    quantity: float
    priority: Optional[int] = None
    reason_code: Optional[str] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmInventoryTargetsCreate(BaseModel):
    inventory_target_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    target_qty: float
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    target_dos: Optional[int] = None
    effective_from: date
    effective_to: Optional[date] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryTargetsUpdate(BaseModel):
    inventory_target_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    target_qty: Optional[float] = None
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    target_dos: Optional[int] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmInventoryTargetsOut(BaseModel):
    inventory_target_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    target_qty: float
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    target_dos: Optional[int] = None
    effective_from: date
    effective_to: Optional[date] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmKpiAlertsCreate(BaseModel):
    kpi_alert_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    kpi_value_id: Optional[uuid.UUID] = None
    alert_type: str
    threshold_breached: str
    actual_value: Optional[float] = None
    threshold_value: Optional[float] = None
    alerted_at: datetime
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiAlertsUpdate(BaseModel):
    kpi_alert_id: Optional[uuid.UUID] = None
    kpi_definition_id: Optional[uuid.UUID] = None
    kpi_value_id: Optional[uuid.UUID] = None
    alert_type: Optional[str] = None
    threshold_breached: Optional[str] = None
    actual_value: Optional[float] = None
    threshold_value: Optional[float] = None
    alerted_at: Optional[datetime] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiAlertsOut(BaseModel):
    kpi_alert_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    kpi_value_id: Optional[uuid.UUID] = None
    alert_type: str
    threshold_breached: str
    actual_value: Optional[float] = None
    threshold_value: Optional[float] = None
    alerted_at: datetime
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmKpiBenchmarksCreate(BaseModel):
    benchmark_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    benchmark_type: str
    benchmark_value: Optional[float] = None
    source: Optional[str] = None
    evaluation_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiBenchmarksUpdate(BaseModel):
    benchmark_id: Optional[uuid.UUID] = None
    kpi_definition_id: Optional[uuid.UUID] = None
    benchmark_type: Optional[str] = None
    benchmark_value: Optional[float] = None
    source: Optional[str] = None
    evaluation_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiBenchmarksOut(BaseModel):
    benchmark_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    benchmark_type: str
    benchmark_value: Optional[float] = None
    source: Optional[str] = None
    evaluation_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmKpiDefinitionsCreate(BaseModel):
    kpi_definition_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: str
    formula: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green: Optional[float] = None
    threshold_yellow: Optional[float] = None
    threshold_red: Optional[float] = None
    frequency: Optional[str] = None
    data_source: Optional[str] = None
    owner_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiDefinitionsUpdate(BaseModel):
    kpi_definition_id: Optional[uuid.UUID] = None
    kpi_code: Optional[str] = None
    kpi_name: Optional[str] = None
    kpi_category: Optional[str] = None
    formula: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green: Optional[float] = None
    threshold_yellow: Optional[float] = None
    threshold_red: Optional[float] = None
    frequency: Optional[str] = None
    data_source: Optional[str] = None
    owner_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiDefinitionsOut(BaseModel):
    kpi_definition_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: str
    formula: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green: Optional[float] = None
    threshold_yellow: Optional[float] = None
    threshold_red: Optional[float] = None
    frequency: Optional[str] = None
    data_source: Optional[str] = None
    owner_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmKpiValuesCreate(BaseModel):
    kpi_value_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: date
    period_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiValuesUpdate(BaseModel):
    kpi_value_id: Optional[uuid.UUID] = None
    kpi_definition_id: Optional[uuid.UUID] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: Optional[date] = None
    period_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmKpiValuesOut(BaseModel):
    kpi_value_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: date
    period_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainAgentExecutionsCreate(BaseModel):
    agent_execution_id: uuid.UUID
    agent_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    tool_calls: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainAgentExecutionsUpdate(BaseModel):
    agent_execution_id: Optional[uuid.UUID] = None
    agent_id: Optional[uuid.UUID] = None
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    tool_calls: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainAgentExecutionsOut(BaseModel):
    agent_execution_id: uuid.UUID
    agent_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    tool_calls: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainAgentsCreate(BaseModel):
    agent_id: uuid.UUID
    agent_code: str
    agent_name: str
    agent_type: str
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    prompt_template_id: Optional[uuid.UUID] = None
    agent_config: Optional[dict] = None
    memory_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainAgentsUpdate(BaseModel):
    agent_id: Optional[uuid.UUID] = None
    agent_code: Optional[str] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    prompt_template_id: Optional[uuid.UUID] = None
    agent_config: Optional[dict] = None
    memory_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainAgentsOut(BaseModel):
    agent_id: uuid.UUID
    agent_code: str
    agent_name: str
    agent_type: str
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    prompt_template_id: Optional[uuid.UUID] = None
    agent_config: Optional[dict] = None
    memory_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainChainsCreate(BaseModel):
    chain_id: uuid.UUID
    chain_code: str
    chain_name: str
    chain_type: str
    llm_config_id: Optional[uuid.UUID] = None
    prompt_template_id: Optional[uuid.UUID] = None
    chain_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainChainsUpdate(BaseModel):
    chain_id: Optional[uuid.UUID] = None
    chain_code: Optional[str] = None
    chain_name: Optional[str] = None
    chain_type: Optional[str] = None
    llm_config_id: Optional[uuid.UUID] = None
    prompt_template_id: Optional[uuid.UUID] = None
    chain_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainChainsOut(BaseModel):
    chain_id: uuid.UUID
    chain_code: str
    chain_name: str
    chain_type: str
    llm_config_id: Optional[uuid.UUID] = None
    prompt_template_id: Optional[uuid.UUID] = None
    chain_config: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainDocumentsCreate(BaseModel):
    document_id: uuid.UUID
    vector_store_id: Optional[uuid.UUID] = None
    document_source: Optional[str] = None
    content: str
    meta_data: Optional[dict] = None
    chunk_count: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainDocumentsUpdate(BaseModel):
    document_id: Optional[uuid.UUID] = None
    vector_store_id: Optional[uuid.UUID] = None
    document_source: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    chunk_count: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainDocumentsOut(BaseModel):
    document_id: uuid.UUID
    vector_store_id: Optional[uuid.UUID] = None
    document_source: Optional[str] = None
    content: str
    meta_data: Optional[dict] = None
    chunk_count: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainExecutionsCreate(BaseModel):
    chain_execution_id: uuid.UUID
    chain_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainExecutionsUpdate(BaseModel):
    chain_execution_id: Optional[uuid.UUID] = None
    chain_id: Optional[uuid.UUID] = None
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainExecutionsOut(BaseModel):
    chain_execution_id: uuid.UUID
    chain_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage: Optional[dict] = None
    cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainLlmConfigsCreate(BaseModel):
    llm_config_id: uuid.UUID
    config_code: str
    provider: str
    model_name: str
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    parameters: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainLlmConfigsUpdate(BaseModel):
    llm_config_id: Optional[uuid.UUID] = None
    config_code: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    parameters: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainLlmConfigsOut(BaseModel):
    llm_config_id: uuid.UUID
    config_code: str
    provider: str
    model_name: str
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    parameters: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainPromptTemplatesCreate(BaseModel):
    prompt_template_id: uuid.UUID
    template_code: str
    template_name: str
    template_text: str
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainPromptTemplatesUpdate(BaseModel):
    prompt_template_id: Optional[uuid.UUID] = None
    template_code: Optional[str] = None
    template_name: Optional[str] = None
    template_text: Optional[str] = None
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainPromptTemplatesOut(BaseModel):
    prompt_template_id: uuid.UUID
    template_code: str
    template_name: str
    template_text: str
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLangchainVectorStoresCreate(BaseModel):
    vector_store_id: uuid.UUID
    store_code: str
    store_name: str
    store_type: str
    connection_config: Optional[dict] = None
    embedding_model: Optional[str] = None
    dimension: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainVectorStoresUpdate(BaseModel):
    vector_store_id: Optional[uuid.UUID] = None
    store_code: Optional[str] = None
    store_name: Optional[str] = None
    store_type: Optional[str] = None
    connection_config: Optional[dict] = None
    embedding_model: Optional[str] = None
    dimension: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLangchainVectorStoresOut(BaseModel):
    vector_store_id: uuid.UUID
    store_code: str
    store_name: str
    store_type: str
    connection_config: Optional[dict] = None
    embedding_model: Optional[str] = None
    dimension: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLanggraphEdgesCreate(BaseModel):
    lg_edge_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    from_node_id: str
    to_node_id: str
    condition_expr: Optional[str] = None
    priority: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphEdgesUpdate(BaseModel):
    lg_edge_id: Optional[uuid.UUID] = None
    lg_workflow_id: Optional[uuid.UUID] = None
    from_node_id: Optional[str] = None
    to_node_id: Optional[str] = None
    condition_expr: Optional[str] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphEdgesOut(BaseModel):
    lg_edge_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    from_node_id: str
    to_node_id: str
    condition_expr: Optional[str] = None
    priority: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLanggraphExecutionsCreate(BaseModel):
    lg_execution_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphExecutionsUpdate(BaseModel):
    lg_execution_id: Optional[uuid.UUID] = None
    lg_workflow_id: Optional[uuid.UUID] = None
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphExecutionsOut(BaseModel):
    lg_execution_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    execution_label: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLanggraphLogsCreate(BaseModel):
    lg_log_id: uuid.UUID
    lg_execution_id: uuid.UUID
    node_id: Optional[str] = None
    log_level: str
    message: str
    log_data: Optional[dict] = None
    logged_at: datetime
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphLogsUpdate(BaseModel):
    lg_log_id: Optional[uuid.UUID] = None
    lg_execution_id: Optional[uuid.UUID] = None
    node_id: Optional[str] = None
    log_level: Optional[str] = None
    message: Optional[str] = None
    log_data: Optional[dict] = None
    logged_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphLogsOut(BaseModel):
    lg_log_id: uuid.UUID
    lg_execution_id: uuid.UUID
    node_id: Optional[str] = None
    log_level: str
    message: str
    log_data: Optional[dict] = None
    logged_at: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLanggraphNodesCreate(BaseModel):
    lg_node_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    node_id: str
    node_type: str
    function_name: Optional[str] = None
    config: Optional[dict] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphNodesUpdate(BaseModel):
    lg_node_id: Optional[uuid.UUID] = None
    lg_workflow_id: Optional[uuid.UUID] = None
    node_id: Optional[str] = None
    node_type: Optional[str] = None
    function_name: Optional[str] = None
    config: Optional[dict] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphNodesOut(BaseModel):
    lg_node_id: uuid.UUID
    lg_workflow_id: uuid.UUID
    node_id: str
    node_type: str
    function_name: Optional[str] = None
    config: Optional[dict] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmLanggraphWorkflowsCreate(BaseModel):
    lg_workflow_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphWorkflowsUpdate(BaseModel):
    lg_workflow_id: Optional[uuid.UUID] = None
    workflow_code: Optional[str] = None
    workflow_name: Optional[str] = None
    description: Optional[str] = None
    dag_definition: Optional[dict] = None
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmLanggraphWorkflowsOut(BaseModel):
    lg_workflow_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmMlModelDeploymentsCreate(BaseModel):
    deployment_id: uuid.UUID
    ml_model_id: uuid.UUID
    version: str
    environment: str
    endpoint_url: Optional[str] = None
    deployed_at: Optional[datetime] = None
    deployed_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    rollback_version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelDeploymentsUpdate(BaseModel):
    deployment_id: Optional[uuid.UUID] = None
    ml_model_id: Optional[uuid.UUID] = None
    version: Optional[str] = None
    environment: Optional[str] = None
    endpoint_url: Optional[str] = None
    deployed_at: Optional[datetime] = None
    deployed_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    rollback_version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelDeploymentsOut(BaseModel):
    deployment_id: uuid.UUID
    ml_model_id: uuid.UUID
    version: str
    environment: str
    endpoint_url: Optional[str] = None
    deployed_at: Optional[datetime] = None
    deployed_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    rollback_version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmMlModelTypesCreate(BaseModel):
    ml_model_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelTypesUpdate(BaseModel):
    ml_model_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelTypesOut(BaseModel):
    ml_model_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmMlModelsCreate(BaseModel):
    ml_model_id: uuid.UUID
    model_code: str
    model_name: str
    model_type_id: Optional[uuid.UUID] = None
    framework: Optional[str] = None
    version: Optional[str] = None
    hyperparameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    model_explainability: Optional[dict] = None
    deployment_status: Optional[str] = None
    inference_endpoint: Optional[str] = None
    monitoring_config: Optional[dict] = None
    retrain_schedule: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelsUpdate(BaseModel):
    ml_model_id: Optional[uuid.UUID] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    model_type_id: Optional[uuid.UUID] = None
    framework: Optional[str] = None
    version: Optional[str] = None
    hyperparameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    model_explainability: Optional[dict] = None
    deployment_status: Optional[str] = None
    inference_endpoint: Optional[str] = None
    monitoring_config: Optional[dict] = None
    retrain_schedule: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlModelsOut(BaseModel):
    ml_model_id: uuid.UUID
    model_code: str
    model_name: str
    model_type_id: Optional[uuid.UUID] = None
    framework: Optional[str] = None
    version: Optional[str] = None
    hyperparameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    model_explainability: Optional[dict] = None
    deployment_status: Optional[str] = None
    inference_endpoint: Optional[str] = None
    monitoring_config: Optional[dict] = None
    retrain_schedule: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmMlMonitoringCreate(BaseModel):
    monitoring_id: uuid.UUID
    ml_model_id: uuid.UUID
    evaluation_date: date
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    drift_score: Optional[float] = None
    data_drift_detected: Optional[bool] = None
    sample_count: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlMonitoringUpdate(BaseModel):
    monitoring_id: Optional[uuid.UUID] = None
    ml_model_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    drift_score: Optional[float] = None
    data_drift_detected: Optional[bool] = None
    sample_count: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlMonitoringOut(BaseModel):
    monitoring_id: uuid.UUID
    ml_model_id: uuid.UUID
    evaluation_date: date
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    drift_score: Optional[float] = None
    data_drift_detected: Optional[bool] = None
    sample_count: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmMlTrainingRunsCreate(BaseModel):
    training_run_id: uuid.UUID
    ml_model_id: uuid.UUID
    run_label: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    test_metrics: Optional[dict] = None
    duration_seconds: Optional[int] = None
    status: Optional[str] = None
    run_by: Optional[uuid.UUID] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlTrainingRunsUpdate(BaseModel):
    training_run_id: Optional[uuid.UUID] = None
    ml_model_id: Optional[uuid.UUID] = None
    run_label: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    test_metrics: Optional[dict] = None
    duration_seconds: Optional[int] = None
    status: Optional[str] = None
    run_by: Optional[uuid.UUID] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmMlTrainingRunsOut(BaseModel):
    training_run_id: uuid.UUID
    ml_model_id: uuid.UUID
    run_label: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    test_metrics: Optional[dict] = None
    duration_seconds: Optional[int] = None
    status: Optional[str] = None
    run_by: Optional[uuid.UUID] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkArcsCreate(BaseModel):
    arc_id: uuid.UUID
    arc_code: str
    from_node_id: uuid.UUID
    to_node_id: uuid.UUID
    distance_km: Optional[float] = None
    transit_days: Optional[int] = None
    cost_per_unit: Optional[float] = None
    carbon_per_km: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkArcsUpdate(BaseModel):
    arc_id: Optional[uuid.UUID] = None
    arc_code: Optional[str] = None
    from_node_id: Optional[uuid.UUID] = None
    to_node_id: Optional[uuid.UUID] = None
    distance_km: Optional[float] = None
    transit_days: Optional[int] = None
    cost_per_unit: Optional[float] = None
    carbon_per_km: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkArcsOut(BaseModel):
    arc_id: uuid.UUID
    arc_code: str
    from_node_id: uuid.UUID
    to_node_id: uuid.UUID
    distance_km: Optional[float] = None
    transit_days: Optional[int] = None
    cost_per_unit: Optional[float] = None
    carbon_per_km: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkCapacitiesCreate(BaseModel):
    capacity_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    capacity_type: str
    capacity_qty: float
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkCapacitiesUpdate(BaseModel):
    capacity_id: Optional[uuid.UUID] = None
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    capacity_type: Optional[str] = None
    capacity_qty: Optional[float] = None
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkCapacitiesOut(BaseModel):
    capacity_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    capacity_type: str
    capacity_qty: float
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkCostsCreate(BaseModel):
    network_cost_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    cost_type: str
    fixed_cost: Optional[float] = None
    variable_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkCostsUpdate(BaseModel):
    network_cost_id: Optional[uuid.UUID] = None
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    cost_type: Optional[str] = None
    fixed_cost: Optional[float] = None
    variable_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkCostsOut(BaseModel):
    network_cost_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    cost_type: str
    fixed_cost: Optional[float] = None
    variable_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkFlowsCreate(BaseModel):
    flow_id: uuid.UUID
    network_scenario_id: uuid.UUID
    from_node_id: uuid.UUID
    to_node_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    quantity: float
    flow_cost: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkFlowsUpdate(BaseModel):
    flow_id: Optional[uuid.UUID] = None
    network_scenario_id: Optional[uuid.UUID] = None
    from_node_id: Optional[uuid.UUID] = None
    to_node_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    flow_cost: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkFlowsOut(BaseModel):
    flow_id: uuid.UUID
    network_scenario_id: uuid.UUID
    from_node_id: uuid.UUID
    to_node_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    quantity: float
    flow_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkNodesCreate(BaseModel):
    node_id: uuid.UUID
    node_code: str
    node_name: str
    node_type: str
    location_id: Optional[uuid.UUID] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkNodesUpdate(BaseModel):
    node_id: Optional[uuid.UUID] = None
    node_code: Optional[str] = None
    node_name: Optional[str] = None
    node_type: Optional[str] = None
    location_id: Optional[uuid.UUID] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkNodesOut(BaseModel):
    node_id: uuid.UUID
    node_code: str
    node_name: str
    node_type: str
    location_id: Optional[uuid.UUID] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkRiskAssessmentCreate(BaseModel):
    risk_assessment_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    risk_type: str
    risk_probability: Optional[float] = None
    risk_impact: Optional[float] = None
    risk_score: Optional[float] = None
    mitigation_status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkRiskAssessmentUpdate(BaseModel):
    risk_assessment_id: Optional[uuid.UUID] = None
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    risk_type: Optional[str] = None
    risk_probability: Optional[float] = None
    risk_impact: Optional[float] = None
    risk_score: Optional[float] = None
    mitigation_status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkRiskAssessmentOut(BaseModel):
    risk_assessment_id: uuid.UUID
    node_id: Optional[uuid.UUID] = None
    arc_id: Optional[uuid.UUID] = None
    risk_type: str
    risk_probability: Optional[float] = None
    risk_impact: Optional[float] = None
    risk_score: Optional[float] = None
    mitigation_status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmNetworkScenariosCreate(BaseModel):
    network_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    scenario_type: str
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkScenariosUpdate(BaseModel):
    network_scenario_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    scenario_type: Optional[str] = None
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmNetworkScenariosOut(BaseModel):
    network_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    scenario_type: str
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOptimizationExecutionLogCreate(BaseModel):
    exec_log_id: uuid.UUID
    problem_id: uuid.UUID
    started_at: datetime
    completed_at: Optional[datetime] = None
    status: str
    error_message: Optional[str] = None
    solver_type: Optional[str] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationExecutionLogUpdate(BaseModel):
    exec_log_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    solver_type: Optional[str] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationExecutionLogOut(BaseModel):
    exec_log_id: uuid.UUID
    problem_id: uuid.UUID
    started_at: datetime
    completed_at: Optional[datetime] = None
    status: str
    error_message: Optional[str] = None
    solver_type: Optional[str] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOptimizationProblemsCreate(BaseModel):
    problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    objective_function: Optional[dict] = None
    constraints_def: Optional[dict] = None
    variables_def: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solution_id: Optional[uuid.UUID] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationProblemsUpdate(BaseModel):
    problem_id: Optional[uuid.UUID] = None
    problem_code: Optional[str] = None
    problem_name: Optional[str] = None
    problem_type: Optional[str] = None
    description: Optional[str] = None
    objective_type: Optional[str] = None
    objective_function: Optional[dict] = None
    constraints_def: Optional[dict] = None
    variables_def: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solution_id: Optional[uuid.UUID] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationProblemsOut(BaseModel):
    problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    objective_function: Optional[dict] = None
    constraints_def: Optional[dict] = None
    variables_def: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solution_id: Optional[uuid.UUID] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOptimizationSensitivityCreate(BaseModel):
    sensitivity_id: uuid.UUID
    solution_id: uuid.UUID
    parameter_name: str
    base_value: Optional[float] = None
    low_value: Optional[float] = None
    high_value: Optional[float] = None
    impact_on_objective: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationSensitivityUpdate(BaseModel):
    sensitivity_id: Optional[uuid.UUID] = None
    solution_id: Optional[uuid.UUID] = None
    parameter_name: Optional[str] = None
    base_value: Optional[float] = None
    low_value: Optional[float] = None
    high_value: Optional[float] = None
    impact_on_objective: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationSensitivityOut(BaseModel):
    sensitivity_id: uuid.UUID
    solution_id: uuid.UUID
    parameter_name: str
    base_value: Optional[float] = None
    low_value: Optional[float] = None
    high_value: Optional[float] = None
    impact_on_objective: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOptimizationSolutionsCreate(BaseModel):
    solution_id: uuid.UUID
    problem_id: uuid.UUID
    solution_label: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_feasible: Optional[bool] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationSolutionsUpdate(BaseModel):
    solution_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    solution_label: Optional[str] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_feasible: Optional[bool] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOptimizationSolutionsOut(BaseModel):
    solution_id: uuid.UUID
    problem_id: uuid.UUID
    solution_label: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    gap_pct: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_feasible: Optional[bool] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOrtoolsProblemsCreate(BaseModel):
    ortools_problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    problem_definition: dict
    input_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    warm_start_solution: Optional[dict] = None
    parallelization_config: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOrtoolsProblemsUpdate(BaseModel):
    ortools_problem_id: Optional[uuid.UUID] = None
    problem_code: Optional[str] = None
    problem_name: Optional[str] = None
    problem_type: Optional[str] = None
    problem_definition: Optional[dict] = None
    input_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    warm_start_solution: Optional[dict] = None
    parallelization_config: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOrtoolsProblemsOut(BaseModel):
    ortools_problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    problem_definition: dict
    input_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    warm_start_solution: Optional[dict] = None
    parallelization_config: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmOrtoolsSolutionsCreate(BaseModel):
    ortools_solution_id: uuid.UUID
    ortools_problem_id: uuid.UUID
    solution_label: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    gap_pct: Optional[float] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOrtoolsSolutionsUpdate(BaseModel):
    ortools_solution_id: Optional[uuid.UUID] = None
    ortools_problem_id: Optional[uuid.UUID] = None
    solution_label: Optional[str] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    gap_pct: Optional[float] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmOrtoolsSolutionsOut(BaseModel):
    ortools_solution_id: uuid.UUID
    ortools_problem_id: uuid.UUID
    solution_label: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    gap_pct: Optional[float] = None
    solver_status: Optional[str] = None
    is_optimal: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPickPathLearningCreate(BaseModel):
    learning_id: uuid.UUID
    picker_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    historical_path: Optional[dict] = None
    actual_distance_m: Optional[float] = None
    actual_duration_min: Optional[int] = None
    optimal_distance_m: Optional[float] = None
    optimal_duration_min: Optional[int] = None
    efficiency_pct: Optional[float] = None
    pick_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathLearningUpdate(BaseModel):
    learning_id: Optional[uuid.UUID] = None
    picker_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    historical_path: Optional[dict] = None
    actual_distance_m: Optional[float] = None
    actual_duration_min: Optional[int] = None
    optimal_distance_m: Optional[float] = None
    optimal_duration_min: Optional[int] = None
    efficiency_pct: Optional[float] = None
    pick_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathLearningOut(BaseModel):
    learning_id: uuid.UUID
    picker_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    historical_path: Optional[dict] = None
    actual_distance_m: Optional[float] = None
    actual_duration_min: Optional[int] = None
    optimal_distance_m: Optional[float] = None
    optimal_duration_min: Optional[int] = None
    efficiency_pct: Optional[float] = None
    pick_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPickPathProblemsCreate(BaseModel):
    pick_path_problem_id: uuid.UUID
    problem_name: str
    warehouse_id: uuid.UUID
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    location_count: Optional[int] = None
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    solve_time_ms: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathProblemsUpdate(BaseModel):
    pick_path_problem_id: Optional[uuid.UUID] = None
    problem_name: Optional[str] = None
    warehouse_id: Optional[uuid.UUID] = None
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    objective_type: Optional[str] = None
    algorithm: Optional[str] = None
    status: Optional[str] = None
    location_count: Optional[int] = None
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    solve_time_ms: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathProblemsOut(BaseModel):
    pick_path_problem_id: uuid.UUID
    problem_name: str
    warehouse_id: uuid.UUID
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    location_count: Optional[int] = None
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    solve_time_ms: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPickPathSolutionsCreate(BaseModel):
    pick_path_solution_id: uuid.UUID
    pick_path_problem_id: uuid.UUID
    picker_id: Optional[uuid.UUID] = None
    location_sequence: dict
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    locations_visited: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathSolutionsUpdate(BaseModel):
    pick_path_solution_id: Optional[uuid.UUID] = None
    pick_path_problem_id: Optional[uuid.UUID] = None
    picker_id: Optional[uuid.UUID] = None
    location_sequence: Optional[dict] = None
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    locations_visited: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPickPathSolutionsOut(BaseModel):
    pick_path_solution_id: uuid.UUID
    pick_path_problem_id: uuid.UUID
    picker_id: Optional[uuid.UUID] = None
    location_sequence: dict
    total_distance_m: Optional[float] = None
    total_duration_min: Optional[int] = None
    locations_visited: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPredictionAccuracyCreate(BaseModel):
    pred_accuracy_id: uuid.UUID
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    evaluation_date: date
    total_predictions: Optional[int] = None
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionAccuracyUpdate(BaseModel):
    pred_accuracy_id: Optional[uuid.UUID] = None
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    total_predictions: Optional[int] = None
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionAccuracyOut(BaseModel):
    pred_accuracy_id: uuid.UUID
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    evaluation_date: date
    total_predictions: Optional[int] = None
    mape: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    bias: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPredictionFeaturesCreate(BaseModel):
    feature_id: uuid.UUID
    prediction_id: uuid.UUID
    feature_name: str
    feature_value: Optional[float] = None
    feature_importance: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionFeaturesUpdate(BaseModel):
    feature_id: Optional[uuid.UUID] = None
    prediction_id: Optional[uuid.UUID] = None
    feature_name: Optional[str] = None
    feature_value: Optional[float] = None
    feature_importance: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionFeaturesOut(BaseModel):
    feature_id: uuid.UUID
    prediction_id: uuid.UUID
    feature_name: str
    feature_value: Optional[float] = None
    feature_importance: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPredictionOverridesCreate(BaseModel):
    override_id: uuid.UUID
    prediction_id: uuid.UUID
    override_value: float
    original_value: float
    reason: str
    override_by: uuid.UUID
    override_at: datetime
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionOverridesUpdate(BaseModel):
    override_id: Optional[uuid.UUID] = None
    prediction_id: Optional[uuid.UUID] = None
    override_value: Optional[float] = None
    original_value: Optional[float] = None
    reason: Optional[str] = None
    override_by: Optional[uuid.UUID] = None
    override_at: Optional[datetime] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionOverridesOut(BaseModel):
    override_id: uuid.UUID
    prediction_id: uuid.UUID
    override_value: float
    original_value: float
    reason: str
    override_by: uuid.UUID
    override_at: datetime
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPredictionTypesCreate(BaseModel):
    prediction_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionTypesUpdate(BaseModel):
    prediction_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionTypesOut(BaseModel):
    prediction_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPredictionsCreate(BaseModel):
    prediction_id: uuid.UUID
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    prediction_date: date
    prediction_value: Optional[float] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    features: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionsUpdate(BaseModel):
    prediction_id: Optional[uuid.UUID] = None
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    prediction_date: Optional[date] = None
    prediction_value: Optional[float] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    features: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPredictionsOut(BaseModel):
    prediction_id: uuid.UUID
    ml_model_id: Optional[uuid.UUID] = None
    prediction_type_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    prediction_date: date
    prediction_value: Optional[float] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    confidence_level: Optional[float] = None
    features: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementContractsCreate(BaseModel):
    contract_id: uuid.UUID
    contract_number: str
    partner_id: uuid.UUID
    contract_type: str
    start_date: date
    end_date: Optional[date] = None
    value_limit: Optional[float] = None
    currency_code: Optional[str] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementContractsUpdate(BaseModel):
    contract_id: Optional[uuid.UUID] = None
    contract_number: Optional[str] = None
    partner_id: Optional[uuid.UUID] = None
    contract_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    value_limit: Optional[float] = None
    currency_code: Optional[str] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementContractsOut(BaseModel):
    contract_id: uuid.UUID
    contract_number: str
    partner_id: uuid.UUID
    contract_type: str
    start_date: date
    end_date: Optional[date] = None
    value_limit: Optional[float] = None
    currency_code: Optional[str] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementRecommendationsCreate(BaseModel):
    proc_recommendation_id: uuid.UUID
    proc_scenario_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: uuid.UUID
    quantity: float
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    delivery_date: Optional[date] = None
    incoterm: Optional[str] = None
    score: Optional[float] = None
    rank: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementRecommendationsUpdate(BaseModel):
    proc_recommendation_id: Optional[uuid.UUID] = None
    proc_scenario_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    delivery_date: Optional[date] = None
    incoterm: Optional[str] = None
    score: Optional[float] = None
    rank: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementRecommendationsOut(BaseModel):
    proc_recommendation_id: uuid.UUID
    proc_scenario_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: uuid.UUID
    quantity: float
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    delivery_date: Optional[date] = None
    incoterm: Optional[str] = None
    score: Optional[float] = None
    rank: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementSavingsCreate(BaseModel):
    savings_id: uuid.UUID
    recommendation_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    savings_type: str
    estimated_savings: Optional[float] = None
    actual_savings: Optional[float] = None
    currency_code: Optional[str] = None
    realized_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementSavingsUpdate(BaseModel):
    savings_id: Optional[uuid.UUID] = None
    recommendation_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    savings_type: Optional[str] = None
    estimated_savings: Optional[float] = None
    actual_savings: Optional[float] = None
    currency_code: Optional[str] = None
    realized_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementSavingsOut(BaseModel):
    savings_id: uuid.UUID
    recommendation_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    savings_type: str
    estimated_savings: Optional[float] = None
    actual_savings: Optional[float] = None
    currency_code: Optional[str] = None
    realized_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementScenariosCreate(BaseModel):
    proc_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    total_demand: Optional[float] = None
    objective_type: str
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementScenariosUpdate(BaseModel):
    proc_scenario_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    total_demand: Optional[float] = None
    objective_type: Optional[str] = None
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementScenariosOut(BaseModel):
    proc_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    total_demand: Optional[float] = None
    objective_type: str
    status: Optional[str] = None
    total_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementStrategiesCreate(BaseModel):
    strategy_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    strategy_type: str
    sourcing_type: str
    supplier_count: Optional[int] = None
    risk_tolerance: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementStrategiesUpdate(BaseModel):
    strategy_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    strategy_type: Optional[str] = None
    sourcing_type: Optional[str] = None
    supplier_count: Optional[int] = None
    risk_tolerance: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementStrategiesOut(BaseModel):
    strategy_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    strategy_type: str
    sourcing_type: str
    supplier_count: Optional[int] = None
    risk_tolerance: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmProcurementTcoCreate(BaseModel):
    tco_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    unit_price: Optional[float] = None
    logistics_cost: Optional[float] = None
    quality_cost: Optional[float] = None
    risk_cost: Optional[float] = None
    inventory_cost: Optional[float] = None
    total_cost: Optional[float] = None
    calculation_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementTcoUpdate(BaseModel):
    tco_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    unit_price: Optional[float] = None
    logistics_cost: Optional[float] = None
    quality_cost: Optional[float] = None
    risk_cost: Optional[float] = None
    inventory_cost: Optional[float] = None
    total_cost: Optional[float] = None
    calculation_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmProcurementTcoOut(BaseModel):
    tco_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    unit_price: Optional[float] = None
    logistics_cost: Optional[float] = None
    quality_cost: Optional[float] = None
    risk_cost: Optional[float] = None
    inventory_cost: Optional[float] = None
    total_cost: Optional[float] = None
    calculation_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmPromotionCalendarsCreate(BaseModel):
    promotion_id: uuid.UUID
    promotion_code: str
    promotion_name: str
    start_date: date
    end_date: date
    discount_pct: Optional[float] = None
    promotion_type: Optional[str] = None
    expected_lift_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPromotionCalendarsUpdate(BaseModel):
    promotion_id: Optional[uuid.UUID] = None
    promotion_code: Optional[str] = None
    promotion_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    discount_pct: Optional[float] = None
    promotion_type: Optional[str] = None
    expected_lift_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmPromotionCalendarsOut(BaseModel):
    promotion_id: uuid.UUID
    promotion_code: str
    promotion_name: str
    start_date: date
    end_date: date
    discount_pct: Optional[float] = None
    promotion_type: Optional[str] = None
    expected_lift_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmRoutingDistanceMatrixCreate(BaseModel):
    distance_id: uuid.UUID
    from_location_id: uuid.UUID
    to_location_id: uuid.UUID
    distance_km: Optional[float] = None
    duration_minutes: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingDistanceMatrixUpdate(BaseModel):
    distance_id: Optional[uuid.UUID] = None
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    distance_km: Optional[float] = None
    duration_minutes: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingDistanceMatrixOut(BaseModel):
    distance_id: uuid.UUID
    from_location_id: uuid.UUID
    to_location_id: uuid.UUID
    distance_km: Optional[float] = None
    duration_minutes: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmRoutingLocationsCreate(BaseModel):
    routing_location_id: uuid.UUID
    location_code: str
    location_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    address_text: Optional[str] = None
    time_window_earliest: Optional[datetime] = None
    time_window_latest: Optional[datetime] = None
    service_time_minutes: Optional[int] = None
    demand_qty: Optional[float] = None
    demand_weight_kg: Optional[float] = None
    demand_volume_cbm: Optional[float] = None
    priority: Optional[int] = None
    is_depot: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingLocationsUpdate(BaseModel):
    routing_location_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    address_text: Optional[str] = None
    time_window_earliest: Optional[datetime] = None
    time_window_latest: Optional[datetime] = None
    service_time_minutes: Optional[int] = None
    demand_qty: Optional[float] = None
    demand_weight_kg: Optional[float] = None
    demand_volume_cbm: Optional[float] = None
    priority: Optional[int] = None
    is_depot: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingLocationsOut(BaseModel):
    routing_location_id: uuid.UUID
    location_code: str
    location_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    address_text: Optional[str] = None
    time_window_earliest: Optional[datetime] = None
    time_window_latest: Optional[datetime] = None
    service_time_minutes: Optional[int] = None
    demand_qty: Optional[float] = None
    demand_weight_kg: Optional[float] = None
    demand_volume_cbm: Optional[float] = None
    priority: Optional[int] = None
    is_depot: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmRoutingProblemsCreate(BaseModel):
    routing_problem_id: uuid.UUID
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    vehicle_count: Optional[int] = None
    location_count: Optional[int] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingProblemsUpdate(BaseModel):
    routing_problem_id: Optional[uuid.UUID] = None
    problem_name: Optional[str] = None
    problem_type: Optional[str] = None
    description: Optional[str] = None
    objective_type: Optional[str] = None
    algorithm: Optional[str] = None
    status: Optional[str] = None
    vehicle_count: Optional[int] = None
    location_count: Optional[int] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingProblemsOut(BaseModel):
    routing_problem_id: uuid.UUID
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    algorithm: Optional[str] = None
    status: Optional[str] = None
    vehicle_count: Optional[int] = None
    location_count: Optional[int] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmRoutingSolutionsCreate(BaseModel):
    routing_solution_id: uuid.UUID
    routing_problem_id: uuid.UUID
    vehicle_id: Optional[uuid.UUID] = None
    stop_sequence: dict
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    total_demand: Optional[float] = None
    capacity_utilization_pct: Optional[float] = None
    carbon_emissions_kg: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingSolutionsUpdate(BaseModel):
    routing_solution_id: Optional[uuid.UUID] = None
    routing_problem_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    stop_sequence: Optional[dict] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    total_demand: Optional[float] = None
    capacity_utilization_pct: Optional[float] = None
    carbon_emissions_kg: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingSolutionsOut(BaseModel):
    routing_solution_id: uuid.UUID
    routing_problem_id: uuid.UUID
    vehicle_id: Optional[uuid.UUID] = None
    stop_sequence: dict
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_cost: Optional[float] = None
    total_demand: Optional[float] = None
    capacity_utilization_pct: Optional[float] = None
    carbon_emissions_kg: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmRoutingVehiclesCreate(BaseModel):
    routing_vehicle_id: uuid.UUID
    vehicle_code: str
    vehicle_name: Optional[str] = None
    vehicle_type: Optional[str] = None
    capacity_weight_kg: Optional[float] = None
    capacity_volume_cbm: Optional[float] = None
    max_stops: Optional[int] = None
    start_location_id: Optional[uuid.UUID] = None
    end_location_id: Optional[uuid.UUID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    fixed_cost: Optional[float] = None
    cost_per_km: Optional[float] = None
    cost_per_hour: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingVehiclesUpdate(BaseModel):
    routing_vehicle_id: Optional[uuid.UUID] = None
    vehicle_code: Optional[str] = None
    vehicle_name: Optional[str] = None
    vehicle_type: Optional[str] = None
    capacity_weight_kg: Optional[float] = None
    capacity_volume_cbm: Optional[float] = None
    max_stops: Optional[int] = None
    start_location_id: Optional[uuid.UUID] = None
    end_location_id: Optional[uuid.UUID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    fixed_cost: Optional[float] = None
    cost_per_km: Optional[float] = None
    cost_per_hour: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmRoutingVehiclesOut(BaseModel):
    routing_vehicle_id: uuid.UUID
    vehicle_code: str
    vehicle_name: Optional[str] = None
    vehicle_type: Optional[str] = None
    capacity_weight_kg: Optional[float] = None
    capacity_volume_cbm: Optional[float] = None
    max_stops: Optional[int] = None
    start_location_id: Optional[uuid.UUID] = None
    end_location_id: Optional[uuid.UUID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    fixed_cost: Optional[float] = None
    cost_per_km: Optional[float] = None
    cost_per_hour: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScenarioComparisonsCreate(BaseModel):
    comparison_id: uuid.UUID
    baseline_scenario_id: uuid.UUID
    alternative_scenario_id: uuid.UUID
    comparison_data: Optional[dict] = None
    summary: Optional[str] = None
    recommended_scenario_id: Optional[uuid.UUID] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioComparisonsUpdate(BaseModel):
    comparison_id: Optional[uuid.UUID] = None
    baseline_scenario_id: Optional[uuid.UUID] = None
    alternative_scenario_id: Optional[uuid.UUID] = None
    comparison_data: Optional[dict] = None
    summary: Optional[str] = None
    recommended_scenario_id: Optional[uuid.UUID] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioComparisonsOut(BaseModel):
    comparison_id: uuid.UUID
    baseline_scenario_id: uuid.UUID
    alternative_scenario_id: uuid.UUID
    comparison_data: Optional[dict] = None
    summary: Optional[str] = None
    recommended_scenario_id: Optional[uuid.UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScenarioResultsCreate(BaseModel):
    scenario_result_id: uuid.UUID
    scenario_id: uuid.UUID
    result_key: str
    result_value: Optional[float] = None
    result_text: Optional[str] = None
    result_json: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioResultsUpdate(BaseModel):
    scenario_result_id: Optional[uuid.UUID] = None
    scenario_id: Optional[uuid.UUID] = None
    result_key: Optional[str] = None
    result_value: Optional[float] = None
    result_text: Optional[str] = None
    result_json: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioResultsOut(BaseModel):
    scenario_result_id: uuid.UUID
    scenario_id: uuid.UUID
    result_key: str
    result_value: Optional[float] = None
    result_text: Optional[str] = None
    result_json: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScenarioTemplatesCreate(BaseModel):
    template_id: uuid.UUID
    template_name: str
    description: Optional[str] = None
    template_data: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioTemplatesUpdate(BaseModel):
    template_id: Optional[uuid.UUID] = None
    template_name: Optional[str] = None
    description: Optional[str] = None
    template_data: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioTemplatesOut(BaseModel):
    template_id: uuid.UUID
    template_name: str
    description: Optional[str] = None
    template_data: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScenarioTypesCreate(BaseModel):
    scenario_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioTypesUpdate(BaseModel):
    scenario_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenarioTypesOut(BaseModel):
    scenario_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScenariosCreate(BaseModel):
    scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    scenario_type_id: Optional[uuid.UUID] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    probability: Optional[float] = None
    impact_assessment: Optional[dict] = None
    recommendations: Optional[dict] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    version: Optional[int] = None
    parent_scenario_id: Optional[uuid.UUID] = None
    template_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenariosUpdate(BaseModel):
    scenario_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    scenario_type_id: Optional[uuid.UUID] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    probability: Optional[float] = None
    impact_assessment: Optional[dict] = None
    recommendations: Optional[dict] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    version: Optional[int] = None
    parent_scenario_id: Optional[uuid.UUID] = None
    template_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScenariosOut(BaseModel):
    scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    scenario_type_id: Optional[uuid.UUID] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    probability: Optional[float] = None
    impact_assessment: Optional[dict] = None
    recommendations: Optional[dict] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    version: Optional[int] = None
    parent_scenario_id: Optional[uuid.UUID] = None
    template_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScipyProblemsCreate(BaseModel):
    scipy_problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    problem_definition: dict
    input_data: Optional[dict] = None
    method_type: Optional[str] = None
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyProblemsUpdate(BaseModel):
    scipy_problem_id: Optional[uuid.UUID] = None
    problem_code: Optional[str] = None
    problem_name: Optional[str] = None
    problem_type: Optional[str] = None
    problem_definition: Optional[dict] = None
    input_data: Optional[dict] = None
    method_type: Optional[str] = None
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyProblemsOut(BaseModel):
    scipy_problem_id: uuid.UUID
    problem_code: str
    problem_name: str
    problem_type: str
    problem_definition: dict
    input_data: Optional[dict] = None
    method_type: Optional[str] = None
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScipyResultsCreate(BaseModel):
    scipy_result_id: uuid.UUID
    scipy_problem_id: uuid.UUID
    result_label: Optional[str] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    execution_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    success: Optional[bool] = None
    status: Optional[str] = None
    message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyResultsUpdate(BaseModel):
    scipy_result_id: Optional[uuid.UUID] = None
    scipy_problem_id: Optional[uuid.UUID] = None
    result_label: Optional[str] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    execution_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    success: Optional[bool] = None
    status: Optional[str] = None
    message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyResultsOut(BaseModel):
    scipy_result_id: uuid.UUID
    scipy_problem_id: uuid.UUID
    result_label: Optional[str] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    execution_time_ms: Optional[int] = None
    iterations: Optional[int] = None
    success: Optional[bool] = None
    status: Optional[str] = None
    message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmScipyStatisticalTestsCreate(BaseModel):
    stat_test_id: uuid.UUID
    test_name: str
    test_type: str
    input_data: Optional[dict] = None
    test_statistic: Optional[float] = None
    p_value: Optional[float] = None
    result_summary: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyStatisticalTestsUpdate(BaseModel):
    stat_test_id: Optional[uuid.UUID] = None
    test_name: Optional[str] = None
    test_type: Optional[str] = None
    input_data: Optional[dict] = None
    test_statistic: Optional[float] = None
    p_value: Optional[float] = None
    result_summary: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmScipyStatisticalTestsOut(BaseModel):
    stat_test_id: uuid.UUID
    test_name: str
    test_type: str
    input_data: Optional[dict] = None
    test_statistic: Optional[float] = None
    p_value: Optional[float] = None
    result_summary: Optional[str] = None
    executed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSeasonalityIndicesCreate(BaseModel):
    seasonality_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_type: str
    period_code: str
    index_value: float
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSeasonalityIndicesUpdate(BaseModel):
    seasonality_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_type: Optional[str] = None
    period_code: Optional[str] = None
    index_value: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSeasonalityIndicesOut(BaseModel):
    seasonality_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_type: str
    period_code: str
    index_value: float
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSolverBenchmarksCreate(BaseModel):
    benchmark_id: uuid.UUID
    solver_type_id: uuid.UUID
    problem_type: str
    problem_size: str
    avg_solve_time_ms: Optional[int] = None
    avg_gap_pct: Optional[float] = None
    avg_iterations: Optional[int] = None
    memory_mb: Optional[int] = None
    test_date: date
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverBenchmarksUpdate(BaseModel):
    benchmark_id: Optional[uuid.UUID] = None
    solver_type_id: Optional[uuid.UUID] = None
    problem_type: Optional[str] = None
    problem_size: Optional[str] = None
    avg_solve_time_ms: Optional[int] = None
    avg_gap_pct: Optional[float] = None
    avg_iterations: Optional[int] = None
    memory_mb: Optional[int] = None
    test_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverBenchmarksOut(BaseModel):
    benchmark_id: uuid.UUID
    solver_type_id: uuid.UUID
    problem_type: str
    problem_size: str
    avg_solve_time_ms: Optional[int] = None
    avg_gap_pct: Optional[float] = None
    avg_iterations: Optional[int] = None
    memory_mb: Optional[int] = None
    test_date: date
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSolverInstancesCreate(BaseModel):
    solver_instance_id: uuid.UUID
    solver_type_id: uuid.UUID
    instance_name: str
    parameters: Optional[dict] = None
    license_key_enc: Optional[str] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverInstancesUpdate(BaseModel):
    solver_instance_id: Optional[uuid.UUID] = None
    solver_type_id: Optional[uuid.UUID] = None
    instance_name: Optional[str] = None
    parameters: Optional[dict] = None
    license_key_enc: Optional[str] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverInstancesOut(BaseModel):
    solver_instance_id: uuid.UUID
    solver_type_id: uuid.UUID
    instance_name: str
    parameters: Optional[dict] = None
    license_key_enc: Optional[str] = None
    version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSolverLogsCreate(BaseModel):
    solver_log_id: uuid.UUID
    solver_instance_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    log_level: str
    log_message: str
    log_timestamp: datetime
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverLogsUpdate(BaseModel):
    solver_log_id: Optional[uuid.UUID] = None
    solver_instance_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    log_level: Optional[str] = None
    log_message: Optional[str] = None
    log_timestamp: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverLogsOut(BaseModel):
    solver_log_id: uuid.UUID
    solver_instance_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    log_level: str
    log_message: str
    log_timestamp: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSolverParametersCreate(BaseModel):
    solver_param_id: uuid.UUID
    solver_type_id: uuid.UUID
    param_code: str
    param_name: str
    param_type: str
    default_value: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverParametersUpdate(BaseModel):
    solver_param_id: Optional[uuid.UUID] = None
    solver_type_id: Optional[uuid.UUID] = None
    param_code: Optional[str] = None
    param_name: Optional[str] = None
    param_type: Optional[str] = None
    default_value: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverParametersOut(BaseModel):
    solver_param_id: uuid.UUID
    solver_type_id: uuid.UUID
    param_code: str
    param_name: str
    param_type: str
    default_value: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSolverTypesCreate(BaseModel):
    solver_type_id: uuid.UUID
    solver_code: str
    solver_name: str
    solver_framework: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverTypesUpdate(BaseModel):
    solver_type_id: Optional[uuid.UUID] = None
    solver_code: Optional[str] = None
    solver_name: Optional[str] = None
    solver_framework: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSolverTypesOut(BaseModel):
    solver_type_id: uuid.UUID
    solver_code: str
    solver_name: str
    solver_framework: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopCyclesCreate(BaseModel):
    sop_cycle_id: uuid.UUID
    cycle_code: str
    cycle_name: str
    fiscal_year: int
    fiscal_period: int
    cycle_start: date
    cycle_end: date
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopCyclesUpdate(BaseModel):
    sop_cycle_id: Optional[uuid.UUID] = None
    cycle_code: Optional[str] = None
    cycle_name: Optional[str] = None
    fiscal_year: Optional[int] = None
    fiscal_period: Optional[int] = None
    cycle_start: Optional[date] = None
    cycle_end: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopCyclesOut(BaseModel):
    sop_cycle_id: uuid.UUID
    cycle_code: str
    cycle_name: str
    fiscal_year: int
    fiscal_period: int
    cycle_start: date
    cycle_end: date
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopDecisionsCreate(BaseModel):
    sop_decision_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    decision_type: str
    decision_description: str
    decision_data: Optional[dict] = None
    rationale: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopDecisionsUpdate(BaseModel):
    sop_decision_id: Optional[uuid.UUID] = None
    sop_scenario_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    decision_description: Optional[str] = None
    decision_data: Optional[dict] = None
    rationale: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopDecisionsOut(BaseModel):
    sop_decision_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    decision_type: str
    decision_description: str
    decision_data: Optional[dict] = None
    rationale: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopDemandPlansCreate(BaseModel):
    sop_demand_plan_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    forecast_qty: Optional[float] = None
    booked_qty: Optional[float] = None
    total_demand: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopDemandPlansUpdate(BaseModel):
    sop_demand_plan_id: Optional[uuid.UUID] = None
    sop_scenario_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    forecast_qty: Optional[float] = None
    booked_qty: Optional[float] = None
    total_demand: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopDemandPlansOut(BaseModel):
    sop_demand_plan_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    forecast_qty: Optional[float] = None
    booked_qty: Optional[float] = None
    total_demand: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopKpisCreate(BaseModel):
    sop_kpi_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    kpi_code: str
    kpi_value: Optional[float] = None
    kpi_target: Optional[float] = None
    kpi_variance: Optional[float] = None
    evaluation_date: date
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopKpisUpdate(BaseModel):
    sop_kpi_id: Optional[uuid.UUID] = None
    sop_scenario_id: Optional[uuid.UUID] = None
    kpi_code: Optional[str] = None
    kpi_value: Optional[float] = None
    kpi_target: Optional[float] = None
    kpi_variance: Optional[float] = None
    evaluation_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopKpisOut(BaseModel):
    sop_kpi_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    kpi_code: str
    kpi_value: Optional[float] = None
    kpi_target: Optional[float] = None
    kpi_variance: Optional[float] = None
    evaluation_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopReconciliationCreate(BaseModel):
    reconciliation_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    total_demand: Optional[float] = None
    total_supply: Optional[float] = None
    gap_qty: Optional[float] = None
    gap_pct: Optional[float] = None
    resolution: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopReconciliationUpdate(BaseModel):
    reconciliation_id: Optional[uuid.UUID] = None
    sop_scenario_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    total_demand: Optional[float] = None
    total_supply: Optional[float] = None
    gap_qty: Optional[float] = None
    gap_pct: Optional[float] = None
    resolution: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopReconciliationOut(BaseModel):
    reconciliation_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    total_demand: Optional[float] = None
    total_supply: Optional[float] = None
    gap_qty: Optional[float] = None
    gap_pct: Optional[float] = None
    resolution: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopScenariosCreate(BaseModel):
    sop_scenario_id: uuid.UUID
    sop_cycle_id: uuid.UUID
    scenario_name: str
    scenario_type: str
    description: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopScenariosUpdate(BaseModel):
    sop_scenario_id: Optional[uuid.UUID] = None
    sop_cycle_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    scenario_type: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopScenariosOut(BaseModel):
    sop_scenario_id: uuid.UUID
    sop_cycle_id: uuid.UUID
    scenario_name: str
    scenario_type: str
    description: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSopSupplyPlansCreate(BaseModel):
    sop_supply_plan_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    production_qty: Optional[float] = None
    procurement_qty: Optional[float] = None
    transfer_in_qty: Optional[float] = None
    total_supply: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopSupplyPlansUpdate(BaseModel):
    sop_supply_plan_id: Optional[uuid.UUID] = None
    sop_scenario_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    production_qty: Optional[float] = None
    procurement_qty: Optional[float] = None
    transfer_in_qty: Optional[float] = None
    total_supply: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSopSupplyPlansOut(BaseModel):
    sop_supply_plan_id: uuid.UUID
    sop_scenario_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    production_qty: Optional[float] = None
    procurement_qty: Optional[float] = None
    transfer_in_qty: Optional[float] = None
    total_supply: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierForecastsCreate(BaseModel):
    supplier_forecast_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    forecast_start: date
    forecast_end: date
    forecast_qty: float
    committed_qty: Optional[float] = None
    confirmation_status: Optional[str] = None
    confirmed_by: Optional[uuid.UUID] = None
    confirmed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierForecastsUpdate(BaseModel):
    supplier_forecast_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    forecast_start: Optional[date] = None
    forecast_end: Optional[date] = None
    forecast_qty: Optional[float] = None
    committed_qty: Optional[float] = None
    confirmation_status: Optional[str] = None
    confirmed_by: Optional[uuid.UUID] = None
    confirmed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierForecastsOut(BaseModel):
    supplier_forecast_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    forecast_start: date
    forecast_end: date
    forecast_qty: float
    committed_qty: Optional[float] = None
    confirmation_status: Optional[str] = None
    confirmed_by: Optional[uuid.UUID] = None
    confirmed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierPerformanceCreate(BaseModel):
    performance_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    metric_type: str
    metric_value: Optional[float] = None
    uom_code: Optional[str] = None
    measurement_date: date
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierPerformanceUpdate(BaseModel):
    performance_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    metric_type: Optional[str] = None
    metric_value: Optional[float] = None
    uom_code: Optional[str] = None
    measurement_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierPerformanceOut(BaseModel):
    performance_id: uuid.UUID
    partner_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    metric_type: str
    metric_value: Optional[float] = None
    uom_code: Optional[str] = None
    measurement_date: date
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierProfilesCreate(BaseModel):
    supplier_profile_id: uuid.UUID
    partner_id: uuid.UUID
    capabilities: Optional[str] = None
    certifications: Optional[dict] = None
    total_capacity: Optional[float] = None
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    lead_time_days: Optional[int] = None
    payment_terms: Optional[str] = None
    incoterm: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierProfilesUpdate(BaseModel):
    supplier_profile_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    capabilities: Optional[str] = None
    certifications: Optional[dict] = None
    total_capacity: Optional[float] = None
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    lead_time_days: Optional[int] = None
    payment_terms: Optional[str] = None
    incoterm: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierProfilesOut(BaseModel):
    supplier_profile_id: uuid.UUID
    partner_id: uuid.UUID
    capabilities: Optional[str] = None
    certifications: Optional[dict] = None
    total_capacity: Optional[float] = None
    min_order_qty: Optional[float] = None
    max_order_qty: Optional[float] = None
    lead_time_days: Optional[int] = None
    payment_terms: Optional[str] = None
    incoterm: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierRiskAssessmentsCreate(BaseModel):
    risk_assessment_id: uuid.UUID
    partner_id: uuid.UUID
    assessment_date: date
    financial_risk: Optional[float] = None
    operational_risk: Optional[float] = None
    geopolitical_risk: Optional[float] = None
    esg_risk: Optional[float] = None
    overall_risk: Optional[float] = None
    risk_level: Optional[str] = None
    mitigation_plan: Optional[str] = None
    assessor_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierRiskAssessmentsUpdate(BaseModel):
    risk_assessment_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    assessment_date: Optional[date] = None
    financial_risk: Optional[float] = None
    operational_risk: Optional[float] = None
    geopolitical_risk: Optional[float] = None
    esg_risk: Optional[float] = None
    overall_risk: Optional[float] = None
    risk_level: Optional[str] = None
    mitigation_plan: Optional[str] = None
    assessor_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierRiskAssessmentsOut(BaseModel):
    risk_assessment_id: uuid.UUID
    partner_id: uuid.UUID
    assessment_date: date
    financial_risk: Optional[float] = None
    operational_risk: Optional[float] = None
    geopolitical_risk: Optional[float] = None
    esg_risk: Optional[float] = None
    overall_risk: Optional[float] = None
    risk_level: Optional[str] = None
    mitigation_plan: Optional[str] = None
    assessor_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierScorecardsCreate(BaseModel):
    scorecard_id: uuid.UUID
    partner_id: uuid.UUID
    evaluation_date: date
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    innovation_score: Optional[float] = None
    sustainability_score: Optional[float] = None
    overall_score: Optional[float] = None
    rating: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierScorecardsUpdate(BaseModel):
    scorecard_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    innovation_score: Optional[float] = None
    sustainability_score: Optional[float] = None
    overall_score: Optional[float] = None
    rating: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierScorecardsOut(BaseModel):
    scorecard_id: uuid.UUID
    partner_id: uuid.UUID
    evaluation_date: date
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    innovation_score: Optional[float] = None
    sustainability_score: Optional[float] = None
    overall_score: Optional[float] = None
    rating: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplierSustainabilityCreate(BaseModel):
    sustainability_id: uuid.UUID
    partner_id: uuid.UUID
    carbon_footprint: Optional[float] = None
    water_usage: Optional[float] = None
    waste_generated: Optional[float] = None
    renewable_energy_pct: Optional[float] = None
    report_date: date
    cert_body: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierSustainabilityUpdate(BaseModel):
    sustainability_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    carbon_footprint: Optional[float] = None
    water_usage: Optional[float] = None
    waste_generated: Optional[float] = None
    renewable_energy_pct: Optional[float] = None
    report_date: Optional[date] = None
    cert_body: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplierSustainabilityOut(BaseModel):
    sustainability_id: uuid.UUID
    partner_id: uuid.UUID
    carbon_footprint: Optional[float] = None
    water_usage: Optional[float] = None
    waste_generated: Optional[float] = None
    renewable_energy_pct: Optional[float] = None
    report_date: date
    cert_body: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyCalendarDatesCreate(BaseModel):
    calendar_date_id: uuid.UUID
    supply_calendar_id: uuid.UUID
    calendar_date: date
    is_working_day: Optional[bool] = None
    capacity_pct: Optional[float] = None
    shift_count: Optional[int] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyCalendarDatesUpdate(BaseModel):
    calendar_date_id: Optional[uuid.UUID] = None
    supply_calendar_id: Optional[uuid.UUID] = None
    calendar_date: Optional[date] = None
    is_working_day: Optional[bool] = None
    capacity_pct: Optional[float] = None
    shift_count: Optional[int] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyCalendarDatesOut(BaseModel):
    calendar_date_id: uuid.UUID
    supply_calendar_id: uuid.UUID
    calendar_date: date
    is_working_day: Optional[bool] = None
    capacity_pct: Optional[float] = None
    shift_count: Optional[int] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyCalendarsCreate(BaseModel):
    supply_calendar_id: uuid.UUID
    calendar_code: str
    calendar_name: str
    calendar_type: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyCalendarsUpdate(BaseModel):
    supply_calendar_id: Optional[uuid.UUID] = None
    calendar_code: Optional[str] = None
    calendar_name: Optional[str] = None
    calendar_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyCalendarsOut(BaseModel):
    supply_calendar_id: uuid.UUID
    calendar_code: str
    calendar_name: str
    calendar_type: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyConstraintsCreate(BaseModel):
    supply_constraint_id: uuid.UUID
    constraint_code: str
    constraint_name: str
    constraint_type: str
    constraint_value: Optional[float] = None
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyConstraintsUpdate(BaseModel):
    supply_constraint_id: Optional[uuid.UUID] = None
    constraint_code: Optional[str] = None
    constraint_name: Optional[str] = None
    constraint_type: Optional[str] = None
    constraint_value: Optional[float] = None
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyConstraintsOut(BaseModel):
    supply_constraint_id: uuid.UUID
    constraint_code: str
    constraint_name: str
    constraint_type: str
    constraint_value: Optional[float] = None
    uom_code: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyLeadTimesCreate(BaseModel):
    lead_time_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    lead_time_days: int
    lead_time_variance: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyLeadTimesUpdate(BaseModel):
    lead_time_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    lead_time_variance: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyLeadTimesOut(BaseModel):
    lead_time_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    lead_time_days: int
    lead_time_variance: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyPlanLinesCreate(BaseModel):
    supply_plan_line_id: uuid.UUID
    supply_plan_id: uuid.UUID
    line_num: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    source_type: str
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    quantity: float
    uom_code: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyPlanLinesUpdate(BaseModel):
    supply_plan_line_id: Optional[uuid.UUID] = None
    supply_plan_id: Optional[uuid.UUID] = None
    line_num: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    source_type: Optional[str] = None
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyPlanLinesOut(BaseModel):
    supply_plan_line_id: uuid.UUID
    supply_plan_id: uuid.UUID
    line_num: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    source_type: str
    source_location_id: Optional[uuid.UUID] = None
    destination_location_id: Optional[uuid.UUID] = None
    quantity: float
    uom_code: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyPlansCreate(BaseModel):
    supply_plan_id: uuid.UUID
    plan_name: str
    description: Optional[str] = None
    plan_type: str
    demand_forecast_source: Optional[uuid.UUID] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyPlansUpdate(BaseModel):
    supply_plan_id: Optional[uuid.UUID] = None
    plan_name: Optional[str] = None
    description: Optional[str] = None
    plan_type: Optional[str] = None
    demand_forecast_source: Optional[uuid.UUID] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyPlansOut(BaseModel):
    supply_plan_id: uuid.UUID
    plan_name: str
    description: Optional[str] = None
    plan_type: str
    demand_forecast_source: Optional[uuid.UUID] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    objective_value: Optional[float] = None
    total_cost: Optional[float] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplyRisksCreate(BaseModel):
    supply_risk_id: uuid.UUID
    supplier_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    risk_type: str
    risk_level: str
    risk_score: Optional[float] = None
    risk_description: Optional[str] = None
    mitigation_plan: Optional[str] = None
    identified_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyRisksUpdate(BaseModel):
    supply_risk_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    risk_type: Optional[str] = None
    risk_level: Optional[str] = None
    risk_score: Optional[float] = None
    risk_description: Optional[str] = None
    mitigation_plan: Optional[str] = None
    identified_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplyRisksOut(BaseModel):
    supply_risk_id: uuid.UUID
    supplier_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    risk_type: str
    risk_level: str
    risk_score: Optional[float] = None
    risk_description: Optional[str] = None
    mitigation_plan: Optional[str] = None
    identified_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmSupplySourcesCreate(BaseModel):
    supply_source_id: uuid.UUID
    source_code: str
    source_name: str
    source_type: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplySourcesUpdate(BaseModel):
    supply_source_id: Optional[uuid.UUID] = None
    source_code: Optional[str] = None
    source_name: Optional[str] = None
    source_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmSupplySourcesOut(BaseModel):
    supply_source_id: uuid.UUID
    source_code: str
    source_name: str
    source_type: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationConstraintsCreate(BaseModel):
    trans_constraint_id: uuid.UUID
    constraint_type: str
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    max_length: Optional[float] = None
    max_width: Optional[float] = None
    max_height: Optional[float] = None
    hazmat_allowed: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationConstraintsUpdate(BaseModel):
    trans_constraint_id: Optional[uuid.UUID] = None
    constraint_type: Optional[str] = None
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    max_length: Optional[float] = None
    max_width: Optional[float] = None
    max_height: Optional[float] = None
    hazmat_allowed: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationConstraintsOut(BaseModel):
    trans_constraint_id: uuid.UUID
    constraint_type: str
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    max_length: Optional[float] = None
    max_width: Optional[float] = None
    max_height: Optional[float] = None
    hazmat_allowed: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationCostsCreate(BaseModel):
    trans_cost_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    rate_type: str
    rate_value: Optional[float] = None
    currency_code: Optional[str] = None
    fuel_surcharge_pct: Optional[float] = None
    accessorial_charges: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationCostsUpdate(BaseModel):
    trans_cost_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    rate_type: Optional[str] = None
    rate_value: Optional[float] = None
    currency_code: Optional[str] = None
    fuel_surcharge_pct: Optional[float] = None
    accessorial_charges: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationCostsOut(BaseModel):
    trans_cost_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    rate_type: str
    rate_value: Optional[float] = None
    currency_code: Optional[str] = None
    fuel_surcharge_pct: Optional[float] = None
    accessorial_charges: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationModesCreate(BaseModel):
    mode_id: uuid.UUID
    mode_code: str
    mode_name: str
    description: Optional[str] = None
    carbon_factor: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationModesUpdate(BaseModel):
    mode_id: Optional[uuid.UUID] = None
    mode_code: Optional[str] = None
    mode_name: Optional[str] = None
    description: Optional[str] = None
    carbon_factor: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationModesOut(BaseModel):
    mode_id: uuid.UUID
    mode_code: str
    mode_name: str
    description: Optional[str] = None
    carbon_factor: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationRecommendationsCreate(BaseModel):
    trans_recommendation_id: uuid.UUID
    trans_scenario_id: uuid.UUID
    recommendation_type: str
    description: Optional[str] = None
    estimated_savings: Optional[float] = None
    priority: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationRecommendationsUpdate(BaseModel):
    trans_recommendation_id: Optional[uuid.UUID] = None
    trans_scenario_id: Optional[uuid.UUID] = None
    recommendation_type: Optional[str] = None
    description: Optional[str] = None
    estimated_savings: Optional[float] = None
    priority: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationRecommendationsOut(BaseModel):
    trans_recommendation_id: uuid.UUID
    trans_scenario_id: uuid.UUID
    recommendation_type: str
    description: Optional[str] = None
    estimated_savings: Optional[float] = None
    priority: Optional[int] = None
    justification: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationScenariosCreate(BaseModel):
    trans_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    objective_type: str
    status: Optional[str] = None
    total_cost: Optional[float] = None
    total_distance_km: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationScenariosUpdate(BaseModel):
    trans_scenario_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    objective_type: Optional[str] = None
    status: Optional[str] = None
    total_cost: Optional[float] = None
    total_distance_km: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationScenariosOut(BaseModel):
    trans_scenario_id: uuid.UUID
    scenario_name: str
    description: Optional[str] = None
    objective_type: str
    status: Optional[str] = None
    total_cost: Optional[float] = None
    total_distance_km: Optional[float] = None
    carbon_footprint: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmTransportationServiceLevelsCreate(BaseModel):
    trans_service_level_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    transit_time_hours: Optional[int] = None
    on_time_pct: Optional[float] = None
    loss_damage_pct: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationServiceLevelsUpdate(BaseModel):
    trans_service_level_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    transit_time_hours: Optional[int] = None
    on_time_pct: Optional[float] = None
    loss_damage_pct: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmTransportationServiceLevelsOut(BaseModel):
    trans_service_level_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    mode_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    transit_time_hours: Optional[int] = None
    on_time_pct: Optional[float] = None
    loss_damage_pct: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehouseAislesCreate(BaseModel):
    aisle_id: uuid.UUID
    zone_id: uuid.UUID
    aisle_code: str
    direction: Optional[str] = None
    length_m: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseAislesUpdate(BaseModel):
    aisle_id: Optional[uuid.UUID] = None
    zone_id: Optional[uuid.UUID] = None
    aisle_code: Optional[str] = None
    direction: Optional[str] = None
    length_m: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseAislesOut(BaseModel):
    aisle_id: uuid.UUID
    zone_id: uuid.UUID
    aisle_code: str
    direction: Optional[str] = None
    length_m: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehouseLocationsCreate(BaseModel):
    wh_location_id: uuid.UUID
    warehouse_id: uuid.UUID
    aisle_id: Optional[uuid.UUID] = None
    location_code: str
    location_type: str
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    z_coordinate: Optional[float] = None
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseLocationsUpdate(BaseModel):
    wh_location_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    aisle_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_type: Optional[str] = None
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    z_coordinate: Optional[float] = None
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseLocationsOut(BaseModel):
    wh_location_id: uuid.UUID
    warehouse_id: uuid.UUID
    aisle_id: Optional[uuid.UUID] = None
    location_code: str
    location_type: str
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    z_coordinate: Optional[float] = None
    max_weight: Optional[float] = None
    max_volume: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehousePickBatchesCreate(BaseModel):
    batch_id: uuid.UUID
    batch_code: str
    batch_type: str
    warehouse_id: uuid.UUID
    order_count: Optional[int] = None
    total_items: Optional[int] = None
    status: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickBatchesUpdate(BaseModel):
    batch_id: Optional[uuid.UUID] = None
    batch_code: Optional[str] = None
    batch_type: Optional[str] = None
    warehouse_id: Optional[uuid.UUID] = None
    order_count: Optional[int] = None
    total_items: Optional[int] = None
    status: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickBatchesOut(BaseModel):
    batch_id: uuid.UUID
    batch_code: str
    batch_type: str
    warehouse_id: uuid.UUID
    order_count: Optional[int] = None
    total_items: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehousePickLinesCreate(BaseModel):
    pick_line_id: uuid.UUID
    pick_order_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    quantity: float
    picked_qty: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_num: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickLinesUpdate(BaseModel):
    pick_line_id: Optional[uuid.UUID] = None
    pick_order_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    picked_qty: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_num: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickLinesOut(BaseModel):
    pick_line_id: uuid.UUID
    pick_order_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    quantity: float
    picked_qty: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_num: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehousePickOrdersCreate(BaseModel):
    pick_order_id: uuid.UUID
    order_id: Optional[uuid.UUID] = None
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    scheduled_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickOrdersUpdate(BaseModel):
    pick_order_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    scheduled_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehousePickOrdersOut(BaseModel):
    pick_order_id: uuid.UUID
    order_id: Optional[uuid.UUID] = None
    wave_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    scheduled_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehouseWavesCreate(BaseModel):
    wave_id: uuid.UUID
    wave_code: str
    wave_type: str
    warehouse_id: uuid.UUID
    scheduled_time: Optional[datetime] = None
    cutoff_time: Optional[datetime] = None
    order_count: Optional[int] = None
    status: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseWavesUpdate(BaseModel):
    wave_id: Optional[uuid.UUID] = None
    wave_code: Optional[str] = None
    wave_type: Optional[str] = None
    warehouse_id: Optional[uuid.UUID] = None
    scheduled_time: Optional[datetime] = None
    cutoff_time: Optional[datetime] = None
    order_count: Optional[int] = None
    status: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseWavesOut(BaseModel):
    wave_id: uuid.UUID
    wave_code: str
    wave_type: str
    warehouse_id: uuid.UUID
    scheduled_time: Optional[datetime] = None
    cutoff_time: Optional[datetime] = None
    order_count: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ScmWarehouseZonesCreate(BaseModel):
    zone_id: uuid.UUID
    warehouse_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: str
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseZonesUpdate(BaseModel):
    zone_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    zone_code: Optional[str] = None
    zone_name: Optional[str] = None
    zone_type: Optional[str] = None
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ScmWarehouseZonesOut(BaseModel):
    zone_id: uuid.UUID
    warehouse_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: str
    x_coordinate: Optional[float] = None
    y_coordinate: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}
