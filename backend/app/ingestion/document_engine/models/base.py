"""
Base model for all document objects.
"""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class BaseDocumentNode(BaseModel):
    """
    Base class inherited by every document element.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier."
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata."
    )