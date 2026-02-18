from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        elif isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError()
            return Distance(km=round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return (self.km < other.km)
        return (self.km < other)

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return (self.km > other.km)
        return (self.km > other)

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return (self.km <= other.km)
        return (self.km <= other)

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return (self.km >= other.km)
        return (self.km >= other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return (self.km == other.km)
        return (self.km == other)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
