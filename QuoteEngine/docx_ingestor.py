from docx import Document
from pathlib import Path
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


__all__ = ["DOCXIngestor"]


class DOCXIngestor(IngestorInterface):
    """Ingestor for .docx files."""

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse a .docx file."""
        document = Document(path)
        quotes = []
        for par in document.paragraphs:
            quotes.append(par.text)
        quotes = list(filter(lambda item: len(item.split(" - ")) == 2, quotes))
        return [
            QuoteModel(quote.split(" - ")[1].rstrip("\n"), quote.split(" - ")[0].replace('"', "")) for quote in quotes
        ]
