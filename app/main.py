from __future__ import annotations

from types import NotImplementedType
from typing import Union


Number = Union[int, float]
DistanceLike = Union[Number, "Distance"]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
        self, other: DistanceLike
    ) -> Union["Distance", NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: DistanceLike) -> "Distance":
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: Number) -> Union["Distance", NotImplementedType]:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(
        self, other: Number
    ) -> Union["Distance", NotImplementedType]:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(
        self, other: DistanceLike
    ) -> Union[bool, NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(
        self, other: DistanceLike
    ) -> Union[bool, NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: object) -> Union[bool, NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __le__(
        self, other: DistanceLike
    ) -> Union[bool, NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(
        self, other: DistanceLike
    ) -> Union[bool, NotImplementedType]:
        other_km = self._extract_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    def _extract_km(self, other: object) -> Union[Number, NotImplementedType]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented
