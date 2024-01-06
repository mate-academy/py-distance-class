from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
            self, other: Distance | int | float
    ) -> Distance:
        if isinstance(other, int | float):
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(
            self, other: Distance | float | int
    ) -> Distance:
        if isinstance(other, int | float):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: float | int) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: float | int) -> Distance:
        if other != 0:
            self.km = round(self.km / other, 2)
            return self

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int | float):
            return self.km >= other
        return self.km >= other.km
