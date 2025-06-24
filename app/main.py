from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: int) -> Distance:
        self.km = round(self.km / other, 2)
        return self

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other
