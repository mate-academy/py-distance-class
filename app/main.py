from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:g} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km:g})"

    # --- Helpers ---
    def _to_km(self, other: Union["Distance", Number]) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    # --- Addition ---
    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        return Distance(self.km + self._to_km(other))

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        self.km += self._to_km(other)
        return self

    # --- Multiplication ---
    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * float(other))

    # --- True Division ---
    def __truediv__(self, other: Number) -> "Distance":
        result = self.km / float(other)
        return Distance(round(result, 2))

    # --- Comparisons ---
    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self._to_km(other)

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > self._to_km(other)

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        return self.km == self._to_km(other)

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= self._to_km(other)

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= self._to_km(other)

