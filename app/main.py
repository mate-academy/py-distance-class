from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: float) -> Distance:
        self.km = km

    def __eq__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __gt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        self.km = self.km + other
        return self

    def __truediv__(self, number: float) -> Distance:
        return Distance(round(self.km / number, 2))

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __mul__(self, number: float) -> Distance:
        return Distance(self.km * number)
