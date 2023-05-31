from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if type(other) == int or type(other) == float:
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int) -> Distance:
        if type(other) == int or type(other) == float:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: Distance | float) -> bool:
        if isinstance(other, float) or isinstance(other, int):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | float) -> bool:
        if isinstance(other, float) or isinstance(other, int):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | float) -> bool:
        if isinstance(other, float) or isinstance(other, int):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | float) -> bool:
        return not (self > other)

    def __ge__(self, other: Distance | float) -> bool:
        return not (self < other)
