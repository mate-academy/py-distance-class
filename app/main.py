from __future__ import annotations


class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                f"unsupported operand type(s)for +: "
                f"'Distance' and '{type(other)}'"
            )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError(
                f"unsupported operand type(s) for +=: "
                f"'Distance' and '{type(other)}'"
            )

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: "
                f"'Distance' and '{type(other)}'"
            )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other != 0:
                return Distance(round(self.km / other, 2))
            else:
                raise ZeroDivisionError("division by zero")
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: "
                f"'Distance' and '{type(other)}'"
            )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                f"unsupported operand type(s) for <: "
                f"'Distance' and '{type(other)}'"
            )

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                f"unsupported operand type(s) for >: "
                f"'Distance' and '{type(other)}'"
            )

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                f"unsupported operand type(s) for ==: "
                f"'Distance' and '{type(other)}'"
            )

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for <=: "
                f"'Distance' and '{type(other)}'"
            )

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for >=: "
                f"'Distance' and '{type(other)}'"
            )
