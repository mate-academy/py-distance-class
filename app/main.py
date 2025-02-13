from __future__ import annotations, division


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        if self.km < other:
            return True
        return False

    def __gt__(self, other: int | float) -> bool:
        if self.km > other:
            return True
        return False

    def __eq__(self, other: int | float) -> bool:
        if self.km == other:
            return True
        return False

    def __le__(self, other: int | float) -> bool:
        if self.km <= other:
            return True
        return False

    def __ge__(self, other: int | float) -> bool:
        if self.km >= other:
            return True
        return False
