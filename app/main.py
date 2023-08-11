from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance | int | float:
        if not isinstance(other, Distance):
            return Distance(self.km + other)

        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance | int | float:
        if not isinstance(other, Distance):
            self.km += other
            return self

        self.km += other.km
        return self

    def __mul__(self, number: Distance | int | float) -> Distance | int | float:
        self.km *= number
        return self

    def __truediv__(self, number: Distance | int | float) -> Distance | int | float:
        self.km = round(self.km / number, 2)
        return self

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return True if self.km < other else False

        return True if self.km < other.km else False

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return True if self.km > other else False

        return True if self.km > other.km else False

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return True if self.km == other else False

        return True if self.km == other.km else False

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return True if self.km <= other else False

        return True if self.km <= other.km else False

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return True if self.km >= other else False

        return True if self.km >= other.km else False
