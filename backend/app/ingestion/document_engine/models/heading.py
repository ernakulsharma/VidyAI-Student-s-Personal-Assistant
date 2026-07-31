"""
Heading model.
"""

from pydantic import Field

from .base import BaseDocumentNode


class HeadingNode(BaseDocumentNode):

    title: str

    level: int = Field(
        ...,
        ge=1
    )

    page_number: int = Field(
        ...,
        ge=1
    )

    parent_id: str | None = None