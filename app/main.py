from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + float(other))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: 'Distance' and "
                f"'{type(other).__name__}'"
            )
        return self

    def __mul__(self, other: Union[float, int]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * float(other))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __truediv__(self, other: Union[float, int]) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Division by zero is not allowed.")
            result = self.km / other
            return Distance(round(result, 2))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for "
                f"/: 'Distance' and '{type(other).__name__}'"
            )

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for <: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for >: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for ==: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for <=: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for >=: 'Distance' and "
                f"'{type(other).__name__}'"
            )
