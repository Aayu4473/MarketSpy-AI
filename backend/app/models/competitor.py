from app.models.base import Base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone

class Competitor(Base):
   __tablename__="competitors"

   id: Mapped[int]= mapped_column(primary_key=True, index=True)
   name: Mapped[str]= mapped_column(String(500), nullable=False, unique=True)

   created_at: Mapped[datetime]= mapped_column(
      DateTime(timezone=True),
      default=lambda: datetime.now(timezone.utc),
      onupdate=lambda: datetime.now(timezone.utc)

   )

   reports= relationship("Reports", back_populates="competitor", cascade="all, delete-orphan")
   metrics = relationship("Metrics", back_populates="competitor", cascade="all, delete-orphan")