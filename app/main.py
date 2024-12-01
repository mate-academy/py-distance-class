from typing import Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        if isinstance(other, int | float):
            return Distance(km=self.km + other)
        else:
            raise TypeError("Can't calculate")

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            raise TypeError("Can't calculate")

    def __mul__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            return Distance(km=self.km * other)
        else:
            raise TypeError("Can't calculate")

    def __truediv__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            if other == 0:
                raise ArithmeticError("Can't divide by ZERO")
            else:
                return Distance(km=round(self.km / other, 2))
        else:
            raise TypeError("Can't calculate")

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, int | float):
            return self.km < other
        else:
            raise TypeError("Can't calculate")

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, int | float):
            return self.km > other
        else:
            raise TypeError("Can't calculate")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, int | float):
            return self.km == other
        else:
            raise TypeError("Can't calculate")

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, int | float):
            return self.km <= other
        else:
            raise TypeError("Can't calculate")

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, int | float):
            return self.km >= other
        else:
            raise TypeError("Can't calculate")
