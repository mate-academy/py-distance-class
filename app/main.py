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

    def __add__(self, other: object) -> int | float | Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __iadd__(self, other: object) -> int | float | Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, number: int) -> int | float | Distance:
        return Distance(self.km * number)

    def __truediv__(self, other: int) -> int | float | Distance:
        return Distance(round((self.km / other), 2))

    def __eq__(self, other: object) -> bool:
        return self.km == other

    def __lt__(self, other: object) -> bool:
        return self.km < other
