from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def type_check(other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            other = other.km
        return other

    def __add__(self, other: Distance | int | float) -> Distance:
        other = Distance.type_check(other)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other = Distance.type_check(other)
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: int | float) -> Distance:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km >= other
