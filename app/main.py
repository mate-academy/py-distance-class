from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def is_valid_type(self, other: Distance | int | float) -> None:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"Unsupported operand type {type(other)}")

    def __add__(self, other: Distance | int | float) -> Distance:
        self.is_valid_type(other)
        if type(other) is int:
            return Distance(km=other + self.km)
        elif type(other) is float:
            return Distance(km=other + self.km)
        return Distance(km=self.km + other.km)

    def __radd__(self, other: Distance | int | float) -> Distance:
        self.is_valid_type(other)
        if type(other) is int:
            return Distance(km=other + self.km)
        elif type(other) is float:
            return Distance(km=other + self.km)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.is_valid_type(other)
        if type(other) is int or float:
            self.km = self + other
            return self
        return self + other.km

    def __mul__(self, other: Distance | int | float) -> Distance:
        self.is_valid_type(other)
        if type(other) is int or float:
            return Distance(km=self.km * other)
        return Distance(km=self.km * other.km)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        self.is_valid_type(other)
        if type(other) is int or float:
            return Distance(km=round(self.km / other, 2))
        return Distance(km=round(self.km / other.km, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        self.is_valid_type(other)
        if type(other) is int or float:
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        self.is_valid_type(other)
        if type(other) is int or float:
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        self.is_valid_type(other)
        if type(other) is int or float:
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        self.is_valid_type(other)
        if type(other) is int or float:
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        self.is_valid_type(other)
        if type(other) is int or float:
            return self.km >= other
        return self.km >= other.km
