from __future__ import annotations


class Distance:

    def __init__(self, run: int | float) -> None:
        self.km = run

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            total_distance = self.km + other.km
        else:
            total_distance = self.km + other
        return Distance(total_distance)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other_number: int | float) -> Distance:
        return Distance(self.km * other_number)

    def __truediv__(self, other_number: int | float) -> Distance:
        return Distance(round(self.km / other_number, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        return self == other or self < other

    def __ge__(self, other: int | float | Distance) -> bool:
        return self == other or self > other
