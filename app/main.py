from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        res_sum = self.km + other.km \
            if isinstance(other, Distance) \
            else self.km + other

        return Distance(res_sum)

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        result_sum = round(self.km + other.km, 2) \
            if isinstance(other, Distance) \
            else round(self.km + other, 2)
        self.km = result_sum
        return self

    def __mul__(self, other: [int, float]) -> Distance:
        mul_result = self.km * other
        return Distance(mul_result)

    def __truediv__(self, number: [int, float]) -> Distance:
        truediv_result = round(self.km / number, 2)
        return Distance(truediv_result)

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < other.km \
            if isinstance(other, Distance) \
            else self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > other.km \
            if isinstance(other, Distance) \
            else self.km > other

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == other.km \
            if isinstance(other, Distance) \
            else self.km == other

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= other.km \
            if isinstance(other, Distance) \
            else self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= other.km \
            if isinstance(other, Distance) \
            else self.km >= other
