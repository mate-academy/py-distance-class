# app/main.py
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import Union

Number = Union[int, float]


class Distance:
    """Representa uma distância em quilômetros."""

    def __init__(self, km: Number) -> None:
        self.km: float = float(km)

    # --------- helpers internos ---------
    @staticmethod
    def _fmt(value: float) -> str:
        """Formata sem sufixo .0 quando inteiro exato."""
        return format(value, "g")

    @staticmethod
    def _to_km(other: Union["Distance", Number]) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        raise TypeError(
            f"unsupported operand type: {type(other)!r}"
        )

    # --------- representação ---------
    def __str__(self) -> str:
        return f"Distance: {self._fmt(self.km)} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self._fmt(self.km)})"

    # --------- aritmética ---------
    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        km_sum = self.km + self._to_km(other)
        return Distance(km_sum)

    def __radd__(self, other: Number) -> "Distance":
        # permite 10 + Distance(5)
        return self.__add__(other)

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        self.km += self._to_km(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * float(other))

    def __rmul__(self, other: Number) -> "Distance":
        # permite 3 * Distance(5)
        return self.__mul__(other)

    def __truediv__(self, other: Number) -> "Distance":
        if not isinstance(other, (int, float)):
            return NotImplemented
        divisor = float(other)
        if divisor == 0.0:
            raise ZeroDivisionError("division by zero")
        # Arredonda para 2 casas (half up), p/ casar com os testes:
        # 50/3 -> 16.67, 30/7 -> 4.29, 12.6/3.3 -> 3.82
        rounded_km = (
            Decimal(str(self.km)) / Decimal(str(divisor))
        ).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
        return Distance(float(rounded_km))

    # --------- comparações ---------
    def _cmp_value(self, other: Union["Distance", Number]) -> float:
        return self._to_km(other)

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self._cmp_value(other)

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= self._cmp_value(other)

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > self._cmp_value(other)

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= self._cmp_value(other)

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, (int, float, Distance)):
            return self.km == self._to_km(other)  # type: ignore[arg-type]
        return NotImplemented  # permite comparação simétrica
