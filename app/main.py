from __future__ import annotations
from typing import Any
from types import NotImplementedType


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def _get_other_km(self, other: Any) -> float | int | NotImplementedType:
        """Helper to get km from another object or number."""
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(
        self, other: Distance | int | float
    ) -> bool | NotImplementedType:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(
        self, other: Distance | int | float
    ) -> bool | NotImplementedType:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: object) -> bool | NotImplementedType:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __le__(
        self, other: Distance | int | float
    ) -> bool | NotImplementedType:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(
        self, other: Distance | int | float
    ) -> bool | NotImplementedType:
        other_km = self._get_other_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
