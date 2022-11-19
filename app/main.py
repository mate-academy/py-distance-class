from __future__ import annotations


class Distance:

    def __init__(self, km: [int, float]) -> None:
        if km == 0:
            self.km = []
        else:
            self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: [int, float, Distance]) -> [int, float]:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: [int, float, Distance]) -> [int, float]:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: [int, float]) -> [int, float]:
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)

    def __truediv__(self, other: [int, float, Distance]) -> [int, float]:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: [int, float, Distance]) -> bool:
        return self.km < other

    def __gt__(self, other: [int, float, Distance]) -> bool:
        return self.km > other

    def __eq__(self, other: [int, float, Distance]) -> bool:
        return self.km == other

    def __le__(self, other: [int, float, Distance]) -> bool:
        return self.km <= other

    def __ge__(self, other: [int, float, Distance]) -> bool:
        return self.km >= other

    def __len__(self) -> [int, float]:
        return len(self.km)
