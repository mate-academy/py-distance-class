
from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Distance | int) -> Distance:
        value_to_add = other.km if isinstance(other, Distance) else other
        return Distance(value_to_add + self.km)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: Distance | int) -> Distance:
        value_to_add = other.km if isinstance(other, Distance) else other
        self.km += value_to_add
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __le__(self, other: int | float | Distance) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __eq__(self, other: int | float | Distance) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __ge__(self, other: int | float | Distance) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km

    def __gt__(self, other: int | float | Distance) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km
