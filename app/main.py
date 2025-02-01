from __future__ import annotations


class Distance:
    def __init__(self, km: any) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __ne__(self, other: int | float) -> bool:
        return self.km != other
