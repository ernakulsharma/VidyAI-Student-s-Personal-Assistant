"""
Figure model.
"""

from pydantic import Field

from .base import BaseDocumentNode


class Figure(BaseDocumentNode):

    caption: str | None = None

    reference: str | None = None

    page_number: int = Field(
        ...,
        ge=1
    )