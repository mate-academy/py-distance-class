from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
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
                f"Unsupported operand type(s) for +: 'Distance' and "
                f"'{type(other).__name__}'"
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
                f"Unsupported operand type(s) for +=: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __mul__(self, value: int) -> Distance:
        return Distance(self.km * value)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(
                f"Unsupported operand type(s) for /: 'Distance' and "
                f"'{type(other).__name__}'"
            )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(f"Unsupported operand type(s) for <: 'Distance' "
                            f"and {type(other).__name__}")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(f"Unsupported operand type(s) for >: 'Distance' "
                            f"and {type(other).__name__}")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(f"Unsupported operand type(s) for ==: 'Distance' "
                            f"and {type(other).__name__}")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(f"Unsupported operand type(s) for <=: 'Distance' "
                            f"and {type(other).__name__}")

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(f"Unsupported operand type(s) for >=: 'Distance' "
                            f"and {type(other).__name__}")
