from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            result = other.km + self.km
        result = other + self.km
        self.km = result
        return self

    def __mul__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            result = self.km * other.km
        result = self.km * other
        return Distance(result)

    def __truediv__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            result = self.km / other.km
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
