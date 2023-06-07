from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={str(self.km)})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(km=self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(km=round((self.km / other), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        else:
            return self.km >= other.km
