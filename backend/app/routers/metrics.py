from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db # match your exact get_db path
from app.schemas.metrics import MetricsCreate, MetricsResponse
from app.crud import metrics as crud_metrics

router = APIRouter(
    prefix="/metrics",
    tags=["metrics"]
)

@router.post("/", response_model=MetricsResponse, status_code=status.HTTP_201_CREATED)
async def create_new_metric(metric_in: MetricsCreate, db: AsyncSession = Depends(get_db)):
    """
    Log a new numerical data point or KPI metric for a competitor.
    """
    try:
        return await crud_metrics.create_metric(db=db, metric_in=metric_in)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to log metric data point: {str(e)}"
        )