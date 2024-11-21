from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def get_func(instance: Distance | int | float) -> float:
        return instance.km if isinstance(instance, Distance) else instance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_func(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.get_func(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.get_func(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.get_func(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.get_func(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.get_func(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.get_func(other)
