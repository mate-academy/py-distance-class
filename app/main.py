from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number")
        if km <= 0:
            raise ValueError("Distance cannot be negative or zero")

        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | float | int) -> "Distance":
        if isinstance(other, (float, int)):
            other = Distance(other)
        if not isinstance(other, Distance):
            raise TypeError("Can only add another Distance or a number")
        if other.km <= 0:
            raise ValueError("Cannot add a negative or zero distance")
        return Distance(self.km + other.km)

    def __iadd__(self, other: "Distance" | float | int) -> "Distance":
        if isinstance(other, (int, float)):
            other = Distance(other)
        if not isinstance(other, Distance):
            raise TypeError("Can only add another Distance or a number")
        if other.km <= 0:
            raise ValueError("Cannot add a negative or zero distance")
        self.km += other.km
        return self

    def __mul__(self, other: float | int) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply by a number")
        if other <= 0:
            raise ValueError("Cannot multiply by a negative or zero value")
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError("Can only divide by a number")
        if other <= 0:
            raise ValueError("Cannot divide by a negative or zero value")
        result = round(self.km / other, 2)
        return Distance(result)
    # __lt__, __gt__, __eq__, __le__, __ge__

    def __get_km(self, other: "Distance" | float | int) -> float:
        if isinstance(other, (int, float)):
            return other
        if isinstance(other, Distance):
            return other.km
        raise TypeError("Can only compare with another Distance or a number")

    def __lt__(self, other: "Distance" | float | int) -> bool:
        other_km = self.__get_km(other)
        return self.km < other_km

    def __gt__(self, other: "Distance" | float | int) -> bool:
        other_km = self.__get_km(other)
        return self.km > other_km

    def __eq__(self, other: "Distance" | float | int) -> bool:
        other_km = self.__get_km(other)
        return self.km == other_km

    def __le__(self, other: "Distance" | float | int) -> bool:
        other_km = self.__get_km(other)
        return self.km <= other_km

    def __ge__(self, other: "Distance" | float | int) -> bool:
        other_km = self.__get_km(other)
        return self.km >= other_km
