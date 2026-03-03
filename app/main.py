from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km!r})"

    def __add__(self, km2: Distance | float | int) -> Any:
        if isinstance(km2, Distance):
            return Distance(self.km + km2.km)
        else:
            return Distance(self.km + km2)

    def __iadd__(self, km2: Distance | float | int) -> Any:
        if isinstance(km2, Distance):
            self.km += km2.km
        elif isinstance(km2, (float, int)):
            self.km += km2
        return self

    def __mul__(self, num: Distance | float | int) -> Any:
        if isinstance(num, (int, float)):
            return Distance(self.km * num)

    def __truediv__(self, km2: Distance | float | int) -> Any:
        if isinstance(km2, (int, float)):
            return Distance(round((self.km / km2), 2))

    def __gt__(self, km2: Distance | float | int) -> bool:
        if isinstance(km2, Distance):
            return self.km > km2.km
        elif isinstance(km2, (float, int)):
            return self.km > km2

    def __lt__(self, km2: Distance | float | int) -> bool:
        if isinstance(km2, Distance):
            return self.km < km2.km
        elif isinstance(km2, (float, int)):
            return self.km < km2

    def __eq__(self, km2: Distance | float | int) -> bool:
        if isinstance(km2, Distance):
            return self.km == km2.km
        elif isinstance(km2, (float, int)):
            return self.km == km2

    def __le__(self, km2: Distance | float | int) -> bool:
        if isinstance(km2, Distance):
            return self.km <= km2.km
        elif isinstance(km2, (float, int)):
            return self.km <= km2

    def __ge__(self, km2: Distance | float | int) -> bool:
        if isinstance(km2, Distance):
            return self.km >= km2.km
        elif isinstance(km2, (float, int)):
            return self.km >= km2
