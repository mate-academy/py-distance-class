from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
from typing import Union

Number = Union[int, float]


@total_ordering
@dataclass
class Distance:
    km: float

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __radd__(self, other: Number) -> "Distance":
        # supports: 10 + Distance(5)
        return Distance(float(other) + self.km)

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += float(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * float(other))

    def __rmul__(self, other: Number) -> "Distance":
        return Distance(float(other) * self.km)

    def __truediv__(self, other: Number) -> "Distance":
        result = self.km / float(other)
        return Distance(round(result, 2))

    def _other_km(self, other: Union["Distance", Number]) -> float:
        return other.km if isinstance(other, Distance) else float(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == self._other_km(other)  # type: ignore[arg-type]

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < self._other_km(other)
