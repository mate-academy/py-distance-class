from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int) -> Distance:
        self.km = self + other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: int) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: int) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: int) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: int) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km
