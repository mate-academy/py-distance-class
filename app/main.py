from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            result = self.km * other
        else:
            return NotImplemented
        return Distance(result)

    def __truediv__(self, other: Any) -> Distance:
        if isinstance(other, (int, float)):
            result = round(self.km / other, 2)
        else:
            return NotImplemented
        return Distance(result)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            return NotImplemented
        return self.km < other_value

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            return NotImplemented
        return self.km > other_value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            return NotImplemented
        return self.km == other_value

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            return NotImplemented
        return self.km <= other_value

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            other_value = other.km
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            return NotImplemented
        return self.km >= other_value
