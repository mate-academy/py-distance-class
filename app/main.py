from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        return Distance(
            km=self.km + other
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            km=round((self.km / other), 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
