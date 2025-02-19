from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __le__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __gt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __ge__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other

    def __eq__(self, other: float | int | Distance) -> bool:
        if isinstance(other, Distance):
            return round(self.km, 2) == round(other.km, 2)
        elif isinstance(other, (int, float)):
            return round(self.km, 2) == round(other, 2)
