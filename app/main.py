from __future__ import annotations, division
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            instance_distance = Distance(km=other)
            return Distance(self.km + instance_distance.km)

    def __iadd__(self, other: Union[Distance, int]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            instance_distance = Distance(km=other)
            self.km += instance_distance.km
            return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            instance_distance = Distance(km=other)
            return self.km < instance_distance.km

    def __gt__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            instance_distance = Distance(km=other)
            return self.km > instance_distance.km

    def __eq__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            instance_distance = Distance(km=other)
            return self.km == instance_distance.km

    def __le__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            instance_distance = Distance(km=other)
            return self.km <= instance_distance.km

    def __ge__(self, other: Union[Distance, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            instance_distance = Distance(km=other)
            return self.km >= instance_distance.km
