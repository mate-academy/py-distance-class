from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        self.km += other_km
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        if other != 0:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
