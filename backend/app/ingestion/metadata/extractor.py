from pathlib import Path

from app.schemas.extracted_metadata import ExtractedMetadata


class MetadataExtractor:
    """
    Extract metadata from a parsed document.
    """

    def extract(
        self,
        document,
        original_file: Path,
    ) -> ExtractedMetadata:

        markdown = document.export_to_markdown()

        words = len(markdown.split())

        reading_time = max(
            1,
            words // 200,
        )

        return ExtractedMetadata(
            title=original_file.stem,
            words=words,
            reading_time=reading_time,
        )