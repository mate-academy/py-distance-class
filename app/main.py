from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __radd__(self, other) -> Distance:
        if isinstance(other, Distance):
            return Distance(other.km + self.km)
        return Distance(other + self.km)

    def __iadd__(self, other) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other) -> Distance:
        if isinstance(other, Distance):
            self.km *= other.km
            return self.km
        self.km *= other
        return Distance(self.km)

    def __truediv__(self, other) -> Distance:
        if isinstance(other, Distance):
            self.km /= other.km
            return self.km
        self.km /= other
        return Distance(round(self.km, 2))

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return other == self.km

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return other > self.km

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return other < self.km

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return other >= self.km

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return other <= self.km

    def __len__(self) -> int:
        return self.km
