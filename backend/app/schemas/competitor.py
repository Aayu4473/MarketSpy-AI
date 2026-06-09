from pydantic import BaseModel
from typing import Optional

# 🚀 1. THE BASE: The core traits every competitor must have
class CompetitorBase(BaseModel):
    name: str
    website: Optional[str] = None
    industry: Optional[str] = None

# 🚀 2. THE CREATE BOUNCER: What data is REQUIRED to create a new one?
# We inherit from CompetitorBase so we don't have to rewrite 'name', 'website', etc.
class CompetitorCreate(CompetitorBase):
    pass # 'pass' just means "I have the exact same rules as CompetitorBase above"

# 🚀 3. THE RESPONSE FORMAT: What data do we hand back to the user?
class CompetitorResponse(CompetitorBase):
    id: int # When we reply, we MUST include the database ID!

    class Config:
        # This magic line tells Pydantic to read SQLAlchemy database objects seamlessly
        from_attributes = True