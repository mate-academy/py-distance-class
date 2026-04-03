from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _get_value(self,
                   other: Distance | int | float
                   ) -> int | float | type(NotImplemented):
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __add__(self, other: Distance | int | float) -> Distance:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: object) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: object) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __eq__(self, other: object) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __le__(self, other: object) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: object) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value
