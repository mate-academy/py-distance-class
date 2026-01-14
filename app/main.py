from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        km = self.km / other
        return Distance(round(km, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        if not isinstance(other, Distance):
            lt = self.km < other
            return lt
        lt = self.km < other.km
        return lt

    def __le__(self, other: Distance | float | int) -> bool:
        if not isinstance(other, Distance):
            le = self.km <= other
            return le
        le = self.km <= other.km
        return le

    def __eq__(self, other: Distance | float | int) -> bool:
        if not isinstance(other, Distance):
            eq = self.km == other
            return eq
        eq = self.km == other.km
        return eq

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            ge = self.km >= other.km
            return ge
        ge = self.km >= other
        return ge

    def __gt__(self, other: Distance | float | int) -> bool:
        if not isinstance(other, Distance):
            gt = self.km > other
            return gt
        gt = self.km > other.km
        return gt
