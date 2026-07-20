import uuid
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class PortalUserCreate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    email: str
    password_hash: str
    full_name: str
    is_active: bool = True


class PortalUserUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class PortalUserOut(BaseModel):
    portal_user_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    email: str
    full_name: str
    is_active: bool
    last_login_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


class RfqResponseCreate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quoted_price: float
    lead_time_days: int
    valid_until: date
    status: str = "SUBMITTED"
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class RfqResponseUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quoted_price: Optional[float] = None
    lead_time_days: Optional[int] = None
    valid_until: Optional[date] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class RfqResponseOut(BaseModel):
    response_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quoted_price: float
    lead_time_days: int
    valid_until: date
    status: str
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


class ShipmentAdviceCreate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    po_id: Optional[uuid.UUID] = None
    asn_number: str
    ship_date: datetime
    expected_arrival: datetime
    status: str = "SHIPPED"
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ShipmentAdviceUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    po_id: Optional[uuid.UUID] = None
    asn_number: Optional[str] = None
    ship_date: Optional[datetime] = None
    expected_arrival: Optional[datetime] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ShipmentAdviceOut(BaseModel):
    asn_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    po_id: Optional[uuid.UUID] = None
    asn_number: str
    ship_date: datetime
    expected_arrival: datetime
    status: str
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}
