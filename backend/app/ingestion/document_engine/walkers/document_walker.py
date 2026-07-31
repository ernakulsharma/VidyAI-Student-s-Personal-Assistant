"""
Document Walker.

Provides a unified iterator over a DoclingDocument.
All document analyzers should consume document elements
through this class instead of accessing Docling directly.
"""

from __future__ import annotations

from collections.abc import Iterator

from app.core.logging import logger


class DocumentWalker:
    """
    Walks through a DoclingDocument and yields
    document items in reading order.
    """

    def __init__(self, document):
        self.document = document

    def walk(self) -> Iterator:
        """
        Iterate over every document element.

        Yields
        ------
        tuple
            (item, level)
        """

        logger.info("Walking parsed document...")

        for item, level in self.document.iterate_items():

            yield item, level

        logger.success("Document walk completed.")