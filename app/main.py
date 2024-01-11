from functools import total_ordering
from typing import Any


@total_ordering
class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:

        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:

        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Any) -> Any:
        if isinstance(other, Distance):

            return Distance(km=self.km + other.km)

        return Distance(km=self.km + other)

    def __iadd__(self, other: int | float | Any) -> Any:
        if isinstance(other, Distance):
            self.km = self.km + other.km

            return self

        self.km = self.km + other

        return self

    def __mul__(self, other: int | float | Any) -> Any:

        return Distance(km=self.km * other)

    def __truediv__(self, other: int | float) -> Any:

        return Distance(km=round((self.km / other), 2))

    def __lt__(self, other: int | float | Any) -> bool:

        if isinstance(other, Distance):

            return self.km < other.km

        return self.km < other

    def __eq__(self, other: int | float | Any) -> bool:

        if isinstance(other, Distance):

            return self.km == other.km

        return self.km == other
