from __future__ import annotations

from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km!r})"

    # Helper to coerce Distance | int | float to km float
    def _coerce_other_to_km(self, other: Union[int, float, "Distance"]) -> float | NotImplemented:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        return NotImplemented

    # arithmetic
    def __add__(self, other: int | float | Distance) -> Distance | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __radd__(self, other: int | float | Distance) -> Distance | NotImplemented:
        return self.__add__(other)

    def __iadd__(self, other: int | float | Distance) -> Distance | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other: int | float) -> Distance | NotImplemented:
        if isinstance(other, (int, float)):
            return Distance(self.km * float(other))
        return NotImplemented

    def __rmul__(self, other: int | float) -> Distance | NotImplemented:
        return self.__mul__(other)

    def __truediv__(self, other: int | float) -> Distance | NotImplemented:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / float(other), 2))
        return NotImplemented

    # comparisons
    def __eq__(self, other: int | float | Distance) -> bool | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other: int | float | Distance) -> bool | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other: int | float | Distance) -> bool | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __gt__(self, other: int | float | Distance) -> bool | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __ge__(self, other: int | float | Distance) -> bool | NotImplemented:
        other_km = self._coerce_other_to_km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km
