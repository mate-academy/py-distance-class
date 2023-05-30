from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if type(other) in (int, float):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if type(other) in (int, float):
            self.km = self.km + other
            return self
        self.km = self.km + other.km
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return (Distance(km=round(self.km / other, 2)))

    def __lt__(self, other: Distance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if type(other) in (int, float):
            return self.km >= other
        return self.km >= other.km


distance1 = Distance(50)
distance2 = Distance(15)
distance1 += distance2
print(distance1)
