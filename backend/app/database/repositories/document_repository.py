from sqlalchemy.orm import Session

from app.database.models.document import Document
from app.database.repositories.base_repository import BaseRepository


class DocumentRepository(BaseRepository):
    """
    Handles all database operations
    related to documents.
    """

    def create(self, **kwargs):

        try:

            document = Document(**kwargs)

            self.db.add(document)

            self.db.commit()

            self.db.refresh(document)

            return document

        except Exception as e:

            self.db.rollback()

            import traceback

            traceback.print_exc()

            print("\n=======================")
            print("DATABASE ERROR")
            print("=======================")
            print(type(e))
            print(e)

            raise
    
    def get_by_id(
        self,
        document_id: int,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.id == document_id
            )
            .first()
        )
    
    def get_by_public_id(
        self,
        public_id: str,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.public_id == public_id
            )
            .first()
        )
    
    def get_by_sha256(
        self,
        sha256: str,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.sha256 == sha256
            )
            .first()
        )
    
    def find_by_sha256(
        self,
        sha256: str,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.sha256 == sha256
            )
            .first()
        )
    
    def list_documents(
        self,
    ):

        return (
            self.db.query(Document)
            .all()
        )
    
    def update_status(
        self,
        document: Document,
        status: str,
    ):

        document.status = status

        self.db.commit()

        self.db.refresh(
            document,
        )

        return document
    
    def delete(
        self,
        document: Document,
    ):

        self.db.delete(
            document,
        )

        self.db.commit()