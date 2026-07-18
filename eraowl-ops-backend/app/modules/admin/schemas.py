from typing import Optional
import uuid
from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None


class UserOut(BaseModel):
    user_id: uuid.UUID
    username: str
    email: str
    is_active: bool
    last_login_at: Optional[datetime] = None
    permission_version: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str


class UserAssignRoles(BaseModel):
    role_ids: list[uuid.UUID]


class UserAssignBusinessUnits(BaseModel):
    bu_ids: list[uuid.UUID]


class RoleOut(BaseModel):
    role_id: uuid.UUID
    role_name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PrivilegeOut(BaseModel):
    privilege_id: uuid.UUID
    module: str
    action: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


class UserWithRoles(UserOut):
    roles: list[RoleOut] = []
    business_unit_ids: list[uuid.UUID] = []


class RoleCreate(BaseModel):
    role_name: str
    description: Optional[str] = None


class RoleUpdate(BaseModel):
    role_name: Optional[str] = None
    description: Optional[str] = None


class RoleAssignPermissions(BaseModel):
    privilege_ids: list[uuid.UUID]


class RoleWithPermissions(RoleOut):
    privileges: list[PrivilegeOut] = []


class PrivilegeCreate(BaseModel):
    module: str
    action: str
    description: Optional[str] = None


class AuditLogOut(BaseModel):
    audit_log_id: uuid.UUID
    user_id: Optional[uuid.UUID] = None
    action: str
    target_entity: str
    target_id: Optional[uuid.UUID] = None
    old_value: Optional[dict] = None
    new_value: Optional[dict] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserOut


class RefreshRequest(BaseModel):
    refresh_token: str
    access_token: str | None = None


class LogoutRequest(BaseModel):
    refresh_token: str
    access_token: str | None = None


class PermissionMatrixResponse(BaseModel):
    roles: list[RoleOut]
    privileges: list[PrivilegeOut]
    matrix: dict[str, list[str]]


class PermissionMatrixSync(BaseModel):
    matrix: dict[str, list[str]]


# ── UI Personalization Schemas ──


class UiPersonalizationLoadRequest(BaseModel):
    page_key: str


class UiPersonalizationLoadResponse(BaseModel):
    page_key: str
    schema_version: str
    layout: dict
    source: str = "template"  # "template" | "user" | "role"


class UiPersonalizationSaveRequest(BaseModel):
    page_key: str
    target_user_id: Optional[uuid.UUID] = None
    target_role_id: Optional[uuid.UUID] = None
    override_json: dict
    as_delta: bool = True


class UiStandardTemplateOut(BaseModel):
    id: uuid.UUID
    page_key: str
    schema_version: str
    base_layout_json: dict
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserUiPersonalizationOut(BaseModel):
    id: uuid.UUID
    page_key: str
    user_id: Optional[uuid.UUID] = None
    role_id: Optional[uuid.UUID] = None
    override_json: dict
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UiTemplateSummaryOut(BaseModel):
    page_key: str
    schema_version: str
    component_count: int


class UiTemplateDetailOut(BaseModel):
    id: str
    page_key: str
    schema_version: str
    base_layout_json: dict
    component_count: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


# ---------------------------------------------------------------------------
# User Profiles (EBS Profile Options)
# ---------------------------------------------------------------------------


class ProfileOptionCreate(BaseModel):
    profile_option_name: str
    user_profile_option_name: str
    description: Optional[str] = None
    value_type: str = "text"  # text | number | date | checkbox | url
    sql_validation: Optional[str] = None
    site_enabled: bool = True
    application_enabled: bool = False
    role_enabled: bool = False
    user_enabled: bool = False
    is_system: bool = False


class ProfileOptionUpdate(BaseModel):
    user_profile_option_name: Optional[str] = None
    description: Optional[str] = None
    value_type: Optional[str] = None
    sql_validation: Optional[str] = None
    site_enabled: Optional[bool] = None
    application_enabled: Optional[bool] = None
    role_enabled: Optional[bool] = None
    user_enabled: Optional[bool] = None
    is_system: Optional[bool] = None


class ProfileOptionOut(BaseModel):
    profile_option_id: uuid.UUID
    profile_option_name: str
    user_profile_option_name: str
    description: Optional[str] = None
    value_type: str
    sql_validation: Optional[str] = None
    site_enabled: bool
    application_enabled: bool
    role_enabled: bool
    user_enabled: bool
    is_system: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProfileLevelOut(BaseModel):
    profile_level_id: int
    level_code: str
    name: str
    description: Optional[str] = None
    precedence: int

    model_config = {"from_attributes": True}


class ProfileOptionValueOut(BaseModel):
    id: uuid.UUID
    profile_option_id: uuid.UUID
    level: str
    level_key: Optional[str] = None
    profile_option_value: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProfileValueSetRequest(BaseModel):
    """Set (upsert) a profile option value at a given level.

    ``level`` must be one of: site, application, role, user.
    ``level_key`` is required for application/role/user and identifies the
    concrete target (module string, role_id, or user_id).  For site it is null.
    """

    level: str
    level_key: Optional[str] = None
    profile_option_value: str


class EffectiveProfileValueOut(BaseModel):
    profile_option_name: str
    effective_value: Optional[str] = None
    resolved_level: Optional[str] = None
    level_key: Optional[str] = None
    is_default: bool = False
