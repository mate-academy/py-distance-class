from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, num: int | float | Distance) -> Distance | str:
        if isinstance(num, (int, float)):
            return Distance(self.km + num)
        elif isinstance(num, Distance):
            return Distance(self.km + num.km)
        return "Invalid number!"

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, num: int | float) -> Distance:
        if isinstance(num, (int, float)):
            return Distance(self.km * num)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int | float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int | float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int | float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int | float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int | float)):
            return self.km >= other
        return NotImplemented
