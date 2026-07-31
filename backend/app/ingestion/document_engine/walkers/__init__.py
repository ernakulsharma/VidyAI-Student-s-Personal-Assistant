"""
Document walkers.

Walkers traverse parsed documents and provide a consistent
stream of document elements to downstream analyzers.
"""

from .document_walker import DocumentWalker

__all__ = ["DocumentWalker"]