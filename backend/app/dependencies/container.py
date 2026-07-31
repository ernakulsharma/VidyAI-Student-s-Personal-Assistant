from functools import lru_cache

from app.embeddings.bge_m3_embedding import BGEM3Embedding
from app.vectorstore.chroma_store import ChromaStore
from app.services.storage_service import StorageService
from app.database.session import SessionLocal

@lru_cache
def get_storage_service():
    return StorageService()


@lru_cache
def get_embedding_service():
    return BGEM3Embedding()


@lru_cache
def get_vector_store():
    return ChromaStore()


def get_db_session():
    """
    Returns a SQLAlchemy database session.
    """
    return SessionLocal()