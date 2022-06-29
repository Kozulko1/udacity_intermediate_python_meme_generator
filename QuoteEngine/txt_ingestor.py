from pathlib import Path
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


__all__ = ["TXTIngestor"]


class TXTIngestor(IngestorInterface):
    """Ingestor for .txt files."""

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse a .txt file."""
        with open(path) as file:
            quotes = file.readlines()
            quotes = list(filter(lambda item: len(item.split(" - ")) == 2, quotes))
        return [
            QuoteModel(quote.split(" - ")[1].rstrip("\n"), quote.split(" - ")[0].replace('"', "")) for quote in quotes
        ]
