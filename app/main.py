from __future__ import annotations
from typing import Union, Type


class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    @staticmethod
    def validator(
            other: Union[Distance, int, float],
            *numeric_types,
            distance: Type["Distance"] = None
    ) -> Union[Distance, int, float, None]:
        if numeric_types and not isinstance(other, (numeric_types, distance)):
            raise TypeError(
                "Operator must be of a Distance instance or number"
            )

        if distance and isinstance(other, Distance):
            return other.km

        return other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> "Distance":
        return Distance(self.km + self.validator(
            other, int, float, distance=Distance
        ))

    def __iadd__(self, other: Union[Distance, int, float]) -> "Distance":
        self.km += self.validator(other, distance=Distance)
        return self

    def __mul__(self, other: Union[Distance, int, float]) -> "Distance":
        return Distance(self.km * self.validator(other, int, float))

    def __truediv__(self, other: Union[Distance, int, float]) -> "Distance":
        result_km = self.km / self.validator(other, int, float)
        return Distance(round(result_km, 2))

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km < self.validator(other, int, float, distance=Distance)

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        return self.km > self.validator(other, int, float, distance=Distance)

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        return self.km == self.validator(other, int, float, distance=Distance)

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        return self.km <= self.validator(other, int, float, distance=Distance)

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= self.validator(other, int, float, distance=Distance)
