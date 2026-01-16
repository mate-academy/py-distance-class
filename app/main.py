from __future__ import annotations
from ctypes import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[float, Distance]) -> None:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[float, Distance]) -> None:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[float, Distance]) -> None:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
