from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: Number = km

    @staticmethod
    def _get_km(value: Union[Distance, Number]) -> Union[Number, None]:
        """Отримати значення km або None, якщо тип не підходить."""
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return None

    # ------- STRING REPRESENTATION -------

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # ------- ADDITION -------

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return Distance(self.km + km)

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        self.km += km
        return self

    # ------- MULTIPLICATION -------

    def __mul__(self, other: Number) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    # ------- TRUE DIVISION -------

    def __truediv__(self, other: Number) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        result = round(self.km / other, 2)
        return Distance(result)

    # ------- COMPARISON OPERATORS -------

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km < km

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km > km

    def __eq__(self, other: Union[Distance, Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km == km

    def __le__(self, other: Union[Distance, Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km <= km

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        km = self._get_km(other)
        if km is None:
            return NotImplemented
        return self.km >= km
