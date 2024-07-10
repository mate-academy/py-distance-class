from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km!r})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km * other)

    def __truediv__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __lt__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __le__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __gt__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __ge__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
