from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + other.km) \
            if isinstance(other, Distance) else Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Any:
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other.km \
            if isinstance(other, Distance) else self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other.km \
            if isinstance(other, Distance) else self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other.km \
            if isinstance(other, Distance) else self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other.km \
            if isinstance(other, Distance) else self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other.km \
            if isinstance(other, Distance) else self.km >= other
