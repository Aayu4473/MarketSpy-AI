from datetime import datetime, timezone
from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Report(Base):
    __tablename__= "reports"
    id: Mapped[int]= mapped_column(primary_key=True, index=True)

    competitor_id: Mapped[int]=mapped_column(ForeignKey("competitors.id", ondelete="CASCADE"), nullable=False)

    # 2. Core Payload Attributes
    target_url: Mapped[str] = mapped_column(String(500), nullable=False)
    # Text type allows for large, unrestricted multi-paragraph markdown analysis text strings
    ai_markdown_analysis: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

    competitor = relationship("Competitor", back_populates="reports")