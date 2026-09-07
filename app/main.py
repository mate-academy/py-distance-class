from __future__ import annotations
from typing import Union


class Distance:
    """A class to represent a distance in kilometers."""

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def _get_km(self, other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        other_km = self._get_km(other)
        return Distance(self.km + other_km)

    def __radd__(self, other: Union[int, float]) -> "Distance":
        return Distance(self.km + other)

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot multiply Distance by Distance")
        return Distance(self.km * other)

    def __rmul__(self, other: int | float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("Cannot divide Distance by Distance")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == self._get_km(other)
        return NotImplemented

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= self._get_km(other)
