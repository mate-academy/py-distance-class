from __future__ import annotations

class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> float:
        if isinstance(other, Distance) is True:
            return self.km + other.km
        else:
            return self.km + other

    def __iadd__(self, other) -> None:
        if isinstance(other, Distance) is True:
            self.km += other.km
        else:
            self.km += other

    def __mul__(self, other) -> float:
        if isinstance(other, Distance) is True:
            return self.km * other.km
        else:
            return self.km * other

    def __truediv__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(round(self.km / other.km, 2))
        else:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km < other.km)
        else:
            return Distance(self.km < other)

    def __gt__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km > other.km)
        else:
            return Distance(self.km > other)

    def __eq__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km == other.km)
        else:
            return Distance(self.km == other)

    def __le__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km <= other.km)
        else:
            return Distance(self.km <= other)

    def __ge__(self, other) -> Distance:
        if isinstance(other, Distance) is True:
            return Distance(self.km >= other.km)
        else:
            return Distance(self.km >= other)
