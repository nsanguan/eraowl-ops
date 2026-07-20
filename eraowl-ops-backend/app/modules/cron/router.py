from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.modules.cron.schemas import CronJobStatusOut

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/status", response_model=CronJobStatusOut)
async def cron_status(db: AsyncSession = Depends(get_db)):
    return CronJobStatusOut(checked_at=datetime.utcnow())
