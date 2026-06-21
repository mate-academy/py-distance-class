from __future__ import annotations


Number = int | float


def _get_val(other: Distance | Number) -> Number:
    return other.km if isinstance(other, Distance) else other


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | Number) -> Distance:
        distance_value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + distance_value)

    def __iadd__(self, other: Distance | Number) -> Distance:
        distance_value = other.km if isinstance(other, Distance) else other
        self.km += distance_value
        return self

    def __mul__(self, other: Number) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Number) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | Number) -> bool:
        return self.km < _get_val(other)

    def __gt__(self, other: Distance | Number) -> bool:
        return self.km > _get_val(other)

    def __eq__(self, other: Distance | Number) -> bool:
        return self.km == _get_val(other)

    def __le__(self, other: Distance | Number) -> bool:
        return self.km <= _get_val(other)

    def __ge__(self, other: Distance | Number) -> bool:
        return self.km >= _get_val(other)
