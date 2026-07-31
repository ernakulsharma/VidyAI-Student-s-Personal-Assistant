from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    """
    Base interface for all embedding providers.
    """

    @abstractmethod
    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """
        pass