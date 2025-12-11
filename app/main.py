from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        self.km: float | int = km

    @staticmethod
    def _value(other: float | int | Distance) -> float | int:
        return other.km if isinstance(other, Distance) else other

    @staticmethod
    def _fmt_num(num: float | int) -> str:
        if isinstance(num, float):
            return str(int(num)) if num.is_integer() else str(num)
        return str(num)

    def __str__(self) -> str:
        return f"Distance: {self._fmt_num(self.km)} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self._fmt_num(self.km)})"

    def __add__(self, other: float | int | Distance) -> Distance:
        return Distance(self.km + self._value(other))

    def __iadd__(self, other: float | int | Distance) -> Distance:
        self.km += self._value(other)
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: float | int | Distance) -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: float | int | Distance) -> bool:
        return self.km > self._value(other)

    def __eq__(self, other: float | int | Distance) -> bool:
        return self.km == self._value(other)

    def __le__(self, other: float | int | Distance) -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: float | int | Distance) -> bool:
        return self.km >= self._value(other)
