from sqlmodel import Field
from app.shared.module_base.mixins import AuditMixin, SoftDeleteMixin, UUIDPKMixin
from typing import Optional


class YourEntity(UUIDPKMixin, AuditMixin, SoftDeleteMixin, table=True):
    __tablename__ = "your_entities"
    __table_args__ = {"schema": "your_module"}

    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)
