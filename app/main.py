from __future__ import annotations


class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        else:
            self.km = self.km + other
        return self

    def __mul__(self, other: (int, float)) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, operand: (int, float)) -> Distance:
        other = round((self.km / operand), 2)
        return Distance(other)

    def __lt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other: (int, float, Distance)) -> bool:
        return not self < other

    def __le__(self, other: (int, float, Distance)) -> bool:
        return not self > other

    def __eq__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __len__(self):
        return self.km
