from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | float | list) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, type(self.km)):
            self.km += other
        else:
            self.km += list(other)
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __len__(self) -> float:
        return self.km
