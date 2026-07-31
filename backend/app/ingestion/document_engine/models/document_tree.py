"""
Document tree model.
"""

from pydantic import Field

from .base import BaseDocumentNode
from .section import Section


class DocumentTree(BaseDocumentNode):

    title: str

    sections: list[Section] = Field(
        default_factory=list
    )

    statistics: dict = Field(
        default_factory=dict
    )

    def add_section(self, section: Section):
        self.sections.append(section)

    @property
    def total_sections(self) -> int:
        return len(self.sections)

    @property
    def total_paragraphs(self) -> int:
        return sum(
            len(section.paragraphs)
            for section in self.sections
        )

    @property
    def total_tables(self) -> int:
        return sum(
            len(section.tables)
            for section in self.sections
        )

    @property
    def total_figures(self) -> int:
        return sum(
            len(section.figures)
            for section in self.sections
        )