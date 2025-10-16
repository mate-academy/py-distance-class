from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            f"unsupported operand type(s) for +: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __iadd__(self, other: Distance | float) -> Distance:
        result = self + other
        self.km = result.km
        return self

    def __mul__(self, other: float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"unsupported operand type(s) for *: 'Distance' and "
                f"'{type(other).__name__}'"
            )
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"unsupported operand type(s) for /: 'Distance' and "
                f"'{type(other).__name__}'"
            )
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
            f"unsupported operand type(s) for <: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __le__(self, other: Distance | float) -> bool:
        return self < other or self == other

    def __gt__(self, other: Distance | float) -> bool:
        if isinstance(other, Distance):
            return other < self
        if isinstance(other, (int, float)):
            return other < self.km
        raise TypeError(
            f"unsupported operand type(s) for >: 'Distance' and "
            f"'{type(other).__name__}'"
        )

    def __ge__(self, other: Distance | float) -> bool:
        return self > other or self == other
