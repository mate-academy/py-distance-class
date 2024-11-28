from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def conversion_data(
            some_data: Distance | int | float) -> Distance | int | float:
        if isinstance(some_data, Distance):
            return some_data.km
        return some_data

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.conversion_data(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.conversion_data(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsupported operation class Distance * {type(other)}"
            )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(
                f"Unsupported operation class Distance / {type(other)}"
            )

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.conversion_data(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.conversion_data(other)
