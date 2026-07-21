from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.db.session import get_db 
from app.schemas.report import ReportCreate
from app.core.ai_service import generate_market_report
from app.models.metrics import Metrics
from app.schemas.metrics import MetricResponse
from app.agents.crew import run_competitive_analysis_crew
from pydantic import BaseModel

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


@router.get("/metrics/{competitor_id}", response_model=List[MetricResponse], status_code=status.HTTP_200_OK)
async def get_competitor_metrics(
    competitor_id: int, 
    db: AsyncSession = Depends(get_db)
):
    """
    Fetch all extracted financial and operational metrics stored for a specific competitor.
    Serves the clean historical data records downstream to dashboards or external API consumers.
    """
    try:
        # 1. Query the database for all metrics rows belonging to this competitor
        result = await db.execute(
            select(Metrics).where(Metrics.competitor_id == competitor_id)
        )
        metrics_list = result.scalars().all()

        # 2. Raise a clean 404 error if no data rows exist for the given competitor
        if not metrics_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"No metrics found for Competitor ID {competitor_id}. Ensure the background intelligence worker has finished running."
            )

        # 3. Stream out the typed array of rows matching your Pydantic schema
        return metrics_list

    except HTTPException:
        # Re-raise standard 404 HTTP exceptions so they don't hit the generic interceptor below
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database retrieval operation failed: {str(e)}"
        )
    
class AnalysisResponse(BaseModel):
    competitor_id: int
    executive_report: str

# ==========================================
# 🤖 PHASE 3: CREWAI AGENT EXECUTION ROUTE
# ==========================================
@router.post("/{competitor_id}/analyze", response_model=AnalysisResponse)
def generate_executive_analysis(competitor_id: int):
    """
    Triggers the Phase 3 CrewAI multi-agent collective. 
    The Financial Analyst fetches data from the DB, and the Strategist writes the report.
    """
    try:
        # ⚠️ Note: This is a synchronous AI execution. 
        # It will take 30-90 seconds for the agents to think, debate, and write.
        final_report = run_competitive_analysis_crew(competitor_id)
        
        return {
            "competitor_id": competitor_id,
            "executive_report": str(final_report)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent collective failed to execute: {str(e)}"
        )