from __future__ import annotations
from typing import Callable, Union


def actions_based_on_incoming_data(func: any) -> Callable:
    def wraper(self: Distance, other: Union[Distance, int, float]) -> Callable:
        if isinstance(other, Distance):
            return func(self.km, other.km)
        if isinstance(other, (int, float)):
            return func(self.km, other)

    return wraper


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @actions_based_on_incoming_data
    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(self + other)

    def __iadd__(self, other: float) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
        if isinstance(other, (int, float)):
            self.km = self.km + other
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round((self.km / other), 2))

    @actions_based_on_incoming_data
    def __lt__(self, other: float) -> bool:
        return self < other

    @actions_based_on_incoming_data
    def __gt__(self, other: float) -> bool:
        return self > other

    @actions_based_on_incoming_data
    def __eq__(self, other: float) -> bool:
        return self == other

    @actions_based_on_incoming_data
    def __le__(self, other: float) -> bool:
        return self <= other

    @actions_based_on_incoming_data
    def __ge__(self, other: float) -> bool:
        print(type(other))
        return self >= other

    def __len__(self) -> float:
        return self.km
