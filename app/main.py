from __future__ import annotations
from typing import Union
from math import isclose


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    @property
    def km(self) -> int | float:
        return self._km

    @km.setter
    def km(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"""Unsupported type. Expected float or int.
                Got {type(value)} instead."""
            )
        self._km = value

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance | None:
        if isinstance(other, (Distance, int, float)):
            return Distance(self.km + getattr(other, "km", other))

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance | None:
        if isinstance(other, (Distance, int, float)):
            self.km += getattr(other, "km", other)
            return self

    def __mul__(self, other: Union[float, int]) -> Distance | None:
        if isinstance(other, (Distance, int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: Union[float, int]) -> Distance | None:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool | None:
        if isinstance(other, (Distance, int, float)):
            return self.km < getattr(other, "km", other)

    def __gt__(self, other: Union[Distance, int, float]) -> bool | None:
        if isinstance(other, (Distance, int, float)):
            return self.km > getattr(other, "km", other)

    def __eq__(self, other: Union[Distance, int, float]) -> bool | None:
        if isinstance(other, (Distance, int, float)):
            return isclose(self.km, getattr(other, "km", other))

    def __le__(self, other: Union[Distance, int, float]) -> bool | None:
        if isinstance(other, (Distance, int, float)):
            return self.km <= getattr(other, "km", other)

    def __ge__(self, other: Union[Distance, int, float]) -> bool | None:
        return not self.km < other
