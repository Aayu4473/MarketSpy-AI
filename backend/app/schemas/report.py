from pydantic import BaseModel
from datetime import datetime
from pydantic import HttpUrl

class ReportBase(BaseModel):
    competitor_id: int
    target_url: str
   

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes=True
