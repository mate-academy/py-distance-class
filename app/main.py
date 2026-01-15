from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, (float, int)):
            self.km += other
            return self
        elif isinstance(other, Distance):
            self.km += other.km
            return self
        return NotImplemented

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (float, int, Distance)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __mul__(self, other: float | int | Distance) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        return NotImplemented

    def __lt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, (float, int, Distance)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: float | int | Distance) -> bool:
        if isinstance(other, (float, int, Distance)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: float | int | Distance) -> bool:
        if isinstance(other, (float, int, Distance)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: float | int | Distance) -> bool:
        if isinstance(other, (float, int, Distance)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: float | int | Distance) -> bool:
        if isinstance(other, (float, int, Distance)):
            return self.km >= other
        return NotImplemented
