from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance((self.km) * float(other))

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(float(self.km) / float(other), 2))

    def __lt__(self, other: Distance) -> bool:
        return self.km < other

    def __gt__(self, other: Distance) -> bool:
        return self.km > other

    def __eq__(self, other: Distance) -> bool:
        return self.km == other

    def __le__(self, other: Distance) -> bool:
        return self.km <= other

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other
