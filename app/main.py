from __future__ import annotations

from typing import Callable, Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    @staticmethod
    def other_value_parser(func: Callable) -> Callable:
        """Декоратор для вилучення числового значення з операнда 'other'."""

        def wrapper(self: Any, other: Distance | int | float) -> Any:
            other_value = other
            if isinstance(other, Distance):
                other_value = other.km
            elif isinstance(other, (int, float)):
                other_value = other
            else:
                print(f"{type(other)} not supported")
            return func(self, other_value)

        return wrapper

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @other_value_parser
    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int , float)):
            self.km += other
        else:
            print(f"{type(other)} not supported")
        return self

    # @other_value_parser
    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    # @other_value_parser
    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round((self.km / other), 2))

    @other_value_parser
    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other

    @other_value_parser
    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other

    @other_value_parser
    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other

    @other_value_parser
    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other

    @other_value_parser
    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other
