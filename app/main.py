from __future__ import annotations
from typing import Any, Union


OtherInputType = Union[float, int]


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: OtherInputType | Distance) -> Distance:
        return Distance(
            self.km + self.number_return(other)
        )

    def __iadd__(self, other: OtherInputType | Distance) -> Distance:
        self.km += self.number_return(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                self.km * self.number_return(other)
            )

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(
            round((self.km / other), 2)
        )

    def __lt__(self, other: OtherInputType | Distance) -> bool:
        return self.km < self.number_return(other)

    def __gt__(self, other: OtherInputType | Distance) -> bool:
        return self.km > self.number_return(other)

    def __eq__(self, other: OtherInputType | Distance) -> bool:
        return self.km == self.number_return(other)

    def __le__(self, other: OtherInputType | Distance) -> bool:
        return self.km <= self.number_return(other)

    def __ge__(self, other: OtherInputType | Distance) -> bool:
        return self.km >= self.number_return(other)

    @staticmethod
    def number_return(number: Any) -> int | float | None:
        if isinstance(number, Distance):
            return number.km
        return number
