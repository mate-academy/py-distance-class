from __future__ import annotations
from typing import Any


# noinspection PyMethodFirstArgAssignment
class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def united_standard(default: Distance | int | float) -> Any:
        return default.km if isinstance(default, Distance) else default

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + Distance.united_standard(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += Distance.united_standard(other)
        return self

    def __mul__(self, other: Distance | int | float) -> Any:
        if isinstance(other, (int, float)) is False:
            return
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Any:
        if isinstance(other, (int, float)) is False:
            return
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < Distance.united_standard(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > Distance.united_standard(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == Distance.united_standard(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= Distance.united_standard(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= Distance.united_standard(other)
