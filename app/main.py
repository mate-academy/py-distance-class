from __future__ import annotations


class Distance:
    def __init__(self: int, km: int):
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: (int, float)) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __mul__(self, other: (int, float)) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        return Distance(self.km * other.km)

    def __truediv__(self, other: (int, float)) -> float:
        if isinstance(other, (float, int)):
            return Distance(round((self.km / other), 2))
        return Distance(round((self.km / other.km), 2))

    def __len__(self) -> Distance:
        return self

    def __iadd__(self, other: (int, float)) -> Distance:
        if isinstance(other, (float, int)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __eq__(self, other: (int, float)) -> bool:
        if isinstance(other, (float, int)):
            return self.km == other
        return self.km == other

    def __gt__(self, other: (int, float)) -> bool:
        if isinstance(other, (float, int)):
            return self.km > other
        return self.km > other

    def __lt__(self, other: (int, float)) -> bool:
        if isinstance(other, (float, int)):
            return self.km < other
        return self.km < other

    def __ge__(self, other: (int, float)) -> bool:
        if isinstance(other, (float, int)):
            return self.km >= other
        return self.km >= other

    def __le__(self, other: (int, float)) -> bool:
        if isinstance(other, (float, int)):
            return self.km <= other
        return self.km <= other
