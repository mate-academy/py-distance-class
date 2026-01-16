from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        self.km += other
        return self

    def __mul__(self, scalar: int | float) -> Distance:
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)

    def __truediv__(self, divisor: int | float) -> Distance:
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km >= other
