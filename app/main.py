from __future__ import annotations
from __future__ import division
from functools import total_ordering


def to_float(other: float | int | Distance) -> float | int | Distance:
    if isinstance(other, Distance):
        return other.km

    return other


@total_ordering
class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km + to_float(other))

    def __iadd__(self, other: float | int | Distance) -> Distance:
        self.km += to_float(other)
        return self

    def __mul__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int | Distance) -> Distance:
        div = self.km / other
        return Distance(round(div, 2))

    def __eq__(self, other: float | int | Distance) -> bool:
        return self.km == to_float(other)

    def __lt__(self, other: float | int | Distance) -> bool:
        return self.km < to_float(other)
