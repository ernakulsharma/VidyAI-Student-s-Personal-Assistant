from sqlalchemy.orm import Session


class BaseRepository:
    """
    Base repository for all database repositories.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db