from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: float | int | Distance) -> Distance:
        if isinstance(other_distance, Distance):
            return Distance(self.km + other_distance.km)
        return Distance(self.km + other_distance)

    def __iadd__(self, other_distance: float | int | Distance) -> Distance:
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
            return self
        self.km += other_distance
        return self

    def __mul__(self, number: float | int) -> Distance:
        new_distance = self.km * number
        return Distance(new_distance)

    def __truediv__(self, number: float | int) -> Distance:
        new_distance = round(self.km / number, 2)
        return Distance(new_distance)

    def __lt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
