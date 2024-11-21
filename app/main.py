from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, num: int) -> Distance:
        return Distance(
            km=self.km * num
        )

    def __truediv__(self, num: int) -> Distance:
        return Distance(
            km=round(self.km / num, 2)
        )

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
