from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km = self.km + other.km
        return self

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            self.km = round(self.km / other, 2)
            return self
        raise TypeError("Unsupported operand type: " + type(other).__name__
                        + " - Divisor must be an int or float.")

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other : int | float | Distance) -> bool:
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
