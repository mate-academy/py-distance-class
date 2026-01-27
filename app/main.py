from __future__ import annotations

from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: Number = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Union[Distance, Number]) -> Union[Number, object]:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km + other_km)  # type: ignore[operator]

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        self.km = self.km + other_km  # type: ignore[operator]
        return self

    def __mul__(self, other: Number) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km * other)  # type: ignore[operator]

    def __truediv__(self, other: Number) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        result = round(self.km / other, 2)  # type: ignore[operator]
        return Distance(result)

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km < other_km  # type: ignore[operator]

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km > other_km  # type: ignore[operator]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: Union[Distance, Number]) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km <= other_km  # type: ignore[operator]

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented  # type: ignore[return-value]
        return self.km >= other_km  # type: ignore[operator]
