from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | (int, float)) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise ValueError("Unsupported operand type for +")

    def __iadd__(self, other: Distance | (int, float)) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise ValueError("Unsupported operand type for +=")
        return self

    def __mul__(self, factor: int | float) -> Distance:
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        else:
            raise TypeError(
                "Multiplication of Distance instances is not supported."
            )

    def __truediv__(self, divisor: int | float) -> Distance:
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self, other: Distance | (int, float)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise ValueError("Unsupported operand type for <")

    def __gt__(self, other: Distance | (int, float)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise ValueError("Unsupported operand type for >")

    def __eq__(self, other: Distance | (int, float)) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise ValueError("Unsupported operand type for ==")

    def __le__(self, other: Distance | (int, float)) -> bool:
        return not self > other

    def __ge__(self, other: Distance | (int, float)) -> bool:
        return not self < other
