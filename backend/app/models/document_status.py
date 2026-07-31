from enum import Enum


class DocumentStatus(str, Enum):

    UPLOADED = "UPLOADED"

    PARSING = "PARSING"

    PARSED = "PARSED"

    CHUNKING = "CHUNKING"

    INDEXING = "INDEXING"

    READY = "READY"

    FAILED = "FAILED"