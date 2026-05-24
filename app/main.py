from __future__ import annotations


def _get_km(other: Distance | int | float) -> int | float:
    if isinstance(other, Distance):
        return other.km
    if isinstance(other, (int, float)):
        return other
    raise TypeError


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
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

    def __lt__(self, other: Distance | int | float) -> bool:
        try:
            return self.km < _get_km(other)
        except TypeError:
            return NotImplemented

    def __gt__(self, other: Distance | int | float) -> bool:
        try:
            return self.km > _get_km(other)
        except TypeError:
            return NotImplemented

    def __eq__(self, other: Distance | int | float) -> bool:
        try:
            return self.km == _get_km(other)
        except TypeError:
            return NotImplemented

    def __le__(self, other: Distance | int | float) -> bool:
        try:
            return self.km <= _get_km(other)
        except TypeError:
            return NotImplemented

    def __ge__(self, other: Distance | int | float) -> bool:
        try:
            return self.km >= _get_km(other)
        except TypeError:
            return NotImplemented
