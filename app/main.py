from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(
            self.km + other.km
            if isinstance(other, Distance)
            else self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km = self.km + other.km \
            if isinstance(other, Distance) \
            else self.km + other
        return self

    def __mul__(self, multiplier: int) -> Distance:
        self.km *= multiplier
        return self

    def __truediv__(self, devider: int) -> Distance:
        self.km = round(self.km / devider, 2)
        return self

    def __lt__(self, other: Distance | int) -> bool:
        return (self.km < other.km
                if isinstance(other, Distance)
                else self.km < other)

    def __gt__(self, other: Distance | int) -> bool:
        return (self.km > other.km
                if isinstance(other, Distance)
                else self.km > other)

    def __eq__(self, other: Distance | int) -> bool:
        return not self.__gt__(other) and not self.__lt__(other)

    def __le__(self, other: Distance | int) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: Distance | int) -> bool:
        return not self.__lt__(other)
