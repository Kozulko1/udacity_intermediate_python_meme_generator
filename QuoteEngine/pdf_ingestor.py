"""Module for ingesting pdf files."""

import subprocess

from pathlib import Path
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .txt_ingestor import TXTIngestor


__all__ = ["PDFIngestor"]


class PDFIngestor(IngestorInterface):
    """Ingestor for .pdf files."""

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse a .pdf file."""
        temp_txt_file = Path("./tmp.txt")
        command = f"pdftotext -layout -nopgbrk {path} {temp_txt_file}"
        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)
        output = TXTIngestor.parse(temp_txt_file)
        Path.unlink(temp_txt_file)
        return output
