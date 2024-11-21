from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
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
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, number: int | float) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> Distance:
        return Distance(round((self.km / number), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | bool) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
