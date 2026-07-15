from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime


class CreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True


class UpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class Response(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
    model_config = {"from_attributes": True}
