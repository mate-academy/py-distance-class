from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km_value(self, other: Union[int, float, Distance])\
            -> Union[int, float, None]:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return None

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        other_km = self._get_km_value(other)
        return Distance(self.km + other_km)

    def __radd__(self, other: Union[int, float, Distance]) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        other_km = self._get_km_value(other)
        self.km += other_km
        return self

    def __mul__(self, other: float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("__mul__ supports numeric values, not Distance")

    def __rmul__(self, other: Union[int, float]) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        other_km = self._get_km_value(other)
        return self.km < other_km

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        other_km = self._get_km_value(other)
        return self.km > other_km

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        other_km = self._get_km_value(other)
        return self.km == other_km

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        return not self > other

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        return not self < other
