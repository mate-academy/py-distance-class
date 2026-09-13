from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_km: Distance | int | float) -> Distance:
        if isinstance(new_km, (int, float)):
            new_km = Distance(new_km)
        return Distance(self.km + new_km.km)

    def __iadd__(self, new_km: Distance | int | float) -> Distance:
        if isinstance(new_km, (int, float)):
            new_km = Distance(new_km)
        self.km += new_km.km
        return self

    def __mul__(self, factor: int | float) -> Distance:
        return Distance(self.km * factor)

    def __truediv__(self, divisor: int | float) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km
