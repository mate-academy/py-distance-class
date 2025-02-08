from __future__ import annotations


class Distance:
    @staticmethod
    def check_is_instance(other: Distance | int) -> bool:
        return isinstance(other, Distance)

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if self.check_is_instance(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if self.check_is_instance(other):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | int) -> Distance:
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < other

    def __gt__(self, other: Distance | int) -> bool:
        return self.km > other

    def __eq__(self, other: Distance | int) -> bool:
        return self.km == other

    def __le__(self, other: Distance | int) -> bool:
        return self.km <= other

    def __ge__(self, other: Distance | int) -> bool:
        return self.km >= other
