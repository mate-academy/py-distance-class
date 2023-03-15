from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, Distance):
            return Distance(other * self.km)

    def __truediv__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, Distance):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
