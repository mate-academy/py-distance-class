from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[Distance, float, int]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return Distance(
            self.km + km_of_other
        )

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        km_of_other = other if not isinstance(other, Distance) else other.km
        self.km += km_of_other
        return self

    def __mul__(self, num: Union[Distance, float, int]) -> Distance:
        return Distance(
            self.km * num
        )

    def __truediv__(self, num: Union[Distance, float, int]) -> Distance:
        return Distance(
            round(self.km / num, 2)
        )

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return self.km < km_of_other

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return self.km > km_of_other

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return self.km == km_of_other

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return self.km <= km_of_other

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        km_of_other = other if not isinstance(other, Distance) else other.km
        return self.km >= km_of_other
