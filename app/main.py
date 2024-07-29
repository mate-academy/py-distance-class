from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def extract_km(other: Distance | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        raise TypeError("Unsupported operand type")

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.extract_km(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.extract_km(other)
        return self

    def __mul__(self, factor: int | float) -> Distance:
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented

    def __truediv__(self, divisor: int | float) -> Distance:
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.extract_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.extract_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.extract_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.extract_km(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.extract_km(other)
