from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import text
from sqlalchemy.future import select

from app.db.session import get_db
from app.schemas.competitor import CompetitorCreate, CompetitorResponse
from app.crud import competitor as crud_competitor
from app.models.competitor import Competitor

# WIRING THE AI ENGINE: Adjust this import path if ai_service is in a different folder
from app.core.ai_service import generate_market_report 

router = APIRouter(
    prefix="/competitors",
    tags=["Competitors"]
)

# POST: Create a new competitor and trigger AI analysis
@router.post("/", response_model=CompetitorResponse)
async def create_competitor(
    competitor_in: CompetitorCreate,
    db: AsyncSession = Depends(get_db)
):
    # 1. Check if the competitor already exists
    result = await db.execute(select(Competitor).where(Competitor.name == competitor_in.name))
    existing_competitor = result.scalar_one_or_none()
    
    if existing_competitor:
        raise HTTPException(status_code=400, detail=f"Competitor '{competitor_in.name}' already exists. Please select them from the sidebar.")

    # 2. Save the new company to the database
    new_competitor = await crud_competitor.create_competitor(db=db, competitor_in=competitor_in)
    
    # 3. Automatically add https:// if the user forgot it
    target_url = getattr(new_competitor, "website", "")
    if target_url and not target_url.startswith(("http://", "https://")):
        target_url = f"https://{target_url}"
    
    # 4. WAKE UP THE AI ENGINE! 
    try:
        if target_url:
            print(f"Triggering AI Engine for {new_competitor.name} at {target_url}...")
            await generate_market_report(competitor_id=new_competitor.id, target_url=target_url, db=db)
    except Exception as e:
        print(f"AI Engine failed to execute: {e}")

    # Added 'await' to support AsyncSession
    db.add(new_competitor)
    await db.commit()
    await db.refresh(new_competitor) # <--- THIS IS THE MAGIC FIX

    # 5. Prevent the MissingGreenlet crash by returning a standard dictionary
    return {
        "id": new_competitor.id,
        "name": new_competitor.name,
        "website": target_url,
        "industry": getattr(new_competitor, "industry", None),
        "created_at": new_competitor.created_at
    }

# GET: Fetch all tracked competitors
@router.get("/", response_model=List[CompetitorResponse])
async def read_competitors(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_db)
):
    return await crud_competitor.get_competitors(db=db, skip=skip, limit=limit)

# GET: Fetch details, metrics, and report for a specific competitor
@router.get("/{competitor_id}")
async def read_competitor_details(
    competitor_id: int,
    db: AsyncSession = Depends(get_db)
):
    competitor = await crud_competitor.get_competitor_by_id(db=db, competitor_id=competitor_id) 
    
    if not competitor:
        raise HTTPException(status_code=404, detail="Competitor not found")
        
    metrics_query = await db.execute(
        text("SELECT metric_type, value FROM metrics WHERE competitor_id = :id"),
        {"id": competitor_id}
    )
    metrics_list = [{"label": row[0], "value": str(row[1]), "change": ""} for row in metrics_query.fetchall()]
        
    report_query = await db.execute(
        text("SELECT ai_markdown_analysis FROM reports WHERE competitor_id = :id ORDER BY created_at DESC LIMIT 1"),
        {"id": competitor_id}
    )
    report_row = report_query.fetchone()
    latest_report_md = report_row[0] if report_row else "No Report Found. Run an analysis first."

    return {
        "id": competitor.id,
        "name": competitor.name,
        "domain": getattr(competitor, "website", "N/A"),
        "metrics": metrics_list,
        "report": latest_report_md
    }

# DELETE: Fully converted to async
@router.delete("/{competitor_id}")
async def delete_competitor(competitor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Competitor).where(Competitor.id == competitor_id))
    competitor = result.scalar_one_or_none()
    
    if not competitor:
        raise HTTPException(status_code=404, detail="Competitor not found")
        
    await db.delete(competitor)
    await db.commit()
    return {"message": "Competitor deleted successfully"}