from __future__ import annotations


class Distance:

    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _get_value(
        self, other: Distance | int | float
    ) -> float | NotImplemented:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: Distance | int | float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __eq__(self, other: Distance | int | float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: Distance | int | float) -> bool:
        value = self._get_value(other)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value
    