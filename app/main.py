from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def get_addend(other: Distance | int) -> int:
        return other.km if isinstance(other, Distance) else other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        return Distance(self.km + Distance.get_addend(other))

    def __iadd__(self, other: Distance | int) -> Distance:
        self.km += Distance.get_addend(other)
        return self

    def __mul__(self, factor: int) -> Distance:
        return Distance(self.km * factor)

    def __truediv__(self, divider: int) -> Distance:
        return Distance(round(self.km / divider, 2))

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < self.get_addend(other)

    def __gt__(self, other: Distance | int) -> bool:
        return self.km > self.get_addend(other)

    def __eq__(self, other: Distance | int) -> bool:
        return self.km == self.get_addend(other)

    def __le__(self, other: Distance | int) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: Distance | int) -> bool:
        return not self.__lt__(other)
