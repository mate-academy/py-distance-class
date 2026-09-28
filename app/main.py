from __future__ import annotations
from typing import Any, Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _get_km(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: Any) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: Any) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __le__(self, other: Any) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: Any) -> bool:
        other_km = self._get_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
