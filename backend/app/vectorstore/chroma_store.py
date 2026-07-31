import chromadb

from app.core.logging import logger
from app.core.settings import settings


class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(settings.chroma_path)
        )

        self.collection = self.client.get_or_create_collection(
            name="vidyai_documents"
        )

    def add(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.success(
            f"Inserted {len(ids)} chunks into ChromaDB."
        )

    def search(
        self,
        query_embedding,
        top_k=5,
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )