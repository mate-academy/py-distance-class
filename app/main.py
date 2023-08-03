from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(
                km=self.km + other
            )
        else:
            return Distance(
                km=self.km + other.km
            )

    def __iadd__(self, other: Distance | float) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError

        return Distance(
            km=self.km * other
        )

    def __truediv__(self, num: int) -> Distance:
        return Distance(
            km=round(self.km / num, 2)
        )

    def __lt__(self, other: Distance | float) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | float) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | float) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | float) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | float) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km
