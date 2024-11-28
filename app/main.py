from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km
