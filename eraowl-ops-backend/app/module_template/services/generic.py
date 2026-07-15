from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.module_base.generic import BaseGenericService


class YourModuleGenericService(BaseGenericService):
    ALLOWED_TABLES = {}
