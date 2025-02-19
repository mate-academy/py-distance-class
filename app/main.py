from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            km = self.km + other.km
        elif isinstance(other, (int, float)):
            km = self.km + other
        else:
            raise TypeError("Unsupported type for addition")
        return Distance(km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for in-place addition")
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

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
