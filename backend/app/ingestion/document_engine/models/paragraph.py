"""
Paragraph model.
"""

from pydantic import Field

from .base import BaseDocumentNode


class Paragraph(BaseDocumentNode):

    text: str = Field(
        ...,
        description="Paragraph text."
    )

    page_number: int = Field(
        ...,
        ge=1,
        description="Page number."
    )

    order: int = Field(
        ...,
        ge=0,
        description="Paragraph order inside section."
    )