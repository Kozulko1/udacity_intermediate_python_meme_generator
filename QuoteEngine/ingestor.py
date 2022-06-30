"""Module for ingesting all allowed files."""

from pathlib import Path
from typing import List

from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .ingestor_interface import IngestorInterface
from .pdf_ingestor import PDFIngestor
from .quote_model import QuoteModel
from .txt_ingestor import TXTIngestor


__all__ = ["Ingestor"]


class Ingestor(IngestorInterface):
    """Ingestor for all supported file types."""

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse a .csv, .docx, .pdf or .txt file."""
        if not cls.can_ingest(path):
            raise NotImplementedError(
                "There are no implemented parsers for provided file type."
            )
        file_extension = str(path).split(".")[-1]
        if file_extension == "csv":
            return CSVIngestor.parse(path)
        if file_extension == "docx":
            return DOCXIngestor.parse(path)
        if file_extension == "pdf":
            return PDFIngestor.parse(path)
        if file_extension == "txt":
            return TXTIngestor.parse(path)
