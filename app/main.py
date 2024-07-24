from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: Distance) -> Distance | None:
        if isinstance(other, (int, float)):
            return Distance(round(self.km * other, 3))
        elif isinstance(other, Distance):
            Distance(round(self.km * other.km, 3))
        return None

    def __truediv__(self, other: Distance) -> Distance | None:
        if isinstance(other, (int, float)):
            if other == 0:
                return None
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            Distance(round(self.km / other.km, 2))
        return None

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            if isinstance(other, (int, float)):
                return self.km < other

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            if isinstance(other, (int, float)):
                return self.km > other

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            if isinstance(other, (int, float)):
                return self.km <= other

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            if isinstance(other, (int, float)):
                return self.km >= other

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            if isinstance(other, (int, float)):
                return self.km == other
