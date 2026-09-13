from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    @staticmethod
    def checker(other: int | float | Distance) -> int:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: int | float | Distance) -> Distance:
        return Distance(km=self.km + self.checker(other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += self.checker(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < self.checker(other)

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > self.checker(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == self.checker(other)

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= self.checker(other)

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= self.checker(other)
