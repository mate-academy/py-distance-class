from typing import Union


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type(s) for +: 'Distance' and {type(other)}")

        return Distance(self.km + (other.km if isinstance(other, Distance) else other))

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if not isinstance(other, (Distance, int, float)):
            raise TypeError(f"unsupported operand type(s) for +=: 'Distance' and {type(other)}")

        self.km += (other.km if isinstance(other, Distance) else other)
        return self

    def __mul__(self, factor: Union[int, float]) -> "Distance":
        if not isinstance(factor, (int, float)):
            raise TypeError(f"unsupported operand type(s) for *: 'Distance' and {type(factor)}")

        return Distance(self.km * factor)

    def __truediv__(self, divisor: Union[int, float]) -> "Distance":
        if not isinstance(divisor, (int, float)):
            raise TypeError(f"unsupported operand type(s) for /: 'Distance' and {type(divisor)}")
        if divisor == 0:
            raise ZeroDivisionError("division by zero is not allowed")

        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km >= (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == (other.km if isinstance(other, Distance) else other)
