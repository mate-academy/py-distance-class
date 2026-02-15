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

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported operand type for /")

    def __gt__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value

    def __lt__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int | float):
            self.km += other
        return self
