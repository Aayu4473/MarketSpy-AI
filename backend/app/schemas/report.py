from pydantic import BaseModel
from datetime import datetime
from pydantic import HttpUrl

class ReportBase(BaseModel):
    competitor_id: int
    target_url: str
    ai_markdown_analysis: str

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    created_At: datetime

    class Config:
        from_attributes=True
