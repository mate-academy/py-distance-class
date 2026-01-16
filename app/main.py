from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | Distance) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | Distance) -> Distance:
        if isinstance(other, (int, float)):
            other = Distance(other)
        self.km = self + other
        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float, Distance)):
            other = Distance(other)
        return Distance(self.km * other.km)

    def __truediv__(self, other: float | Distance) -> Distance:
        if isinstance(other, (int, float, Distance)):
            other = Distance(other)
        return Distance(round(self.km / other.km, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km > other.km

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km == other.km

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km <= other.km

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            other = Distance(other)
        return self.km >= other.km

    def __len__(self) -> int | float:
        return self.km
