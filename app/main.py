from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, type(self)):
            return Distance(self.km + other.km)
        elif isinstance(other, int | float):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, type(self)):
            self.km += other.km
            return self
        elif isinstance(other, int | float):
            self.km += other
            return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float | Distance) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= other
