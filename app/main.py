from __future__ import annotations

from numbers import Number
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _other_km(self, other: Union["Distance", float]) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, Number):
            return other
        raise TypeError(
            f"Unsupported operand type: {type(other)}"
        )

    def __add__(self, other: Union["Distance", float]) -> "Distance":
        return Distance(self.km + self._other_km(other))

    def __iadd__(self, other: Union["Distance", float]) -> "Distance":
        self.km += self._other_km(other)
        return self

    def __mul__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError(
                "Cannot multiply Distance by Distance"
            )
        return Distance(self.km * self._other_km(other))

    def __truediv__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError(
                "Cannot divide Distance by Distance"
            )
        return Distance(round(self.km / self._other_km(other), 2))

    def __eq__(self, other: Union["Distance", float]) -> bool:
        return self.km == self._other_km(other)

    def __gt__(self, other: Union["Distance", float]) -> bool:
        return self.km > self._other_km(other)

    def __ge__(self, other: Union["Distance", float]) -> bool:
        return self.km >= self._other_km(other)

    def __lt__(self, other: Union["Distance", float]) -> bool:
        return self.km < self._other_km(other)

    def __le__(self, other: Union["Distance", float]) -> bool:
        return self.km <= self._other_km(other)
