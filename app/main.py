from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def verify_data(other: int | float | Distance) -> int | float:
        return other if isinstance(other, (int, float)) else other.km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        value = self.verify_data(other)
        return Distance(self.km + value)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        value = self.verify_data(other)
        self.km += value
        return self

    def __mul__(self, other: int | float) -> None:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> None:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        value = self.verify_data(other)
        return self.km < value

    def __gt__(self, other: int | float | Distance) -> bool:
        value = self.verify_data(other)
        return self.km > value

    def __eq__(self, other: int | float | Distance) -> bool:
        value = self.verify_data(other)
        return self.km == value

    def __le__(self, other: int | float | Distance) -> bool:
        value = self.verify_data(other)
        return self.km <= value

    def __ge__(self, other: int | float | Distance) -> bool:
        return self.km >= other
