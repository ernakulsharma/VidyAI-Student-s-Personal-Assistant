from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".txt",
    ".md",
}

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB


class DocumentValidator:

    @staticmethod
    def validate(path: Path):

        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        if path.stat().st_size > MAX_FILE_SIZE:
            raise ValueError(
                "Document exceeds maximum allowed size."
            )