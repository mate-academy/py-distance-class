from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
            return self
        self.km += other.km
        return self

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, float):
            self.km *= other
            return self
        self.km *= other
        return self

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            self.km = round(self.km / other, 2)
            return self

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return self.km >= other
        return self.km >= other.km
