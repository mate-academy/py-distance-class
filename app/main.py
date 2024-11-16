from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            raise TypeError(f"Unsupported operand type(s) for "
                            f"+: 'Distance' and '{type(other)}'")

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError(f"Unsupported operand type(s) for "
                            f"+=: 'Distance' and '{type(other)}'")
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(f"Unsupported type for "
                            f"multiplication: {type(other)}")

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(km=round(self.km / other, 2))
        raise TypeError("Can only divide Distance by a scalar (int or float).")

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")
