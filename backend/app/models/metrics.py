from datetime import datetime, timezone
from sqlalchemy import String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Metrics(Base):
    """
    SQLAlchemy Model representing the 'metrics' table.
    Tracks chronological numerical data points for our target entities.
    """
    __tablename__ = "metrics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    # Links this metric to a specific competitor
    competitor_id: Mapped[int] = mapped_column(ForeignKey("competitors.id", ondelete="CASCADE"), nullable=False)

    # Core data points
    metric_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)  # e.g., "pricing", "alexa_rank"
    value: Mapped[float] = mapped_column(Float, nullable=False)                       # Numerical float value

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

    # Relational link back to the competitor parent row
    competitor = relationship("Competitor", back_populates="metrics")