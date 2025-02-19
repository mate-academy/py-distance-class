from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, float | int):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, float | int):
            self.km += other
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        if other == 0:
            raise ValueError("Cannot divide by zero")
        result = round((self.km / other), 2)
        return Distance(result)

    def __lt__(self, other: float | int) -> bool:
        return self.km < other

    def __gt__(self, other: float | int) -> bool:
        return self.km > other

    def __eq__(self, other: float | int) -> bool:
        return self.km == other

    def __le__(self, other: float | int) -> bool:
        return self.km <= other

    def __ge__(self, other: float | int) -> bool:
        return self.km >= other
