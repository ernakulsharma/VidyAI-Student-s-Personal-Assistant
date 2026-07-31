from pydantic import BaseModel


class AcademicChunk(BaseModel):
    """
    Production-grade semantic chunk.
    """

    chunk_id: int

    document_id: str

    section_id: int

    heading: str

    level: int

    content: str

    page: int | None = None

    keywords: list[str] = []

    entities: list[str] = []

    previous_chunk: int | None = None

    next_chunk: int | None = None

    parent_section: str | None = None

    token_count: int

    word_count: int