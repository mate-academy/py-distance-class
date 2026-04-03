from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_value(value: Distance | int | float) -> int | float:
        if isinstance(value, Distance):
            return value.km
        return value

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + Distance.get_value(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += Distance.get_value(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < Distance.get_value(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > Distance.get_value(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= Distance.get_value(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= Distance.get_value(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == Distance.get_value(other)
