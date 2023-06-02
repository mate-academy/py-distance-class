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
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other

        return self

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            res = Distance(self.km * other.km)
        else:
            res = Distance(self.km * other)

        return res

    def __truediv__(self, other: int | Distance) -> Distance:
        if isinstance(other, Distance):
            res = Distance(round(self.km / other.km, 2))
        else:
            res = Distance(round(self.km / other, 2))

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            res = self.km < other.km
        else:
            res = self.km < other

        return res

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= other

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            res = self.km > other.km
        else:
            res = self.km > other

        return res

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            res = self.km >= other.km
        else:
            res = self.km >= other

        return res

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            res = self.km == other.km
        else:
            res = self.km == other

        return res
