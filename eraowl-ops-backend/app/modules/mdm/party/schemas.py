from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime


class AddressCreate(BaseModel):
    country: str
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    is_active: bool = True


class AddressUpdate(BaseModel):
    country: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    is_active: Optional[bool] = None


class AddressOut(BaseModel):
    address_id: uuid.UUID
    country: Optional[str]
    address_line1: str
    address_line2: Optional[str]
    city: str
    state: Optional[str]
    postal_code: Optional[str]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartyCreate(BaseModel):
    party_number: str
    party_name: str
    party_type: str = "ORGANIZATION"
    tax_reference: Optional[str] = None
    is_active: bool = True


class PartyUpdate(BaseModel):
    party_number: Optional[str] = None
    party_name: Optional[str] = None
    party_type: Optional[str] = None
    tax_reference: Optional[str] = None
    is_active: Optional[bool] = None


class PartyOut(BaseModel):
    party_id: uuid.UUID
    party_number: str
    party_name: str
    party_type: str
    tax_reference: Optional[str]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartySiteCreate(BaseModel):
    party_id: uuid.UUID
    address_id: uuid.UUID
    party_site_number: str
    site_name: Optional[str] = None
    is_active: bool = True


class PartySiteUpdate(BaseModel):
    address_id: Optional[uuid.UUID] = None
    party_site_number: Optional[str] = None
    site_name: Optional[str] = None
    is_active: Optional[bool] = None


class PartySiteOut(BaseModel):
    party_site_id: uuid.UUID
    party_id: uuid.UUID
    address_id: uuid.UUID
    party_site_number: str
    site_name: Optional[str]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PartySiteUseCreate(BaseModel):
    party_site_id: uuid.UUID
    site_use_type: str
    is_primary: bool = False
    is_active: bool = True


class PartySiteUseUpdate(BaseModel):
    site_use_type: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: Optional[bool] = None


class PartySiteUseOut(BaseModel):
    site_use_id: uuid.UUID
    party_site_id: uuid.UUID
    site_use_type: str
    is_primary: bool
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
    party_role_id: Optional[uuid.UUID] = None
    supplier_code: Optional[str] = None
    currency_code: Optional[str] = None
    vendor_type_lookup_code: Optional[str] = None
    payment_method_code: Optional[str] = None
    payment_term_days: int = 30
    is_active: bool = True


class SupplierUpdate(BaseModel):
    supplier_code: Optional[str] = None
    currency_code: Optional[str] = None
    vendor_type_lookup_code: Optional[str] = None
    payment_method_code: Optional[str] = None
    payment_term_days: Optional[int] = None
    is_active: Optional[bool] = None


class SupplierOut(BaseModel):
    supplier_id: uuid.UUID
    party_id: uuid.UUID
    party_role_id: Optional[uuid.UUID]
    supplier_code: Optional[str]
    currency_code: Optional[str]
    vendor_type_lookup_code: Optional[str]
    payment_method_code: Optional[str]
    payment_term_days: int
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class CustomerCreate(BaseModel):
    party_id: uuid.UUID
    party_role_id: Optional[uuid.UUID] = None
    customer_code: Optional[str] = None
    customer_class_code: Optional[str] = None
    credit_limit: Optional[float] = None
    payment_term_days: int = 30
    is_active: bool = True


class CustomerUpdate(BaseModel):
    customer_code: Optional[str] = None
    customer_class_code: Optional[str] = None
    credit_limit: Optional[float] = None
    payment_term_days: Optional[int] = None
    is_active: Optional[bool] = None


class CustomerOut(BaseModel):
    customer_id: uuid.UUID
    party_id: uuid.UUID
    party_role_id: Optional[uuid.UUID]
    customer_code: Optional[str]
    customer_class_code: Optional[str]
    credit_limit: Optional[float]
    payment_term_days: int
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class CompositeSiteInput(BaseModel):
    country: str
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    site_name: Optional[str] = None
    site_uses: list[str] = []


class CompositePartyCreate(BaseModel):
    party_number: str
    party_name: str
    party_type: str = "ORGANIZATION"
    tax_reference: Optional[str] = None
    roles: list[str] = []
    vendor_type_lookup_code: Optional[str] = None
    payment_method_code: Optional[str] = None
    customer_class_code: Optional[str] = None
    credit_limit: Optional[float] = None
    sites: list[CompositeSiteInput] = []


class TcaSiteView(BaseModel):
    party_site_id: uuid.UUID
    party_site_number: str
    site_name: Optional[str]
    address: Optional[AddressOut] = None
    site_uses: list[PartySiteUseOut] = []


class TcaPartyView(BaseModel):
    party: PartyOut
    roles: list[PartyRoleOut] = []
    supplier: Optional[SupplierOut] = None
    customer: Optional[CustomerOut] = None
    sites: list[TcaSiteView] = []


class TreeNode(BaseModel):
    node_id: str
    node_type: str
    label: str
    children: list["TreeNode"] = []
    entity: Optional[dict] = None


class TreeResponse(BaseModel):
    tree: list[TreeNode]


class TreeUpdateRequest(BaseModel):
    node_type: str
    action: str  # 'update' | 'add' | 'delete'
    entity: dict

