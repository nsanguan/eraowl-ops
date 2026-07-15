from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime


class AddressCreate(BaseModel):
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state_province: str
    postal_code: str
    country_code: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_active: bool = True


class AddressUpdate(BaseModel):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_active: Optional[bool] = None


class AddressOut(BaseModel):
    address_id: uuid.UUID
    address_line1: str
    address_line2: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: str
    country_code: str
    latitude: Optional[float]
    longitude: Optional[float]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartyCreate(BaseModel):
    party_type: str
    party_name: str
    tax_id: Optional[str] = None
    is_active: bool = True


class PartyUpdate(BaseModel):
    party_type: Optional[str] = None
    party_name: Optional[str] = None
    tax_id: Optional[str] = None
    is_active: Optional[bool] = None


class PartyOut(BaseModel):
    party_id: uuid.UUID
    party_type: str
    party_name: str
    tax_id: Optional[str]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartySiteCreate(BaseModel):
    party_id: uuid.UUID
    address_id: uuid.UUID
    site_name: Optional[str] = None
    is_primary: bool = False
    is_active: bool = True


class PartySiteUpdate(BaseModel):
    address_id: Optional[uuid.UUID] = None
    site_name: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: Optional[bool] = None


class PartySiteOut(BaseModel):
    party_site_id: uuid.UUID
    party_id: uuid.UUID
    address_id: uuid.UUID
    site_name: Optional[str]
    is_primary: bool
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartySiteUseCreate(BaseModel):
    party_site_id: uuid.UUID
    use_type: str
    is_active: bool = True


class PartySiteUseUpdate(BaseModel):
    use_type: Optional[str] = None
    is_active: Optional[bool] = None


class PartySiteUseOut(BaseModel):
    party_site_use_id: uuid.UUID
    party_site_id: uuid.UUID
    use_type: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartyRoleCreate(BaseModel):
    party_id: uuid.UUID
    role_type: str
    is_active: bool = True


class PartyRoleUpdate(BaseModel):
    role_type: Optional[str] = None
    is_active: Optional[bool] = None


class PartyRoleOut(BaseModel):
    party_role_id: uuid.UUID
    party_id: uuid.UUID
    role_type: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SupplierCreate(BaseModel):
    party_id: uuid.UUID
    supplier_code: str
    payment_term_days: int = 30
    currency: str
    is_active: bool = True


class SupplierUpdate(BaseModel):
    supplier_code: Optional[str] = None
    payment_term_days: Optional[int] = None
    currency: Optional[str] = None
    is_active: Optional[bool] = None


class SupplierOut(BaseModel):
    supplier_id: uuid.UUID
    party_id: uuid.UUID
    supplier_code: str
    payment_term_days: int
    currency: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class CustomerCreate(BaseModel):
    party_id: uuid.UUID
    customer_code: str
    credit_limit: Optional[float] = None
    payment_term_days: int = 30
    is_active: bool = True


class CustomerUpdate(BaseModel):
    customer_code: Optional[str] = None
    credit_limit: Optional[float] = None
    payment_term_days: Optional[int] = None
    is_active: Optional[bool] = None


class CustomerOut(BaseModel):
    customer_id: uuid.UUID
    party_id: uuid.UUID
    customer_code: str
    credit_limit: Optional[float]
    payment_term_days: int
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
