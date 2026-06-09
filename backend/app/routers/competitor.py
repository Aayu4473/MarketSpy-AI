from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.competitor import CompetitorCreate, CompetitorResponse
from app.crud import competitor as crud_competitor

router=APIRouter(
    prefix="/competitors",
    tags=["Competitors"]
)
 #Create a new competitor
@router.post("/", response_model=CompetitorResponse)
async def create_competitor(
    competitor_in: CompetitorCreate, # The Bouncer checks the incoming data
    db: AsyncSession= Depends(get_db)
):
    # Hand the safe data to the Vault Manager (CRUD)
    return await crud_competitor.create_competitor(db=db, competitor_in=competitor_in)

# GET: Fetch all tracked competitors
@router.get("/", response_model=List[CompetitorResponse])
async def read_competitors(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_db)
):
    # Ask the Vault Manager for the list
    return await crud_competitor.get_competitors(db=db, skip=skip, limit=limit)