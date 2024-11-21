from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, (float, int)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, (float, int)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, (float, int)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, (float, int)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | float | int) -> bool:
        return self < other or self == other

    def __ge__(self, other: Distance | float | int) -> bool:
        return self > other or self == other
