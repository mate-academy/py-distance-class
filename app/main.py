from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.instance_check(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.instance_check(other)
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.instance_check(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.instance_check(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.instance_check(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return not self > other

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self < other

    def __len__(self) -> int | float:
        return self.km

    @staticmethod
    def instance_check(other: Distance) -> int | float:
        return other.km if isinstance(other, Distance) else other
