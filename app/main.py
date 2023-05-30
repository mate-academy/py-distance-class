from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return (Distance(self.km + other.km) if isinstance(other, Distance)
                else Distance(self.km + other))

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km = (self.km + other.km if isinstance(other, Distance)
                   else self.km + other)
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        return True if self.km == other else False

    def __lt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        return True if self.km < other else False

    def __le__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        return True if self.km <= other else False

    def __gt__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        return True if self.km > other else False

    def __ge__(self, other: Distance | int) -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        return True if self.km >= other else False
