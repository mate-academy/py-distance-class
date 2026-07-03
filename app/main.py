from __future__ import annotations
from types import NotImplementedType


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Distance | int | float
                ) -> int | float | NotImplementedType:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: Distance | int | float) -> Distance:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(round(self.km + km, 2))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __gt__(self, other: Distance | int | float) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __eq__(self, other: Distance | int | float) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km == km

    def __le__(self, other: Distance | int | float) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __ge__(self, other: Distance | int | float) -> bool:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km
