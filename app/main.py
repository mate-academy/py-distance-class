from __future__ import annotations
import operator
from typing import Union


class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[int, Distance]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def _validate(
            self,
            other: Union[int, Distance],
            operator: operator
    ) -> operator:
        if isinstance(other, Distance):
            return operator(self.km, other.km)
        else:
            return operator(self.km, other)

    def __lt__(self, other: Union[int, Distance]) -> bool:
        return self._validate(other, operator.lt)

    def __gt__(self, other: Union[int, Distance]) -> bool:
        return self._validate(other, operator.gt)

    def __eq__(self, other: Union[int, Distance]) -> bool:
        return self._validate(other, operator.eq)

    def __le__(self, other: Union[int, Distance]) -> bool:
        return self._validate(other, operator.le)

    def __ge__(self, other: Union[int, Distance]) -> bool:
        return self._validate(other, operator.ge)
