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
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km / other
            rounded_km = round(result, 2)
            return Distance(rounded_km)
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return self.km < other_km

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return self.km > other_km

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return self.km == other_km

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        return self.km >= other_km
