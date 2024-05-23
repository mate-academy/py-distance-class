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
            total = self.km + other.km
        elif isinstance(other, (int, float)):
            total = self.km + other
        return Distance(total)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            total = self.km * other
            return Distance(total)
        else:
            raise TypeError("unsupport")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            total = self.km / other
            return Distance(round(total, 2))
        else:
            raise TypeError("unsupport")

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km

        elif isinstance(other, (int, float)):
            return self.km >= other
