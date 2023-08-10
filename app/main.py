from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        new_km = self.km + (other.km if isinstance(other, Distance) else other)
        return Distance(new_km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, num: int | float) -> Distance:
        if isinstance(num, (int, float)):
            new_km = round(self.km * num, 3)
            return Distance(new_km)

    def __truediv__(self, num: int | float) -> Distance:
        if isinstance(num, (int, float)):
            new_km = round(self.km / num, 2)
            return Distance(new_km)

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other

        return self.km < other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other

        return self.km > other.km

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other

        return self.km == other.km

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other

        return self.km <= other.km

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other

        return self.km >= other.km
