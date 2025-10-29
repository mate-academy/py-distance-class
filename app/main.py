from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_km = other.km if isinstance(other, Distance) else other
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return NotImplemented
        result_km = self.km * other
        return Distance(result_km)

    def __rmul__(self, other: int | float) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError
        if other == 0:
            raise ZeroDivisionError
        result_km = round((self.km / other), 2)
        return Distance(result_km)

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
