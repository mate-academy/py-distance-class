from __future__ import annotations
from typing import Union


Numeric = Union[int, float]


class Distance:
    def __init__(self, km: Numeric) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_str = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance(km={km_str})"

    def __add__(self, other: Union[Distance, Numeric]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union[Distance, Numeric]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: Numeric) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: Numeric) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: Union[Distance, Numeric]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union[Distance, Numeric]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Union[Distance, Numeric]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[Distance, Numeric]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[Distance, Numeric]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
