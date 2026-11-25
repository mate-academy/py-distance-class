from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: float | Distance) -> Distance:
        if isinstance(other_distance, Distance):
            total_distance = self.km + other_distance.km
        else:
            total_distance = self.km + other_distance
        return Distance(total_distance)

    def __iadd__(self, other_distance: float | Distance) -> Distance:
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
        else:
            self.km += other_distance
        return self

    def __mul__(self, number: float) -> Distance:
        new_distance = self.km * number
        return Distance(new_distance)

    def __truediv__(self, number: float) -> Distance:
        new_distance = round(self.km / number, 2)
        return Distance(new_distance)

    def __lt__(self, other: float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
