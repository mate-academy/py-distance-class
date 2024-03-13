from __future__ import annotations
from typing import Any


class Distance:

    @staticmethod
    def print_error_mess_dist(other_value: Any) -> str:
        return (f"Argument {other_value} must be Distance "
                f"or float or int type, not {type(other_value)}.")

    @staticmethod
    def print_error_message(other_value: Any) -> str:
        return (f"Argument {other_value} must be"
                f"float or int type, not {type(other_value)}.")

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(self.km + other)
        else:
            raise TypeError(self.print_error_mess_dist(other))

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (float, int)):
            self.km += other
        else:
            raise TypeError(self.print_error_mess_dist(other))
        return self

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(self.km * other)
        else:
            raise TypeError(self.print_error_message(other))

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (float, int)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(self.print_error_message(other))

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (float, int)):
            return self.km < other
        else:
            raise TypeError(self.print_error_mess_dist(other))

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other
        else:
            raise TypeError(self.print_error_mess_dist(other))

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other
        else:
            raise TypeError(self.print_error_mess_dist(other))

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other
        else:
            raise TypeError(self.print_error_mess_dist(other))

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
        else:
            raise TypeError(self.print_error_mess_dist(other))
