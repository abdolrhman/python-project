import uuid
import uuid as uuid_pkg
from datetime import UTC, datetime
from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..core.db.database import Base

from enum import Enum as PyEnum

class ReviewStatus(PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    APPROVED = "approved"
    REJECTED = "rejected"

class Review(Base):
    __tablename__ = "review"

    # Non-default fields
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product.id", ondelete="CASCADE"), nullable=False, type_=UUID(as_uuid=True))

    # Relationship
    product: Mapped["Product"] = relationship("Product", back_populates="reviews")

    # Default fields
    id: Mapped[uuid_pkg.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default_factory=uuid_pkg.uuid4, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    status: Mapped[ReviewStatus] = mapped_column(Enum(ReviewStatus), default=ReviewStatus.PENDING, nullable=False)
