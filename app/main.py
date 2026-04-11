from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            second_distance = other.km
        else:
            second_distance = other
        return Distance(km=self.km + second_distance)

    def __iadd__(self, other: Distance | int | float) -> Distance:

        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        self.km += other_distance
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:

        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return self.km < other_distance

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return self.km > other_distance

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return self.km <= other_distance

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return self.km >= other_distance

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_distance = other.km
        else:
            other_distance = other
        return self.km == other_distance
