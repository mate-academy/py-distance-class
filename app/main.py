from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km: int = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            km = other.km
        else:
            km = other
        return Distance(self.km + km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance | NotImplemented:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance | NotImplemented:
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        other_value = other.km if isinstance(other, Distance) else other
        return self.km < other_value

    def __gt__(self, other: Distance | int | float) -> bool:
        other_value = other.km if isinstance(other, Distance) else other
        return self.km > other_value

    def __eq__(self, other: Distance | int | float) -> bool:
        other_value = other.km if isinstance(other, Distance) else other
        return self.km == other_value

    def __le__(self, other: Distance | int | float) -> bool:
        other_value = other.km if isinstance(other, Distance) else other
        return self.km <= other_value

    def __ge__(self, other: Distance | int) -> bool:
        other_value = other.km if isinstance(other, Distance) else other
        return self.km >= other_value
