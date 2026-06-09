##CRUD FILE VAULT MANAGER
# The Manager's only job is to take approved data from the front door (BOUNCER-SCHEMAS) and 
# carry it down into the secure database.

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.competitor import Competitor
from app.schemas.competitor import CompetitorCreate 

async def create_competitor(db: AsyncSession, competitor_in: CompetitorCreate) -> Competitor:
                                             # VIP PASS having valid data from schemas bouncer
#The Manager then physically unpacks the data from the VIP pass (competitor_in) and 
# places it into the metal box (db_obj):

#Take the name from the VIP pass ➔ Put it in the box's name slot.
#Take the website from the VIP pass ➔ Put it in the box's website slot.

    db_obj= Competitor(
        name=competitor_in.name,
        website=competitor_in.website,
        industry= competitor_in.industry
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

# 🚀 2. READ (ALL): Fetch a complete list of tracked companies
async def get_competitors(db: AsyncSession, skip: int = 0, limit: int = 100):
    # Construct a selective SQL query with pagination boundaries
    statement = select(Competitor).offset(skip).limit(limit)
    result = await db.execute(statement)
    return result.scalars().all() # Return as a clean Python list

# 🚀 3. READ (BY ID): Look up one exact company
async def get_competitor_by_id(db: AsyncSession, competitor_id: int) -> Competitor | None:
    statement= select(Competitor).where(Competitor.id== competitor_id)
    result= await db.execute(statement)
    return result.scalars().first()   # Return the single match or None


