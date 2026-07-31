from pathlib import Path

from docling.document_converter import DocumentConverter

from app.core.logging import logger
from app.ingestion.parsers.base import BaseParser


class DoclingParser(BaseParser):
    """
    Parses academic documents using Docling.
    """

    def __init__(self):
        self.converter = DocumentConverter()

    def parse(
        self,
        document_path: Path,
    ) -> dict:

        logger.info(
            f"Parsing document: {document_path.name}"
        )

        result = self.converter.convert(
            str(document_path)
        )

        document = result.document

        markdown = document.export_to_markdown()

        logger.success(
            "Document parsed successfully."
        )

        return {
            "document": document,
            "markdown": markdown,
        }