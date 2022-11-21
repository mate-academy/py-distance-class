from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if other.__class__ is Distance:
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if other.__class__ is Distance:
            self.km = self.km + other.km
            return self
        self.km = self.km + other
        return self

    def __mul__(self, mul: int) -> Distance:
        return Distance(self.km * mul)

    def __truediv__(self, div: int) -> Distance:
        return Distance(round(self.km / div, 2))

    def __lt__(self, distance: Distance | float | int) -> bool:
        if distance.__class__ is Distance:
            return self.km < distance
        return self.km < distance

    def __gt__(self, distance: Distance | float | int) -> bool:
        if distance.__class__ is Distance:
            return self.km > distance
        return self.km > distance

    def __eq__(self, distance: Distance | float | int) -> bool:
        if distance.__class__ is Distance:
            return self.km == distance
        return self.km == distance

    def __le__(self, distance: Distance | float | int) -> bool:
        if distance.__class__ is Distance:
            return self.km <= distance
        return self.km <= distance

    def __ge__(self, distance: Distance | float | int) -> bool:
        if distance.__class__ is Distance:
            return self.km >= distance
        return self.km >= distance

    def __len__(self) -> float:
        return self.km


distance1 = Distance(20)
distance2 = distance1 / 7
print(distance1.__repr__())
