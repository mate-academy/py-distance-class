from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        self.km = self.km + other
        return self

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km = self.km + other
        else:
            self.km += other.km
        return self

    def __mul__(self, number: int) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: float | int) -> Distance:
        return Distance(round(self.km / number, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __ne__(self, other: Distance | int | float) -> bool:
        return not self.km == other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return not self.km == other and not self.km < other
        return not self.km == other.km and not self.km < other.km

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return not self.km < other
        return not self.km < other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other or self.km < other
        return self.km == other.km or self.km < other.km
