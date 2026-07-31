"""
Table model.
"""

from pydantic import Field

from .base import BaseDocumentNode


class Table(BaseDocumentNode):

    title: str | None = None

    caption: str | None = None

    markdown: str = ""

    rows: int = Field(
        default=0,
        ge=0
    )

    columns: int = Field(
        default=0,
        ge=0
    )

    page_number: int = Field(
        ...,
        ge=1
    )