from app.shared.module_base.generic import BaseGenericService
from app.modules.admin.models import User, Role, Privilege, AuditLog, RefreshToken


class AdminGenericService(BaseGenericService):
    ALLOWED_TABLES = {
        "users": User,
        "roles": Role,
        "privileges": Privilege,
        "audit_logs": AuditLog,
        "refresh_tokens": RefreshToken,
    }
