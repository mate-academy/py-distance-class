from __future__ import annotations
from typing import Any


class Distance:

    def __init__(self, km: Distance) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if type(other) != Distance:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: Any) -> Any:
        if type(other) != Distance:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Any) -> Any:
        if type(other) != Distance:
            result = self.km * other
            return Distance(result)
        else:
            result = self.km * other.km
        print(result)

    def __truediv__(self, other: Any) -> Any:
        div = self.km / other
        return Distance(round(div, 2))

    def __lt__(self, other: Any) -> bool:
        return self.km < other

    def __gt__(self, other: Any) -> bool:
        return self.km > other

    def __eq__(self, other: Any) -> bool:
        return self.km == other

    def __le__(self, other: Any) -> bool:
        return self.km <= other

    def __ge__(self, other: Any) -> bool:
        return self.km >= other
