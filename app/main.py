from __future__ import annotations


class Distance:

    def __init__(self, km: (float | int)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (Distance | int | float)) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (float, int)):
            return Distance(self.km + other)

    def __iadd__(self, other: (Distance | int | float)) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        if isinstance(other, (float, int)):
            self.km = self.km + other
        return self

    def __mul__(self, num: (float | int)) -> Distance:
        return Distance(self.km * num)

    def __truediv__(self, num: (float | int)) -> Distance:
        if num != 0:
            return Distance(round(self.km / num, 2))
        else:
            raise ZeroDivisionError(f"num = {num} zero division error")

    def __lt__(self, other: (Distance | int | float)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (float, int)):
            return self.km < other

    def __le__(self, other: (Distance | int | float)) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (float, int)):
            return self.km <= other

    def __gt__(self, other: (Distance | int | float)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (float, int)):
            return self.km > other

    def __ge__(self, other: (Distance | int | float)) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (float, int)):
            return self.km >= other

    def __eq__(self, other: (Distance | int | float)) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (float, int)):
            return self.km == other
