from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db 
from app.schemas.report import ReportCreate
from app.core.ai_service import generate_market_report

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_report(
    report_in: ReportCreate, 
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    """
    Ingest a competitor target configuration, offload web scraping and 
    Gemini LLM reasoning to a non-blocking background task worker, 
    and immediately return an execution acknowledgment.
    """
    # 1. Validate the input URL structure safely before spinning up a worker
    if not report_in.target_url.startswith(("http://", "https://")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid target URL schema. URL must begin with 'http://' or 'https://'"
        )

    try:
        # 2. Schedule the heavy AI processing and extraction pipeline to execute in the background
        background_tasks.add_task(
            generate_market_report, 
            report_in.competitor_id, 
            report_in.target_url, 
            db
        )
        
        # 3. Respond instantly so the client API client isn't left hanging on a blocking connection
        return {
            "status": "processing",
            "message": f"Autonomous intelligence engine initialized for competitor ID {report_in.competitor_id}.",
            "target_url": report_in.target_url
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to initialize analysis worker: {str(e)}"
        )