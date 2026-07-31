from abc import ABC, abstractmethod


class BaseEmbedding(ABC):

    @abstractmethod
    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for a list of texts.
        """
        pass