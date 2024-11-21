from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def __verify_data(
        cls,
        data: int | float | Distance
    ) -> int | float | Distance:
        if type(data) == int or type(data) == float:
            value = data
        elif type(data) == Distance:
            value = data.km
        return value

    def __add__(self, other: int | float | Distance) -> Distance:
        value = Distance.__verify_data(other)
        return Distance(self.km + value)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        value = Distance.__verify_data(other)
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: int | float | Distance) -> bool:
        value = Distance.__verify_data(other)
        return self.km == value

    def __gt__(self, other: int | float | Distance) -> bool:
        value = Distance.__verify_data(other)
        return self.km > value

    def __ge__(self, other: int | float | Distance) -> bool:
        value = Distance.__verify_data(other)
        return self.km >= value

    def __lt__(self, other: int | float | Distance) -> bool:
        value = Distance.__verify_data(other)
        return self.km < value

    def __le__(self, other: int | float | Distance) -> bool:
        value = Distance.__verify_data(other)
        return self.km <= value
