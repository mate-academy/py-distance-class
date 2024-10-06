from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Distance:
    km: float | int

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (float, int)):
            return Distance(self.km + other)
        raise TypeError(
            f"Unsupported operand type(s) for +: 'Distance' and '"
            f"{type(other).__name__}'"
        )

    def __iadd__(self, other: "Distance | float") -> Distance:
        self.km += (other.km if isinstance(other, Distance) else other)
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | float") -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: "Distance | float") -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: "Distance | float") -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: "Distance | float") -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: "Distance | float") -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
