from __future__ import annotations


class Distance:
    def __init__(self, km: float = 0.0) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> Distance:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return Distance(km=self.km + new_distance.km)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, number: int) -> Distance:
        new_distance = Distance(self.km * number)
        return new_distance

    def __truediv__(self, number: float) -> Distance:
        new_distance = Distance(round(self.km / number, 2))
        return new_distance

    def __lt__(self, other: float) -> bool:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return self.km < new_distance.km
        return self.km < other.km

    def __gt__(self, other: float) -> bool:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return self.km > new_distance.km
        return self.km > other.km

    def __eq__(self, other: float) -> bool:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return self.km == new_distance.km
        return self.km == other.km

    def __le__(self, other: float) -> bool:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return self.km <= new_distance.km
        return self.km <= other.km

    def __ge__(self, other: float) -> bool:
        if not isinstance(other, Distance):
            new_distance = Distance(km=other)
            return self.km >= new_distance.km
        return self.km >= other.km
