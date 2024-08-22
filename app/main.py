from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km
        self.real = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(self.km + other.real)

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km += other.real
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < other.real

    def __gt__(self, other: Distance) -> bool:
        return self.km > other.real

    def __eq__(self, other: Distance) -> bool:
        return self.km == other.real

    def __le__(self, other: Distance) -> bool:
        return self.km <= other.real

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other.real
