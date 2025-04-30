from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance | None:
        if isinstance(other, Distance):
            foot = Distance(self.km + other.km)
            return foot
        if isinstance(other, int | float):
            cool = Distance(self.km + other)
            return cool

    def __iadd__(self, other: Distance | int | float) -> Distance | None:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, int | float):
            self.km += other
            return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        distance_m = Distance(
            self.km * other
        )
        return distance_m

    def __truediv__(self, other: Distance | int | float) -> Distance:
        distance_tr = Distance(
            round(self.km / other, 2)
        )
        return distance_tr

    def __lt__(self, other: Distance | int | float) -> bool | None:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, int | float):
            return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool | None:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, int | float):
            return self.km > other

    def __le__(self, other: Distance | int | float) -> bool | None:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, int | float):
            return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool | None:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, int | float):
            return self.km >= other

    def __eq__(self, other: Distance | int | float) -> bool | None:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, int | float):
            return self.km == other
