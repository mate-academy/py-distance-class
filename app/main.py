from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.km if isinstance(other, Distance) else other
        return self
