from __future__ import division, annotations
from typing import Union


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, value: Union[int, Distance]) -> Distance:
        if isinstance(value, Distance):
            return Distance(self.km + value.km)

        return Distance(self.km + value)

    def __iadd__(self, value: Union[float, Distance]) -> Distance:
        if isinstance(value, Distance):
            self.km = self.km + value.km
            return self

        self.km = self.km + value
        return self

    def __mul__(self, value: int) -> Distance:
        return Distance(self.km * value)

    def __truediv__(self, value: int) -> Distance:
        return Distance(round(self.km / value, 2))

    def __lt__(self, value: Union[int, Distance]) -> bool:
        if isinstance(value, Distance):
            return self.km < value.km

        return self.km < value

    def __gt__(self, value: Union[int, Distance]) -> bool:
        if isinstance(value, Distance):
            return self.km > value.km

        return self.km > value

    def __eq__(self, value: Union[int, Distance]) -> bool:
        if isinstance(value, Distance):
            return self.km == value.km

        return self.km == value

    def __le__(self, value: Union[int, Distance]) -> bool:
        if isinstance(value, Distance):
            return self.km <= value.km

        return self.km <= value

    def __ge__(self, value: Union[int, Distance]) -> bool:
        if isinstance(value, Distance):
            return self.km >= value.km

        return self.km >= value
