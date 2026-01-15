from typing import Any


class Distance:
    def __init__(self: Any, km: float | int) -> Any:
        self.km = km

    def __str__(self: Any) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Any) -> str:
        return f"Distance(km={self.km})"

    def __add__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +")
        return self

    def __mul__(self: Any, other: Any) -> Any:
        return Distance(self.km * other)

    def __truediv__(self: Any, other: Any) -> Any:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for <")

    def __gt__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for >")

    def __eq__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type for ==")

    def __le__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type for <=")

    def __ge__(self: Any, other: Any) -> Any:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type for >=")
