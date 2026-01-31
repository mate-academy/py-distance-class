from __future__ import annotations
from typing import Union


Number = Union[int, float]


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Union[Distance, Number]) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: Number) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == self._get_km(other)

    def __le__(self, other: Union[Distance, Number]) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        return self.km >= self._get_km(other)
