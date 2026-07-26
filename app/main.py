from __future__ import annotations


class Distance:
    """Represent a daily running distance in kilometers."""

    def __init__(self, km: int | float) -> None:
        """Initialize distance with a value in kilometers."""
        self.km = km

    def __str__(self) -> str:
        """Return informal string representation."""
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """Return formal string representation."""
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        """Add another Distance or number to this distance."""
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        """Add another Distance or number in-place."""
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        """Multiply distance by a numeric scalar."""
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        """Divide distance by a scalar, rounded to 2 decimals."""
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        """Check equality against a Distance or number."""
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: Distance | int | float) -> bool:
        """Check strictly less than against a Distance or number."""
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        """Check strictly greater than against a Distance or number."""
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __le__(self, other: Distance | int | float) -> bool:
        """Check less than or equal against a Distance or number."""
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        """Check greater than or equal against a Distance or number."""
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
