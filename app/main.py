from __future__ import annotations
from typing import Any, Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_val(self, other: Any) -> Union[float, int]:
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: Any) -> Distance:
        return Distance(self.km + self._get_val(other))

    def __iadd__(self, other: Any) -> Distance:
        self.km += self._get_val(other)
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        resultado = round(self.km / other, 2)
        return Distance(resultado)

    def __lt__(self, other: Any) -> bool:
        return self.km < self._get_val(other)

    def __gt__(self, other: Any) -> bool:
        return self.km > self._get_val(other)

    def __eq__(self, other: Any) -> bool:
        return self.km == self._get_val(other)

    def __le__(self, other: Any) -> bool:
        return self.km <= self._get_val(other)

    def __ge__(self, other: Any) -> bool:
        return self.km >= self._get_val(other)
