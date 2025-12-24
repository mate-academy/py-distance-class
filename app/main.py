from __future__ import annotations, division


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, int | float):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, int | float):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> Distance:
        rounded_distance = round((self.km / other), 2)
        return Distance(km=rounded_distance)

    def __lt__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, int | float):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, int | float):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, int | float):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, int | float):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        if not isinstance(other, int | float):
            return self.km >= other.km
        return self.km >= other
