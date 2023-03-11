from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int or float or Distance) -> Distance:
        if type(other) == int or type(other) == float:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: int or float or Distance) -> Distance:
        if type(other) == int or type(other) == float:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int or float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        if other != 0:
            self.km = round(self.km / other, 2)
            return self
        else:
            return ZeroDivisionError

    def __lt__(self, other: int or float or Distance) -> bool:
        if type(other) == int or type(other) == float:
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: int or float or Distance) -> bool:
        if type(other) == int or type(other) == float:
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: int or float or Distance) -> bool:
        if type(other) == int or type(other) == float:
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: int or float or Distance) -> bool:
        if type(other) == int or type(other) == float:
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: int or float or Distance) -> bool:
        if type(other) == int or type(other) == float:
            return self.km >= other
        else:
            return self.km >= other.km
