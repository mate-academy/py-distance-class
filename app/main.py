from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | float) -> Distance:
        if isinstance(other, (float, int)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km

        return self

    def __mul__(self, num: float) -> Distance:
        return Distance(self.km * num)

    def __truediv__(self, num: float) -> Distance:
        return Distance(round(self.km / num, 2))

    def __lt__(self, other: Distance | float) -> bool:
        if isinstance(other, (float, int)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: Distance | float) -> bool:
        if isinstance(other, (float, int)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: Distance | float) -> bool:
        if isinstance(other, (float, int)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: Distance | float) -> bool:
        if isinstance(other, (float, int)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: Distance | float) -> bool:
        if isinstance(other, (float, int)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
