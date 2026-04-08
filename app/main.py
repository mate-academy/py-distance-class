from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        result = self.km / other
        return Distance(round(result, 2))

    def _get_value(self, other: Distance | int | float) -> int | float:
        return other.km if isinstance(other, Distance) else other

    # Métodos de comparação com anotação explícita de retorno booleano
    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == self._get_value(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._get_value(other)
