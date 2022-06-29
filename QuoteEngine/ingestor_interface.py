from abc import ABC
from pathlib import Path
from typing import List

from .quote_model import QuoteModel


__all__ = ["IngestorInterface"]


class IngestorInterface(ABC):
    """Base interface for concrete ingestors."""

    possible_extensions = ["csv", "docx", "pdf", "txt"]

    @classmethod
    def can_ingest(cls, path: Path) -> bool:
        """Check if there are concrete ingestors that can ingest filetype from argument."""
        extension = str(path).split(".")[-1]
        return extension in cls.possible_extensions

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Abstract method for parsing different file types."""
        pass
