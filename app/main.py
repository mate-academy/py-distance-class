from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int | float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_km: Union[int | float] | "Distance") -> "Distance":
        if isinstance(new_km, Distance):
            return Distance(self.km + new_km.km)
        return Distance(self.km + new_km)

    def __iadd__(self, new_km: Union[int | float] | "Distance") -> "Distance":
        if isinstance(new_km, Distance):
            self.km += new_km.km
            return self
        self.km += new_km
        return self

    def __mul__(self, new_km: Union[int | float]) -> "Distance":
        return Distance(self.km * new_km)

    def __truediv__(self, new_km: Union[int | float]) -> "Distance":
        return Distance(round(self.km / new_km, 2))

    def __lt__(self, new_km: Union[int | float] | "Distance") -> bool:
        if isinstance(new_km, Distance):
            return self.km < new_km.km
        return self.km < new_km

    def __gt__(self, new_km: Union[int | float] | "Distance") -> bool:
        if isinstance(new_km, Distance):
            return self.km > new_km.km
        return self.km > new_km

    def __eq__(self, new_km: Union[int | float] | "Distance") -> bool:
        if isinstance(new_km, Distance):
            return self.km == new_km.km
        return self.km == new_km

    def __le__(self, new_km: Union[int | float] | "Distance") -> bool:
        if isinstance(new_km, Distance):
            return self.km <= new_km.km
        return self.km <= new_km

    def __ge__(self, new_km: Union[int | float] | "Distance") -> bool:
        if isinstance(new_km, Distance):
            return self.km >= new_km.km
        return self.km >= new_km
