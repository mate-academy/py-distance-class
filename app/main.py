from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self
        self.km = self.km + other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> None | Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return None

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: int | float) -> bool:
        return Distance.__lt__(self, other) or Distance.__eq__(self, other)

    def __ge__(self, other: int | float) -> bool:
        return Distance.__gt__(self, other) or Distance.__eq__(self, other)
