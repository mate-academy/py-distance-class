from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self
        self.km += other.km
        return self

    def __mul__(self, number: int | float | Distance) -> Distance:
        return Distance(self.km * number)

    def __truediv__(self, number: int | float | Distance) -> Distance:
        return Distance(round(self.km / number, 2))

    def __lt__(self, number: int) -> bool:
        if self.km < number:
            return True
        return False

    def __gt__(self, number: int) -> bool:
        if self.km > number:
            return True
        return False

    def __eq__(self, number: int) -> bool:
        if self.km == number:
            return True
        return False

    def __le__(self, number: int) -> bool:
        if self.km <= number:
            return True
        return False

    def __ge__(self, number: int) -> bool:
        if self.km >= number:
            return True
        return False
