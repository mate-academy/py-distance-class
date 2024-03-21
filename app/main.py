from __future__ import division
from typing import Union


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)

    def __sub__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError(
                f"unsupported operand type(s) for -: "
                f"'Distance' and '{type(other)}'"
            )
        elif isinstance(other, (int, float)):
            return Distance(self.km - other)

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: "
                f"'Distance' and {type(other)}"
            )

    def __truediv__(self, number: int | float) -> "Distance":
        if isinstance(number, (int, float)):
            return Distance(round(self.km / number, 2))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for /: "
                f"'Distance' and {type(number)}"
            )

    def __iadd__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            raise TypeError(
                "Unsupported operand type(s) for +=: "
                "'Distance' and '{}'".format(
                    type(other)
                )
            )

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return not self.__lt__(other)

    def __ne__(self, other: Union["Distance", int, float]) -> bool:
        return not self.__eq__(other)
