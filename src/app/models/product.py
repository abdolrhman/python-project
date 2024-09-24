import uuid as uuid_pkg
from datetime import UTC, datetime
from sqlalchemy import DateTime, String, Numeric, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .category import category_products
from ..core.db.database import Base

class Product(Base):
    __tablename__ = "product"

    # Non-default fields
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    # Relationships
    categories: Mapped[list["Category"]] = relationship(
        "Category", secondary=category_products, back_populates="products", init=False
    )
    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="product", cascade="all, delete-orphan", init=False)

    # Default fields
    id: Mapped[uuid_pkg.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default_factory=uuid_pkg.uuid4, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
