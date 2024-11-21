from __future__ import annotations
from __future__ import division


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __round__(self) -> int:
        return round(self.km)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
