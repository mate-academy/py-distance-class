from __future__ import annotations
from typing import TypeAlias, SupportsFloat


DistAnnot: TypeAlias = "Distance | SupportsFloat"


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: DistAnnot) -> Distance:
        return Distance(self.km + self.instance(other))

    def __iadd__(self, other: DistAnnot) -> Distance:
        self.km += self.instance(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: DistAnnot) -> bool:
        return self.km < self.instance(other)

    def __gt__(self, other: DistAnnot) -> bool:
        return self.km > self.instance(other)

    def __eq__(self, other: DistAnnot) -> bool:
        return self.km == self.instance(other)

    def __le__(self, other: DistAnnot) -> bool:
        return self.km <= self.instance(other)

    def __ge__(self, other: DistAnnot) -> bool:
        return self.km >= self.instance(other)

    @staticmethod
    def instance(value: DistAnnot) -> float:
        return value.km if isinstance(value, Distance) else value
