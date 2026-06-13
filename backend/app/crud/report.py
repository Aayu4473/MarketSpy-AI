from sqlalchemy.ext.asyncio import AsyncSession
from app.models.report import Report
from app.schemas.report import ReportCreate

async def create_report(db: AsyncSession, report_in: ReportCreate) -> Report:
    db_obj=Report(**report_in.model_dump())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
