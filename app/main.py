from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> Distance:
        return Distance(self.km + self.instance_check(other))

    def __iadd__(self, other) -> Distance:
        self.km += self.instance_check(other)
        return self

    def __mul__(self, other) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        return self.km < self.instance_check(other)

    def __gt__(self, other) -> bool:
        return self.km > self.instance_check(other)

    def __eq__(self, other) -> bool:
        return self.km == self.instance_check(other)

    def __le__(self, other) -> bool:
        return not self > other

    def __ge__(self, other) -> bool:
        return not self < other

    def __len__(self) -> int:
        return self.km

    @staticmethod
    def instance_check(other) -> int | float:
        return other.km if isinstance(other, Distance) else other
