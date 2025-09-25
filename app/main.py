from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for +: 'Distance' and '{type(other).__name__}'")

        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
            return self

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for +: 'Distance' and '{type(other).__name__}'")

        self.km += other.km
        return self

    def __mul__(self, other: float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type(s) for *: 'Distance' and '{type(other).__name__}'")

        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type(s) for /: 'Distance' and '{type(other).__name__}'")

        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for <: 'Distance' and '{type(other).__name__}'")

        return self.km < other.km

    def __gt__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for >: 'Distance' and '{type(other).__name__}'")

        return self.km > other.km

    def __eq__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for ==: 'Distance' and '{type(other).__name__}'")

        return self.km == other.km

    def __le__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for <=: 'Distance' and '{type(other).__name__}'")

        return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other

        if not isinstance(other, Distance):
            raise TypeError(f"unsupported operand type(s) for >=: 'Distance' and '{type(other).__name__}'")

        return self.km >= other.km
