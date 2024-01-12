from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            lt = self.km < other.km
        else:
            lt = self.km < other

        return lt

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            eq = self.km == other.km
        else:
            eq = self.km == other

        return eq
