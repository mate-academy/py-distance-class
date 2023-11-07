from typing import TypeVar

#  "I'm not sure if this is the best solution"
#  " for creating accurate type annotations, "
#  "but the others are not working for me."

T = TypeVar("T", bound="Distance")


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: T | int | float) -> T:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Unsupported operand types")

    def __iadd__(self, other: T | int | float) -> T:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, (int, float)):
            self.km += other
        if not isinstance(other, (Distance, int, float)):
            raise TypeError("Unsupported operand types")
        return self

    def __mul__(self, other: int | float) -> T:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported operand types")

    def __truediv__(self, other: int | float) -> T:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported operand types")

    def __lt__(self, other: T | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Unsupported operand types")

    def __gt__(self, other: T | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Unsupported operand types")

    def __eq__(self, other: T | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Unsupported operand types")

    def __le__(self, other: T | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Unsupported operand types")

    def __ge__(self, other: T | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Unsupported operand types")
