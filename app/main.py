from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance | NotImplemented:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance | NotImplemented:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def _get_value(self, other: Distance | int | float) -> (float
                                                            | NotImplemented):
        if isinstance(other, (int, float)):
            return other
        if isinstance(other, Distance):
            return other.km
        return NotImplemented

    def __lt__(self, other: Distance | int | float) -> bool | NotImplemented:
        distance_value = self._get_value(other)
        if distance_value is NotImplemented:
            return NotImplemented
        return self.km < distance_value

    def __gt__(self, other: Distance | int | float) -> bool | NotImplemented:
        distance_value = self._get_value(other)
        if distance_value is NotImplemented:
            return NotImplemented
        return self.km > distance_value

    def __ge__(self, other: Distance | int | float) -> bool | NotImplemented:
        distance_value = self._get_value(other)
        if distance_value is NotImplemented:
            return NotImplemented
        return self.km >= distance_value

    def __le__(self, other: Distance | int | float) -> bool | NotImplemented:
        distance_value = self._get_value(other)
        if distance_value is NotImplemented:
            return NotImplemented
        return self.km <= distance_value

    def __eq__(self, other: Distance | int | float) -> bool | NotImplemented:
        distance_value = self._get_value(other)
        if distance_value is NotImplemented:
            return NotImplemented
        return self.km == distance_value
