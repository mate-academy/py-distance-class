from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, other: float | int) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        if not isinstance(other, Distance):
            return Distance(float(f"{self.km / other:.2f}"))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other
