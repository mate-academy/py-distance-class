from typing import Self


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Self | int | float) -> Self:
        if isinstance(other, Distance):
            total = self.km + other.km
        elif isinstance(other, (int, float)):
            total = self.km + float(other)
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: 'Distance' "
                "and '{}'".format(type(other).__name__)
            )
        return Distance(total)

    def __iadd__(self, other: Self | int | float) -> Self:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += float(other)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +=: "
                f"'Distance' and '{type(other).__name__}'"
            )
        return self

    def __mul__(self, other: int | float) -> Self:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"Unsupported operand type(s) for *: "
                f"'Distance' and '{type(other).__name__}'"
            )
        return Distance(self.km * other)

    def __rmul__(self, other: int | float) -> Self:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Self:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"Unsupported operand type(s) for /: "
                f"'Distance' and '{type(other).__name__}'"
            )
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return NotImplemented

    def __lt__(self, other: Self | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < float(other)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > float(other)
        return NotImplemented

    def __le__(self, other: Self | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= float(other)
        return NotImplemented

    def __ge__(self, other: Self | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= float(other)
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km != other.km
        if isinstance(other, (int, float)):
            return self.km != float(other)
        return NotImplemented
