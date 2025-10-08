from __future__ import annotations
from typing import Union


class Distance:
    """
    A class to represent distance in kilometers, with support for
    arithmetic and comparison operations.
    """

    def __init__(self, km: Union[int, float]) -> None:
        """Initializes a Distance object."""
        self.km = km

    def __str__(self) -> str:
        """Returns a user-friendly string representation."""
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """Returns a developer-friendly, unambiguous string representation."""
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        """Handles addition (distance + other)."""
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        """Handles in-place addition (distance += other)."""
        if isinstance(other, (int, float)):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __mul__(self, other: Union[int, float]) -> Distance:
        """Handles multiplication (distance * number)."""
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Union[int, float]) -> Distance:
        """Handles true division (distance / number)."""
        if isinstance(other, (int, float)):
            result = round(self.km / other, 2)
            return Distance(result)
        return NotImplemented

    def _get_other_km(
        self, other: Union[Distance, int, float]
    ) -> Union[int, float]:
        """Helper method to extract km value for comparisons."""
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(
            "Unsupported operand type(s) for comparison: "
            f"'Distance' and '{type(other).__name__}'"
        )

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        """Handles the less than operator (<)."""
        other_km = self._get_other_km(other)
        return self.km < other_km

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        """Handles the greater than operator (>)."""
        other_km = self._get_other_km(other)
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        """Handles the equality operator (==)."""
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        other_km = self._get_other_km(other)
        return self.km == other_km

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        """Handles the less than or equal to operator (<=)."""
        other_km = self._get_other_km(other)
        return self.km <= other_km

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        """Handles the greater than or equal to operator (>=)."""
        other_km = self._get_other_km(other)
        return self.km >= other_km

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        """Handles the greater than or equal to operator (>=)."""
        other_km = self._get_other_km(other)
        return self.km >= other_km
