from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km
        self.real = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(km=self.km + other.real)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.real
        return self

    def __mul__(self, value: int) -> Distance:
        return Distance(km=self.km * value)

    def __truediv__(self, value: float) -> Distance:
        return Distance(km=round((self.km / value), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other.real

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other.real

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other.real

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other.real

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other.real
