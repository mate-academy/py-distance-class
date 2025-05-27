from __future__ import division
from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if not isinstance(other, (int, float, Distance)):
            raise TypeError(
                f"Cannot compose Distance with {type(other).__name__}"
            )
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float, Distance)):
            self.km += other.km if isinstance(other, Distance) else other
            return self
        raise TypeError(
            f"Unsupported operand type(s) "
            f"for +=: 'Distance' and '{type(other).__name__}'"
        )

    def __mul__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"You cannot multiply Distance with {type(other).__name__}"
        )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"Unsupported operand type(s) "
            f"for /: 'Distance' and '{type(other).__name__}'"
        )

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        return NotImplemented

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        return NotImplemented

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        return NotImplemented

    def __le__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        return NotImplemented

    def __ge__(self, other: int | float | Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        return NotImplemented
