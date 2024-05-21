from __future__ import annotations
from typing import Union


class Distance:
    Number = Union[int, float]

    def __init__(self, km: Number) -> None:
        self.km = km

    @staticmethod
    def get_type(other: Number | Distance) -> Number:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        raise TypeError(f"Unsupported type: {type(other)}")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Number | Distance) -> Distance:
        return Distance(self.km + self.get_type(other))

    def __iadd__(self, other: Number | Distance) -> Distance:
        self.km += self.get_type(other)
        return self

    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(
                "'__mul__' method should not accept Distance instances"
            )
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(
                "'__truediv__' method should not accept Distance instances"
            )
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Number) -> bool:
        return self.km < self.get_type(other)

    def __gt__(self, other: Number) -> bool:
        return self.km > self.get_type(other)

    def __eq__(self, other: Number) -> bool:
        return self.km == self.get_type(other)

    def __le__(self, other: Number) -> bool:
        return self.km <= self.get_type(other)

    def __ge__(self, other: Number) -> bool:
        return self.km >= self.get_type(other)
