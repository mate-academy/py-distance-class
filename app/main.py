from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def validate(other: int | float | Distance) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"Unsupported type for operation: {type(other)}")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km + self.validate(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self.validate(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance instance is not supported")
        return Distance(self.km * self.validate(other))

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance instance is not supported")
        return Distance(round(self.km / self.validate(other), 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.validate(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.validate(other)
