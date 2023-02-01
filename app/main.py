from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> Distance:
        if not isinstance(other, Distance):
            other = Distance(other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: object) -> Distance:
        if not isinstance(other, Distance):
            other = Distance(other)
        self.km += other.km
        return self

    def __mul__(self, other: Distance) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Distance) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km > other.km

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km == other.km

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km <= other.km

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km >= other.km

    def __len__(self) -> float:
        return self.km
