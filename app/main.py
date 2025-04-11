from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def type_other(other: Union["Distance", float, int]) -> float:
        if type(other) == Distance:
            return other.km
        else:
            return other

    def __add__(self, other: Union["Distance", float, int]) -> "Distance":
        new_km = self.km + self.type_other(other)
        return Distance(new_km)

    def __iadd__(self, other: Union["Distance", float, int]) -> "Distance":
        self.km += self.type_other(other)
        return self

    def __mul__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Can't multiply Distance by non-numeric type")

    def __truediv__(self, other: Union["Distance", float, int]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Can't decrees Distance by non-numeric type")

    def __lt__(self, other: Union["Distance", float, int]) -> bool:
        return self.km < self.type_other(other)

    def __le__(self, other: Union["Distance", float, int]) -> bool:
        return self.km <= self.type_other(other)

    def __gt__(self, other: Union["Distance", float, int]) -> bool:
        return self.km > self.type_other(other)

    def __ge__(self, other: Union["Distance", float, int]) -> bool:
        return self.km >= self.type_other(other)

    def __eq__(self, other: Union["Distance", float, int]) -> bool:
        return self.km == self.type_other(other)
