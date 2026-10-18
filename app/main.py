from typing import Callable
from functools import wraps


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def is_other_distance_obj(funk: Callable) -> Callable:
        @wraps(funk)
        def inner(
                self: "Distance",
                other: "Distance | int | float") -> "Distance":
            if not isinstance(other, Distance):
                other = Distance(other)
            return funk(self, other)

        return inner

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @is_other_distance_obj
    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.km + other.km)

    @is_other_distance_obj
    def __iadd__(self, other: "Distance") -> "Distance":
        self.km += other.km
        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> "Distance":
        return Distance(round(self.km / number, 2))

    @is_other_distance_obj
    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    @is_other_distance_obj
    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    @is_other_distance_obj
    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km

    @is_other_distance_obj
    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km

    @is_other_distance_obj
    def __eq__(self, other: "Distance") -> bool:
        return self.km == other.km
