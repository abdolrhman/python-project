from datetime import UTC, datetime
import uuid as uuid_pkg
from sqlalchemy import DateTime, ForeignKey, String, Table, Column, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..core.db.database import Base

category_products = Table(
    'category_products',
    Base.metadata,
    Column('category_id', ForeignKey('category.id'), primary_key=True),
    Column('product_id', ForeignKey('product.id'), primary_key=True)
)

class Category(Base):
    __tablename__ = "category"

    # Non-default fields first
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    # Use a lambda function to delay evaluation of remote_side
    children: Mapped[list["Category"]] = relationship(
        "Category",
        backref="parent",
        remote_side=lambda: [Category.id],
        init=False
    )

    products: Mapped[list["Product"]] = relationship(
        "Product", secondary=category_products, back_populates="categories", init=False
    )

    parent_id: Mapped[uuid_pkg.UUID | None] = mapped_column(ForeignKey("category.id"), nullable=True)

    # Correctly set the default_factory for UUID generation
    id: Mapped[uuid_pkg.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default_factory=uuid_pkg.uuid4, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)