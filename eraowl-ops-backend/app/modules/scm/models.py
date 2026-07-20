import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Float, Integer,
    SmallInteger, String, Text, Time, Interval, LargeBinary,
    Numeric, ARRAY, func,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB, JSON
from sqlalchemy import ForeignKey
from sqlmodel import Field, SQLModel


class AgentProposals(SQLModel, table=True):
    __tablename__ = "agent_proposals"
    __table_args__ = {"schema": "scm"}

    proposal_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    conflict_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.conflicts.conflict_id"), nullable=True))

    agent_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    agent_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    proposal: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    utility_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    confidence: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class BusinessWeights(SQLModel, table=True):
    __tablename__ = "business_weights"
    __table_args__ = {"schema": "scm"}

    weight_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    config_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    cost_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    service_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    quality_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    speed_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    sustainability_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class Conflicts(SQLModel, table=True):
    __tablename__ = "conflicts"
    __table_args__ = {"schema": "scm"}

    conflict_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    conflict_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    affected_items: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    resolution: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ControlTowerActivities(SQLModel, table=True):
    __tablename__ = "control_tower_activities"
    __table_args__ = {"schema": "scm"}

    activity_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    activity_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    source: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ControlTowerAlerts(SQLModel, table=True):
    __tablename__ = "control_tower_alerts"
    __table_args__ = {"schema": "scm"}

    alert_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    severity: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    source: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    acknowledged: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class DemandForecasts(SQLModel, table=True):
    __tablename__ = "demand_forecasts"
    __table_args__ = {"schema": "scm"}

    forecast_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    forecast_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    forecasted_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class DisruptionScenarios(SQLModel, table=True):
    __tablename__ = "disruption_scenarios"
    __table_args__ = {"schema": "scm"}

    scenario_id: str = Field(sa_column=Column(String(50), primary_key=True))

    name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    disruption_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    parameters: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    expected_impact: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    test_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class EscalationTickets(SQLModel, table=True):
    __tablename__ = "escalation_tickets"
    __table_args__ = {"schema": "scm"}

    ticket_id: str = Field(sa_column=Column(String(50), primary_key=True))

    level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    issue_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    urgency: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    impact: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    strategic_alignment: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    deadline: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    resolution: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ExperienceLedger(SQLModel, table=True):
    __tablename__ = "experience_ledger"
    __table_args__ = {"schema": "scm"}

    entry_id: str = Field(sa_column=Column(String(50), primary_key=True))

    category: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    context: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    decision: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    outcome: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    confidence: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    learned_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    expires_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    access_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_accessed: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ExperienceLedgerCold(SQLModel, table=True):
    __tablename__ = "experience_ledger_cold"
    __table_args__ = {"schema": "scm"}

    entry_id: str = Field(sa_column=Column(String(50), primary_key=True))

    category: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    context: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    decision: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    outcome: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    confidence: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    learned_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    expires_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    access_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_accessed: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    archived_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class LotSizePolicies(SQLModel, table=True):
    __tablename__ = "lot_size_policies"
    __table_args__ = {"schema": "scm"}

    policy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    policy_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    min_order_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_order_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    fixed_order_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reorder_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reorder_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carrying_cost_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    ordering_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpActionMessages(SQLModel, table=True):
    __tablename__ = "mrp_action_messages"
    __table_args__ = {"schema": "scm"}

    action_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mrp_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    exception_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_exceptions.exception_id"), nullable=True))

    action_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    current_value: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    suggested_value: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    executed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpDemandRecords(SQLModel, table=True):
    __tablename__ = "mrp_demand_records"
    __table_args__ = {"schema": "scm"}

    demand_record_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mrp_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    period: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    gross_quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bom_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    bom_path: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    pegging_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpExceptions(SQLModel, table=True):
    __tablename__ = "mrp_exceptions"
    __table_args__ = {"schema": "scm"}

    exception_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mrp_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    exception_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    severity: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    suggested_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    period: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    quantity_impact: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_impact: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpPegging(SQLModel, table=True):
    __tablename__ = "mrp_pegging"
    __table_args__ = {"schema": "scm"}

    pegging_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mrp_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    demand_record_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_demand_records.demand_record_id"), nullable=True))

    supply_record_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_supply_records.supply_record_id"), nullable=True))

    peg_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    quantity_pegged: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    bom_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpPlans(SQLModel, table=True):
    __tablename__ = "mrp_plans"
    __table_args__ = {"schema": "scm"}

    mrp_plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    plan_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    planning_horizon_days: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    bucket_size: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    planning_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    frozen_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MrpSupplyRecords(SQLModel, table=True):
    __tablename__ = "mrp_supply_records"
    __table_args__ = {"schema": "scm"}

    supply_record_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mrp_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    period: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    release_period: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    order_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    pegging_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class PlanScenarios(SQLModel, table=True):
    __tablename__ = "plan_scenarios"
    __table_args__ = {"schema": "scm"}

    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    base_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    scenario_plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("scm.mrp_plans.mrp_plan_id"), nullable=True))

    scenario_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    comparison_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class PlanningTimeFences(SQLModel, table=True):
    __tablename__ = "planning_time_fences"
    __table_args__ = {"schema": "scm"}

    fence_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    organization_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    demand_time_fence_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    planning_time_fence_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    demand_fence_action: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    planning_fence_action: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ReplenishmentPlans(SQLModel, table=True):
    __tablename__ = "replenishment_plans"
    __table_args__ = {"schema": "scm"}

    plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    target_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    recommended_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    source_type: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    status: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiAgentExecutionLogs(SQLModel, table=True):
    __tablename__ = "scm_ai_agent_execution_logs"
    __table_args__ = {"schema": "scm"}

    ai_agent_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    agent_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    action: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    token_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_usd: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiCostTracking(SQLModel, table=True):
    __tablename__ = "scm_ai_cost_tracking"
    __table_args__ = {"schema": "scm"}

    cost_tracking_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    model_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    provider: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    token_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    input_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    output_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_per_token: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 10), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    cost_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiDecisions(SQLModel, table=True):
    __tablename__ = "scm_ai_decisions"
    __table_args__ = {"schema": "scm"}

    ai_decision_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    decision_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    decision_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    accepted: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    accepted_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    accepted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiExperimentTracking(SQLModel, table=True):
    __tablename__ = "scm_ai_experiment_tracking"
    __table_args__ = {"schema": "scm"}

    experiment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    experiment_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    ml_model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    hyperparameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    artifacts: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    run_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiFeatureStore(SQLModel, table=True):
    __tablename__ = "scm_ai_feature_store"
    __table_args__ = {"schema": "scm"}

    feature_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    feature_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    feature_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    feature_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiModelRegistry(SQLModel, table=True):
    __tablename__ = "scm_ai_model_registry"
    __table_args__ = {"schema": "scm"}

    model_registry_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    deployment_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAiWorkflowState(SQLModel, table=True):
    __tablename__ = "scm_ai_workflow_state"
    __table_args__ = {"schema": "scm"}

    ai_state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    state_key: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    state_value: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    thread_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    checkpoint: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlertEscalations(SQLModel, table=True):
    __tablename__ = "scm_alert_escalations"
    __table_args__ = {"schema": "scm"}

    escalation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    alert_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    escalated_to: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    escalation_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    escalated_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlertNotifications(SQLModel, table=True):
    __tablename__ = "scm_alert_notifications"
    __table_args__ = {"schema": "scm"}

    notification_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    alert_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    channel: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    recipient: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    sent_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlertRules(SQLModel, table=True):
    __tablename__ = "scm_alert_rules"
    __table_args__ = {"schema": "scm"}

    alert_rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    alert_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    condition_config: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    severity: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    escalation_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlertTypes(SQLModel, table=True):
    __tablename__ = "scm_alert_types"
    __table_args__ = {"schema": "scm"}

    alert_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    default_severity: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlerts(SQLModel, table=True):
    __tablename__ = "scm_alerts"
    __table_args__ = {"schema": "scm"}

    alert_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    alert_rule_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    alert_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    severity: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    title: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    alert_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    escalated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlgorithmTests(SQLModel, table=True):
    __tablename__ = "scm_algorithm_tests"
    __table_args__ = {"schema": "scm"}

    algo_test_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    algo_version_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    test_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    test_input: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    expected_output: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    actual_output: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    passed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tested_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tested_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlgorithmVersions(SQLModel, table=True):
    __tablename__ = "scm_algorithm_versions"
    __table_args__ = {"schema": "scm"}

    algo_version_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    algorithm_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    version_label: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    release_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    validated_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    validated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmAlgorithms(SQLModel, table=True):
    __tablename__ = "scm_algorithms"
    __table_args__ = {"schema": "scm"}

    algorithm_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    algorithm_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    algorithm_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    algorithm_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    inputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    outputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    default_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    performance_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    code_repository_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    documentation_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmBinPackingItems(SQLModel, table=True):
    __tablename__ = "scm_bin_packing_items"
    __table_args__ = {"schema": "scm"}

    packing_item_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    length_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    width_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    height_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    weight_kg: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    allow_rotate: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_fragile: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    stackable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hazmat_class: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmBinPackingMetrics(SQLModel, table=True):
    __tablename__ = "scm_bin_packing_metrics"
    __table_args__ = {"schema": "scm"}

    packing_metric_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    packing_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    bin_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    volume_utilization_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    weight_utilization_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    wasted_volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    center_of_gravity_x: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    center_of_gravity_y: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    center_of_gravity_z: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    stability_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmBinPackingProblems(SQLModel, table=True):
    __tablename__ = "scm_bin_packing_problems"
    __table_args__ = {"schema": "scm"}

    packing_problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    bin_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bin_count_available: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    algorithm: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    total_items: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    bins_used: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    utilization_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmBinPackingResults(SQLModel, table=True):
    __tablename__ = "scm_bin_packing_results"
    __table_args__ = {"schema": "scm"}

    packing_result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    packing_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    bin_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    bin_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    position_x: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    position_y: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    position_z: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    orientation: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    sequence_num: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmBinTypes(SQLModel, table=True):
    __tablename__ = "scm_bin_types"
    __table_args__ = {"schema": "scm"}

    bin_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    bin_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    bin_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    length_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    width_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    height_mm: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    max_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tare_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDemandClasses(SQLModel, table=True):
    __tablename__ = "scm_demand_classes"
    __table_args__ = {"schema": "scm"}

    demand_class_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    class_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    class_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDemandDrivers(SQLModel, table=True):
    __tablename__ = "scm_demand_drivers"
    __table_args__ = {"schema": "scm"}

    demand_driver_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    driver_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    driver_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    data_source: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDemandSources(SQLModel, table=True):
    __tablename__ = "scm_demand_sources"
    __table_args__ = {"schema": "scm"}

    demand_source_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDemandTimeSeries(SQLModel, table=True):
    __tablename__ = "scm_demand_time_series"
    __table_args__ = {"schema": "scm"}

    time_series_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    demand_class_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bucket_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    bucket_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    bucket_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    source_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_actual: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionAllocationRules(SQLModel, table=True):
    __tablename__ = "scm_distribution_allocation_rules"
    __table_args__ = {"schema": "scm"}

    allocation_rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    rule_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rule_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionCostToServe(SQLModel, table=True):
    __tablename__ = "scm_distribution_cost_to_serve"
    __table_args__ = {"schema": "scm"}

    cost_to_serve_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    cost_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    cost_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionNetwork(SQLModel, table=True):
    __tablename__ = "scm_distribution_network"
    __table_args__ = {"schema": "scm"}

    dist_network_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    node_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    node_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    node_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionPlanLines(SQLModel, table=True):
    __tablename__ = "scm_distribution_plan_lines"
    __table_args__ = {"schema": "scm"}

    dist_plan_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    dist_plan_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    from_node_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    to_node_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    planned_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionPlans(SQLModel, table=True):
    __tablename__ = "scm_distribution_plans"
    __table_args__ = {"schema": "scm"}

    dist_plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    plan_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmDistributionServiceLevels(SQLModel, table=True):
    __tablename__ = "scm_distribution_service_levels"
    __table_args__ = {"schema": "scm"}

    service_level_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    target_service_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    target_fill_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    target_otif: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmForecastAccuracy(SQLModel, table=True):
    __tablename__ = "scm_forecast_accuracy"
    __table_args__ = {"schema": "scm"}

    accuracy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    forecast_version_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    mape: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    mae: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rmse: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    bias: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    sample_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmForecastModels(SQLModel, table=True):
    __tablename__ = "scm_forecast_models"
    __table_args__ = {"schema": "scm"}

    forecast_model_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    model_framework: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmForecastValues(SQLModel, table=True):
    __tablename__ = "scm_forecast_values"
    __table_args__ = {"schema": "scm"}

    forecast_value_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    forecast_version_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bucket_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    bucket_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    point_forecast: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    lower_bound: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    upper_bound: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    confidence_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    actual_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    forecast_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    mape: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_overridden: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    override_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    override_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    override_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmForecastVersions(SQLModel, table=True):
    __tablename__ = "scm_forecast_versions"
    __table_args__ = {"schema": "scm"}

    forecast_version_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    version_label: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    forecast_model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    forecast_horizon_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    bucket_type: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmIntegrationConnections(SQLModel, table=True):
    __tablename__ = "scm_integration_connections"
    __table_args__ = {"schema": "scm"}

    connection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    connection_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    connection_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    auth_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmIntegrationLogs(SQLModel, table=True):
    __tablename__ = "scm_integration_logs"
    __table_args__ = {"schema": "scm"}

    integration_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    direction: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    payload: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    response: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    logged_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmIntegrationMappings(SQLModel, table=True):
    __tablename__ = "scm_integration_mappings"
    __table_args__ = {"schema": "scm"}

    mapping_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    mapping_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_field: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    target_field: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    transformation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryAging(SQLModel, table=True):
    __tablename__ = "scm_inventory_aging"
    __table_args__ = {"schema": "scm"}

    aging_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    batch_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    receipt_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    age_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryClassifications(SQLModel, table=True):
    __tablename__ = "scm_inventory_classifications"
    __table_args__ = {"schema": "scm"}

    classification_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    abc_class: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    xyz_class: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    fsn_class: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    ved_class: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    classification_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryHealth(SQLModel, table=True):
    __tablename__ = "scm_inventory_health"
    __table_args__ = {"schema": "scm"}

    health_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    inventory_turns: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    days_of_supply: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    excess_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    obsolescence_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    stockout_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    fill_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryOptimizationParams(SQLModel, table=True):
    __tablename__ = "scm_inventory_optimization_params"
    __table_args__ = {"schema": "scm"}

    param_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    holding_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    ordering_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    shortage_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_service_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    demand_variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lead_time_variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    review_period_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryPolicies(SQLModel, table=True):
    __tablename__ = "scm_inventory_policies"
    __table_args__ = {"schema": "scm"}

    inventory_policy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    policy_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    policy_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    policy_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    min_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reorder_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reorder_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    safety_stock: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_service_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    holding_cost_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    ordering_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    shortage_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryRecommendations(SQLModel, table=True):
    __tablename__ = "scm_inventory_recommendations"
    __table_args__ = {"schema": "scm"}

    recommendation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rec_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    from_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    to_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    reason_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    justification: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmInventoryTargets(SQLModel, table=True):
    __tablename__ = "scm_inventory_targets"
    __table_args__ = {"schema": "scm"}

    inventory_target_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    target_qty: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    min_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_dos: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmKpiAlerts(SQLModel, table=True):
    __tablename__ = "scm_kpi_alerts"
    __table_args__ = {"schema": "scm"}

    kpi_alert_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    kpi_value_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    alert_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    threshold_breached: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    threshold_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    alerted_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    acknowledged_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmKpiBenchmarks(SQLModel, table=True):
    __tablename__ = "scm_kpi_benchmarks"
    __table_args__ = {"schema": "scm"}

    benchmark_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    benchmark_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    benchmark_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    source: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmKpiDefinitions(SQLModel, table=True):
    __tablename__ = "scm_kpi_definitions"
    __table_args__ = {"schema": "scm"}

    kpi_definition_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    kpi_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    kpi_category: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    formula: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    unit: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    threshold_green: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    threshold_yellow: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    threshold_red: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    frequency: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    data_source: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    owner_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmKpiValues(SQLModel, table=True):
    __tablename__ = "scm_kpi_values"
    __table_args__ = {"schema": "scm"}

    kpi_value_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_type: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainAgentExecutions(SQLModel, table=True):
    __tablename__ = "scm_langchain_agent_executions"
    __table_args__ = {"schema": "scm"}

    agent_execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    execution_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning_trace: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    token_usage: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    cost_usd: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainAgents(SQLModel, table=True):
    __tablename__ = "scm_langchain_agents"
    __table_args__ = {"schema": "scm"}

    agent_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    agent_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    agent_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    llm_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tools: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prompt_template_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    agent_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    memory_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainChains(SQLModel, table=True):
    __tablename__ = "scm_langchain_chains"
    __table_args__ = {"schema": "scm"}

    chain_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    chain_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    chain_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    chain_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    llm_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    prompt_template_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    chain_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainDocuments(SQLModel, table=True):
    __tablename__ = "scm_langchain_documents"
    __table_args__ = {"schema": "scm"}

    document_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vector_store_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    document_source: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    content: str = Field(default=None, sa_column=Column(Text, nullable=False))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    chunk_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainExecutions(SQLModel, table=True):
    __tablename__ = "scm_langchain_executions"
    __table_args__ = {"schema": "scm"}

    chain_execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    chain_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    execution_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    token_usage: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    cost_usd: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainLlmConfigs(SQLModel, table=True):
    __tablename__ = "scm_langchain_llm_configs"
    __table_args__ = {"schema": "scm"}

    llm_config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    config_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    provider: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    temperature: Optional[float] = Field(default=None, sa_column=Column(Numeric(3, 2), nullable=True))

    max_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    top_p: Optional[float] = Field(default=None, sa_column=Column(Numeric(3, 2), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainPromptTemplates(SQLModel, table=True):
    __tablename__ = "scm_langchain_prompt_templates"
    __table_args__ = {"schema": "scm"}

    prompt_template_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    template_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    template_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    template_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    input_variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_parser: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLangchainVectorStores(SQLModel, table=True):
    __tablename__ = "scm_langchain_vector_stores"
    __table_args__ = {"schema": "scm"}

    vector_store_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    store_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    store_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    store_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    connection_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    embedding_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    dimension: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLanggraphEdges(SQLModel, table=True):
    __tablename__ = "scm_langgraph_edges"
    __table_args__ = {"schema": "scm"}

    lg_edge_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lg_workflow_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    from_node_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    to_node_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    condition_expr: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLanggraphExecutions(SQLModel, table=True):
    __tablename__ = "scm_langgraph_executions"
    __table_args__ = {"schema": "scm"}

    lg_execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lg_workflow_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    execution_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    current_node: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLanggraphLogs(SQLModel, table=True):
    __tablename__ = "scm_langgraph_logs"
    __table_args__ = {"schema": "scm"}

    lg_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lg_execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    node_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    log_level: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    log_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    logged_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLanggraphNodes(SQLModel, table=True):
    __tablename__ = "scm_langgraph_nodes"
    __table_args__ = {"schema": "scm"}

    lg_node_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lg_workflow_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    node_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    node_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    function_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmLanggraphWorkflows(SQLModel, table=True):
    __tablename__ = "scm_langgraph_workflows"
    __table_args__ = {"schema": "scm"}

    lg_workflow_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    workflow_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    dag_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    state_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_enabled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hitl_nodes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmMlModelDeployments(SQLModel, table=True):
    __tablename__ = "scm_ml_model_deployments"
    __table_args__ = {"schema": "scm"}

    deployment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ml_model_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    version: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    environment: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    deployed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    deployed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    rollback_version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmMlModelTypes(SQLModel, table=True):
    __tablename__ = "scm_ml_model_types"
    __table_args__ = {"schema": "scm"}

    ml_model_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmMlModels(SQLModel, table=True):
    __tablename__ = "scm_ml_models"
    __table_args__ = {"schema": "scm"}

    ml_model_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    hyperparameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_data_source: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    training_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_importance: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    model_explainability: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    deployment_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    inference_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    monitoring_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retrain_schedule: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmMlMonitoring(SQLModel, table=True):
    __tablename__ = "scm_ml_monitoring"
    __table_args__ = {"schema": "scm"}

    monitoring_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ml_model_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    precision: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    recall: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    f1_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    rmse: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    mae: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    drift_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    data_drift_detected: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sample_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmMlTrainingRuns(SQLModel, table=True):
    __tablename__ = "scm_ml_training_runs"
    __table_args__ = {"schema": "scm"}

    training_run_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ml_model_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    run_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    training_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    test_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    duration_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    run_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkArcs(SQLModel, table=True):
    __tablename__ = "scm_network_arcs"
    __table_args__ = {"schema": "scm"}

    arc_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    arc_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    from_node_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    to_node_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    transit_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_per_unit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carbon_per_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkCapacities(SQLModel, table=True):
    __tablename__ = "scm_network_capacities"
    __table_args__ = {"schema": "scm"}

    capacity_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    node_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    arc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    capacity_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    capacity_qty: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkCosts(SQLModel, table=True):
    __tablename__ = "scm_network_costs"
    __table_args__ = {"schema": "scm"}

    network_cost_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    node_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    arc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    cost_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    fixed_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variable_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkFlows(SQLModel, table=True):
    __tablename__ = "scm_network_flows"
    __table_args__ = {"schema": "scm"}

    flow_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    network_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    from_node_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    to_node_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    flow_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkNodes(SQLModel, table=True):
    __tablename__ = "scm_network_nodes"
    __table_args__ = {"schema": "scm"}

    node_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    node_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    node_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    node_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkRiskAssessment(SQLModel, table=True):
    __tablename__ = "scm_network_risk_assessment"
    __table_args__ = {"schema": "scm"}

    risk_assessment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    node_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    arc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    risk_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    risk_probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    risk_impact: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    risk_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    mitigation_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmNetworkScenarios(SQLModel, table=True):
    __tablename__ = "scm_network_scenarios"
    __table_args__ = {"schema": "scm"}

    network_scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    scenario_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carbon_footprint: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOptimizationExecutionLog(SQLModel, table=True):
    __tablename__ = "scm_optimization_execution_log"
    __table_args__ = {"schema": "scm"}

    exec_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    started_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    solver_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOptimizationProblems(SQLModel, table=True):
    __tablename__ = "scm_optimization_problems"
    __table_args__ = {"schema": "scm"}

    problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    objective_function: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints_def: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    variables_def: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    data_sources: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOptimizationSensitivity(SQLModel, table=True):
    __tablename__ = "scm_optimization_sensitivity"
    __table_args__ = {"schema": "scm"}

    sensitivity_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    parameter_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    base_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    low_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    high_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    impact_on_objective: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOptimizationSolutions(SQLModel, table=True):
    __tablename__ = "scm_optimization_solutions"
    __table_args__ = {"schema": "scm"}

    solution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    solution_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    solution_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    solver_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_feasible: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "scm_ortools_problems"
    __table_args__ = {"schema": "scm"}

    ortools_problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    problem_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    warm_start_solution: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parallelization_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmOrtoolsSolutions(SQLModel, table=True):
    __tablename__ = "scm_ortools_solutions"
    __table_args__ = {"schema": "scm"}

    ortools_solution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ortools_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    solution_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    solution_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solver_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPickPathLearning(SQLModel, table=True):
    __tablename__ = "scm_pick_path_learning"
    __table_args__ = {"schema": "scm"}

    learning_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    picker_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    historical_path: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    actual_distance_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_duration_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    optimal_distance_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    optimal_duration_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    efficiency_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    pick_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPickPathProblems(SQLModel, table=True):
    __tablename__ = "scm_pick_path_problems"
    __table_args__ = {"schema": "scm"}

    pick_path_problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    wave_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    batch_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    algorithm: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    location_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_distance_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPickPathSolutions(SQLModel, table=True):
    __tablename__ = "scm_pick_path_solutions"
    __table_args__ = {"schema": "scm"}

    pick_path_solution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    pick_path_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    picker_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_sequence: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    total_distance_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    locations_visited: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPredictionAccuracy(SQLModel, table=True):
    __tablename__ = "scm_prediction_accuracy"
    __table_args__ = {"schema": "scm"}

    pred_accuracy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ml_model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    prediction_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    total_predictions: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    mape: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    mae: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rmse: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    bias: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPredictionFeatures(SQLModel, table=True):
    __tablename__ = "scm_prediction_features"
    __table_args__ = {"schema": "scm"}

    feature_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    prediction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    feature_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    feature_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    feature_importance: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPredictionOverrides(SQLModel, table=True):
    __tablename__ = "scm_prediction_overrides"
    __table_args__ = {"schema": "scm"}

    override_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    prediction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    override_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    original_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    reason: str = Field(default=None, sa_column=Column(Text, nullable=False))

    override_by: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    override_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPredictionTypes(SQLModel, table=True):
    __tablename__ = "scm_prediction_types"
    __table_args__ = {"schema": "scm"}

    prediction_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPredictions(SQLModel, table=True):
    __tablename__ = "scm_predictions"
    __table_args__ = {"schema": "scm"}

    prediction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ml_model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    prediction_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    prediction_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    prediction_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lower_bound: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    upper_bound: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    confidence_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    features: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementContracts(SQLModel, table=True):
    __tablename__ = "scm_procurement_contracts"
    __table_args__ = {"schema": "scm"}

    contract_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    contract_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    contract_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    value_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    terms: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementRecommendations(SQLModel, table=True):
    __tablename__ = "scm_procurement_recommendations"
    __table_args__ = {"schema": "scm"}

    proc_recommendation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    proc_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    delivery_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    incoterm: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    rank: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    justification: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementSavings(SQLModel, table=True):
    __tablename__ = "scm_procurement_savings"
    __table_args__ = {"schema": "scm"}

    savings_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    recommendation_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    contract_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    savings_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    estimated_savings: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_savings: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    realized_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementScenarios(SQLModel, table=True):
    __tablename__ = "scm_procurement_scenarios"
    __table_args__ = {"schema": "scm"}

    proc_scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    total_demand: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementStrategies(SQLModel, table=True):
    __tablename__ = "scm_procurement_strategies"
    __table_args__ = {"schema": "scm"}

    strategy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    category_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    strategy_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    sourcing_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    supplier_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    risk_tolerance: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmProcurementTco(SQLModel, table=True):
    __tablename__ = "scm_procurement_tco"
    __table_args__ = {"schema": "scm"}

    tco_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    partner_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    unit_price: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    logistics_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quality_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    risk_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    inventory_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    calculation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmPromotionCalendars(SQLModel, table=True):
    __tablename__ = "scm_promotion_calendars"
    __table_args__ = {"schema": "scm"}

    promotion_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    promotion_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    promotion_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    discount_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    promotion_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    expected_lift_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmRoutingDistanceMatrix(SQLModel, table=True):
    __tablename__ = "scm_routing_distance_matrix"
    __table_args__ = {"schema": "scm"}

    distance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    from_location_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    to_location_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    duration_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmRoutingLocations(SQLModel, table=True):
    __tablename__ = "scm_routing_locations"
    __table_args__ = {"schema": "scm"}

    routing_location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    location_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    address_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    time_window_earliest: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    time_window_latest: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    service_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    demand_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    demand_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    demand_volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_depot: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmRoutingProblems(SQLModel, table=True):
    __tablename__ = "scm_routing_problems"
    __table_args__ = {"schema": "scm"}

    routing_problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    algorithm: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    vehicle_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    location_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmRoutingSolutions(SQLModel, table=True):
    __tablename__ = "scm_routing_solutions"
    __table_args__ = {"schema": "scm"}

    routing_solution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    routing_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    stop_sequence: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    total_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_demand: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    capacity_utilization_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    carbon_emissions_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmRoutingVehicles(SQLModel, table=True):
    __tablename__ = "scm_routing_vehicles"
    __table_args__ = {"schema": "scm"}

    routing_vehicle_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    vehicle_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    vehicle_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    capacity_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    capacity_volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_stops: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    start_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    end_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    fixed_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_per_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_per_hour: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScenarioComparisons(SQLModel, table=True):
    __tablename__ = "scm_scenario_comparisons"
    __table_args__ = {"schema": "scm"}

    comparison_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    baseline_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    alternative_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    comparison_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    recommended_scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScenarioResults(SQLModel, table=True):
    __tablename__ = "scm_scenario_results"
    __table_args__ = {"schema": "scm"}

    scenario_result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    result_key: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    result_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    result_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    result_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScenarioTemplates(SQLModel, table=True):
    __tablename__ = "scm_scenario_templates"
    __table_args__ = {"schema": "scm"}

    template_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    template_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    template_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScenarioTypes(SQLModel, table=True):
    __tablename__ = "scm_scenario_types"
    __table_args__ = {"schema": "scm"}

    scenario_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScenarios(SQLModel, table=True):
    __tablename__ = "scm_scenarios"
    __table_args__ = {"schema": "scm"}

    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    scenario_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objectives: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    impact_assessment: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    recommendations: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    parent_scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    template_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScipyProblems(SQLModel, table=True):
    __tablename__ = "scm_scipy_problems"
    __table_args__ = {"schema": "scm"}

    scipy_problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    problem_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    method_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScipyResults(SQLModel, table=True):
    __tablename__ = "scm_scipy_results"
    __table_args__ = {"schema": "scm"}

    scipy_result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scipy_problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    result_label: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    success: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmScipyStatisticalTests(SQLModel, table=True):
    __tablename__ = "scm_scipy_statistical_tests"
    __table_args__ = {"schema": "scm"}

    stat_test_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    test_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    test_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    test_statistic: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    p_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    result_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSeasonalityIndices(SQLModel, table=True):
    __tablename__ = "scm_seasonality_indices"
    __table_args__ = {"schema": "scm"}

    seasonality_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    period_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    period_code: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    index_value: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSolverBenchmarks(SQLModel, table=True):
    __tablename__ = "scm_solver_benchmarks"
    __table_args__ = {"schema": "scm"}

    benchmark_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    problem_size: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    avg_solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    avg_iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    memory_mb: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    test_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSolverInstances(SQLModel, table=True):
    __tablename__ = "scm_solver_instances"
    __table_args__ = {"schema": "scm"}

    solver_instance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    instance_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    license_key_enc: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSolverLogs(SQLModel, table=True):
    __tablename__ = "scm_solver_logs"
    __table_args__ = {"schema": "scm"}

    solver_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_instance_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    log_level: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    log_message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    log_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSolverParameters(SQLModel, table=True):
    __tablename__ = "scm_solver_parameters"
    __table_args__ = {"schema": "scm"}

    solver_param_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    param_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    param_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    param_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    default_value: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    min_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSolverTypes(SQLModel, table=True):
    __tablename__ = "scm_solver_types"
    __table_args__ = {"schema": "scm"}

    solver_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    solver_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    solver_framework: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopCycles(SQLModel, table=True):
    __tablename__ = "scm_sop_cycles"
    __table_args__ = {"schema": "scm"}

    sop_cycle_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cycle_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    cycle_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    fiscal_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    fiscal_period: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    cycle_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    cycle_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopDecisions(SQLModel, table=True):
    __tablename__ = "scm_sop_decisions"
    __table_args__ = {"schema": "scm"}

    sop_decision_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    decision_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    decision_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    decision_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    rationale: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopDemandPlans(SQLModel, table=True):
    __tablename__ = "scm_sop_demand_plans"
    __table_args__ = {"schema": "scm"}

    sop_demand_plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    forecast_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    booked_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_demand: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopKpis(SQLModel, table=True):
    __tablename__ = "scm_sop_kpis"
    __table_args__ = {"schema": "scm"}

    sop_kpi_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    kpi_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    kpi_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    kpi_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    kpi_variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopReconciliation(SQLModel, table=True):
    __tablename__ = "scm_sop_reconciliation"
    __table_args__ = {"schema": "scm"}

    reconciliation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    total_demand: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_supply: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gap_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    resolution: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopScenarios(SQLModel, table=True):
    __tablename__ = "scm_sop_scenarios"
    __table_args__ = {"schema": "scm"}

    sop_scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_cycle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    scenario_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    scenario_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSopSupplyPlans(SQLModel, table=True):
    __tablename__ = "scm_sop_supply_plans"
    __table_args__ = {"schema": "scm"}

    sop_supply_plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sop_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    production_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    procurement_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    transfer_in_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_supply: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierForecasts(SQLModel, table=True):
    __tablename__ = "scm_supplier_forecasts"
    __table_args__ = {"schema": "scm"}

    supplier_forecast_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    forecast_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    forecast_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    forecast_qty: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    committed_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    confirmation_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    confirmed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    confirmed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierPerformance(SQLModel, table=True):
    __tablename__ = "scm_supplier_performance"
    __table_args__ = {"schema": "scm"}

    performance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    metric_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    metric_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    measurement_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierProfiles(SQLModel, table=True):
    __tablename__ = "scm_supplier_profiles"
    __table_args__ = {"schema": "scm"}

    supplier_profile_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    capabilities: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    certifications: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    total_capacity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    min_order_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_order_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    payment_terms: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    incoterm: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierRiskAssessments(SQLModel, table=True):
    __tablename__ = "scm_supplier_risk_assessments"
    __table_args__ = {"schema": "scm"}

    risk_assessment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    assessment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    financial_risk: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    operational_risk: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    geopolitical_risk: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    esg_risk: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    overall_risk: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    risk_level: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    mitigation_plan: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    assessor_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierScorecards(SQLModel, table=True):
    __tablename__ = "scm_supplier_scorecards"
    __table_args__ = {"schema": "scm"}

    scorecard_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    quality_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    delivery_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    cost_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    innovation_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    sustainability_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    overall_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    rating: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplierSustainability(SQLModel, table=True):
    __tablename__ = "scm_supplier_sustainability"
    __table_args__ = {"schema": "scm"}

    sustainability_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    carbon_footprint: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    water_usage: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    waste_generated: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    renewable_energy_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    report_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    cert_body: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyCalendarDates(SQLModel, table=True):
    __tablename__ = "scm_supply_calendar_dates"
    __table_args__ = {"schema": "scm"}

    calendar_date_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    supply_calendar_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    calendar_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_working_day: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    capacity_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    shift_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyCalendars(SQLModel, table=True):
    __tablename__ = "scm_supply_calendars"
    __table_args__ = {"schema": "scm"}

    supply_calendar_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    calendar_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    calendar_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    calendar_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyConstraints(SQLModel, table=True):
    __tablename__ = "scm_supply_constraints"
    __table_args__ = {"schema": "scm"}

    supply_constraint_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    constraint_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    constraint_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    constraint_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    constraint_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyLeadTimes(SQLModel, table=True):
    __tablename__ = "scm_supply_lead_times"
    __table_args__ = {"schema": "scm"}

    lead_time_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    supplier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    destination_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lead_time_days: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    lead_time_variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyPlanLines(SQLModel, table=True):
    __tablename__ = "scm_supply_plan_lines"
    __table_args__ = {"schema": "scm"}

    supply_plan_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    supply_plan_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    line_num: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    destination_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyPlans(SQLModel, table=True):
    __tablename__ = "scm_supply_plans"
    __table_args__ = {"schema": "scm"}

    supply_plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    plan_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    demand_forecast_source: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplyRisks(SQLModel, table=True):
    __tablename__ = "scm_supply_risks"
    __table_args__ = {"schema": "scm"}

    supply_risk_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    supplier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    risk_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    risk_level: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    risk_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    risk_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    mitigation_plan: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    identified_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmSupplySources(SQLModel, table=True):
    __tablename__ = "scm_supply_sources"
    __table_args__ = {"schema": "scm"}

    supply_source_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationConstraints(SQLModel, table=True):
    __tablename__ = "scm_transportation_constraints"
    __table_args__ = {"schema": "scm"}

    trans_constraint_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    constraint_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    max_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_volume: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_length: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_width: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_height: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    hazmat_allowed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationCosts(SQLModel, table=True):
    __tablename__ = "scm_transportation_costs"
    __table_args__ = {"schema": "scm"}

    trans_cost_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    mode_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lane_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    rate_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rate_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    fuel_surcharge_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    accessorial_charges: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationModes(SQLModel, table=True):
    __tablename__ = "scm_transportation_modes"
    __table_args__ = {"schema": "scm"}

    mode_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mode_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    mode_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    carbon_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationRecommendations(SQLModel, table=True):
    __tablename__ = "scm_transportation_recommendations"
    __table_args__ = {"schema": "scm"}

    trans_recommendation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    trans_scenario_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    recommendation_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    estimated_savings: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    justification: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationScenarios(SQLModel, table=True):
    __tablename__ = "scm_transportation_scenarios"
    __table_args__ = {"schema": "scm"}

    trans_scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carbon_footprint: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmTransportationServiceLevels(SQLModel, table=True):
    __tablename__ = "scm_transportation_service_levels"
    __table_args__ = {"schema": "scm"}

    trans_service_level_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    mode_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lane_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    transit_time_hours: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_time_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    loss_damage_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehouseAisles(SQLModel, table=True):
    __tablename__ = "scm_warehouse_aisles"
    __table_args__ = {"schema": "scm"}

    aisle_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    zone_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    aisle_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    length_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehouseLocations(SQLModel, table=True):
    __tablename__ = "scm_warehouse_locations"
    __table_args__ = {"schema": "scm"}

    wh_location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    aisle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    location_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    x_coordinate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    y_coordinate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    z_coordinate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_volume: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehousePickBatches(SQLModel, table=True):
    __tablename__ = "scm_warehouse_pick_batches"
    __table_args__ = {"schema": "scm"}

    batch_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    batch_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    order_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_items: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehousePickLines(SQLModel, table=True):
    __tablename__ = "scm_warehouse_pick_lines"
    __table_args__ = {"schema": "scm"}

    pick_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    pick_order_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    picked_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    sequence_num: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehousePickOrders(SQLModel, table=True):
    __tablename__ = "scm_warehouse_pick_orders"
    __table_args__ = {"schema": "scm"}

    pick_order_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    wave_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    batch_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    scheduled_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehouseWaves(SQLModel, table=True):
    __tablename__ = "scm_warehouse_waves"
    __table_args__ = {"schema": "scm"}

    wave_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    wave_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    wave_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    scheduled_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    cutoff_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    order_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ScmWarehouseZones(SQLModel, table=True):
    __tablename__ = "scm_warehouse_zones"
    __table_args__ = {"schema": "scm"}

    zone_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    zone_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    zone_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    zone_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    x_coordinate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    y_coordinate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

