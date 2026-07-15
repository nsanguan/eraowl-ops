from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime


class OrgCorporateCreate(BaseModel):
    corp_name: str
    corp_code: str
    is_active: bool = True


class OrgCorporateUpdate(BaseModel):
    corp_name: Optional[str] = None
    corp_code: Optional[str] = None
    is_active: Optional[bool] = None


class OrgCorporateOut(BaseModel):
    corporate_id: uuid.UUID
    corp_name: str
    corp_code: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class OrgCompanyCreate(BaseModel):
    corporate_id: uuid.UUID
    legal_name: str
    tax_id: str
    company_code: str
    is_active: bool = True


class OrgCompanyUpdate(BaseModel):
    legal_name: Optional[str] = None
    tax_id: Optional[str] = None
    company_code: Optional[str] = None
    is_active: Optional[bool] = None


class OrgCompanyOut(BaseModel):
    company_id: uuid.UUID
    corporate_id: uuid.UUID
    legal_name: str
    tax_id: str
    company_code: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class OrgBusinessUnitCreate(BaseModel):
    company_id: uuid.UUID
    bu_name: str
    bu_code: str
    is_active: bool = True


class OrgBusinessUnitUpdate(BaseModel):
    bu_name: Optional[str] = None
    bu_code: Optional[str] = None
    is_active: Optional[bool] = None


class OrgBusinessUnitOut(BaseModel):
    business_unit_id: uuid.UUID
    company_id: uuid.UUID
    bu_name: str
    bu_code: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class OrgSiteCreate(BaseModel):
    business_unit_id: uuid.UUID
    site_name: str
    site_code: str
    address_id: Optional[uuid.UUID] = None
    is_active: bool = True


class OrgSiteUpdate(BaseModel):
    site_name: Optional[str] = None
    site_code: Optional[str] = None
    address_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None


class OrgSiteOut(BaseModel):
    site_id: uuid.UUID
    business_unit_id: uuid.UUID
    site_name: str
    site_code: str
    address_id: Optional[uuid.UUID]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class OrgWarehouseCreate(BaseModel):
    site_id: uuid.UUID
    warehouse_name: str
    warehouse_code: str
    is_active: bool = True


class OrgWarehouseUpdate(BaseModel):
    warehouse_name: Optional[str] = None
    warehouse_code: Optional[str] = None
    is_active: Optional[bool] = None


class OrgWarehouseOut(BaseModel):
    warehouse_id: uuid.UUID
    site_id: uuid.UUID
    warehouse_name: str
    warehouse_code: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class OrgWarehouseLocatorCreate(BaseModel):
    warehouse_id: uuid.UUID
    zone: str
    aisle: str
    rack: str
    bin: str
    locator_code: str
    is_active: bool = True


class OrgWarehouseLocatorUpdate(BaseModel):
    zone: Optional[str] = None
    aisle: Optional[str] = None
    rack: Optional[str] = None
    bin: Optional[str] = None
    locator_code: Optional[str] = None
    is_active: Optional[bool] = None


class OrgWarehouseLocatorOut(BaseModel):
    warehouse_locator_id: uuid.UUID
    warehouse_id: uuid.UUID
    zone: str
    aisle: str
    rack: str
    bin: str
    locator_code: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
