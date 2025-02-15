from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def to_distance(value: Distance | int | float) -> float:
        if isinstance(value, Distance):
            return value.km
        elif isinstance(value, (int, float)):
            return float(value)
        raise TypeError("Unsupported type for arithmetic with Distance")

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.to_distance(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.to_distance(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Multiplication only supports int or float types")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Division only supports int or float types")

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.to_distance(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.to_distance(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.to_distance(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.to_distance(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.to_distance(other)
