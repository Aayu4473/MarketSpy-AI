from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Master Metadata Registry for SQLAlchemy 2.0.
    All enterprise database models (Competitors, Reports, Metrics) 
    will inherit from this Base class so they are auto-indexed by the ORM engine.
    """
    pass