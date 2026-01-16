from typing import Self


class Distance:
    def __init__(self, km: int) -> None:
        self.km: int = km

    def __str__(self) -> str:
        return f"Distance: {self.km} km"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> Self:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return NotImplemented

    def __iadd__(self, other: object) -> Self:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: object) -> Self:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        elif isinstance(other, Distance):
            return Distance(self.km * other.km)
        else:
            return NotImplemented

    def __truediv__(self, other: object) -> Self:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            return Distance(round(self.km / other.km, 2))
        else:
            return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented


dist1 = Distance(100)
dist2 = Distance(200)
print(dist1)             # Distance: 100 km
print(repr(dist2))      # Distance(km=200)
dist3 = dist1 + dist2
print(dist3)            # Distance: 300 km
