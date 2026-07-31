from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for every SQLAlchemy model.
    """
    pass


# Import ORM models so SQLAlchemy metadata is populated
from app.database.models import *  # noqa: F401,F403