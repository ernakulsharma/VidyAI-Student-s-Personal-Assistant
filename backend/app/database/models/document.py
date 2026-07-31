from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Document(Base):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    public_id: Mapped[str] = mapped_column(
        String(36),
        unique=True,
        default=lambda: str(uuid4()),
    )

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id"),
    )

    title: Mapped[str] = mapped_column(
        String(255),
    )

    filename: Mapped[str] = mapped_column(
        String(255),
    )

    sha256: Mapped[str] = mapped_column(
        String(64),
        unique=True,
    )

    parser: Mapped[str] = mapped_column(
        String(50),
    )

    status: Mapped[str] = mapped_column(
        String(50),
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    workspace = relationship(
        "Workspace",
        back_populates="documents",
    )