from sqlalchemy.ext.asyncio import AsyncSession
from app.models.metrics import Metrics
from app.schemas.metrics import MetricsCreate

async def create_metric(db: AsyncSession, metric_in: MetricsCreate) -> Metrics:
    """
    Inserts a historical data metrics point linked to a specific competitor.
    """
    db_obj = Metrics(**metric_in.model_dump())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
