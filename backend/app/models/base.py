from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Master Metadata Registry for SQLAlchemy 2.0.
    All enterprise database models (Competitors, Reports, Metrics) 
    will inherit from this Base class so they are auto-indexed by the ORM engine.
    """
    pass

# 2. Import all your models here so SQLAlchemy registers them onto the Base metadata
# This solves the 'failed to locate a name' 500 error!
from app.models.competitor import Competitor
from app.models.report import Report
from app.models.metrics import Metrics