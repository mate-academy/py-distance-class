from __future__ import annotations


class Distance:
    def __init__(self, distance: int | float) -> None:
        self.km = distance

    @staticmethod
    def is_not_distance(other: int | float | Distance) -> bool:
        return isinstance(other, (int, float))

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: int | float | Distance) -> Distance:
        if self.is_not_distance(other):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if self.is_not_distance(other):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __eq__(self, other: int | float | Distance) -> bool:
        return self.km == other if self.is_not_distance(other) else self.km == other.km

    def __gt__(self, other: int | float | Distance) -> bool:
        return self.km > other if self.is_not_distance(other) else self.km > other.km

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= other if self.is_not_distance(other) else self.km >= other.km

    def __le__(self, other: Distance | int | float) -> bool:
        return not self.__gt__(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return not self.__ge__(other)

    def __truediv__(self, other: int | float) -> Distance:
        self.km = round(self.km / other, 2)
        return self
