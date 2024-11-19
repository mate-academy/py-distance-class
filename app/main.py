from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for addition")
        return self

    def __mul__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported type for multiplication")

    def __truediv__(self, divisor: int) -> Distance:
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        else:
            raise TypeError("Unsupported type for division")

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported type for comparison")

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported type for comparison")

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported type for comparison")

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported type for comparison")

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported type for comparison")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
