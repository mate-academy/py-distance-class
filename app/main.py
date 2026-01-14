from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(
            self, other: Union[Distance, int, float]) -> Distance:
        if (isinstance(other, Distance)):
            amount = other.km
        elif (isinstance(other, (int, float))):
            amount = float(other)
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'Distance' and '{type(other).__name__}'")
        return Distance(self.km + amount)

    def __iadd__(
            self, other: Union[Distance, int, float]) -> Distance:
        if (isinstance(other, Distance)):
            amount = other.km
        elif (isinstance(other, (int, float))):
            amount = float(other)
        else:
            raise TypeError(f"unsupported operand type(s) for +=: "
                            f"'Distance' and '{type(other).__name__}'")
        self.km += amount
        return self

    def __mul__(
            self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type(s) for *: "
                            f"'Distance' and '{type(other).__name__}'")
        amount = float(other)
        result_km = self.km * amount
        return Distance(result_km)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(f"unsupported operand type(s) for /: "
                            f"'Distance' and '{type(other).__name__}'")
        if other == 0:
            raise ZeroDivisionError("division by zero")
        new_km = self.km / other
        return Distance(round(new_km, 2))

    def _as_km(self, other: Union[Distance, int, float]) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return float(other)
        else:
            return NotImplemented

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        value = self._as_km(other)
        if value is NotImplemented:
            raise TypeError(f"'<' not supported between instances of "
                            f"'Distance' and '{type(other).__name__}'")
        return self.km < value

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        value = self._as_km(other)
        if value is NotImplemented:
            raise TypeError(f"'<' not supported between instances of "
                            f"'Distance' and '{type(other).__name__}'")
        return self.km > value

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        value = self._as_km(other)
        if value is NotImplemented:
            raise TypeError(f"'==' not supported between instances of "
                            f"'Distance' and '{type(other).__name__}'")
        return self.km == value

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        value = self._as_km(other)
        if value is NotImplemented:
            raise TypeError(f"'<=' not supported between instances of "
                            f"'Distance' and '{type(other).__name__}'")
        return self.km <= value

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        value = self._as_km(other)
        if value is NotImplemented:
            raise TypeError(f"'>=' not supported between instances of "
                            f"'Distance' and '{type(other).__name__}'")
        return self.km >= value
