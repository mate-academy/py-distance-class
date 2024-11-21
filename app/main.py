from __future__ import annotations


class Distance:

    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @classmethod
    def check_other(cls, other: Distance | float | int) -> Distance:
        if not isinstance(other, Distance) and isinstance(other, int | float):
            return Distance(other)
        return other

    def __add__(self, other: Distance | float | int) -> Distance:
        return Distance(self.km + Distance.check_other(other).km)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        self.km += Distance.check_other(other).km
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        res = round(self.km / other, 2)
        return Distance(res)

    def __lt__(self, other: Distance | float | int) -> bool:
        return self.km < Distance.check_other(other).km

    def __gt__(self, other: Distance | float | int) -> bool:
        return self.km > Distance.check_other(other).km

    def __eq__(self, other: Distance | float | int) -> bool:
        return self.km == Distance.check_other(other).km

    def __le__(self, other: Distance | float | int) -> bool:
        return self.km <= Distance.check_other(other).km

    def __ge__(self, other: Distance | float | int) -> bool:
        return self.km >= Distance.check_other(other).km
