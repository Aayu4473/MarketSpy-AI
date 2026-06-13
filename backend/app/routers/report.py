from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db 
from app.schemas.report import ReportCreate, ReportResponse
from app.crud import report as crud_report

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.post("/", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
async def create_new_report(report_in: ReportCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new AI market intelligence report for a specific competitor.
    """
    try:
        return await crud_report.create_report(db=db, report_in=report_in)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create report: {str(e)}"
        )