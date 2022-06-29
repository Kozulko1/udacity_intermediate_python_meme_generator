from pandas import read_csv
from pathlib import Path
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


__all__ = ["CSVIngestor"]


class CSVIngestor(IngestorInterface):
    """Ingestor for .csv files."""

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse a .csv file."""
        file = read_csv(path)
        return [QuoteModel(**line_content) for _, line_content in file.iterrows()]
