from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def conv_num(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.conv_num(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.conv_num(other)

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.conv_num(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.conv_num(other)
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))
