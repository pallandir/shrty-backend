from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from app.database import Base


class URLORM(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(unique=True)
    mapped_url: Mapped[str] = mapped_column()
    visited: Mapped[int] = mapped_column(nullable=True)
    last_visit: Mapped[date] = mapped_column(nullable=True)
    last_update: Mapped[date] = mapped_column(nullable=True)
