from datetime import UTC, datetime

from app.core.logging import logger
from app.ingestion.parsers.docling_parser import DoclingParser
from app.ingestion.pipeline_context import PipelineContext
from app.ingestion.stages.base_stage import BaseStage
from app.services.storage_service import StorageService
from app.ingestion.document_engine.analyzers.structure_analyzer import (
    StructureAnalyzer,
)
from pprint import pprint

class ParsingStage(BaseStage):
    """
    Parses the uploaded document using Docling.
    """

    def __init__(self):
        self.parser = DoclingParser()
        self.storage = StorageService()
        self.structure = StructureAnalyzer()

    def process(
        self,
        context: PipelineContext,
    ) -> None:

        logger.info(
            f"Parsing document: {context.document_path.name}"
        )

        parsed = self.parser.parse(
            context.document_path
        )

        context.parsed_document = parsed["document"]
        print(type(context.parsed_document))
        print(dir(context.parsed_document))

        pprint(vars(context.parsed_document))

        context.markdown = parsed["markdown"]

        doc = context.parsed_document

        print("\n" + "=" * 80)
        print("DOCLING DOCUMENT TYPE")
        print("=" * 80)
        print(type(doc))

        print("\n" + "=" * 80)
        print("AVAILABLE ATTRIBUTES")
        print("=" * 80)
        print(dir(doc))

        print("\n" + "=" * 80)
        print("DOCUMENT REPRESENTATION")
        print("=" * 80)

        try:
            pprint(vars(doc))
        except Exception:
            print(doc)

        self.storage.save_markdown(
            context.markdown,
            context.workspace,
        )

        # Update manifest
        context.manifest.parsing.completed = True
        context.manifest.parsing.timestamp = datetime.now(UTC)
        context.manifest.parsing.version = "docling"

        self.storage.update_manifest(
            context.manifest,
            context.workspace,
        )

        self.structure.analyze(
            context,
        )

        logger.success(
            "Parsing stage completed."
        )