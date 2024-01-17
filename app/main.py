from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> None:
        value = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + value)

    def __iadd__(self, other: int | float | Distance) -> None:
        value = other if isinstance(other, (int, float)) else other.km
        self.km += value
        return self

    def __mul__(self, other: int | float | Distance) -> None:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float | Distance) -> None:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: int | float | Distance) -> None:
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> None:
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> None:
        return self.km == other

    def __le__(self, other: int | float | Distance) -> None:
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> None:
        return self.km >= other
