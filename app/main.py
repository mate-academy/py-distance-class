from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.extract_distance(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.extract_distance(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.extract_distance(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.extract_distance(other)

    @staticmethod
    def extract_distance(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            other = other.km
        return other
