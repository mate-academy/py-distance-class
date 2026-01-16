from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented  # на случай чужих типов

    def __iadd__(self, other: Union[Distance, Number]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented  # type: ignore[return-value]
        return self

    def __mul__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance * Distance is not supported")
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        return Distance(self.km * other)

    def __rmul__(self, other: Number) -> Distance:
        # только число * Distance
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        return Distance(other * self.km)

    def __truediv__(self, other: Number) -> Distance:
        if isinstance(other, Distance):
            raise TypeError("Distance / Distance is not supported")
        if not isinstance(other, (int, float)):
            return NotImplemented  # type: ignore[return-value]
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Union[Distance, Number]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __lt__(self, other: Union[Distance, Number]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[Distance, Number]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union[Distance, Number]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[Distance, Number]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
