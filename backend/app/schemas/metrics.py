from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricsBase(BaseModel):
    competitor_id: int
    metric_type: str
    value: float
    source_url: Optional[str]= None

class MetricCreate(MetricsBase):
    pass

class MetricResponse(MetricsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes= True 