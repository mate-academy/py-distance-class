from __future__ import annotations

from functools import total_ordering
from typing import Any


@total_ordering
class Distance:
    def __init__(self, km: float) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        km_str = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_repr = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance(km={km_repr})"

    def _value(self, other: Any) -> float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        return None

    def __add__(self, other: float | int | Distance) -> Distance:
        other_value = self._value(other)
        if other_value is not None:
            return Distance(self.km + other_value)
        return NotImplemented  # type: ignore[return-value]

    def __radd__(self, other: float | int | Distance) -> Distance:
        return self.__add__(other)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        other_value = self._value(other)
        if other_value is not None:
            self.km += other_value
            return self
        return NotImplemented  # type: ignore[return-value]

    def __mul__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented  # type: ignore[return-value]

    def __rmul__(self, other: float | int) -> Distance:
        return self.__mul__(other)

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result_km = round(self.km / other, 2)
            return Distance(result_km)
        return NotImplemented  # type: ignore[return-value]

    def __eq__(self, other: Any) -> bool:
        other_value = self._value(other)
        if other_value is not None:
            return self.km == other_value
        return NotImplemented  # type: ignore[return-value]

    def __lt__(self, other: Any) -> bool:
        other_value = self._value(other)
        if other_value is not None:
            return self.km < other_value
        return NotImplemented  # type: ignore[return-value]
