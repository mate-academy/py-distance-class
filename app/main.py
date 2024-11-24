from typing import Any


class Distance:
    def __init__(self, km: [int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __iadd__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: "
                f"'Distance' and '{type(other).__name__}'"
            )
        return self

    def __mul__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("'__mul__' method should "
                            "not accept Distance instance")
        elif isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __truediv__(self, other: Any) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError("'__truediv__' method should "
                            "not accept Distance instance")
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            num = round(self.km / other, 2)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for /: "
                f"'Distance' and '{type(other).__name__}'"
            )
        return Distance(num)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(f"Unsupported operand type(s) for <: "
                            f"'Distance' and '{type(other).__name__}'"
                            )

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(f"Unsupported operand type(s) for >: "
                            f"'Distance' and '{type(other).__name__}'"
                            )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(f"Unsupported operand type(s) for ==: "
                            f"'Distance' and '{type(other).__name__}'"
                            )

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(f"Unsupported operand type(s) for <=: "
                            f"'Distance' and '{type(other).__name__}'"
                            )

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(f"Unsupported operand type(s) for >=: "
                            f"'Distance' and '{type(other).__name__}'"
                            )
