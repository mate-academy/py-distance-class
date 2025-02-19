from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self

        self.km += other
        return self

    def __mul__(self, multiplier: int | float) -> Distance:
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other

    def __ne__(self, other: Distance | int | float) -> bool:
        return not self == other

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        return self.km > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return self > other or self == other

    def __lt__(self, other: Distance | int | float) -> bool:
        return not self >= other

    def __le__(self, other: Distance | int | float) -> bool:
        return not self > other
