from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return Distance(self.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: float) -> Distance:
        self.km *= other
        return Distance(self.km)

    def __truediv__(self, other: float) -> Distance:
        self.km = round(self.km / other, 2)
        return Distance(self.km)

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < Distance(other).km

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == Distance(other).km

    def __le__(self, other: int | float | Distance) -> bool:
        return self < other or self == other

    def __gt__(self, other: int | float | Distance) -> bool:
        return not self <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        return not self < other
