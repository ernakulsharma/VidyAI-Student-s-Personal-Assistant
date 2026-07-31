from pydantic import BaseModel


class ExtractedMetadata(BaseModel):
    title: str | None = None

    pages: int | None = None

    headings: int = 0

    tables: int = 0

    figures: int = 0

    references: int = 0

    words: int = 0

    reading_time: int = 0