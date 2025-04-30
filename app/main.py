from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> object:
        if isinstance(other, (int, float)):
            out = self.km + other
            return Distance(out)
        out = self.km + other.km
        return Distance(out)

    def __iadd__(self, other: Distance) -> object:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, other: Distance) -> object:
        if isinstance(other, (int, float)):
            out = self.km * other
            return Distance(out)
        return NotImplemented

    def __truediv__(self, other: Distance) -> object:
        if isinstance(other, (int, float)):
            out = self.km / other
            return Distance(round(out, 2))
        return NotImplemented

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km
