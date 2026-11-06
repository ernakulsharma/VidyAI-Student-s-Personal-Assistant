from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(min_length=1, max_length=4000)


class SourceReference(BaseModel):
    document_id: str | None = None
    filename: str
    heading: str | None = None
    chunk_id: int | None = None


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceReference] = Field(default_factory=list)
