"""Model class for a quote."""

__all__ = ["QuoteModel"]


class QuoteModel:
    """Display models for a quote."""

    def __init__(self, author: str, body: str) -> None:
        """Instantiate a new QuoteModel object."""
        self.author = author
        self.body = body

    def __str__(self) -> str:
        """Return the quote in a string format."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self) -> str:
        """Return the quote in a string format."""
        return f'"{self.body}" - {self.author}'
