from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __radd__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km + other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        self.km += other
        return self

    def __mul__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km * other)

    def __imul__(self, other: float | int | Distance) -> Distance:
        return self * other

    def __truediv__(self, other: float | int | Distance) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: float | int | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: float | int | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: float | int | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: float | int | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: float | int | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km
