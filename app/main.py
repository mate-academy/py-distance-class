from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        raise TypeError(
            f"unsupported operand type(s) for +: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError(
            f"unsupported operand type(s) for +=: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        raise TypeError(
            f"unsupported operand type(s) for *: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if not other:
                raise ZeroDivisionError("Division by zero")
            return Distance(km=round(self.km / other, 2))
        raise TypeError(
            f"unsupported operand type(s) for /: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
            f"unsupported operand type(s) for comparing: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(
            f"unsupported operand type(s) for comparing: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        raise TypeError(
            f"unsupported operand type(s) for comparing: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __le__(self, other: Distance | int | float) -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return not self.__lt__(other)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
