from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km: int = km

    @staticmethod
    def _get_value(other: Distance) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError("Operand must be Distance or number")

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        value = self._get_value(other)
        return Distance(self.km + value)

    def __iadd__(self, other: Distance) -> Distance:
        value = self._get_value(other)
        self.km += value
        return self

    def __mul__(self, other: "int, float") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Operand must be Distance or number")

    def __truediv__(self, other: "int, float") -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]

        if other == 0:
            raise ZeroDivisionError("Division by zero")

        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: Distance) -> bool:
        value = self._get_value(other)
        return self.km < value

    def __gt__(self, other: Distance) -> bool:
        value = self._get_value(other)
        return self.km > value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == self._get_value(other)

    def __le__(self, other: Distance) -> bool:
        value = self._get_value(other)
        return self.km <= value

    def __ge__(self, other: Distance) -> bool:
        value = self._get_value(other)
        return self.km >= value
