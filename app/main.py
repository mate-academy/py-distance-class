from __future__ import annotations

class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_km(self, other: Distance | int | float) -> float:
        """Допоміжний метод для отримання значення km з іншого об'єкта або числа."""
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(f"Unsupported type: {type(other)}")

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._get_km(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self._get_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._get_km(other)
