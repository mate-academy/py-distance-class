from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: Distance | float) -> Distance:
        if isinstance(other_distance, Distance):
            return Distance(self.km + other_distance.km)
        return Distance(self.km + other_distance)

    def __iadd__(self, other_distance: Distance | float) -> Distance:
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
        else:
            self.km += other_distance
        return self

    def __mul__(self, multiplier: float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divider: float) -> Distance:
        return Distance(round(self.km / divider, 2))

    def __lt__(self, other_distance: Distance | float) -> bool:
        if isinstance(other_distance, Distance):
            return self.km < other_distance.km
        return self.km < other_distance

    def __gt__(self, other_distance: Distance | float) -> bool:
        if isinstance(other_distance, Distance):
            return self.km > other_distance.km
        return self.km > other_distance

    def __eq__(self, other_distance: Distance | float) -> bool:
        if isinstance(other_distance, Distance):
            return self.km == other_distance.km
        return self.km == other_distance

    def __le__(self, other_distance: Distance | float) -> bool:
        if isinstance(other_distance, Distance):
            return self.km <= other_distance.km
        return self.km <= other_distance

    def __ge__(self, other_distance: Distance | float) -> bool:
        if isinstance(other_distance, Distance):
            return self.km >= other_distance.km
        return self.km >= other_distance
