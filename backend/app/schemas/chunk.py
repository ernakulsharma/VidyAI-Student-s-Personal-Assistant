from pydantic import BaseModel, Field


class Chunk(BaseModel):
    """
    Represents a semantic knowledge unit.
    """

    chunk_id: int

    heading: str | None = None

    subheading: str | None = None

    page: int | None = None

    content: str

    token_count: int

    word_count: int

    previous_chunk: int | None = None
    next_chunk: int | None = None

    parent_chunk: int | None = None

    child_chunks: list[int] = Field(default_factory=list)

    related_chunks: list[int] = Field(default_factory=list)

    citations: list[str] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)