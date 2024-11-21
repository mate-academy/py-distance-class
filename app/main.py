from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Distance) -> [Distance, int]:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km = self.km + other.km
        return self

    def __mul__(self, other: [Distance, int]) -> [Distance, int]:
        return Distance(km=self.km * other)

    def __truediv__(self, other: [Distance, int]) -> [Distance, int]:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: [Distance, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: [Distance, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: [Distance, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: [Distance, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: [Distance, int]) -> bool:
        if not isinstance(other, Distance):
            return self.km >= other
        return self.km >= other.km

    def __len__(self) -> int:
        return self.km
