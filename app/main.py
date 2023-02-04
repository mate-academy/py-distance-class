from __future__ import annotations


class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, Distance, float)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other.real)
        return Distance(self.km + other.km)

    def __iadd__(self, other: (int, Distance, float)) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other.real
        else:
            self.km += other.km
        return self

    def __mul__(self, other: (int, Distance, float)) -> Distance:
        if isinstance(other, (int, float)):
            self.km *= other.real
        else:
            self.km *= other.km
        return self

    def __truediv__(self, other: (int, Distance, float)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other.real, 2))
        return Distance(round(self.km / other.km, 2))

    def __lt__(self, other: (int, Distance, float)) -> bool:
        if isinstance(other, (int, float)):
            return int(self.km) < int(other.real)
        return self.km < other.km

    def __gt__(self, other: (int, Distance, float)) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other.real
        return self.km > other

    def __eq__(self, other: (int, Distance, float)) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other.real
        return self.km == other.km

    def __le__(self, other: (int, Distance, float)) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other.real
        return self.km <= other.km

    def __ge__(self, other: (int, Distance, float)) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other.real
        return self.km >= other.km

    def __len__(self) -> (float, int):
        return self.km
