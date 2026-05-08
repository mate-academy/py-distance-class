from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(other * self.km)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            result_km = self.km / other
            result_km = round(result_km, 2)
            return Distance(result_km)
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool | NotImplemented:
        if isinstance(other, Distance):
            other = other.km
            return self.km < other
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool | NotImplemented:
        if isinstance(other, Distance):
            other = other.km
            return self.km > other
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool | NotImplemented:
        if isinstance(other, Distance):
            other = other.km
            return self.km == other
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool | NotImplemented:
        if isinstance(other, Distance):
            other = other.km
            return self.km <= other
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool | NotImplemented:
        if isinstance(other, Distance):
            other = other.km
            return self.km >= other
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
