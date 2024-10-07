from __future__ import annotations

from functools import total_ordering


@total_ordering
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
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        if other != 0:
            return Distance(round(self.km / other, 2))
        raise ValueError("Cannot divide by zero.")

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other
