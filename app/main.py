from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def type_check(elem: Distance | int | float) -> int | float | None:
        if not isinstance(elem, Distance | int | float):
            raise TypeError("Other object should be Distance, "
                            "int or float type!")
        if isinstance(elem, Distance):
            elem = elem.km
        return elem

    def __add__(self, other: Distance | int | float) -> Distance:
        other = Distance.type_check(other)
        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        other = Distance.type_check(other)
        self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, int | float):
            raise TypeError("Other object should be int or float type!")
        self.km = self.km * other
        return self

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, int | float):
            raise TypeError("Other object should be int or float type!")
        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km < other

    def __gt__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km > other

    def __eq__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km == other

    def __le__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km <= other

    def __ge__(self, other: Distance | int | float) -> bool:
        other = Distance.type_check(other)
        return self.km >= other
