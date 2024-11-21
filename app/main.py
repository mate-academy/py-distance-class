from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(f"cannot multiply {type(self)} by {type(other)}")
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            raise TypeError(f"cannot multiply {type(self)} by {type(other)}")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: int | float | Distance) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int | float | Distance) -> bool:
        return False if self.__gt__(other) is True else True

    def __ge__(self, other: int | float | Distance) -> bool:
        return False if self.__lt__(other) is True else True
