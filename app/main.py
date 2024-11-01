from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if not isinstance(other, Distance):
            other = Distance(other)
        return Distance(km=self.km + other.km)

    def __radd__(self, other: Any) -> Any:
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other: Any) -> Any:
        if not isinstance(other, Distance):
            other = Distance(other)
        self.km += other.km
        return self

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            raise TypeError
        return Distance(km=self.km * other)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            raise TypeError
        km = self.km / other
        rounded = round(km, 2)
        return Distance(rounded)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km == other.km

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km > other.km

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km >= other.km

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km < other.km

    def __le__(self, other: Any) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km <= other.km
