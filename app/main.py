from __future__ import annotations
from typing import Any


class Distance:
    distances = {}

    def __init__(self, run: float) -> None:
        self.km = run
        Distance.distances[self.km] = self

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            total_distance = self.km + other.km
        else:
            total_distance = self.km + other
        result = Distance(total_distance)
        Distance.distances[result.km] = result
        return result

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other_number: float) -> Distance:
        total_distance = self.km * other_number
        result = Distance(total_distance)
        Distance.distances[result.km] = result
        return result

    def __truediv__(self, other_number: float) -> Distance:
        total_distance = round(self.km / other_number, 2)
        result = Distance(total_distance)
        Distance.distances[result.km] = result
        return result

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
