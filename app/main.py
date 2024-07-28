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
            return Distance(
                self.km + other.km
            )
        elif isinstance(other, int | float):
            return Distance(
                self.km + other
            )
        else:
            raise TypeError("unsupported operand type for +")

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, int | float):
            self.km += other
            return self
        else:
            raise TypeError("unsupported operand type for +")

    def __mul__(self, other: int) -> Distance:
        return Distance(
            km=self.km * other
        )

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(
            km=round(self.km / other, 2)
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other
        else:
            raise TypeError("unsupported operand type for <")

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other
        else:
            raise TypeError("unsupported operand type for >")

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other
        else:
            raise TypeError("unsupported operand type for ==")

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other
        else:
            raise TypeError("unsupported operand type for <=")

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other
        else:
            raise TypeError("unsupported operand type for >=")
