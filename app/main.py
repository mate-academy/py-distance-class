from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self
        else:
            self.km = self.km + other.km
            return self

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            self.km += other.km
            return self

    def __mul__(self, other: int) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: int) -> Distance:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __eq__(self, other: int) -> bool:
        return self.km == other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other
