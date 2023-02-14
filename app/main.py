from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    @staticmethod
    def __typecheck__(other: int | float | Distance) -> None:
        return isinstance(other, Distance)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> float:
        if Distance.__typecheck__(other):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> float:
        if Distance.__typecheck__(other):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> float:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> float:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if Distance.__typecheck__(other):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if self.__eq__(other):
            return False
        return not self.__lt__(other)

    def __eq__(self, other: int | float | Distance) -> bool:
        if Distance.__typecheck__(other):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        if Distance.__typecheck__(other):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int | float | Distance) -> bool:
        if self.__eq__(other):
            return True
        return not self.__le__(other)
