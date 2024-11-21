from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __mul__(self, scalar: int | float) -> Distance:
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, divisor: int | float) -> Distance:
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: int | float) -> bool:
        return (
            self.km < other.km if isinstance(other, Distance)
            else self.km < other
        )

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
