from __future__ import annotations
from types import NotImplementedType

Scalar = int | float


class Distance:
    def __init__(self, km: float = 0.0) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # --- dodawanie ---
    def __add__(self, other: Distance | Scalar) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + float(other))
        raise TypeError("Distance can be added only to Distance, int or float")

    def __radd__(self, other: Scalar) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Distance | Scalar) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += float(other)
            return self
        raise TypeError("Distance can be added only to Distance, int or float")

    # --- mnożenie: tylko skalar ---
    def __mul__(self, factor: Scalar) -> Distance:
        if isinstance(factor, (int, float)):
            return Distance(self.km * float(factor))
        raise TypeError("Distance can be multiplied only by int or float")

    def __rmul__(self, factor: Scalar) -> Distance:
        return self.__mul__(factor)

    # --- dzielenie: tylko skalar, wynik zaokrąglony do 2 miejsc ---
    def __truediv__(self, divisor: Scalar) -> Distance:
        if not isinstance(divisor, (int, float)):
            raise TypeError("Distance can be divided only by int or float")
        if divisor == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Distance(round(self.km / float(divisor), 2))

    # --- porównania: zawijamy sygnatury, NotImplemented dla obcych typów ---
    def __lt__(
        self,
        other: Distance | Scalar,
    ) -> bool | NotImplementedType:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < float(other)
        return NotImplemented

    def __le__(
        self,
        other: Distance | Scalar,
    ) -> bool | NotImplementedType:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= float(other)
        return NotImplemented

    def __gt__(
        self,
        other: Distance | Scalar,
    ) -> bool | NotImplementedType:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > float(other)
        return NotImplemented

    def __ge__(
        self,
        other: Distance | Scalar,
    ) -> bool | NotImplementedType:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= float(other)
        return NotImplemented

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return NotImplemented
