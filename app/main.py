from typing import Union


class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        if self.km == 1:
            return f"Distance: {self.km} kilometer."
        else:
            return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(km=self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (float, int)):
            self.km += other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        return Distance(km=self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (float, int)):
            return self.km < other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (float, int)):
            return self.km > other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (float, int)):
            return self.km == other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (float, int)):
            return self.km <= other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (float, int)):
            return self.km >= other
        else:
            raise TypeError("Operand must be a Distance instance or a number.")
