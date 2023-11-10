from __future__ import annotations


class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def __verify_data(cls, other: int | float | Distance) -> bool:
        if not isinstance(other, (Distance, int, float)):
            raise TypeError("Other must be int, float or Distance")
        return other if isinstance(other, (int, float)) else other.km

    def __add__(self, other: int | float | Distance) -> Distance:
        value = self.__verify_data(other)
        return Distance(self.km + value)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        value = self.__verify_data(other)
        self.km += value
        return self

    def __mul__(self, other: int | float) -> int:
        if not isinstance(other, (int, float)):
            raise TypeError("Other must be int or float")
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> float:
        if not isinstance(other, (int, float)):
            raise TypeError("Other must be int or float ")
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))


    def __eq__(self, other: int | float | Distance) -> bool:
        value = self.__verify_data(other)
        return self.km == value

    def __lt__(self, other: int | float | Distance) -> bool:
        value = self.__verify_data(other)
        return self.km < value

    def __le__(self, other: int | float | Distance) -> bool:
        value = self.__verify_data(other)
        return self.km <= value

    def __gt__(self, other: int | float | Distance) -> bool:
        value = self.__verify_data(other)
        return self.km > value

    def __ge__(self, other: int | float | Distance) -> bool:
        value = self.__verify_data(other)
        return self.km >= value
