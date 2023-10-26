from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __lt__(self, other: int) -> bool:
        return True if self.km < other else False

    def __gt__(self, other: int) -> bool:
        return True if self.km > other else False

    def __le__(self, other: int) -> bool:
        return True if self.km <= other else False

    def __ge__(self, other: int) -> bool:
        return True if self.km >= other else False

    def __eq__(self, other: int) -> bool:
        return True if self.km == other else False

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)
