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
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            self.km *= other
            return self

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            is_equal = self.km == other.km
        else:
            is_equal = self.km == other
        return is_equal

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            is_less_than = self.km < other.km
        else:
            is_less_than = self.km < other
        return is_less_than

    def __gt__(self, other: Distance | int | float) -> bool:
        return not self.__lt__(other) and not self.__eq__(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self.__lt__(other)
