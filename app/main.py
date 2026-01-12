from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self,
                other_distance: Distance | int | float) -> Distance:
        if not isinstance(other_distance, Distance):
            return Distance(
                self.km + other_distance
            )
        return Distance(
            self.km + other_distance.km
        )

    def __iadd__(self,
                 other_distance: Distance | int | float) -> Distance:
        if not isinstance(other_distance, Distance):
            self.km += other_distance
            return self
        self.km += other_distance.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km
