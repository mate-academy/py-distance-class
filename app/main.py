from __future__ import annotations


class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> Distance:
        if isinstance(other, type(self)):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance) -> int:
        if isinstance(other, type(self)):
            self.km = self.km + other.km
            return self
        elif isinstance(other, (int, float)):
            self.km = self.km + other
            return self

    def __mul__(self, other: (int, float)) -> int:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: (int, float)) -> int:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, type(self)):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, type(self)):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, type(self)):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, type(self)):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, type(self)):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
