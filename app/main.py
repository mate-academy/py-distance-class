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

    def _extract_km(self, other: object) -> int | float | None:
        """Extract kilometer value from a Distance object or number."""
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return None

    def __add__(self, other: object) -> Distance:
        """Add another Distance or number to this distance."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: object) -> Distance:
        """Add another Distance or number in-place."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        """Multiply distance by a numeric scalar."""
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        """Divide distance by a scalar, rounded to 2 decimals."""
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """Check equality against a Distance or number."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other: object) -> bool:
        """Check strictly less than against a Distance or number."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: object) -> bool:
        """Check strictly greater than against a Distance or number."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return self.km > other_km

    def __le__(self, other: object) -> bool:
        """Check less than or equal against a Distance or number."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: object) -> bool:
        """Check greater than or equal against a Distance or number."""
        other_km = self._extract_km(other)
        if other_km is None:
            return NotImplemented
        return self.km >= other_km