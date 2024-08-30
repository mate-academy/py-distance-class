from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def _instancecheck(other: distance) -> (int | float):
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        raise TypeError()

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: distance) -> Distance:
        return Distance(self.km + self._instancecheck(other))

    def __iadd__(self, other: distance) -> Distance:
        self.km += self._instancecheck(other)
        return self

    def __mul__(self, other: (int | float)) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: (int | float)) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: distance) -> bool:
        return self.km < self._instancecheck(other)

    def __gt__(self, other: distance) -> bool:
        return self.km > self._instancecheck(other)

    def __eq__(self, other: distance) -> bool:
        return self.km == self._instancecheck(other)

    def __le__(self, other: distance) -> bool:
        return self.km <= self._instancecheck(other)

    def __ge__(self, other: distance) -> bool:
        return self.km >= self._instancecheck(other)


distance = Union[Distance, int, float]  # It won't work in the start of the app
