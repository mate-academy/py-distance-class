from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def is_distance(other: Distance | int | float) -> bool:
        return isinstance(other, Distance)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __eq__(self, other: Distance | int | float) -> bool:
        if Distance.is_distance(other):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: Distance | int | float) -> bool:
        if Distance.is_distance(other):
            return self.km < other.km
        return self.km < other

    def __add__(self, other: Distance | int | float) -> Distance:
        if Distance.is_distance(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if Distance.is_distance(other):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))
