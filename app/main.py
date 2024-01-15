from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def convert_to_real(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + self.convert_to_real(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.convert_to_real(other)
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(km=self.km * multiplier)

    def __truediv__(self, divider: int | float) -> Distance:
        return Distance(km=round(self.km / divider, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.convert_to_real(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.convert_to_real(other)
