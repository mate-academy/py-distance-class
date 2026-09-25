from __future__ import annotations


class Distance:
    def __init__(self, km : int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other : int | Distance) -> Distance:
        if isinstance(other, Distance) :
            add = self.km + other.km
        else:
            add = self.km + other
        return Distance(add)

    def __mul__(self, other : int) -> Distance:
        mul = self.km * other
        return Distance(mul)

    def __iadd__(self, other : int | Distance) -> Distance:
        if isinstance(other, Distance) :
            self.km += other.km
        else:
            self.km += other
        return self

    def __truediv__(self, other : int) -> Distance:
        truediv = self.km / other
        return Distance(round(truediv, 2))

    def __le__(self, other : int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other : int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

    def __eq__(self, other : int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __lt__(self, other : int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other : int | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other
