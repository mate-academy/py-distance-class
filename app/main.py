from __future__ import annotations
from typing import Any


def get_operand_value(func: callable) -> callable:
    def wrapper(self: Distance, distance: Distance | int | float) -> Any:
        if isinstance(distance, Distance):
            return func(self, distance.km)

        return func(self, distance)

    return wrapper


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @get_operand_value
    def __add__(self, distance: int | float) -> Distance:
        return Distance(self.km + distance)

    @get_operand_value
    def __iadd__(self, distance: int | float) -> Distance:
        self.km += distance

        return self

    def __mul__(self, distance: int | float) -> Distance:
        return Distance(self.km * distance)

    def __truediv__(self, distance: int | float) -> Distance:
        return Distance(round(self.km / distance, 2))

    @get_operand_value
    def __lt__(self, distance: int | float) -> bool:
        return self.km < distance

    @get_operand_value
    def __gt__(self, distance: int | float) -> bool:
        return self.km > distance

    @get_operand_value
    def __eq__(self, distance: int | float) -> bool:
        return self.km == distance

    @get_operand_value
    def __le__(self, distance: int | float) -> bool:
        return self.km <= distance

    @get_operand_value
    def __ge__(self, distance: int | float) -> bool:
        return self.km >= distance
