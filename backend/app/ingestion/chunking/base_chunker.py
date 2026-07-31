from abc import ABC, abstractmethod

from app.schemas.chunk import Chunk


class BaseChunker(ABC):

    @abstractmethod
    def chunk(
        self,
        markdown: str,
    ) -> list[Chunk]:
        pass