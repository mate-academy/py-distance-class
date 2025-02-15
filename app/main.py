from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Distance:
        ot = other
        if isinstance(other, Distance):
            ot = other.km
        return Distance(self.km + ot)

    def __iadd__(self, other: int) -> Distance:
        ot = other
        if isinstance(other, Distance):
            ot = other.km
        self.km += ot
        return self

    def __mul__(self, other: int) -> Distance:
        if not isinstance(other, (float, int)):
            raise TypeError("Error")
        if isinstance(other, Distance):
            raise TypeError("Error")

        ot = other
        if isinstance(other, Distance):
            ot = other.km
        return Distance(self.km * ot)

    def __truediv__(self, other: float) -> Distance:
        if not isinstance(other, (float, int)):
            raise TypeError
        if isinstance(other, Distance):
            raise TypeError

        ot = other
        if isinstance(other, Distance):
            ot = other.km
        return Distance(round(self.km / ot, 2))

    def __lt__(self, other: int) -> bool:
        ot = other if isinstance(other, (float, int)) else other.km
        return self.km < ot

    def __gt__(self, other: int) -> bool:
        ot = other if isinstance(other, (float, int)) else other.km
        return self.km > ot

    def __eq__(self, other: int) -> bool:
        ot = other if isinstance(other, (float, int)) else other.km
        return self.km == ot

    def __le__(self, other: int) -> bool:
        ot = other if isinstance(other, (float, int)) else other.km
        return self.km <= ot

    def __ge__(self, other: float) -> bool:
        ot = other if isinstance(other, (float, int)) else other.km
        return self.km >= ot
