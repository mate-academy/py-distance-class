from __future__ import annotations

from typing import Union


class Distance:

    @staticmethod
    def check_other_number(other: Union[int, float]) -> bool:
        return isinstance(other, (int, float))

    @staticmethod
    def check_other_instance(other: Distance) -> bool:
        return isinstance(other, Distance)

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        try:
            if Distance.check_other_number(other):
                return Distance(self.km + other)
            elif Distance.check_other_instance(other):
                return Distance(self.km + other.km)
        except TypeError:
            "'Other' must be type int or float or belong to Distance class"

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        try:
            if Distance.check_other_instance(other):
                self.km += other.km
            elif Distance.check_other_number(other):
                self.km += other
        except TypeError:
            "'Other' must be type int or float or belong to Distance class"
        return self

    def __mul__(self, other: Union[Distance, int, float]) -> Distance:
        if Distance.check_other_number(other):
            return Distance(self.km * other)

    def __truediv__(self, other: Union[Distance, int, float]) -> Distance:
        try:
            if Distance.check_other_number(other):
                return Distance(round(self.km / other, 2))
        except TypeError:
            "'Other' must be type int or float or belong to Distance class"

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other_instance(other):
            return self.km < other.km
        elif Distance.check_other_number(other):
            return self.km < other

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other_instance(other):
            return self.km > other.km
        elif Distance.check_other_number(other):
            return self.km > other

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other_instance(other):
            return self.km == other.km
        elif Distance.check_other_number(other):
            return self.km == other

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other_instance(other):
            return self.km <= other.km
        elif Distance.check_other_number(other):
            return self.km <= other

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if Distance.check_other_instance(other):
            return self.km >= other.km
        elif Distance.check_other_number(other):
            return self.km >= other
