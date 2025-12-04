from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        num = self.get_number_value(other)
        return Distance(km=self.km + num)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        num = self.get_number_value(other)
        self.km = self.km + num
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        num = self.get_number_value(other)
        return self.km < num

    def __gt__(self, other: Distance | int | float) -> bool:
        num = self.get_number_value(other)
        return self.km > num

    def __eq__(self, other: Distance | int | float) -> bool:
        num = self.get_number_value(other)
        return self.km == num

    def __le__(self, other: Distance | int | float) -> bool:
        num = self.get_number_value(other)
        return self.km <= num

    def __ge__(self, other: Distance | int | float) -> bool:
        num = self.get_number_value(other)
        return self.km >= num

    @staticmethod
    def get_number_value(value: Distance | int | float) -> float | int:
        if hasattr(value, "km"):
            return value.km
        else:
            return value
