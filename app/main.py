from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def is_obj(other: int | float | Distance) -> bool:
        return isinstance(other, Distance)

    def __lt__(self, other: int | float | Distance) -> bool:
        return self.km < other.km if self.is_obj(other) else self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > other.km if self.is_obj(other) else self.km > other

    def __le__(self, other: int | float | Distance) -> bool:
        return self.km <= other.km if self.is_obj(other) else self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= other.km if self.is_obj(other) else self.km >= other

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == other.km if self.is_obj(other) else self.km == other

    def __add__(self, other: int | float | Distance) -> Distance:
        return (Distance(self.km + other.km)
                if self.is_obj(other)
                else Distance(self.km + other))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += other.km if self.is_obj(other) else other
        return self

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)
