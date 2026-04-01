from __future__ import annotations


class Distance:

    def __init__(self, distance: int | float) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if type(other) is Distance:
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if type(other) is Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if type(other) is Distance:
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if type(other) is Distance:
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        if type(other) is Distance:
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        if type(other) is Distance:
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        if type(other) is Distance:
            return self.km >= other.km
        return self.km >= other
