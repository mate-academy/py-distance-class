from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km
        print(f"distance.km == {self.km}")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                self.km + other
            )
        if isinstance(other, Distance):
            return Distance(
                self.km + other.km
            )

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        if isinstance(other, Distance):
            self.km += other.km
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int) -> Distance:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            if self.km < other:
                return True
            else:
                return False
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
            else:
                return False

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            if self.km > other:
                return True
            else:
                return False
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
            else:
                return False

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            if self.km == other:
                return True
            else:
                return False
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
            else:
                return False

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            if self.km <= other:
                return True
            else:
                return False
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
            else:
                return False

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        if isinstance(other, (int, float)):
            if self.km >= other:
                return True
            else:
                return False
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
            else:
                return False
