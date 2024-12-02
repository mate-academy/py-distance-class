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
        if self._is_number(other):
            return Distance(km=self.km + other)
        else:
            raise TypeError("Unsupported operand type for + operator")

    def __iadd__(self, other: Any) -> "Distance":
        if self._is_number(other):
            self.km += other
            return self
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            raise TypeError("Unsupported operand type for += operator")

    def __mul__(self, other: Any) -> "Distance":
        if self._is_number(other):
            return Distance(km=self.km * other)
        else:
            raise TypeError("Unsupported operand type for * operator")

    def __truediv__(self, other: Any) -> "Distance":
        if isinstance(other, int | float):
            if other == 0:
                raise ArithmeticError("Can't divide by ZERO")
            else:
                return Distance(km=round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type for / operator")

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if self._is_number(other):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for < operator")

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if self._is_number(other):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for > operator")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if self._is_number(other):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type for == operator")

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if self._is_number(other):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type for <= operator")

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if self._is_number(other):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type for >= operator")

    @staticmethod
    def _is_number(obj: Any) -> bool:
        return isinstance(obj, (int, float))
