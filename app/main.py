from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Union[int, float, Distance]:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance) -> Distance:
        if not isinstance(other, Distance):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, num: int) -> Distance:
        return Distance(self.km * num)

    def __truediv__(self, num: int) -> Distance:
        return Distance(round(self.km / num, 2))

    def __lt__(self, num: Union[int, float, Distance]) -> bool:
        if isinstance(num, Distance):
            return self.km < num.km
        return self.km < num

    def __gt__(self, num: Union[int, float, Distance]) -> bool:
        if isinstance(num, Distance):
            return self.km > num.km
        return self.km > num

    def __eq__(self, num: Union[int, float, Distance]) -> bool:
        if isinstance(num, Distance):
            return self.km == num.km
        return self.km == num

    def __le__(self, num: Union[int, float, Distance]) -> bool:
        if isinstance(num, Distance):
            return self.km <= num.km
        return self.km <= num

    def __ge__(self, num: Union[int, float, Distance]) -> bool:
        if isinstance(num, Distance):
            return self.km >= num.km
        return self.km >= num

    def __len__(self) -> float or int:
        return self.km
