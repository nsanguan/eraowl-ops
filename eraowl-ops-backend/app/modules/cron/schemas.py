from datetime import datetime
from pydantic import BaseModel


class CronJobStatusOut(BaseModel):
    scheduler: str = "cron"
    status: str = "operational"
    checked_at: datetime
