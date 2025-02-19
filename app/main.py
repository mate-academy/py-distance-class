from __future__ import annotations


class Distance:
    def __init__(self, km: float | int = 0) -> None:
        self.km = km

    def __str__(self) -> str:
        return "Distance: {} kilometers.".format(self.km)

    def __repr__(self) -> str:
        return "Distance(km={})".format(self.km)

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, factor: float | int) -> Distance:
        return Distance(self.km * factor)

    def __truediv__(self, divisor: float | int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
