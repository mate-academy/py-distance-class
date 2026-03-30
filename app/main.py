from __future__ import annotations
from typing import Union, Any


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def _get_km(self, other: Any) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError("Unsupported type")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported type")

    def __rmul__(self, other: Union[int, float]) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError("Unsupported type")
        if other == 0:
            raise ZeroDivisionError("The second argument cannot be zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= self._get_km(other)
