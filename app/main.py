from __future__ import annotations

from types import NotImplementedType


Number = int | float


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> Distance | NotImplementedType:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: object) -> Distance | NotImplementedType:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance can only be multiplied by a number")
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance can only be divided by a number")
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: object) -> bool:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other: object) -> bool:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other: object) -> bool:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __gt__(self, other: object) -> bool:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __ge__(self, other: object) -> bool:
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    @staticmethod
    def _get_number_or_distance(value: object) -> Number | NotImplementedType:
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented
