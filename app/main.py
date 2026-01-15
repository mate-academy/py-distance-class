from __future__ import annotations
from __future__ import division
from typing import Any


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def checking_data(cls, other: Distance | int | float) -> (
            Distance | float | int):
        if isinstance(other, Distance):
            return other.km
        else:
            return other

    def __add__(self, other: Distance | int | float) -> Distance:
        data = self.checking_data(other)
        return Distance(self.km + data)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        data = self.checking_data(other)
        self.km += data
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> Any:
        data = self.checking_data(other)
        return self.km < data

    def __gt__(self, other: Distance | int | float) -> Any:
        data = self.checking_data(other)
        return self.km > data

    def __eq__(self, other: Distance | int | float) -> Any:
        data = self.checking_data(other)
        return self.km == data

    def __le__(self, other: Distance | int | float) -> Any:
        data = self.checking_data(other)
        return self.km <= data

    def __ge__(self, other: Distance | int | float) -> Any:
        data = self.checking_data(other)
        return self.km >= data
