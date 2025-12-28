from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, dist: Distance | int | float) -> Distance:
        return (Distance(self.km + dist.km)
                if isinstance(dist, Distance)
                else Distance(self.km + dist))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, dist: int | float) -> Distance:
        return Distance(self.km * dist)

    def __truediv__(self, dist: int | float) -> Distance:
        return Distance(round(self.km / dist, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return (self.km < other
                if not isinstance(other, Distance)
                else self.km < other.km)

    def __gt__(self, other: Distance | int | float) -> bool:
        return (self.km > other
                if not isinstance(other, Distance)
                else self.km > other.km)

    def __eq__(self, other: Distance | int | float) -> bool:
        return (self.km == other
                if not isinstance(other, Distance)
                else self.km == other.km)

    def __le__(self, other: Distance | int | float) -> bool:
        return (self.km <= other
                if not isinstance(other, Distance)
                else self.km <= other.km)

    def __ge__(self, other: Distance | int | float) -> bool:
        return (self.km >= other
                if not isinstance(other, Distance)
                else self.km >= other.km)
