from sentence_transformers import SentenceTransformer

from app.core.settings import settings
from app.embeddings.base_embedding import BaseEmbedding
from app.infrastructure.interfaces.embedding_provider import (
    EmbeddingProvider,
)

class BGEM3Embedding(EmbeddingProvider):

    def __init__(self):

        self.model = SentenceTransformer(
            settings.embedding_model
        )

    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

        return embeddings.tolist()