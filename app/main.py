from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int | Distance) -> Distance:
        return Distance(round(self.km / other, 2))

    def __gt__(self, other: float | int | Distance) -> bool:
        return self.km > other

    def __lt__(self, other: float | int | Distance) -> bool:
        return self.km < other

    def __ge__(self, other: float | int | Distance) -> bool:
        return self.km >= other

    def __le__(self, other: float | int | Distance) -> bool:
        return self.km <= other

    def __eq__(self, other: float | int | Distance) -> bool:
        return self.km == other
