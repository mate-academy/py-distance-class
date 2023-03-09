from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self: float) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: float) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> Distance:
        if type(other) == float:
            return Distance(self.km + other)
        elif type(other) == int:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: float) -> Distance:
        if type(other) == float:
            self.km += other
        elif type(other) == int:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float) -> bool:
        return self.km < other

    def __gt__(self, other: float) -> bool:
        return self.km > other

    def __eq__(self, other: float) -> bool:
        return self.km == other

    def __le__(self, other: float) -> bool:
        return self.km <= other

    def __ge__(self, other: float) -> bool:
        return self.km >= other
