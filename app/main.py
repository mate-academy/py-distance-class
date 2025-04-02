from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            km_to_add = other.km
        elif isinstance(other, (int, float)):
            km_to_add = other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: "
                f"'Distance' and '{type(other).__name__}'"
            )

        return Distance(self.km + km_to_add)

    def __iadd__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            km_to_add = other.km
        elif isinstance(other, (int, float)):
            km_to_add = other
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: "
                f"'Distance' and '{type(other).__name__}'"
            )
        self.km += km_to_add
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __truediv__(self, other: int | float) -> Distance:
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif isinstance(other, (int, float)):
            divided = round(self.km / other, 2)
            return Distance(divided)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for /: "
                f"'Distance' and '{type(other).__name__}'"
            )

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
