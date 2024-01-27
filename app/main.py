from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_dist: Distance | int | float) -> Distance:
        if isinstance(new_dist, (int, float)):
            new_distance = new_dist
        else:
            new_distance = new_dist.km
        return Distance(self.km + new_distance)

    def __iadd__(self, new_dist: Distance | int | float) -> Distance:
        if isinstance(new_dist, Distance):
            self.km += new_dist.km
        else:
            self.km += new_dist
        return self

    def __mul__(self, multiplier: Distance | int | float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, div: int | float) -> Distance:
        return Distance(round(self.km / div, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
