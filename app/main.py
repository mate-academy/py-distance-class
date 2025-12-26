from typing import Union

TOther = Union[int, float, "Distance"]


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    @staticmethod
    def instance_check(other: TOther) -> bool:
        return isinstance(other, (int, float))

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: TOther) -> "Distance":
        if self.instance_check(other):
            return Distance(km=self.km + other)

        return Distance(km=self.km + other.km)

    def __iadd__(self, other: TOther) -> "Distance":
        if self.instance_check(other):
            self.km = self.km + other
        else:
            self.km = self.km + other.km

        return self

    def __mul__(self, other: TOther) -> "Distance":
        return Distance(km=self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: TOther) -> bool:
        if self.instance_check(other):
            return self.km < other

        return self.km < other.km

    def __gt__(self, other: TOther) -> bool:
        if self.instance_check(other):
            return self.km > other

        return self.km > other.km

    def __eq__(self, other: TOther) -> bool:
        if self.instance_check(other):
            return self.km == other

        return self.km == other.km

    def __le__(self, other: TOther) -> bool:
        if self.instance_check(other):
            return self.km <= other

        return self.km <= other.km

    def __ge__(self, other: TOther) -> bool:
        if self.instance_check(other):
            return self.km >= other

        return self.km >= other.km
