import re

from app.ingestion.chunking.base_chunker import BaseChunker
from app.schemas.chunk import Chunk
from app.utils.keyword_extractor import KeywordExtractor


class AcademicChunker(BaseChunker):
    """
    Academic-aware semantic chunker.
    Splits markdown documents into semantic chunks.
    """

    def chunk(
        self,
        markdown: str,
    ) -> list[Chunk]:

        pattern = r"(?=^#{1,6}\s)"

        sections = re.split(
            pattern,
            markdown,
            flags=re.MULTILINE,
        )

        extractor = KeywordExtractor()

        chunks: list[Chunk] = []

        previous_chunk = None

        chunk_id = 1

        for section in sections:

            section = section.strip()

            if not section:
                continue

            lines = section.splitlines()

            heading = None

            if lines and lines[0].startswith("#"):
                heading = lines[0].lstrip("#").strip()

            content = "\n".join(lines).strip()

            chunk = Chunk(
                chunk_id=chunk_id,
                heading=heading,
                subheading=None,
                page=None,
                content=content,
                token_count=len(content.split()),
                word_count=len(content.split()),
                previous_chunk=previous_chunk,
                next_chunk=None,
                parent_chunk=None,
                child_chunks=[],
                related_chunks=[],
                citations=[],
                keywords=extractor.extract(content),
            )

            if chunks:
                chunks[-1].next_chunk = chunk_id

            chunks.append(chunk)

            previous_chunk = chunk_id

            chunk_id += 1

        return chunks