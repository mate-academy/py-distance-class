from __future__ import annotations


class Distance:
    def __init__(self, km: float | int) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Параметр 'km' має бути числом (int або float)")
        self.km: float | int = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(self, other: float | int | Distance) -> float | int:
        if isinstance(other, Distance):
            return other.km
        return other

    def __add__(self, other: float | int | Distance) -> Distance:
        number = self._get_value(other)
        return Distance(self.km + number)

    def __iadd__(self, other: float | int | Distance) -> Distance:
        number = self._get_value(other)
        self.km += number
        return self

    def __mul__(self, other: float | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        result = round(self.km / other, 2)
        return Distance(result)

    def __lt__(self, other: float | int | Distance) -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: float | int | Distance) -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: float | int | Distance) -> bool:
        return self.km == self._get_value(other)

    def __le__(self, other: float | int | Distance) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: float | int | Distance) -> bool:
        return self.km >= self._get_value(other)
