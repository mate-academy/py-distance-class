from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float, Distance]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if type(other) == int or type(other) == float:
            return Distance(
                km=self.km + other
            )
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if type(other) == int or type(other) == float:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km == other
        return self.km == other.km

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        if type(other) == int or type(other) == float:
            return self.km >= other
        return self.km >= other.km

    def __len__(self) -> Union[int, float, Distance]:
        return len(self.km)
