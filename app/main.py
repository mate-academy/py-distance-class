from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self

        if isinstance(other, (int, float)):
            self.km += other
            return self

        return NotImplemented

    def __mul__(self, num: int | float) -> Distance:
        if isinstance(num, (int, float)):
            return Distance(self.km * num)

        return NotImplemented

    def __truediv__(self, num: float | int) -> Distance:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        if not isinstance(num, (int, float)):
            return NotImplemented

        new_km = round(self.km / num, 2)
        return Distance(new_km)

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km

        if isinstance(other, (int, float)):
            return self.km < other

        return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        if isinstance(other, (int, float)):
            return self.km > other

        return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        if isinstance(other, (int, float)):
            return self.km == other

        return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

        if isinstance(other, (int, float)):
            return self.km <= other

        return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km

        if isinstance(other, (int, float)):
            return self.km >= other

        return NotImplemented
