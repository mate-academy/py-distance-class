from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Distance) -> str:
        return f"Distance(km={self.km})"

    def __add__(self: Distance, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(
            km=self.km + other_km
        )

    def __iadd__(self: Distance, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        self.km = self.km + other_km
        return self

    def __mul__(self: Distance, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self: Distance, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self: Distance, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self: Distance, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self: Distance, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self: Distance, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self: Distance, other: Distance | int | float) -> bool:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
