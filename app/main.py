from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def check_argument(other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return other
        return Distance(other)

    def __add__(self, other: Distance | int | float) -> Distance:
        other_distance = self.check_argument(other)
        return Distance(km=self.km + other_distance.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other_distance = self.check_argument(other)
        self.km += other_distance.km
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        other_distance = self.check_argument(other)
        return self.km == other_distance.km

    def __gt__(self, other: Distance | int | float) -> bool:
        other_distance = self.check_argument(other)
        return self.km > other_distance.km

    def __lt__(self, other: Distance | int | float) -> bool:
        other_distance = self.check_argument(other)
        return self.km < other_distance.km

    def __ge__(self, other: Distance | int | float) -> bool:
        other_distance = self.check_argument(other)
        return self.km >= other_distance.km

    def __le__(self, other: Distance | int | float) -> bool:
        other_distance = self.check_argument(other)
        return self.km <= other_distance.km
