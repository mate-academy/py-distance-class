from __future__ import annotations


def is_distance(other: any) -> bool:
    return isinstance(other, Distance)


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        km = self.km + other.km if is_distance(other) else self.km + other
        return Distance(km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.km if is_distance(other) else other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other.km if is_distance(other) else self.km == other

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other.km if is_distance(other) else self.km > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other.km if is_distance(other) else self.km >= other

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other.km if is_distance(other) else self.km < other

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other.km if is_distance(other) else self.km <= other
