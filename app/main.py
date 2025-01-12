from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        elif isinstance(other, int) or isinstance(other, float):
            self.km = self.km + other
        return self

    def __mul__(self, multiply: int) -> Distance:
        return Distance((self.km * multiply))

    def __truediv__(self, divider: int) -> Distance:
        return Distance(round((self.km / divider), 2))

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km < other

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km > other

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km == other

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km <= other

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km >= other
