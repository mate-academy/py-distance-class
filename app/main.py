from typing import Optional


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Optional["Distance"]) -> "Distance":
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return Distance(km=self.km + other.km)

    def __iadd__(
            self, other: int | float | Optional["Distance"]
    ) -> "Distance":
        if not isinstance(other, Distance):
            other = Distance(km=other)
        self.km += other.km
        return self

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(km=round(self.km / other, 2))
        raise TypeError(f"Cannot multiply Distance by {type(other).__name__}")

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        raise TypeError(f"Cannot multiply Distance by {type(other).__name__}")

    def __lt__(self, other: int | float | Optional["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km < other.km

    def __gt__(self, other: int | float | Optional["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km > other.km

    def __eq__(self, other: int | float | Optional["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km == other.km

    def __le__(self, other: int | float | Optional["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km <= other.km

    def __ge__(self, other: int | float | Optional["Distance"]) -> bool:
        if not isinstance(other, Distance):
            other = Distance(km=other)
        return self.km >= other.km
