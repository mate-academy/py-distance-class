from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Distance:
    def __init__(self, km: Number) -> None:
        self.km: float = float(km)

    def _format_km(self) -> str:
        return str(int(self.km)) if self.km.is_integer() else str(self.km)

    def __str__(self) -> str:
        return f"Distance: {self._format_km()} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self._format_km()})"

    def __add__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other: Union["Distance", Number]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other: Number) -> "Distance":
        return Distance(self.km * float(other))

    def __truediv__(self, other: Number) -> "Distance":
        result = self.km / float(other)
        return Distance(round(result, 2))

    def __lt__(self, other: Union["Distance", Number]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else float(other))

    def __gt__(self, other: Union["Distance", Number]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else float(other))

    def __eq__(self, other: Union["Distance", Number]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else float(other))

    def __le__(self, other: Union["Distance", Number]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else float(other))

    def __ge__(self, other: Union["Distance", Number]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else float(other))