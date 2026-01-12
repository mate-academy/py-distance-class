from __future__ import annotations

from typing import Union

Number = Union[int, float, "Distance"]


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _value(self, other: Number) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    def __add__(self, other: Number) -> Distance:
        return Distance(self.km + self._value(other))

    def __iadd__(self, other: Number) -> Distance:
        self.km += self._value(other)
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * float(other))

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if float(other) == 0:
            raise ZeroDivisionError("Distance cannot be divided by zero.")
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other: Number) -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: Number) -> bool:
        return self.km > self._value(other)

    def __eq__(self, other: Number) -> bool:
        return self.km == self._value(other)

    def __le__(self, other: Number) -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: Number) -> bool:
        return self.km >= self._value(other)
