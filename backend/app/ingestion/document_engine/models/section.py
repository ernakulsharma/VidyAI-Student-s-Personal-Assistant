"""
Section model.
"""

from __future__ import annotations

from pydantic import Field

from .base import BaseDocumentNode
from .figure import Figure
from .paragraph import Paragraph
from .table import Table


class Section(BaseDocumentNode):

    title: str

    level: int = Field(
        ...,
        ge=1
    )

    parent_id: str | None = None

    page_start: int = Field(
        ...,
        ge=1
    )

    page_end: int = Field(
        ...,
        ge=1
    )

    paragraphs: list[Paragraph] = Field(
        default_factory=list
    )

    tables: list[Table] = Field(
        default_factory=list
    )

    figures: list[Figure] = Field(
        default_factory=list
    )

    children: list["Section"] = Field(
        default_factory=list
    )

    def add_paragraph(self, paragraph: Paragraph):
        self.paragraphs.append(paragraph)

    def add_table(self, table: Table):
        self.tables.append(table)

    def add_figure(self, figure: Figure):
        self.figures.append(figure)

    def add_child(self, child: "Section"):
        child.parent_id = self.id
        self.children.append(child)


Section.model_rebuild()