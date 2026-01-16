from __future__ import annotations


class Distance:
    def __init__(self, km: [int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, multiplier: int | float | Distance) -> Distance:
        if isinstance(multiplier, (int, float)):
            return Distance(self.km * multiplier)
        raise TypeError("Can only multiply by int or float")

    def __truediv__(self, divisor: int | float | Distance) -> Distance:
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        raise TypeError("Can only divide by int or float")

    def __lt__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: [int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
